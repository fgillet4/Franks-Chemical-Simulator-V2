#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%
KM=0.0233
Vmax=1.2
KI=0.1
Inhibitorconc=0.1
Sinv = np.linspace(0, 100, 1000)
def func(Sinv,KM, Vmax,KI,Inhibitorconc):   
    f1=1/Vmax+(KM/Vmax)*Sinv
    f2=1/Vmax+(KM *Sinv/Vmax)* (1 + Inhibitorconc/KI)
    f3=(Sinv* KM/Vmax) + (1/Vmax)* (1 + Inhibitorconc/KI)
    f4=(1/Vmax)* (1 + Inhibitorconc/KI) + (KM* Sinv/Vmax)* (1 + Inhibitorconc/KI)
    return np.array([f1,f2,f3,f4])

#%%
fig, ax = plt.subplots()
fig.suptitle("""Lineweaver-Burk plots for different types of enzyme Inhibition""", fontweight='bold', x = 0.25, y= 0.98)
plt.subplots_adjust(left  = 0.4)

sol=func(Sinv,KM, Vmax,KI,Inhibitorconc)
p1,p2,p3,p4 = plt.plot(Sinv, sol[0,:],Sinv, sol[1,:],Sinv, sol[2,:],Sinv, sol[3,:])
plt.grid()
plt.ylim(0, 10)
plt.xlim(0, 100)
plt.legend(['No Inhibition','Competitive Inhibition','Uncompetitive Inhibition','Noncompetitive Inhibition'], loc="upper right")
ax.set_xlabel(r'$\frac{1}{(S)}$', fontsize='large')
ax.set_ylabel(r'$-\frac{1}{r_{S}}$', fontsize="large")

plt.text(-62.5, -0.5,
         'Equations'
                  '\n\n'
         'No Inhibition'
         '\n\n'
          r'$\dfrac{1}{-r_S} = \dfrac{1}{V_{max}}+\dfrac{K_M}{V_{max}}*\dfrac{1}{(S)}$'
                 '\n\n'                 
        'Competitive Inhibition'
        '\n\n'
          r'$\dfrac{1}{-r_S} = \dfrac{1}{V_{max}}+\dfrac{1}{(S)}*\left[\dfrac{K_M}{V_{max}}*\left(1+\dfrac{(I)}{K_I}\right)\right]$'
                 '\n\n'
          'Uncompetitive Inhibition'
        '\n\n'
          r'$\dfrac{1}{-r_S} = \dfrac{1}{(S)}*\dfrac{K_M}{V_{max}}+\dfrac{1}{V_{max}}*\left(1+\dfrac{(I)}{K_I}\right)$'
                 '\n\n'
          'Noncompetitive Inhibition'
        '\n\n'
          r'$\dfrac{1}{-r_S} = \dfrac{1}{V_{max}}*\left(1+\dfrac{(I)}{K_I}\right)+\dfrac{1}{(S)}*\dfrac{K_M}{V_{max}}*\left(1+\dfrac{(I)}{K_I}\right)$'
                 '\n\n'  
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_KM = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_Vmax = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_KI = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Inhibitorconc = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)

sKM = Slider(ax_KM, r'$K_M$', 0, 10, valinit=0.0233,valfmt='%1.4f')
sVmax = Slider(ax_Vmax, r'$V_{max}$', 0.1, 10, valinit=1.2,valfmt='%1.2f')
sKI = Slider(ax_KI, r'$K_I$', 0.01, 5, valinit=0.1,valfmt='%1.2f')
sInhibitorconc = Slider(ax_Inhibitorconc, r'$I$', 0, 5, valinit=0.1,valfmt='%1.2f')

##
def update_plot2(val):
    KM = sKM.val
    Vmax = sVmax.val
    KI=sKI.val
    Inhibitorconc=sInhibitorconc.val
    sol=func(Sinv,KM, Vmax,KI,Inhibitorconc)
    p1.set_ydata(sol[0,:])
    p2.set_ydata(sol[1,:])
    p3.set_ydata(sol[2,:])
    p4.set_ydata(sol[3,:])
    fig.canvas.draw_idle()

sKM.on_changed(update_plot2)
sVmax.on_changed(update_plot2)
sKI.on_changed(update_plot2)
sInhibitorconc.on_changed(update_plot2)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKM.reset()
    sVmax.reset()
    sKI.reset()
    sInhibitorconc.reset()
        
button.on_clicked(reset)    

