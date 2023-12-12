#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
Vmax=1.33
KM=0.0266
Curea = np.linspace(0, 0.25, 100)
def func(Curea, Vmax, KM):   
    f1 = Vmax*Curea/(KM+Curea)
    f4=(KM/Vmax)+Curea/Vmax
    return np.array([f1,f4])

#%%
Cinv = np.linspace(0, 500, 100)
def func2(Cinv, Vmax, KM):
    f2 = (1/Vmax)+(KM/Vmax)*Cinv    
    return np.array([f2])

p = np.linspace(0, 50, 100)
def func3(Cinv, Vmax, KM):
    f3 =Vmax-KM*p    
    return np.array([f3])
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 9-2 Evaluation of Michaelis-Menten Parameters Vmax and KM""", fontweight='bold', x = 0.25, y= 0.98)
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.4,hspace=0.4)

sol = func(Curea, Vmax, KM)
f1 = sol[0, :]
f4=sol[1, :]

sol2 = func2(Cinv, Vmax, KM)
f2 = sol2[0, :]

sol3 = func3(p, Vmax, KM)
f3 = sol3[0, :]

p1 = ax1.plot(Curea,f1)[0]
ax1.set_xlabel('$C_{urea}$', fontsize='large')
ax1.set_ylabel('$-r_{urea}$', fontsize='large')
ax1.set_ylim(0,5)
ax1.set_xlim(0,0.2)
ax1.grid()
ax1.set_title('Michaelis-Menten Plot')

p4 = ax4.plot(Curea,f4)[0]
ax4.set_xlabel('$C_{urea}$', fontsize='large')
ax4.set_ylabel(r'$-\frac{C_{urea}}{r_{urea}}$', fontsize='large')
ax4.set_ylim(0,2)
ax4.set_xlim(0,0.25)
ax4.grid()
ax4.set_title('Hanes-Woolf Plot')

p2 = ax2.plot(Cinv,f2)[0]
ax2.set_xlabel(r'$\frac{1}{C_{Urea}}$', fontsize='large')
ax2.set_ylabel(r'$-\frac{1}{r_{Urea}}$', fontsize='large')
ax2.set_ylim(0,100)
ax2.set_xlim(0,500)
ax2.grid()
ax2.set_title('Lineweaver-Burk Plot')

p3 = ax3.plot(p,f3)[0]
ax3.set_xlabel(r'$-\frac{r_{urea}}{C_{urea}}$', fontsize='large')
ax3.set_ylabel(r'$-r_{urea}$', fontsize='large')
ax3.set_ylim(0,5)
ax3.set_xlim(0,50)
ax3.grid()
ax3.set_title('Eadie-Hofstee Plot')

ax2.text(-1343.83, -135.8,
         'Equations'
                  '\n\n'
          'Michaelis-Menten Equation'
          '\n\n'
          r'$-r_{Urea} = \dfrac{V_{max}*C_{Urea}}{(k_M+C_{Urea})}$'
                 '\n\n'                 
          'Lineweaver-Burk Equation'
          '\n\n'
          r'$\dfrac{1}{-r_{Urea}} = \dfrac{1}{V_{max}}+\dfrac{K_M}{V_{max}*C_{Urea}}$'
                 '\n\n' 
        'Eadie-Hofstee Equation'
          '\n\n'
          r'$-r_{Urea}   = V_{max}-K_M*\left(\dfrac{-r_{Urea}}{C_{Urea}}\right)$'
                 '\n\n' 
                'Hanes-Woolf Equation'
          '\n\n'
          r'$\dfrac{C_{Urea}}{-r_{Urea}}   = \dfrac{K_M}{V_{max}}+\dfrac{C_{Urea}}{V_{max}}$'
                 '\n\n' 
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_Vmax = plt.axes([0.1, 0.78, 0.2, 0.02], facecolor=axcolor)
ax_KM = plt.axes([0.1, 0.74, 0.2, 0.02], facecolor=axcolor)

sVmax = Slider(ax_Vmax, r'$V_{max}$', 0, 5, valinit=1.33,valfmt='%1.2f')
sKM = Slider(ax_KM, r'$K_M$', 0.0001, 1, valinit=0.0266,valfmt='%1.4f')

##
def update_plot2(val):
    Vmax = sVmax.val
    KM = sKM.val
    sol = func(Curea, Vmax, KM)
    p1.set_ydata(sol[0,:])
    p4.set_ydata(sol[1,:])
    sol2 = func2(Cinv, Vmax, KM)
    p2.set_ydata(sol2)
    sol3 = func3(p, Vmax, KM)
    p3.set_ydata(sol3)
    fig.canvas.draw_idle()

sVmax.on_changed(update_plot2)
sKM.on_changed(update_plot2)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sVmax.reset()
    sKM.reset()
        
button.on_clicked(reset)    

