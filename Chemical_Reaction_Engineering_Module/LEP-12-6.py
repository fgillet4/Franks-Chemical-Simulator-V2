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
Cp=200
Cao=0.3
To=283
DH1=-55000
DH2=-71500
vo=1000
E2=27000
E1=9900
UA=40000
Ta=330
V=10
A1 = 5.386*10**7;
A2 = 2.908*10**12;
T = np.linspace(250, 750, 100)
def func(T,Cp,Cao,To,DH1,DH2,vo,E2,E1,UA,Ta,V,A1,A2):
    k1=A1*np.exp(-E1/(1.987*T))
    k2=A2*np.exp(-E2/(1.987*T))
    tau=V/vo
    kappa=UA/(vo*Cao*Cp)
    Tc=(To+kappa*Ta)/(1+kappa)
    R=Cp*(1+kappa)*(T-Tc)
    G=-tau*k1/(1+k1*tau)*DH1-k1*tau*k2*tau*DH2/((1+tau*k1)*(1+tau*k2))
    return np.array([G, R])
    

#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 12-6 Multiple Reactions in a CSTR""", fontweight='bold', x = 0.15, y= 0.98)
plt.subplots_adjust(left  = 0.55)

sol = func(T,Cp,Cao,To,DH1,DH2,vo,E2,E1,UA,Ta,V,A1,A2)
G = sol[0, :]
R = sol[1, :]

p1, p2 = ax.plot(T,G, T,R)
ax.legend(['$G (T)$', '$R (T)$'], loc='best')
ax.set_xlabel(r'Temperature $(K)$', fontsize='medium')
ax.set_ylabel(r'$G(T), R(T) \hspace{1} (J/mol)$', fontsize='medium')
ax.set_xlim(250,750)
ax.set_ylim(0,150000)
ax.ticklabel_format(style='sci',scilimits=(4,4),axis='y')
ax.grid()

ax.text(-500, 15000,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax.text(-500, 50000,
         '\n'         
         'Equations'
                  '\n\n'
         r'$A_1 = 5.386*10^{7}\thinspace min^{-1}$'
          '\n'
         r'$A_2 = 2.908*10^{12}\thinspace min^{-1}$'
          '\n' 
         r'$k_{1} = A_1*exp\left(\dfrac{-E_1}{1.987*T}\right)$'
                  '\n\n'
         r'$k_{2} = A_2*exp\left(\dfrac{-E_2}{1.987*T}\right)$'
         '\n\n'
         r'$\tau=V/v_0$'
         '\n\n'
         r'$\kappa=\dfrac{UA}{F_{A0}*C_{P_A}}$'
         '\n\n'
         r'$ T_C=\dfrac{T_0+ \kappa*T_a}{1+\kappa}$'
         '\n\n'
         r'$ R(T)=C_{P_A}*(1+\kappa)\left[T-T_C\right]$'
         '\n\n'
         r'$ G(T)=\left[\dfrac{-\Delta H_{Rx1A}\tau k_1}{1+\tau  k_1}-\dfrac{\tau k_1*\tau k_2* \Delta H_{Rx2B}}{(1+\tau k_1)(1+\tau k_2)}\right]$'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_Cp = plt.axes([0.33, 0.8, 0.12, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.33, 0.75, 0.12, 0.02], facecolor=axcolor)
ax_To = plt.axes([0.33, 0.7, 0.12, 0.02], facecolor=axcolor)
ax_DH1 = plt.axes([0.33, 0.65, 0.12, 0.02], facecolor=axcolor)
ax_DH2 = plt.axes([0.33, 0.6, 0.12, 0.02], facecolor=axcolor)
ax_vo = plt.axes([0.33, 0.55, 0.12, 0.02], facecolor=axcolor)
ax_E1 = plt.axes([0.33, 0.50, 0.12, 0.02], facecolor=axcolor)
ax_E2 = plt.axes([0.33, 0.45, 0.12, 0.02], facecolor=axcolor)
ax_UA = plt.axes([0.33, 0.40, 0.12, 0.02], facecolor=axcolor)
ax_Ta = plt.axes([0.33, 0.35, 0.12, 0.02], facecolor=axcolor)
ax_V = plt.axes([0.33, 0.30, 0.12, 0.02], facecolor=axcolor)


sCp = Slider(ax_Cp, r'$C_P (\frac{J}{mol.K})$', 10, 500, valinit=200,valfmt='%1.0f')
sCao = Slider(ax_Cao, r'$C_{A0}(\frac{mol}{dm^3}) $', 0.05, 1, valinit=0.3,valfmt='%1.2F')
sTo = Slider(ax_To, r'$T_0 (K)$', 273, 1000, valinit=283,valfmt='%1.1f')
sDH1 = Slider(ax_DH1, r'$\Delta H_{Rx1A} (\frac{J}{mol A})$', -70000, -25000, valinit=-55000,valfmt='%1.0f')
sDH2 = Slider(ax_DH2, r'$\Delta H_{Rx2B} (\frac{J}{mol B})$', -90000,-20000, valinit=-71500,valfmt='%1.0f')
svo= Slider(ax_vo, r'$v_0 (\frac{dm^3}{min})$', 500, 3000, valinit=1000,valfmt='%1.0f')
sE1= Slider(ax_E1, r'$E_1  (\frac{cal}{mol})$', 5000, 20000, valinit=9900,valfmt='%1.0f')
sE2= Slider(ax_E2, r'$E_2  (\frac{cal}{mol})$', 10000, 50000, valinit=27000,valfmt='%1.0f')
sUA= Slider(ax_UA, r'$UA (\frac{J}{min.K})$', 10000, 80000, valinit=40000,valfmt='%1.0f')
sTa= Slider(ax_Ta, r'$T_{a} (K)$', 250, 1000, valinit=330,valfmt='%1.0f')
sV= Slider(ax_V, r'$V (dm^3)$', 1, 100, valinit=10,valfmt='%1.1f')

def update_plot2(val):
    Cp = sCp.val    
    Cao =sCao.val
    To=sTo.val
    DH1=sDH1.val
    DH2=sDH2.val
    vo=svo.val
    E1=sE1.val
    E2=sE2.val
    UA=sUA.val
    Ta=sTa.val
    V=sV.val
    sol = func(T,Cp,Cao,To,DH1,DH2,vo,E2,E1,UA,Ta,V,A1,A2)
    G = sol[0, :]
    R = sol[1, :]
    p1.set_ydata(G)
    p2.set_ydata(R)
    fig.canvas.draw_idle()


sCp.on_changed(update_plot2)
sCao.on_changed(update_plot2)
sTo.on_changed(update_plot2)
sDH1.on_changed(update_plot2)
sDH2.on_changed(update_plot2)
svo.on_changed(update_plot2)
sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)
sUA.on_changed(update_plot2)
sTa.on_changed(update_plot2)
sV.on_changed(update_plot2)

resetax = plt.axes([0.34, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCp.reset()
    sCao.reset()
    sTo.reset()
    sDH1.reset()
    sDH2.reset()
    svo.reset()
    sE1.reset()
    sE2.reset()
    sUA.reset()
    sTa.reset()
    sV.reset()
button.on_clicked(reset)    

