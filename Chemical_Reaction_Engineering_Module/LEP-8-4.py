#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
Cao = 2
R = 1.987
A1 = 1.913
A2 = 0.547
E1 = 800
E2 = 600
T = 300
tau = np.linspace(0, 20, 1000)
def func(Cao, A1, A2, E1, E2, T):
    k1=A1*np.exp(-E1/(R*T))
    k2=A2*np.exp(-E2/(R*T))
    Ca = Cao/(1+tau*k1)
    X = (Cao - Ca)/Cao
    Cb = tau*k1*Cao/((1+k1*tau)*(1+k2*tau))
    yeild = np.nan_to_num(Cb/(Cao - Ca))
    Cc = (tau**2)*k1*k2*Cao/((1+k1*tau)*(1+k2*tau))
    selectivity = np.nan_to_num(Cb/Cc)
    return np.array([Ca, Cb, Cc, X, yeild, selectivity])

sol =  func(Cao,A1, A2, E1, E2, T)
#Making E1 and E2 extremely Small solves the problem
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-4: Series Reactions in a CSTR""", x = 0.18, y = 0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.35)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
sol =  func(Cao,A1, A2, E1, E2, T)
Ca = sol[0,:]
Cb = sol[1,:]
Cc = sol[2,:]
X = sol[3, :]
selectivity = sol[5, :]
Yield = sol[4, :]

p1, p2, p3  =ax1.plot(tau, Ca, tau, Cb, tau, Cc)
ax1.legend(['$C_A$', '$C_B$', '$C_C$'], loc='best')
ax1.set_xlabel('tau (hr)', fontsize='medium', )
ax1.set_ylabel(r'Concentration ($mol/dm^3$)', fontsize='medium', )
ax1.grid()
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 4)

p4=ax2.plot(tau, X)[0]
ax2.legend(['X'], loc='upper left')
ax2.set_xlabel('tau (hr)', fontsize='medium', )
ax2.set_ylabel('Conversion', fontsize='medium', )
ax2.grid()
ax2.set_xlim(0, 20)
ax2.set_ylim(0, 1.0)

p5 = ax3.plot(tau, selectivity)[0]
ax3.legend(['$S_{B/C}$'], loc='upper right')
ax3.set_xlabel('tau (hr)', fontsize='medium', )
ax3.set_ylabel('Selectivity', fontsize='medium', )
ax3.grid()
ax3.set_xlim(0, 20)


p6=ax4.plot(tau, sol[4, :])[0]
ax4.legend(['$Y_B$'], loc='best')
ax4.set_xlabel('tau (hr)', fontsize='medium', )
ax4.set_ylabel('Yield', fontsize='medium', )
ax4.grid()
ax4.set_xlim(0, 20)
ax4.set_ylim(0, 1)

ax3.text(-28, -72,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax3.text(-22, 50,
         '\n'
         'Explicit Equations'
                  '\n\n'
         r'$X = \dfrac{(C_{A0} - C_A)}{C_{A0}}$'
         '\n'
          r'$A_1 = 1.913 \thinspace hr^{-1}$'
         '\n'
          r'$A_2 = 0.547 \thinspace hr^{-1}$'
         '\n'
         r'$k_1 = A_1*exp\left(\dfrac{-E_1}{1.987*T}\right)$'       
        '\n\n'
        r'$k_2 = A_2*exp\left(\dfrac{-E_2}{1.987*T}\right)$' 
                  '\n'
        r'$C_A = \dfrac{C_{A0}}{(1+k_1\tau)}$'  
                       '\n'
         r'$C_B = \dfrac{\tau k_1 C_{A0}}{(1+k_1\tau)(1+k_2\tau)}$'  
          '\n'
         r'$C_C = \dfrac{\tau^2 k_1 k_2C_{A0}}{(1+k_1\tau)(1+k_2\tau)}$'  
          '\n\n'          
         r'$Selectivity = \dfrac{C_B}{C_C}$'
                  '\n'
         r'$Yield = \dfrac{C_B}{(C_{A0} - C_A)}$'
         '\n'
         r'$\tau_{max} = \dfrac{1}{\sqrt{k_1k_2}}$'

         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=20), fontweight='bold')


#%%
#Slider Code
axcolor = 'black'

ax_E1 = plt.axes([0.08, 0.83, 0.15, 0.015], facecolor=axcolor)
ax_E2 = plt.axes([0.08, 0.80, 0.15, 0.015], facecolor=axcolor)
ax_T = plt.axes([0.08, 0.77, 0.15, 0.015], facecolor=axcolor)
ax_Cao = plt.axes([0.08, 0.74, 0.15, 0.015], facecolor=axcolor)


sE1 = Slider(ax_E1, r'E$_{1} (\frac{cal}{mol})$', 0, 5000, valinit=800, valfmt = "%1.0f")
sE2 = Slider(ax_E2, r'E$_{2} (\frac{cal}{mol})$',   0,   5000, valinit=600, valfmt = "%1.0f")
sT = Slider(ax_T, r'T (K)', 280, 500, valinit=300, valfmt = "%1.1f")
sCao= Slider(ax_Cao, r'$C_{A0} \frac{mol}{dm^3})$', 0.05, 4, valinit=2,valfmt = "%1.1f")


def update_plot2(val):

    E1 = sE1.val
    E2 = sE2.val
    T = sT.val
    Cao = sCao.val
    sol =  func(Cao,A1,A2, E1, E2, T)
    Ca = sol[0,:]
    Cb = sol[1,:]
    Cc = sol[2,:]
    X = sol[3, :]
    selectivity = sol[5, :]
    yeild = sol[4, :]
    
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(X)
    p5.set_ydata(selectivity)
    p6.set_ydata(yeild)    
    fig.canvas.draw_idle()


sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)
sT.on_changed(update_plot2)
sCao.on_changed(update_plot2)

resetax = plt.axes([0.12, 0.88, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):

    sE1.reset()
    sE2.reset()
    sT.reset()
    sCao.reset()
    
button.on_clicked(reset)

plt.show()
