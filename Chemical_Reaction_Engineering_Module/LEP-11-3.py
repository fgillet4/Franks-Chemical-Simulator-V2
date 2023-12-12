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
Ca0 = 9.3;
To = 330; 
dH = -6900; 
Kc0 = 3.03; 
yA0 = 0.9;
FT0 = 163; 
CpI = 161;
CpA=  141;
Ea=65700;
A=1.0728*10**11;
def ODEfun(Yfuncvec, V, Ca0,To, dH,Kc0,FT0,yA0,
           CpI,CpA,Ea,A):
    X= Yfuncvec[0]
    #Explicit Equation Inline
    thetaI=(1-yA0)/yA0;
    Sumcp=CpA+ thetaI* CpI;
    T = To + (-dH/Sumcp) * X; 
    Fa0=yA0*FT0;
    Kc = Kc0 * np.exp((dH/8.314) * (T - 333) / (T * 333)); 
    k = A * np.exp(-Ea/(8.314*T)); 
    ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X)));  
    # Differential equations
    dXdV = 0 - (ra / Fa0); 
    return np.array([dXdV])

Vspan = np.linspace(0, 5, 100) # Range for the independent variable
y0 = np.array([0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.37)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""LEP-11-3: Adiabatic Liquid-Phase Isomerization of Normal Butane""", fontweight='bold', x = 0.22)

sol = odeint(ODEfun, y0, Vspan, (Ca0,To, dH,Kc0,FT0,yA0,CpI,CpA,Ea,A))
X = sol[:, 0]
thetaI=(1-yA0)/yA0;
Sumcp=CpA+ thetaI* CpI;
T = To + (-dH/Sumcp) * X; 
Fa0=yA0*FT0;
Kc = Kc0 * np.exp((dH/8.314) * (T - 333) / (T * 333)); 
k = A * np.exp(-Ea/(8.314*T)); 
Xe = Kc / (1 + Kc); 
ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X))); 
rate = 0 - ra; 
p1= ax2.plot(Vspan,T)[0]
ax2.legend(['T'], loc='upper right')
ax2.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax2.set_ylabel('Temperature (K)', fontsize='medium')
ax2.set_ylim(300,450)
ax2.set_xlim(0,5)
ax2.grid()

p2,p4 = ax3.plot(Vspan,X,Vspan,Xe)
ax3.legend(['X','$X_e$'], loc='upper right')
ax3.set_ylim(0,1)
ax3.set_xlim(0,5)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium')

p3 = ax4.plot(Vspan, rate)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_ylim(0,140)
ax4.set_xlim(0,5)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax4.set_ylabel('$Rate {(kmol/ m^3.h)}$', fontsize='medium')

ax1.axis('off')
ax1.text(-1.48, -1.35,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-1.45,-1.0,'Differential Equations'
         '\n\n'
        r'$\dfrac{dX}{dV} = \dfrac{-r_{A}}{F_{A0}}$'
                  '\n \n'  
         'Explicit Equations'
                  '\n\n'
                  r'$A = 1.0728*10^{11}\thinspace hr^{-1}$'
                '\n\n'
                r'$F_{T0} = 163\thinspace kmol/h$'
                '\n\n'
         r'$T=T_0 +\dfrac{(-\Delta H_{Rx}^\circ)*X}{\sum_{i}\theta_iC_{pi}}$'   
         '\n'
         r'$K_c = K_{C0}*exp\left(\left(\dfrac{\Delta H_{Rx}^\circ}{8.314}\right)\left(\dfrac{1}{333} - \dfrac{1}{T}\right)\right)$'
                  '\n'
         r'$X_e = \dfrac{K_c}{1+K_c}$'
         '\n'
          r'$k = A*exp\left(\dfrac{-E}{8.314*T}\right)$'
         '\n'
         r'$F_{A0} = y_{A0}*F_{T0}$'
                  '\n'
         r'$\theta_I=\dfrac{(1-y_{A0})}{y_{A0}}$'
         '\n'         
         r'$\sum_{i}\theta_iC_{pi} = C_{P_A} +\theta_IC_{P_I} $'
         '\n'
         r'$-r_A = kC_{A0}\left[1 - \left(1+\dfrac{1}{K_C}\right) X\right]$'
                  '\n'
         r'$rate = -r_A$'
                 '\n'
       , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_Ca0 = plt.axes([0.32, 0.80, 0.2, 0.015], facecolor=axcolor)
ax_To = plt.axes([0.32, 0.75, 0.2, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.32, 0.70, 0.2, 0.015], facecolor=axcolor)
ax_Kc0 = plt.axes([0.32, 0.65, 0.2, 0.015], facecolor=axcolor)
ax_yA0 = plt.axes([0.32, 0.60, 0.2, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.32, 0.55, 0.2, 0.015], facecolor=axcolor)

sCa0 = Slider(ax_Ca0, r'C$_{A0}$($\frac{kmol}{m^3}$)', 1, 20, valinit=9.3,valfmt='%1.1f')
sTo = Slider(ax_To, 'T$_{0}$ ($K$)', 300, 450, valinit=330,valfmt='%1.0f')
sdH= Slider(ax_dH, r'$\Delta H_{Rx}^\circ$ ($\frac{J}{mol}$)', -15000, -1000, valinit=-6900,valfmt='%1.0f')
sKc0 = Slider(ax_Kc0,'$K_{C0}$',0.1, 10, valinit=3.03,valfmt='%1.2f')
syA0 = Slider(ax_yA0, r'y$_{A0}$', 0.05, 1, valinit=0.9,valfmt='%1.2f')
sEa = Slider(ax_Ea, r'$E (\frac{J}{mol})$', 45000, 80000, valinit=65700, valfmt = "%1.0f")

def update_plot2(val):
    Ca0 = sCa0.val
    To =sTo.val
    dH =sdH.val
    Kc0 = sKc0.val
    yA0 = syA0.val
    Ea = sEa.val
    sol = odeint(ODEfun, y0, Vspan, (Ca0,To, dH,Kc0,FT0,yA0,CpI,CpA,Ea,A))
    X = sol[:, 0]
    thetaI=(1-yA0)/yA0;
    Sumcp=CpA+ thetaI* CpI;
    T = To + (-dH/Sumcp) * X; 
    Kc = Kc0 * np.exp((dH/8.314) * (T - 333) / (T * 333));  
    k = A * np.exp(-Ea/(8.314*T)); 
    Xe = Kc / (1 + Kc); 
    ra = 0 - (k * Ca0 * (1 - ((1 + 1 / Kc) * X))); 
    rate = 0 - ra;    
    p1.set_ydata(T)
    p2.set_ydata(X)
    p4.set_ydata(Xe)
    p3.set_ydata(rate)
    fig.canvas.draw_idle()

sCa0.on_changed(update_plot2)
sTo.on_changed(update_plot2)
sdH.on_changed(update_plot2)
sKc0.on_changed(update_plot2)
syA0.on_changed(update_plot2)
sEa.on_changed(update_plot2)

resetax = plt.axes([0.37, 0.86, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCa0.reset()
    sTo.reset()
    sdH.reset()
    sKc0.reset()
    syA0.reset()
    sEa.reset()

button.on_clicked(reset)
    
