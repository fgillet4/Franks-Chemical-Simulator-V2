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
Ca0 = 1.86;
dH = -34500; 
Cpc = 28; 
mc = 500; 
UA = 5000; 
FT0 = 163; 
yA0 = 0.9; 
CpI = 161;
CpA=  141;
Ea=65700;
A=1.073*10**11

def ODEfun(Yfuncvec, V, Ca0,dH,Cpc,mc,UA,FT0,yA0,CpI,CpA,Ea,A):
    Ta= Yfuncvec[0]
    T= Yfuncvec[1]
    X= Yfuncvec[2]
    thetaI=(1-yA0)/yA0;
    sumcp=CpA+ thetaI* CpI;
    Fa0=yA0*FT0/10;
        #Explicit Equation Inline
    k = A*np.exp(-Ea/(8.31*T)); 
    Kc = 3.03 * np.exp((dH/8.314) * (T - 333) / (T * 333)); 
    ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X))); 
    Xe = Kc / (1 + Kc); 
    Qg=ra*dH;
    Qr=UA*(T-Ta);
    rate=-ra
    # Differential equations
    dTadV = UA * (T - Ta) / (mc*Cpc); 
    dTdV = (ra * dH - (UA * (T - Ta))) / (sumcp * Fa0); 
    dXdV = 0 - (ra / Fa0);  
    return np.array([dTadV,dTdV,dXdV])

