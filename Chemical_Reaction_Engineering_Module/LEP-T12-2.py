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
alpha = .0002
To = 330
Uarho = 0.5
Mc = 1000
Cpmc = 18
Hr = -20000
Fao = 5
thetaI = 1
CpI = 40
CpA = 20
thetaB = 1
CpB = 20
Cto = 0.3
Ea = 25000
A = 1.692*10**15;
def ODEfun(Yfuncvec, W, alpha,To, Uarho,Mc,Cpmc,Hr,
           Fao, thetaI, CpI, CpA, thetaB, CpB, Cto,Ea,A):
    
    Ta= Yfuncvec[0]
    p= Yfuncvec[2]
    T= Yfuncvec[1]
    X= Yfuncvec[3]
    #Explicit Equation Inline
    Kc = 1000*(np.exp(Hr/1.987*(1/303-1/T)))
    ka = A*np.exp(-Ea/(1.987*T))
    yao = 1/(1+thetaB+thetaI)
    Cao = yao*Cto
    sumcp = (thetaI*CpI+CpA+thetaB*CpB)
    Ca = Cao*(1-X)*p*To/T
    Cb = Cao*(1-X)*p*To/T
    Cc = Cao*2*X*p*To/T
    ra = -ka*(Ca*Cb-Cc**2/Kc)
    # Differential equations
    dTadW = Uarho*(T-Ta)/(Mc*Cpmc)
    dpdW = -alpha/2*(T/To)/p
    dTdW = (Uarho*(Ta-T)+(-ra)*(-Hr))/(Fao*sumcp)
    dXdW = -ra/Fao
    return np.array([dTadW, dTdW, dpdW , dXdW])

