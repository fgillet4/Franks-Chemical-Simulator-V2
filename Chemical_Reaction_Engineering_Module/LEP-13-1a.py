#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
Ea = 18000
dH = -20202
R=1.987
To=286
CpS=252.2
A=4.816*10**9
def ODEfun(Yfuncvec,t,Ea,dH,R,To,CpS,A):
    X= Yfuncvec[0]
      #Explicit Equation Inline
    T=To+X*(-dH)/CpS
    k = A*np.exp(-Ea/(R*T))
    # Differential equations
    dXdt = k*(1-X)
    return np.array([dXdt])

tspan = np.linspace(0, 2500, 1000) # Range for the independent variable
y0 = np.array([0]) # Initial values for the dependent variables

#%%
fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle("""LEP-13-1a: Batch Reactor (Adiabatic Operation)""", fontweight='bold', x = 0.18, y=0.98)
plt.subplots_adjust(left=0.55)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
sol =  odeint(ODEfun, y0, tspan, (Ea,dH,R,To,CpS,A))
X = sol[:, 0]
T=To+X*(-dH)/CpS
k = A*np.exp(-Ea/(R*T))
p1= ax1.plot(tspan, X)[0]
ax1.legend([r'$X$'], loc='upper right')
ax1.set_xlabel('time $(sec)$', fontsize='medium')
ax1.set_ylabel(r'Conversion', fontsize='medium')
ax1.grid()
ax1.set_ylim(0, 1)
ax1.set_xlim(0, 2500)
p2 = ax2.plot(tspan, T)[0]
plt.legend([r'$T$'], loc='upper right')
ax2.set_xlabel('time $(sec)$', fontsize='medium')
ax2.set_ylabel(r'Temperature $(K)$', fontsize='medium')
ax2.grid()
ax2.set_ylim(275, 500)
ax2.set_xlim(0, 2500)

ax1.text(-2750, -1.3,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-2300, -0.8,'Differential Equations'
         '\n'
         r'$\dfrac{dX}{dt} = k*(1-X)$'
         '\n'
         '\n'
         'Explicit Equations'
         '\n'
         r'$C_{P_S} = 252.2$'
                  '\n\n'
        r'$A = 4.816*10^{9}\thinspace s^{-1}$'
                '\n\n'
         r'$T=T_0 +X \dfrac{(-\Delta H_{Rx})}{C_{P_S}}$'  
         '\n\n'
          r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'   
         '\n'
        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

axcolor = 'black'
ax_dH = plt.axes([0.18, 0.78, 0.18, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.18, 0.74, 0.18, 0.015], facecolor=axcolor)
ax_To = plt.axes([0.18, 0.70, 0.18, 0.015], facecolor=axcolor)
ax_CpS = plt.axes([0.18, 0.66, 0.18, 0.015], facecolor=axcolor)

sdH= Slider(ax_dH, r'$\Delta H_{Rx}^\circ$ ($\frac{cal}{mol}$)', -35000, -10000, valinit=-20202,valfmt='%1.0f')
sEa = Slider(ax_Ea, r'$E$($\frac{cal}{mol}$)', 15000, 22000, valinit=18000,valfmt='%1.0f')
sTo = Slider(ax_To,r'$T_0$ ($K$)', 273, 400, valinit= 286,valfmt='%1.0f')
sCpS = Slider(ax_CpS, r'C$_{P_S}$ ($\frac{cal}{mol.k}$)', 150,400, valinit=252.2,valfmt='%1.1f')


def update_plot2(val):
    dH = sdH.val
    Ea = sEa.val
    To =sTo.val
    CpS=sCpS.val
    sol = odeint(ODEfun, y0, tspan, (Ea,dH,R,To,CpS,A))
    X = sol[:, 0]
    T=To+X*(-dH)/CpS
    p1.set_ydata(X)
    p2.set_ydata(T)
    fig.canvas.draw_idle()

sdH.on_changed(update_plot2)
sEa.on_changed(update_plot2)
sTo.on_changed(update_plot2)
sCpS.on_changed(update_plot2)

resetax = plt.axes([0.18, 0.84, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sdH.reset()
    sEa.reset()
    sTo.reset()
    sCpS.reset()
button.on_clicked(reset)
    
