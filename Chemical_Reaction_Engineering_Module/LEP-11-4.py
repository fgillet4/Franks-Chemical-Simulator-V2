import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

T0=480
dH=-14000
Ke1=75000
thetaI=1
CpA=25
CpI=50
R=1.987
T=np.linspace(300, 900, 200)
Ke = Ke1 * np.exp((dH/R) * (T - 298) / (T * 298))
Xe=Ke/(1+Ke)
XEB=(CpA+thetaI*CpI)*(T-T0)/(-dH) 
fig, ax1 = plt.subplots()
fig.suptitle("""LEP-11-4: Adiabatic Equilibrium Temperature and Conversion""", fontweight='bold', x = 0.22, y= 0.98)
plt.subplots_adjust(left  = 0.4)
p1,p2 = ax1.plot(T,Xe,T,XEB)
ax1.grid()
ax1.set_ylim(0, 1)
ax1.set_xlim(300, 900)
ax1.set_xlabel(r'$T (K)$', fontsize="large")
ax1.set_ylabel(r'$Conversion$', fontsize='large')
ax1.legend([r'$X_{e}$',r'$X_{EB}$'], loc='upper right')

ax1.text(-2.5, 0.15,
         'Equations'
         '\n'
            r'$K_e = K_{e1}*exp\left(\left(\dfrac{\Delta H_{Rx}^\circ}{1.987}\right)\left(\dfrac{1}{298} - \dfrac{1}{T}\right)\right)$'
                  '\n'
         r'$X_e = \dfrac{K_e}{1+K_e}$'
                 '\n\n'  
         r'$X_{EB} =  \dfrac{\left(C_{P_A} +\theta_IC_{P_I}\right)*\left(T-T_0\right)}{-\Delta H_{Rx}^\circ}$'
                 '\n\n'
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
    
      
axcolor = 'black'
ax_T0 = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_dH = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Ke1 = plt.axes([0.1, 0.70, 0.2, 0.02], facecolor=axcolor)
ax_thetaI = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_CpA = plt.axes([0.1, 0.60, 0.2, 0.02], facecolor=axcolor)
ax_CpI = plt.axes([0.1, 0.55, 0.2, 0.02], facecolor=axcolor)


sT0 = Slider(ax_T0, r'$T_0 (K)$', 300, 650, valinit=480,valfmt='%1.0f')
sdH = Slider(ax_dH, r'$-\Delta H_{Rx}^\circ$ ($\frac{cal}{mol}$)',1000, 25000, valinit=14000,valfmt='%1.0f')
sKe1 = Slider(ax_Ke1, r'$K_{e1}$',1000, 150000, valinit=75000,valfmt='%1.0f')
sthetaI = Slider(ax_thetaI, r'$\theta_I$',0.02, 4, valinit=1,valfmt='%1.2f')
sCpA = Slider(ax_CpA, r'C$_{P_A}$ ($\frac{cal}{mol. K}$)',5, 150, valinit=25,valfmt='%1.1f')
sCpI = Slider(ax_CpI, r'C$_{P_I}$ ($\frac{cal}{mol. K}$)',10, 250, valinit=50,valfmt='%1.1f')

def update_plot(val):
    T0 = sT0.val
    dH = -sdH.val
    Ke1 = sKe1.val
    thetaI = sthetaI.val
    CpA = sCpA.val
    CpI = sCpI.val
    Ke = Ke1 * np.exp((dH/R) * (T - 298) / (T * 298))
    Xe=Ke/(1+Ke)
    XEB=(CpA+thetaI*CpI)*(T-T0)/(-dH) 
    p1.set_ydata(Xe)
    p2.set_ydata(XEB)
    fig.canvas.draw_idle()

sT0.on_changed(update_plot)
sdH.on_changed(update_plot)
sKe1.on_changed(update_plot)
sthetaI.on_changed(update_plot)
sCpA.on_changed(update_plot)
sCpI.on_changed(update_plot)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sT0.reset()
    sdH.reset()
    sKe1.reset()
    sthetaI.reset()
    sCpA.reset()
    sCpI.reset()
        
button.on_clicked(reset)    


