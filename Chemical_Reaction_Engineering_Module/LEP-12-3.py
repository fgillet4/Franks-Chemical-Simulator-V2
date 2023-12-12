#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
dH=-36400
A=16.96*10**12
Ea=32400
T0=535
FM0=71.87
FI0=0
FB0=802.8
V=40.1
FA0=43
T = np.linspace(520, 650, 100)
def func(T,dH,A,Ea,T0,FM0,FI0,FB0,V,FA0):
    v0=(FA0/0.9232)+(FB0/3.444)+(FM0/1.5416)+(FI0/1.1)
    tau=V/v0
    k=A*np.exp(-Ea/(1.987* T))
    XMB=(tau*k)/(1+tau*k)
    thetaB=FB0/FA0
    thetaI=FI0/FA0
    thetaM=FM0/FA0
    sumCp=35+thetaB*18+thetaM*19.5+thetaI*28.1
    XEB=(sumCp*(T-T0))/(-(dH-7*(T-528)))
    return np.array([XMB, XEB])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 12-3 Production of Propylene Glycol in an Adibatic CSTR""", fontweight='bold', x = 0.25, y= 0.98)
plt.subplots_adjust(left  = 0.55)

sol = func(T,dH,A,Ea,T0,FM0,FI0,FB0,V,FA0)
XMB = sol[0, :]
XEB = sol[1, :]

p1, p2 = ax.plot(T, XMB, T, XEB)
ax.legend(['$X_{MB}$', '$X_{EB}$'], loc='best')
ax.set_xlabel(r'Temperature $(^\circ R)$', fontsize='medium')
ax.set_ylabel('$Conversion$', fontsize='medium')
ax.set_ylim(0,1)
ax.set_xlim(520,635)
ax.grid()

ax.text(345, 0.25,
                  
         'Equations'
                  '\n\n'            
          r'$\theta_B = \dfrac{F_{B0}}{F_{A0}}$'
                 '\n\n'
         r'$\theta_M = \dfrac{F_{M0}}{F_{A0}}$'
                 '\n\n'
         r'$\theta_I = \dfrac{F_{I0}}{F_{A0}}$'
                 '\n\n'        
         r'$\sum_{i}\theta_iC_{P_i}=C_{P_A}+\theta_B C_{P_B} +\theta_M C_{P_M} +\theta_I C_{P_I}$'
         '\n\n'
         r'$v_0=F_{A0}/0.9232+F_{B0}/3.444+F_{M0}/1.5416+F_{I0}/1.1 $'
         '\n\n'
         r'$\tau=V/v_0$'
         '\n\n'
         r'$k=A\thinspace exp\left(-E_a/(R T)\right) $'
         '\n\n'
         r'$X_{MB}=\dfrac{\tau k}{1+\tau k}$'
         '\n\n'
         r'$X_{EB}=\dfrac{\sum_{i}\theta_iC_{P_i} (T-T_{i0})}{-\Delta H^\circ_{Rx}+7 (T-T_R)}$'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_dH = plt.axes([0.33, 0.75, 0.1, 0.02], facecolor=axcolor)
ax_A = plt.axes([0.33, 0.7, 0.1, 0.02], facecolor=axcolor)
ax_Ea = plt.axes([0.33, 0.65, 0.1, 0.02], facecolor=axcolor)
ax_T0 = plt.axes([0.33, 0.6, 0.1, 0.02], facecolor=axcolor)
ax_FM0 = plt.axes([0.33, 0.55, 0.1, 0.02], facecolor=axcolor)
ax_FI0 = plt.axes([0.33, 0.5, 0.1, 0.02], facecolor=axcolor)
ax_FB0 = plt.axes([0.33, 0.45, 0.1, 0.02], facecolor=axcolor)
ax_V = plt.axes([0.33, 0.4, 0.1, 0.02], facecolor=axcolor)
ax_FA0 = plt.axes([0.33, 0.35, 0.1, 0.02], facecolor=axcolor)

sdH = Slider(ax_dH, r'$\Delta H^\circ_{Rx} (\frac{Btu}{lb-mol})$', -100000, -5000, valinit=-36400,valfmt='%1.0f')
sA = Slider(ax_A, r'$A$', 10**12, 100*10**12, valinit=16.96*10**12,valfmt='%1.0E')
sEa = Slider(ax_Ea, r'$E_a (\frac{Btu}{lb-mol})$', 15000, 80000, valinit=32400,valfmt='%1.0f')
sT0 = Slider(ax_T0, r'$T_{i0}$ ($^\circ R$)', 461, 700, valinit=535,valfmt='%1.0f')
sFM0 = Slider(ax_FM0, r'$F_{M0} (\frac{lbmol}{hr})$', 10, 400, valinit=71.78,valfmt='%1.2f')
sFI0 = Slider(ax_FI0, r'$F_{I0} (\frac{lbmol}{hr})$', 0, 100, valinit=0,valfmt='%1.1f')
sFB0= Slider(ax_FB0, r'$F_{B0} (\frac{lbmol}{hr})$', 100, 1500, valinit=802.8,valfmt='%1.1f')
sV= Slider(ax_V, r'$V (ft^3)$', 5, 150, valinit=40.1,valfmt='%1.1f')
sFA0= Slider(ax_FA0, r'$F_{A0} (\frac{lbmol}{hr})$', 10, 100, valinit=43,valfmt='%1.1f')


def update_plot2(val):
    dH = sdH.val    
    A =sA.val
    Ea=sEa.val
    T0=sT0.val
    FM0=sFM0.val
    FI0=sFI0.val
    FB0=sFB0.val
    V=sV.val
    FA0=sFA0.val
    sol = func(T,dH,A,Ea,T0,FM0,FI0,FB0,V,FA0)
    XMB = sol[0, :]
    XEB = sol[1, :]
    p1.set_ydata(XMB)
    p2.set_ydata(XEB)
    fig.canvas.draw_idle()


sdH.on_changed(update_plot2)
sA.on_changed(update_plot2)
sEa.on_changed(update_plot2)
sT0.on_changed(update_plot2)
sFM0.on_changed(update_plot2)
sFI0.on_changed(update_plot2)
sFB0.on_changed(update_plot2)
sV.on_changed(update_plot2)
sFA0.on_changed(update_plot2)

resetax = plt.axes([0.34, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sdH.reset()
    sA.reset()
    sEa.reset()
    sT0.reset()
    sFM0.reset()
    sFI0.reset()
    sFB0.reset()
    sV.reset()
    sFA0.reset()
button.on_clicked(reset)    