Vspan = np.linspace(0, 5, 1000) # Range for the independent variable
y0 = np.array([315,305,0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.43)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""LEP-12-1a: Butane Isomerization (Co-current)""", fontweight='bold', x = 0.18,y=0.97)

sol = odeint(ODEfun, y0, Vspan, (Ca0,dH,Cpc,mc,UA,FT0,yA0,CpI,CpA,Ea,A))
Ta =sol[:, 0]
T = sol[:, 1]
X = sol[:, 2]
k = A*np.exp(-Ea/(8.31*T));  
Kc = 3.03 * np.exp((dH/8.314) * (T - 333) / (T * 333)); 
ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X))); 
rate=-ra;
Xe = Kc / (1 + Kc); 
Qg=ra*dH;
Qr=UA*(T-Ta);
p1,p2= ax1.plot(Vspan,T,Vspan,Ta)
ax1.legend(['T','$T_a$'], loc='upper right')
ax1.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax1.set_ylabel('Temperature (K)', fontsize='medium')
ax1.set_ylim(300,400)
ax1.set_xlim(0,5)
ax1.grid()
ax1.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p3,p4 = ax2.plot(Vspan,X,Vspan,Xe)
ax2.legend(['X','$X_e$'], loc='upper right')
ax2.set_ylim(0,1)
ax2.set_xlim(0,5)
ax2.grid()
ax2.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p5 = ax4.plot(Vspan, rate)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_ylim(0,50)
ax4.set_xlim(0,5)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax4.set_ylabel('$Rate {(kmol/m^3.h)}$', fontsize='medium')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p6,p7 = ax3.plot(Vspan, Qg, Vspan, Qr)
ax3.legend(['$Q_g$','$Q_r$'], loc='upper right')
ax3.set_ylim(0,1000000)
ax3.set_xlim(0,5)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax3.set_ylabel(r'$Q {(kJ/m^3.hr)}$', fontsize='medium')
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

#ax1.axis('off')
ax1.text(-10,180,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-9.9, 220,'Differential Equations'
         '\n'
         r'$\dfrac{dT_a}{dV} = \dfrac{Ua*(T-T_a)}{m_c*C_{P_{c}}}$'
         '\n'
         r'$\dfrac{dT}{dV} = \dfrac{r_{A}\Delta H_{Rx}-Ua*(T-T_a)}{F_{A0}.\sum_{i}\theta_iC_{P_i}}$'
         '\n'
         r'$\dfrac{dX}{dV} = \dfrac{-r_{A}}{F_{A0}}$'
                  '\n \n'
                  
         'Explicit Equations'
                  '\n\n'
          r'$A = 1.0728*10^{11}\thinspace hr^{-1}$'
          '\n'
          r'$F_{T0} = 163\thinspace kmol/h$'
                '\n'
         r'$K_c = 3.03*exp\left(\left(\dfrac{\Delta H_{Rx}}{8.314}\right)\left(\dfrac{1}{333} - \dfrac{1}{T}\right)\right)$'
                  '\n'
         r'$X_e = \dfrac{K_c}{1+K_c}$'
         '\n'
         r'$k = A*exp\left(\dfrac{-E}{8.31*T}\right)$'
         '\n'
         r'$F_{A0} = \dfrac{y_{A0}.F_{T0}}{10}$'
                  '\n'
        r'$\theta_I=\dfrac{(1-y_{A0})}{y_{A0}}$'
         '\n'
         r'$\sum_{i}\theta_iC_{pi} = C_{P_A} +\theta_IC_{P_I} $'
         '\n'
         r'$r_A = -kC_{A0}\left[1 - \left(1+\dfrac{1}{K_C}\right) X\right]$'
                  '\n'
         r'$rate = -r_A$'
                 '\n'
         r'$Q_g = r_{A}.\Delta H_{Rx}$'
                  '\n'
         r'$Q_r = Ua(T-T_a)$', ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_Ca0 = plt.axes([0.24, 0.78, 0.1, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.24, 0.74, 0.1, 0.015], facecolor=axcolor)
ax_Cpc = plt.axes([0.24, 0.70, 0.1, 0.015], facecolor=axcolor)
ax_mc = plt.axes([0.24, 0.66, 0.1, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.24, 0.62, 0.1, 0.015], facecolor=axcolor)
ax_yA0 = plt.axes([0.24, 0.58, 0.1, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.24, 0.54, 0.1, 0.015], facecolor=axcolor)

sCa0 = Slider(ax_Ca0, r'C$_{A0}$($\frac{mol}{dm^3}$)', 0.5, 20, valinit=1.86,valfmt='%1.1f')
sdH= Slider(ax_dH, r'$\Delta H_{Rx}$ ($\frac{J}{mol}$)', -50000, -10000, valinit=-34500,valfmt='%1.0f')
sCpc = Slider(ax_Cpc,r'C$_{P_C}$($\frac{kJ}{kg.K}$)',10, 200, valinit=28,valfmt='%1.1f')
smc = Slider(ax_mc,r'm$_{c}$ ($\frac{kg}{hr}$)', 100, 1000, valinit= 500,valfmt='%1.0f')
sUA = Slider(ax_UA,r'Ua ($\frac{kJ}{m^3.hr.K}$)', 1000, 10000, valinit=5000,valfmt='%1.0f')
syA0 = Slider(ax_yA0, r'y$_{A0}$', 0.05, 1, valinit=0.9,valfmt='%1.2f')
sEa= Slider(ax_Ea, r'$E$ ($\frac{J}{mol}$)', 40000, 80000, valinit=65700,valfmt='%1.0f')

def update_plot2(val):
    Ca0 = sCa0.val
    dH =sdH.val
    Cpc = sCpc.val
    mc =smc.val
    UA = sUA.val
    yA0 = syA0.val
    Ea= sEa.val
    sol = odeint(ODEfun, y0, Vspan, (Ca0,dH,Cpc,mc,UA,FT0,yA0,CpI,CpA,Ea,A))
    Ta = sol[:, 0]
    T = sol[:, 1]
    X = sol[:, 2]
    thetaI=(1-yA0)/yA0;
    sumcp=CpA+ thetaI* CpI;
    Fa0=yA0*FT0/10;
        #Explicit Equation Inline
    k = A*np.exp(-Ea/(8.314*T));
    Kc = 3.03 * np.exp((dH/8.314) * (T - 333) / (T * 333)); 
    ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X))); 
    rate=-ra;
    Xe = Kc / (1 + Kc); 
    Qg=ra*dH;
    Qr=UA*(T-Ta);   
    p1.set_ydata(T)
    p2.set_ydata(Ta)
    p3.set_ydata(X)
    p4.set_ydata(Xe)
    p5.set_ydata(rate)
    p6.set_ydata(Qg)
    p7.set_ydata(Qr)
    fig.canvas.draw_idle()


sCa0.on_changed(update_plot2)
sdH.on_changed(update_plot2)
sCpc.on_changed(update_plot2)
smc.on_changed(update_plot2)
sUA.on_changed(update_plot2)
syA0.on_changed(update_plot2)
sEa.on_changed(update_plot2)

resetax = plt.axes([0.24, 0.84, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCa0.reset()
    sdH.reset()
    sCpc.reset()
    smc.reset()
    sUA.reset()
    syA0.reset()
    sEa.reset()
button.on_clicked(reset)
    
