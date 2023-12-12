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
CT0=0.1;
UA=4000;
dHrx1=-20000;
dHrx2=-60000;
k1a0=10;
k2a0=0.09;
Ta=373;
To=423;
E1=33256
E2=74826
A1=6.174*10**6
A2=9.618*10**11
def ODEfun(Yfuncvec, V,CT0,UA,dHrx1,dHrx2,k1a0,k2a0,Ta,To,E1,E2,A1,A2):
    Fa= Yfuncvec[0]
    Fb= Yfuncvec[1]
    Fc= Yfuncvec[2]
    T= Yfuncvec[3]
        #Explicit Equation Inline
    Ft = Fa + Fb + Fc; 
    Ca = CT0 * Fa / Ft * To / T; 
    k1a = A1*np.exp(-E1/(8.314 *T)); 
    k2a = A2*np.exp(-E2/(8.314*T)); 
    r1a = 0 - (k1a * Ca); 
    r2a = 0 - (k2a * Ca** 2);
    # Differential equations
    dFadV = r1a + r2a; 
    dFbdV = 0 - r1a;
    dFcdV = 0 - (r2a / 2);
    dTdV = (UA * (Ta - T) + (0 - r1a) *(-dHrx1) + (0 - r2a) *(-dHrx2)) / (90 * Fa + 90 * Fb + 180 * Fc); 
    return np.array([dFadV,dFbdV,dFcdV,dTdV])

