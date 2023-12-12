#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
Kc = 0.1 
CTo = 0.07174
yao = np.linspace(0.0001, 1, 100)
def func(yao, Kc, CTo):
    Cao = yao*CTo
    delta = 1
    epsilon = yao*delta
    f1 = (-Kc + np.sqrt(Kc**2 + 16*Cao*Kc))/(8*Cao)
    f2 = ((epsilon - 1) + np.sqrt((epsilon - 1)**2 + 4*(epsilon + 4*Cao/Kc)))/(2*(epsilon + 4*Cao/Kc))
    
    return np.array([f1, f2])


#%%
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("""Example 4-5 Calculating the Equilibrium Conversion""", fontweight='bold', x = 0.2, y= 0.98)
fig.subplots_adjust(hspace=0.3)
plt.subplots_adjust(left  = 0.5)

sol = func(yao, Kc, CTo)
Xeb = sol[0, :]
Xef = sol[1, :]


p1, p2 = ax1.plot(yao, Xeb, yao, Xef)
ax1.legend(['$X_{eb}$', '$X_{ef}$'], loc='best')
ax1.set_xlabel('$y_{A0}$', fontsize='medium')
ax1.set_ylabel('$Conversion$', fontsize='medium')
ax1.set_ylim(0,1)
ax1.set_xlim(0,1)
ax1.grid()

p3 = ax2.plot(yao, np.nan_to_num(Xeb/Xef))[0]
ax2.legend([r'$\dfrac{X_{eb}}{X_{ef}}$'], loc='best')
ax2.set_ylabel(r'$\dfrac{X_{eb}}{X_{ef}}$', fontsize='medium')
ax2.set_xlabel('$y_{A0}$', fontsize='medium')
ax2.set_ylim(0,1)
ax2.set_xlim(0,1)
ax2.grid()

ax2.text(-0.83, 0.3,
                  
         'Equations'
                  '\n\n'            
          r'$C_{A0} = y_{A0}C_{T0}$'
                 '\n\n'                 
         r'$\delta = 1$'
                 '\n\n'
         r'$\epsilon = y_{A0}.\delta$'   
                  '\n\n'
         r'$X_{ef} = \sqrt{\dfrac{K_c(1-X_{ef})(1+\epsilon X_{ef})}{4C_{A0}}}$'
         '\n\n'
         r'$ X_{eb} =\sqrt{\dfrac{K_c(1-X_{eb})}{4C_{A0}}}$'
         '\n\n'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_Kc = plt.axes([0.15, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_CTo = plt.axes([0.15, 0.7, 0.2, 0.02], facecolor=axcolor)

sKc = Slider(ax_Kc, r'$K_c (\frac{mol}{dm^3})$', 0.01, 5, valinit=0.1,valfmt='%1.2f')
sCTo= Slider(ax_CTo, r'$C_{T0} (\frac{mol}{dm^3})$', 0.005, 5, valinit=0.07174,valfmt='%1.3f')


def update_plot2(val):
    Kc = sKc.val    
    CTo =sCTo.val
    sol = func(yao, Kc, CTo)
    Xeb = sol[0, :]
    Xef = sol[1, :]
    p1.set_ydata(Xeb)
    p2.set_ydata(Xef)
    p3.set_ydata(np.nan_to_num(Xeb/Xef))
    fig.canvas.draw_idle()


sKc.on_changed(update_plot2)
sCTo.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKc.reset()
    sCTo.reset()
button.on_clicked(reset)    

