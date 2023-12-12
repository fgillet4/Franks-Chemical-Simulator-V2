import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

Ks=30
umax=0.5
r1m=625
r2m=610
r3m=567.8
r4m=558.1
Cs = np.linspace(210, 260, 10)
r1c=(Ks/umax)+(250/umax)
r2c=(Ks/umax)+(244/umax)
r3c=(Ks/umax)+(231/umax)
r4c=(Ks/umax)+(218/umax)
rate=(Ks/umax)+(Cs/umax)
x=(250,244,231,218)
y=(625,610,567.8,558.1)
fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle("""LEP-9-4: Estimate the rate-law parameters""", fontweight='bold', x = 0.22, y= 0.98)
plt.subplots_adjust(left  = 0.6)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
p1,p2 = ax1.plot(x,y,'o',Cs,rate)
ax1.legend(['data','$Model\hspace{0.5} fit$'], loc='upper left')
ax1.grid()
ax1.set_ylim(550, 650)
ax1.set_xlim(210, 260)
ax1.set_xlabel(r'$C_S$', fontsize="large")
ax1.set_ylabel(r'$C_C*C_S/r_g$', fontsize='large')
ssquare=(r1m-r1c)**2+(r2m-r2c)**2+(r3m-r3c)**2+(r4m-r4c)**2
x1=(210,230,250,260)
y1=(ssquare,ssquare,ssquare,ssquare)
p3 = ax2.plot(x1,y1)[0]
ax2.grid()
ax2.set_xlim(210, 260)
ax2.set_ylim(0, 15000)
ax2.set_xlabel(r'$C_S$', fontsize="large")
ax2.set_ylabel(r'$Sigma^2$', fontsize='large')
ax1.text(150,550,
         'Equations'
                  '\n\n'
        r'$\dfrac{C_C*C_S}{r_{g}}=\dfrac{K_S}{\mu_{max}}+ \dfrac{C_S}{\mu_{max}}$'                            
                 '\n\n'  
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
         
axcolor = 'black'
ax_Ks = plt.axes([0.2, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_umax = plt.axes([0.2, 0.75, 0.2, 0.02], facecolor=axcolor)

sKs = Slider(ax_Ks, r'$k_s$', 10, 50, valinit=30,valfmt='%1.1f')
sumax = Slider(ax_umax, r'$\mu_{max}$',0.2, 0.6, valinit=0.5,valfmt='%1.3f')

def update_plot(val):
    Ks = sKs.val
    umax = sumax.val
    r1m=625
    r2m=610
    r3m=567.8
    r4m=558.1
    r1c=(Ks/umax)+(250/umax)
    r2c=(Ks/umax)+(244/umax)
    r3c=(Ks/umax)+(231/umax)
    r4c=(Ks/umax)+(218/umax)
    rate=(Ks/umax)+(Cs/umax)
    ssquare=(r1m-r1c)**2+(r2m-r2c)**2+(r3m-r3c)**2+(r4m-r4c)**2
    y1=(ssquare,ssquare,ssquare,ssquare)
    p2.set_ydata(rate)
    p3.set_ydata(y1)
    fig.canvas.draw_idle()

sKs.on_changed(update_plot)
sumax.on_changed(update_plot)

resetax = plt.axes([0.25, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKs.reset()
    sumax.reset()
        
button.on_clicked(reset)    


