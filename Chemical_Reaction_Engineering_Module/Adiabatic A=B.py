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
Ea=10000
dH=-20000
FA0=5
CA0=2
FI0=10
CpA=160
CpI=18
T1=300
T0=310
def ODEfun(Yfuncvec, V, Ea,dH,FA0,CA0,FI0,CpA,CpI,T0):
    X= Yfuncvec[0]
    #Explicit Equation Inline
    thetaI=FI0/FA0
    sumcp = (thetaI*CpI+CpA)
    T=T0+(-dH)*X/sumcp
    Kc = 1000*(np.exp((dH/1.987)*(1/T1-1/T)))
    k = .1*np.exp((Ea/1.987)*(1/T1-1/T))
    Ca = CA0*(1-X)
    Cb=CA0*X
    ra=-k*(Ca-Cb/Kc)
    # Differential equations
    dXdV = -ra/FA0
    return np.array([dXdV])

Vspan = np.linspace(0, 10, 100) # Range for the independent variable
y0 = np.array([0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example Lecture 19: A=B""", fontweight='bold', x = 0.15, y=0.97)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
sol = odeint(ODEfun, y0, Vspan, (Ea,dH,FA0,CA0,FI0,CpA,CpI,T0))
X = sol[:, 0]
thetaI=FI0/FA0
sumcp = (thetaI*CpI+CpA)
T=T0+(-dH)*X/sumcp
Kc = 1000*(np.exp((dH/1.987)*(1/T1-1/T)))
k = .1*np.exp((Ea/1.987)*(1/T1-1/T))
Ca = CA0*(1-X)
Cb=CA0*X
ra=-k*(Ca-Cb/Kc)
Xe=Kc/(1+Kc)
rate=-ra

p1, p2 = ax2.plot(Vspan, X, Vspan,Xe)
ax2.legend(['X', 'X$_{e}$'], loc='lower right')
ax2.set_xlabel('$V (m^3)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0,1.0)
ax2.set_xlim(0,10)
ax2.grid()

p3= ax3.plot(Vspan, T)[0]
ax3.legend(['T'], loc='upper right')
ax3.set_ylim(280,450)
ax3.set_xlim(0,10)
ax3.grid()
ax3.set_xlabel('$V (m^3)$', fontsize='medium')
ax3.set_ylabel('Temperature (K)', fontsize='medium')

p4 = ax4.plot(Vspan, rate)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_ylim(0,4)
ax4.set_xlim(0,10)
ax4.grid()
ax4.set_xlabel('$V (m^3)$', fontsize='medium')
ax4.set_ylabel('Rate', fontsize='medium')

ax1.axis('off')
ax1.text(-1.0, -1.2,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dV} = \dfrac{-r_{A}}{F_{A0}}$'
                  '\n \n'
                  
         'Explicit Equations'
                  '\n\n'
         r'$K_C = 1000*exp\left(\left(\dfrac{\Delta H_{Rx}}{1.987}\right)\left(\dfrac{1}{300} - \dfrac{1}{T}\right)\right)$'
                  '\n\n'
         r'$k = 0.1*exp\left(\left(\dfrac{E_a}{1.987}\right)\left(\dfrac{1}{300} - \dfrac{1}{T}\right)\right)$'
         '\n\n'
         r'$X_e = \dfrac{K_C}{1+ K_C}$'
         '\n'
         r'$\theta_I = \dfrac{F_{I0}}{F_{A0}}$'
                  '\n'
         r'$\sum_{i}\theta_iC_{pi} = \theta_IC_{P_I} + C_{P_A}}$'
         '\n'
         r'$C_A = C_{A0}(1-X)$'
         '\n'
         r'$C_B = C_{A0}*X$'
         '\n'
         r'$T=T_0+ \dfrac{(\Delta H_{Rx})*X}{\sum_{i}\theta_iC_{pi}}$'
                  '\n'
         r'$r_A = -k\left(C_A- \dfrac{C_B}{K_C}\right)$'
                  '\n'
         r'$Rate = -r_{A}$'
                  '\n', ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
    
axcolor = 'black'
ax_Ea = plt.axes([0.3, 0.84, 0.2, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.3, 0.8, 0.2, 0.015], facecolor=axcolor)
ax_FA0 = plt.axes([0.3, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_CA0 = plt.axes([0.3, 0.72, 0.2, 0.015], facecolor=axcolor)
ax_FI0 = plt.axes([0.3, 0.68, 0.2, 0.015], facecolor=axcolor)
ax_CpA = plt.axes([0.3, 0.64, 0.2, 0.015], facecolor=axcolor)
ax_CpI = plt.axes([0.3, 0.60, 0.2, 0.015], facecolor=axcolor)
ax_T0 = plt.axes([0.3, 0.56, 0.2, 0.015], facecolor=axcolor)

sEa = Slider(ax_Ea, r'$E_a$', 1000, 50000, valinit=10000,valfmt='%1.0f')
sdH= Slider(ax_dH,r'$\Delta H_{rx}$',-80000 , -5000, valinit=-20000,valfmt='%1.0f')
sFA0 = Slider(ax_FA0, r'F$_{A0}$', 1, 100, valinit=5,valfmt='%1.1f')
sCA0 = Slider(ax_CA0, r'C$_{A0}$',0.5,100, valinit=2,valfmt='%1.1f')
sFI0 = Slider(ax_FI0, r'F$_{I0}$', 0, 100, valinit=10,valfmt='%1.0f')
sCpA = Slider(ax_CpA, r'C$_{P_A}$ ', 10, 500, valinit=160,valfmt='%1.0f')
sCpI = Slider(ax_CpI, r'C$_{P_I}$ ',5, 100, valinit=18,valfmt='%1.1f')
sT0 = Slider(ax_T0, r'T$_{0}$ ',280, 350, valinit=310,valfmt='%1.0f')

def update_plot2(val):
    
    Ea = sEa.val
    dH =sdH.val
    FA0 = sFA0.val
    CA0 =sCA0.val
    FI0 = sFI0.val
    CpA = sCpA.val
    CpI = sCpI.val
    T0=sT0.val
    sol = odeint(ODEfun, y0, Vspan, (Ea,dH,FA0,CA0,FI0,CpA,CpI,T0))

    X = sol[:, 0]
    thetaI=FI0/FA0
    sumcp = (thetaI*CpI+CpA)
    T=310+(-dH)*X/sumcp
    Kc = 1000*(np.exp((dH/1.987)*(1/T1-1/T)))
    k = .1*np.exp((Ea/1.987)*(1/T1-1/T))
    Ca = CA0*(1-X)
    Cb=CA0*X
    ra=-k*(Ca-Cb/Kc)
    Xe=Kc/(1+Kc)
    rate=-ra
    p1.set_ydata(X)
    p2.set_ydata(Xe)
    p3.set_ydata(T)
    p4.set_ydata(rate)
    fig.canvas.draw_idle()


sEa.on_changed(update_plot2)
sdH.on_changed(update_plot2)
sFA0.on_changed(update_plot2)
sCA0.on_changed(update_plot2)
sFI0.on_changed(update_plot2)
sCpA.on_changed(update_plot2)
sCpI.on_changed(update_plot2)
sT0.on_changed(update_plot2)

resetax = plt.axes([0.33, 0.89, 0.12, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sEa.reset()
    sdH.reset()
    sFA0.reset()
    sCA0.reset()
    sFI0.reset()
    sCpA.reset()
    sCpI.reset()
    sT0.reset()
    
button.on_clicked(reset)
    