Vspan = np.linspace(0, 1, 5000) # Range for the independent variable
y0 = np.array([100,0,0,423]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-12-5: Parallel Reactions in a PFR with Heat Effects""", fontweight='bold', x = 0.2,y=0.97)
plt.subplots_adjust(left  = 0.35)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, Vspan, (CT0,UA,dHrx1,dHrx2,k1a0,k2a0,Ta,To,E1,E2,A1,A2))
Fa =sol[:, 0]
Fb = sol[:, 1]
Fc = sol[:, 2]
T=sol[:,3]
Ft = Fa + Fb + Fc; 
Ca = CT0 * Fa / Ft * To / T; 
Cb = CT0 * Fb / Ft * To / T; 
Cc = CT0 * Fc / Ft * To / T;

k1a = A1*np.exp(-E1/(8.314 *T)); 
k2a = A2*np.exp(-E2/(8.314*T)); 
r1a = 0 - (k1a * Ca); 
r2a = 0 - (k2a * Ca** 2);
Qg=(0 - r1a) *(-dHrx1) + (0 - r2a) *(-dHrx2)
Qr=UA*(T-Ta)
p1= ax2.plot(Vspan,T)[0]
ax2.legend(['T'], loc='upper right')
ax2.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax2.set_ylabel('Temperature (K)', fontsize='medium')
ax2.set_ylim(300,1100)
ax2.set_xlim(0,1)
ax2.grid()
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p2,p3,p4 = ax3.plot(Vspan,Fa,Vspan,Fb,Vspan,Fc)
ax3.legend(['F$_A$','F$_B$','F$_C$'], loc='upper right')
ax3.set_ylim(0,100)
ax3.set_xlim(0,1)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax3.set_ylabel('$F_i$ (mol/s)', fontsize='medium')
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
p5,p6 = ax4.plot(Vspan, Qg, Vspan, Qr)
ax4.legend(['$Q_g$','$Q_r$'], loc='upper right')
ax4.set_ylim(0,9*10**7)
ax4.set_xlim(0,1)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax4.set_ylabel(r'$Q {(J/m^3.s)}$', fontsize='medium')
ax4.ticklabel_format(style='sci',scilimits=(0,0),axis='x')

ax1.axis('off')
ax1.text(-1.35, -1.55,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-1.35, -1.25,
         'Differential Equations'
         '\n'
         r'$\dfrac{dF_A}{dV} = r_{1A}+r_{2A}$'
         '\n'
         r'$\dfrac{dF_B}{dV} = -r_{1A}$'
         '\n'
         r'$\dfrac{dF_C}{dV} =\dfrac{-r_{2A}}{2}$'
        '\n'
         r'$\dfrac{dT}{dV} = \dfrac{(Q_g-Q_r)}{\sum_{i} F_i C_{P_i}}$'
                  '\n'
                  
         'Explicit Equations'
                  '\n'
         r'$A_1 = 6.174*10^{6}\thinspace s^{-1}$'
          '\n'
         r'$A_2 = 9.618*10^{11}\thinspace s^{-1}$'
          '\n' 
         r'$k_{1A} = A_1*exp\left(\dfrac{-E_1}{8.314*T}\right)$'
                  '\n\n'
         r'$k_{2A} = A_2*exp\left(\dfrac{-E_2}{8.314*T}\right)$'
         '\n\n'
         r'$F_T=F_A+F_B+F_C $' 
         '\n'
         r'$r_A =r_{1A}+r_{2A}$'
         '\n'
         r'$C_A=C_{T0}*\left(\dfrac{F_A}{F_T}\right)*\left(\dfrac{T_0}{T}\right)$'
         '\n'
         r'$C_B=C_{T0}*\left(\dfrac{F_B}{F_T}\right)*\left(\dfrac{T_0}{T}\right)$'
         '\n'
         r'$C_C=C_{T0}*\left(\dfrac{F_C}{F_T}\right)*\left(\dfrac{T_0}{T}\right)$'
         '\n\n'
         r'$r_{1A} = -k_{1A}. C_A$'
         '\n'
         r'$r_{2A} = -k_{2A}.(C_A)^2$'
                  '\n'
         r'$S_{B/C}\thinspace overall = \dfrac{F_B}{F_C}$'
         '\n'
         r'$S_{B/C}\thinspace instantaneous = \dfrac{-r_{1A}}{-0.5 r_{2A}}$'
               '\n\n'
         r'$Q_{g} = (-r_{1A})(-\Delta H_{Rx1A})+(-r_{2A})(-\Delta H_{Rx2A})$'
         '\n'
          r'$Q_{r} = Ua*(T-T_a)$'
        , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

axcolor = 'black'
ax_CT0 = plt.axes([0.35, 0.80, 0.17, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.35, 0.76, 0.17, 0.015], facecolor=axcolor)
ax_dHrx1 = plt.axes([0.35, 0.72, 0.17, 0.015], facecolor=axcolor)
ax_dHrx2 = plt.axes([0.35, 0.68, 0.17, 0.015], facecolor=axcolor)
ax_Ta = plt.axes([0.35, 0.64, 0.17, 0.015], facecolor=axcolor)
ax_E1 = plt.axes([0.35, 0.60, 0.17, 0.015], facecolor=axcolor)
ax_E2 = plt.axes([0.35, 0.56, 0.17, 0.015], facecolor=axcolor)

sCT0 = Slider(ax_CT0, r'C$_{T0}$($\frac{mol}{dm^3}$)', 0.01, 1, valinit=0.1,valfmt='%1.2f')
sUA = Slider(ax_UA, r'Ua ($\frac{J}{m^3.s.degC}$)', 100, 20000, valinit=4000,valfmt='%1.0f')
sdHrx1= Slider(ax_dHrx1, r'$\Delta H_{Rx1A}$ ($\frac{J}{mol}$)', -80000, -5000, valinit=-20000,valfmt='%1.0f')
sdHrx2 = Slider(ax_dHrx2, r'$\Delta H_{Rx2A}$ ($\frac{J}{mol}$)',-120000, -5000, valinit=-60000,valfmt='%1.0f')
sTa = Slider(ax_Ta, r'T$_a$(K)', 273, 473, valinit=373,valfmt='%1.0f')
sE1 = Slider(ax_E1, r'E$_1$($\frac{J}{mol}$)', 10000, 60000, valinit=33256,valfmt='%1.0f')
sE2 = Slider(ax_E2, r'E$_2$($\frac{J}{mol}$)', 50000, 100000, valinit=74826,valfmt='%1.0f')

def update_plot2(val):
    CT0 = sCT0.val
    UA =sUA.val
    dHrx1 =sdHrx1.val
    dHrx2 = sdHrx2.val
    Ta = sTa.val
    E1 = sE1.val
    E2 = sE2.val
    sol = odeint(ODEfun, y0, Vspan, (CT0,UA,dHrx1,dHrx2,k1a0,k2a0,Ta,To,E1,E2,A1,A2))
    Fa =sol[:, 0]
    Fb = sol[:, 1]
    Fc = sol[:, 2]
    T=sol[:,3]
    Ft = Fa + Fb + Fc; 
    Ca = CT0 * Fa / Ft * To / T; 
    k1a = A1*np.exp(-E1/(8.314 *T)); 
    k2a = A2*np.exp(-E2/(8.314*T)); 
    r1a = 0 - (k1a * Ca); 
    r2a = 0 - (k2a * Ca** 2); 
    Qg=(0 - r1a) *(-dHrx1) + (0 - r2a) *(-dHrx2)
    Qr=UA*(T-Ta)
    p1.set_ydata(T)
    p2.set_ydata(Fa)
    p3.set_ydata(Fb)
    p4.set_ydata(Fc)
    p5.set_ydata(Qg)
    p6.set_ydata(Qr)
    fig.canvas.draw_idle()


sCT0.on_changed(update_plot2)
sUA.on_changed(update_plot2)
sdHrx1.on_changed(update_plot2)
sdHrx2.on_changed(update_plot2)
sTa.on_changed(update_plot2)
sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)

resetax = plt.axes([0.39, 0.84, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCT0.reset()
    sUA.reset()
    sdHrx1.reset()
    sdHrx2.reset()
    sTa.reset()
    sE1.reset()
    sE2.reset()
    
button.on_clicked(reset)
    