Wspan = np.linspace(0, 4500, 10000) # Range for the independent variable
y0 = np.array([320, 330, 1, 0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-T12-2: Heat Effects in Tubular Reactor with a Gas Phase Reaction""", fontweight='bold', x = 0.25, y=0.99)
plt.subplots_adjust(left  = 0.36)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, Wspan, (alpha, To, Uarho, Mc, Cpmc, Hr, Fao, thetaI, 
                                 CpI, CpA, thetaB, CpB, Cto, Ea,A))
Ta = sol[:, 0]
T = sol[:, 1]
p = sol[:, 2]
X = sol[:, 3]
Kc = 1000*(np.exp(Hr/1.987*(1/303-1/T)))
Xe = ((thetaB + 1)*Kc - (((thetaB + 1)*Kc)**2 - 4*(Kc - 4)*(Kc*thetaB))**0.5)/(2*(Kc - 4))

ka = A*np.exp(-Ea/(1.987*T))
yao = 1/(1+thetaB+thetaI)
Cao = yao*Cto
Ca = Cao*(1-X)*p*To/T
Cb = Cao*(1-X)*p*To/T
Cc = Cao*2*X*p*To/T
ra = -ka*(Ca*Cb-Cc**2/Kc)
Qg = ra*Hr
Qr = Uarho*(T-Ta)

p1, p2, p5 = ax2.plot(Wspan, X, Wspan, Xe, Wspan, p)
ax2.legend(['X', 'X$_{e}$', 'p'], loc='lower right')
ax2.set_xlabel('Weight (kg)', fontsize='medium', fontweight='bold')
ax2.set_ylabel('X, p', fontsize='medium', fontweight='bold')
ax2.set_ylim(0,1.05)
ax2.set_xlim(0,4500)
ax2.grid()
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p3, p4 = ax3.plot(Wspan, Ta, Wspan, T)
ax3.legend(['T$_{a}$', 'T'], loc='upper right')
ax3.set_ylim(300,400)
ax3.set_xlim(0,4500)
ax3.grid()
ax3.set_xlabel('Weight (kg)', fontsize='medium', fontweight='bold')
ax3.set_ylabel('Temperature (K)', fontsize='medium', fontweight='bold')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')


p6, p7 = ax4.plot(Wspan, Qg, Wspan, Qr)
ax4.legend(['$Q_g$', '$Q_r$'], loc='upper right')
ax4.set_ylim(0,200)
ax4.set_xlim(0,4500)
ax4.grid()
ax4.set_xlabel('Weight (kg)', fontsize='medium', fontweight='bold')
ax4.set_ylabel('Q (cal/kg.s)', fontsize='medium', fontweight='bold')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

ax1.axis('off')
ax1.text(-1.41, -1.5,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-1.35, -1.15,'Differential Equations'
         '\n'
         r'$\dfrac{dT_a}{dW} = \dfrac{Uarho*(T-T_a)}{m_c*C_{P_{cool}}}$'
         '\n'
         r'$\dfrac{dp}{dW} = -\dfrac{\alpha*T}{2.T_0.p}$'
         '\n'
         r'$\dfrac{dT}{dW} = \dfrac{Uarho*(T_a - T) + (-r^\prime_{A})(-\Delta H_{Rx})}{F_{A0}.\sum_{i}\theta_iC_{P_i}}$'
         '\n'
         r'$\dfrac{dX}{dW} = \dfrac{-r^\prime_{A}}{F_{A0}}$'
                  '\n \n'
                  
         'Explicit Equations'
                  '\n\n'
          r'$A = 1.692*10^{15}\thinspace dm^{6}/(mol.kg.s)$'
                '\n'
         r'$K_c = 1000*exp\left(\left(\dfrac{\Delta H_{Rx}}{1.987}\right)\left(\dfrac{1}{303} - \dfrac{1}{T}\right)\right)$'
                  '\n'
         r'$X_e = \dfrac{(\theta_B + 1)K_c - \sqrt{((\theta_B + 1)K_c)^2 - 4(K_c - 4)(K_c\theta_B)}}{2(K_c-4)}$'
         '\n'
         r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'   
         '\n'
         r'$y_{A0} = \dfrac{1}{1+\theta_B+\theta_I}$'
         '\n'
         r'$C_{A0} = y_{A0}.C_{T0}$'
                  '\n'
         r'$\sum_{i}\theta_iC_{pi} = \theta_IC_{P_I} + C_{P_A} + \theta_BC_{P_B}$'
         '\n'
         r'$C_A = C_{A0}(1-X).p.T_o/T$'
         '\n'
         r'$C_B = C_{A0}(\theta_B-X).p.T_o/T$'
         '\n'
         r'$C_C = 2C_{A0}.X.p.T_o/T$'
                  '\n'
         r'$r^\prime_A = -k(C_AC_B - \dfrac{C_C^2}{K_C})$'
                  '\n'
         r'$Q_g = r^\prime_{A}.\Delta H_{Rx}$'
                  '\n'
         r'$Q_r = Uarho(T-T_a)$', ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_alpha = plt.axes([0.35, 0.85, 0.2, 0.015], facecolor=axcolor)
ax_Uarho = plt.axes([0.35, 0.81, 0.2, 0.015], facecolor=axcolor)
ax_Hr = plt.axes([0.35, 0.77, 0.2, 0.015], facecolor=axcolor)
ax_Fao = plt.axes([0.35, 0.73, 0.2, 0.015], facecolor=axcolor)
ax_thetaI = plt.axes([0.35, 0.69, 0.2, 0.015], facecolor=axcolor)
ax_CpA = plt.axes([0.35, 0.65, 0.2, 0.015], facecolor=axcolor)
ax_thetaB = plt.axes([0.35, 0.61, 0.2, 0.015], facecolor=axcolor)
ax_Cto = plt.axes([0.35, 0.57, 0.2, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.35, 0.53, 0.2, 0.015], facecolor=axcolor)

salpha = Slider(ax_alpha, r'$\alpha$ ($kg^{-1}$)', .0001, 0.0002, valinit=.0002,valfmt='%1.5f')
sUarho= Slider(ax_Uarho, r'Uarho ($\frac{cal}{kg.s.K}$)', 0.05, 2, valinit=0.5)
sHr = Slider(ax_Hr, r'$\Delta H_{rx}$ ($\frac{kcal}{mol}$)', -30000, -10000, valinit= -20000,valfmt='%1.0f')
sFao = Slider(ax_Fao, r'F$_{A0}$ ($\frac{mol}{s}$)', 1, 10, valinit=5)
sthetaI = Slider(ax_thetaI, r'$\theta_{I}$', 0.2, 5, valinit=1)
sCpA = Slider(ax_CpA, r'C$_{P_A}$ ($\frac{cal}{mol.K}$)', 5, 40, valinit=20)
sthetaB = Slider(ax_thetaB, r'$\theta_{B}$', 0.2, 5, valinit=1)
sCto = Slider(ax_Cto, r'C$_{T_0}$ ($\frac{mol}{dm^3}$)', 0.05, 0.8, valinit=0.3)
sEa = Slider(ax_Ea, r'$E$ ($\frac{kcal}{mol}$)', 20000, 28000, valinit=25000,valfmt='%1.0f')


def update_plot2(val):
    alpha = salpha.val
    Uarho =sUarho.val
    Hr = sHr.val
    Fao = sFao.val
    thetaI = sthetaI.val
    CpA = sCpA.val
    thetaB = sthetaB.val
    Cto = sCto.val
    Ea = sEa.val   
    sol = odeint(ODEfun, y0, Wspan, (alpha, To, Uarho, Mc, Cpmc, Hr, Fao, thetaI, 
                                     CpI, CpA, thetaB, CpB, Cto, Ea,A))
    Ta = sol[:, 0]
    p = sol[:, 2]
    T = sol[:, 1]
    X = sol[:, 3]
    Kc = 1000*(np.exp(Hr/1.987*(1/303-1/T)))
    Xe = ((thetaB + 1)*Kc - (((thetaB + 1)*Kc)**2 - 4*(Kc - 4)*(Kc*thetaB))**0.5)/(2*(Kc - 4))
    ka = A*np.exp(-Ea/(1.987*T))
    yao = 1/(1+thetaB+thetaI)
    Cao = yao*Cto
    Ca = Cao*(1-X)*p*To/T
    Cb = Cao*(1-X)*p*To/T
    Cc = Cao*2*X*p*To/T
    ra = -ka*(Ca*Cb-Cc**2/Kc)
    Qg = ra*Hr
    Qr = Uarho*(T-Ta)    
    p1.set_ydata(X)
    p2.set_ydata(Xe)
    p3.set_ydata(Ta)
    p4.set_ydata(T)
    p5.set_ydata(p)
    p6.set_ydata(Qg)
    p7.set_ydata(Qr)
    fig.canvas.draw_idle()


salpha.on_changed(update_plot2)
sUarho.on_changed(update_plot2)
sHr.on_changed(update_plot2)
sFao.on_changed(update_plot2)
sthetaI.on_changed(update_plot2)
sCpA.on_changed(update_plot2)
sthetaB.on_changed(update_plot2)
sCto.on_changed(update_plot2)
sEa.on_changed(update_plot2)
#

resetax = plt.axes([0.4, 0.89, 0.12, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    salpha.reset()
    sUarho.reset()
    sHr.reset()
    sFao.reset()
    sthetaI.reset()
    sCpA.reset()
    sthetaB.reset()
    sCto.reset()
    sEa.reset()    
button.on_clicked(reset)
    
