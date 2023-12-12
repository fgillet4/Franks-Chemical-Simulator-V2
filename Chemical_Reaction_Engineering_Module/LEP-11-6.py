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
Ca0 = 1
To = 480 
dH = -14000
Ke2 = 75000
A=756.07
Fa0 = 5
thetaI=1 
CpI = 50
CpA=  25
Ea=10000
def ODEfun(Yfuncvec, V, Ca0,To, dH,Ke2,A,Fa0,thetaI,
           CpI,CpA,Ea):
    X= Yfuncvec[0]
    #Explicit Equation Inline
    Sumcp=CpA+ thetaI* CpI
    T = To + (-dH/Sumcp) * X
    Ke = Ke2 * np.exp((dH/1.987) * (T - 298) / (T * 298))
    k = A* np.exp(-Ea/(1.987*T))  
    Xe = Ke / (1 + Ke)
    ra = 0 - (k * Ca0 * (1 -X/Xe))
    # Differential equations
    dXdV = 0 - (ra / Fa0)
    return np.array([dXdV])

Vspan = np.linspace(0, 100, 100) # Range for the independent variable
y0 = np.array([0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.37)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""LEP-11-6: Optimum Entering Temperature for Adiabatic Operation""", fontweight='bold', x = 0.22)

sol = odeint(ODEfun, y0, Vspan, (Ca0,To, dH,Ke2,A,Fa0,thetaI,CpI,CpA,Ea))
X = sol[:, 0]
Sumcp=CpA+ thetaI* CpI
T = To + (-dH/Sumcp) * X
Ke = Ke2 * np.exp((dH/1.987) * (T - 298) / (T * 298))
k = A* np.exp(-Ea/(1.987*T)) 
Xe = Ke / (1 + Ke)
ra = 0 - (k * Ca0 * (1 -X/Xe))
rate = 0 - ra
p1= ax2.plot(Vspan,T)[0]
ax2.legend(['T'], loc='upper right')
ax2.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax2.set_ylabel('Temperature (K)', fontsize='medium')
ax2.set_ylim(300,900)
ax2.set_xlim(0,100)
ax2.grid()

p2,p4 = ax3.plot(Vspan,X,Vspan,Xe)
ax3.legend(['X','$X_e$'], loc='upper right')
ax3.set_ylim(0,1)
ax3.set_xlim(0,100)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium')

p3 = ax4.plot(Vspan, rate)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_ylim(0,0.08)
ax4.set_xlim(0,100)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax4.set_ylabel('$Rate {(mol/ dm^3.min)}$', fontsize='medium')

ax1.axis('off')
ax1.text(-1.5, -1.2,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-1.3,-0.7,'Differential Equations'
         '\n\n'
        r'$\dfrac{dX}{dV} = \dfrac{-r_{A}}{F_{A0}}$'
                  '\n \n'  
         'Explicit Equations'
                  '\n\n'
         r'$A = 756.07\thinspace min^{-1}$'
           '\n\n'
         r'$T=T_0 +\dfrac{(-\Delta H_{Rx}^\circ)*X}{\sum_{i}\theta_iC_{pi}}$'   
         '\n'
         r'$K_e = K_{e2}*exp\left(\left(\dfrac{\Delta H_{Rx}^\circ}{1.987}\right)\left(\dfrac{1}{298} - \dfrac{1}{T}\right)\right)$'
                  '\n'
         r'$X_e = \dfrac{K_e}{1+K_e}$'
         '\n'
         r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$' 
         '\n'
         r'$\theta_I=1$'
         '\n'         
         r'$\sum_{i}\theta_iC_{pi} = C_{P_A} +\theta_IC_{P_I} $'
         '\n'
         r'$-r_A = kC_{A0}\left(1 - \dfrac{X}{X_e}\right)$'
                  '\n'
         r'$rate = -r_A$'
                 '\n'
       , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_Ca0 = plt.axes([0.33, 0.84, 0.2, 0.015], facecolor=axcolor)
ax_To = plt.axes([0.33, 0.80, 0.2, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.33, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_Ke2 = plt.axes([0.33, 0.72, 0.2, 0.015], facecolor=axcolor)
ax_Fa0 = plt.axes([0.33, 0.68, 0.2, 0.015], facecolor=axcolor)
ax_thetaI = plt.axes([0.33, 0.64, 0.2, 0.015], facecolor=axcolor)
ax_CpA = plt.axes([0.33, 0.60, 0.2, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.33, 0.56, 0.2, 0.015], facecolor=axcolor)
ax_CpI =plt.axes([0.33, 0.52, 0.2, 0.015], facecolor=axcolor)

sCa0 = Slider(ax_Ca0, r'C$_{A0}$($\frac{mol}{dm^3}$)', 0.1, 10, valinit=1,valfmt='%1.1f')
sTo = Slider(ax_To, 'T$_{0}$ ($K$)', 300, 700, valinit=480,valfmt='%1.0f')
sdH= Slider(ax_dH, r'$\Delta H_{Rx}^\circ$ ($\frac{cal}{mol}$)', -25000, -5000, valinit=-14000,valfmt='%1.0f')
sKe2 = Slider(ax_Ke2,'$K_{e2}$',5000, 150000, valinit=75000,valfmt='%1.0f')
sFa0 = Slider(ax_Fa0,r'F$_{A0}$ ($\frac{mol}{min}$)', 0.5, 50, valinit= 5,valfmt='%1.1f')
sthetaI = Slider(ax_thetaI, r'$\theta_{I}$', 0.2, 4, valinit=1,valfmt='%1.1f')
sCpA = Slider(ax_CpA, r'C$_{P_A}$ ($\frac{cal}{mol. K}$)', 10, 75, valinit=25,valfmt='%1.0f')
sEa= Slider(ax_Ea, r'E ($\frac{cal}{mol}$)', 1000, 18000, valinit=10000,valfmt='%1.0f')
sCpI = Slider(ax_CpI, r'C$_{P_I}$ ($\frac{cal}{mol. K}$)', 10, 75, valinit=50,valfmt='%1.0f')

def update_plot2(val):
    Ca0 = sCa0.val
    To =sTo.val
    dH =sdH.val
    Ke2 = sKe2.val
    Fa0 =sFa0.val
    thetaI = sthetaI.val
    CpA = sCpA.val
    Ea= sEa.val
    CpI= sCpI.val
    sol = odeint(ODEfun, y0, Vspan, (Ca0,To, dH,Ke2,A,Fa0,thetaI,CpI,CpA,Ea))
    X = sol[:, 0]
    Sumcp=CpA+ thetaI* CpI
    T = To + (-dH/Sumcp) * X
    Ke = Ke2 * np.exp((dH/1.987) * (T - 298) / (T * 298))
    k = A* np.exp(-Ea/(1.987*T)) 
    Xe = Ke / (1 + Ke)
    ra = 0 - (k * Ca0 * (1 -X/Xe))
    rate = 0 - ra
    p1.set_ydata(T)
    p2.set_ydata(X)
    p4.set_ydata(Xe)
    p3.set_ydata(rate)
    fig.canvas.draw_idle()


sCa0.on_changed(update_plot2)
sTo.on_changed(update_plot2)
sdH.on_changed(update_plot2)
sKe2.on_changed(update_plot2)
sFa0.on_changed(update_plot2)
sthetaI.on_changed(update_plot2)
sCpA.on_changed(update_plot2)
sEa.on_changed(update_plot2)
sCpI.on_changed(update_plot2)
resetax = plt.axes([0.37, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCa0.reset()
    sTo.reset()
    sdH.reset()
    sKe2.reset()
    sFa0.reset()
    sthetaI.reset()
    sCpA.reset()
    sEa.reset()
    sCpI.reset()
button.on_clicked(reset)
    
