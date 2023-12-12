#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%
Et1=5
KM=0.0233
Vmax1=1.2
Co=0.1
Et2=0.001
X = np.linspace(0, 1, 1000)
def func(X,KM, Vmax1,Co,Et2):   
    Vmax2=Vmax1*Et2/Et1
    t=(KM/Vmax2)*np.log(1/(1-X))+Co*X/Vmax2
    return np.array([t])

#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 9-3 Batch Enzymatic Reactors""", fontweight='bold', x = 0.2, y= 0.98)
plt.subplots_adjust(left  = 0.4)

t=func(X,KM, Vmax1,Co,Et2)
p1 = plt.plot(t[0,:], X)[0]
plt.grid()
plt.ylim(0, 1)
plt.xlim(0, 1000)
plt.legend(['X'], loc="upper right")
ax.set_xlabel('time (s)', fontsize='medium')
ax.set_ylabel('$Conversion$', fontsize="medium")

plt.text(-500, 0.35,
         'Equations'
                  '\n\n'
          r'$V_{max2} = \dfrac{E_{t2}}{E_{t1}}*V_{max1}$'
                 '\n\n'                 
          r'$t= \dfrac{K_M}{V_{max2}} ln\dfrac{1}{1-X} + \dfrac{C_{urea0}*X}{V_{max2}}  $'
                 '\n\n' 
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_KM = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_Vmax1 = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Co = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Et2 = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)

sKM = Slider(ax_KM, r'$K_M (\frac{mol}{dm^3})$', 0, 5, valinit=0.0233,valfmt='%1.4f')
sVmax1 = Slider(ax_Vmax1, r'$V_{max1}(\frac{mol}{dm^3.s})$', 0.1, 2, valinit=1.2,valfmt='%1.2f')
sCo = Slider(ax_Co, r'$C_{urea0}(\frac{mol}{dm^3})$', 0.0001, 1, valinit=0.1,valfmt='%1.2f')
sEt2 = Slider(ax_Et2, r'$E_{t2}(\frac{gm}{dm^3})$', 0.0001, 1, valinit=0.001,valfmt='%1.3f')

##
def update_plot2(val):
    Vmax1 = sVmax1.val
    KM = sKM.val
    Co=sCo.val
    Et2=sEt2.val
    t=func(X,KM, Vmax1,Co,Et2)
    p1.set_xdata(t[0,:])
    fig.canvas.draw_idle()

sVmax1.on_changed(update_plot2)
sKM.on_changed(update_plot2)
sCo.on_changed(update_plot2)
sEt2.on_changed(update_plot2)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sVmax1.reset()
    sKM.reset()
    sCo.reset()
    sEt2.reset()
        
button.on_clicked(reset)    

