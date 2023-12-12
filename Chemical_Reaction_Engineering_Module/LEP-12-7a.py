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
p = 1; 
E1 = 8000; 
E2 = 12000; 
Cto = 0.2; 
Cpco = 10; 
mc = 50;
To = 300; 
R = 1.987;
DH1b = -15000; 
DH2a = -10000;
Tc = 325; 
Cpa = 10; 
Cpb = 12; 
Cpc = 14;
Cpd = 16; 
Ua = 80; 
A1= 2.695*10**7
A2=1.106*10**9
def ODEfun(Yfuncvec,V,p,E1,E2,Cto,Cpco,mc,To,R,DH1b,DH2a,Tc,Cpa,Cpb,Cpc,Cpd,Ua,A1,A2):
    Fa= Yfuncvec[0]
    Fb= Yfuncvec[1]
    Fc= Yfuncvec[2]
    Fd= Yfuncvec[3]
    T= Yfuncvec[4]
    Ta= Yfuncvec[5]
    
    #Explicit Equation Inline
    Ft = Fa + Fb + Fc + Fd; 
    sumFiCpi = Cpa * Fa + Cpb * Fb + Cpc * Fc + Cpd * Fd; 
    Ca = Cto * Fa / Ft * To / T * p;
    Cb = Cto * Fb / Ft * To / T * p; 
    Cc = Cto * Fc / Ft * To / T * p; 
    k1a = A1*np.exp(-E1 /(R* T)); 
    k2c = A2*np.exp(-E2 / (R* T)); 
    r1a = 0 - (k1a * Ca * Cb** 2);
    r1c = 0 - r1a; 
    r2c = 0 - (k2c * Ca**2 * Cc**3); 
    r1b = 2 * r1a;
    rb = r1b; 
    r2a = 2 / 3 * r2c;
    rc = r1c + r2c; 
    r2d = -1 / 3 * r2c; 
    ra = r1a + r2a; 
    rd = r2d; 
    Qg = r1b * DH1b + r2a * DH2a; 
    Qr = Ua * (T - Ta); 
    # Differential equations
    dFadV = ra; 
    dFbdV = rb; 
    dFcdV = rc; 
    dFddV = rd; 
    dTdV = (Qg - Qr) / sumFiCpi; 
    dTadV = Ua * (T - Ta) / mc / Cpco;
    return np.array([dFadV, dFbdV, dFcdV, dFddV, dTdV, dTadV])

Vspan = np.linspace(0, 10, 1000) # Range for the independent variable
y0 = np.array([5, 10, 0, 0, 300, 325]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.32)
fig.suptitle("""LEP-12-7a:Complex Reactions with Heat Effects in a PFR (Co-current)""", fontweight='bold', x = 0.5,y=0.97)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, Vspan, (p,E1,E2,Cto,Cpco,mc,To,R,DH1b,DH2a,Tc,Cpa,Cpb,Cpc,Cpd,Ua,A1,A2))
Fa =sol[:, 0]
Fb = sol[:, 1]
Fc = sol[:, 2]
Fd = sol[:, 3]
T = sol[:, 4]
Ta = sol[:, 5]
Ft = Fa + Fb + Fc + Fd; 
sumFiCpi = Cpa * Fa + Cpb * Fb + Cpc * Fc + Cpd * Fd; 
Ca = Cto * Fa / Ft * To / T * p;
Cb = Cto * Fb / Ft * To / T * p; 
Cc = Cto * Fc / Ft * To / T * p; 
k1a = A1*np.exp(-E1 /(R* T)); 
k2c = A2*np.exp(-E2 / (R* T));
r1a = 0 - (k1a * Ca * Cb** 2);
r1c = 0 - r1a; 
r2c = 0 - (k2c * Ca**2 * Cc**3); 
r1b = 2 * r1a;
rb = r1b; 
r2a = 2 / 3 * r2c;
rc = r1c + r2c; 
r2d = -1 / 3 * r2c; 
ra = r1a + r2a; 
rd = r2d; 
Qg = r1b * DH1b + r2a * DH2a; 
Qr = Ua * (T - Ta);
Scd = np.nan_to_num(Fc/Fd)

p1,p2= ax2.plot(Vspan,T,Vspan,Ta)
ax2.legend(['T','$T_a$'], loc='upper right')
ax2.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax2.set_ylabel('Temperature (K)', fontsize='medium')
ax2.set_ylim(200,1400)
ax2.set_xlim(0,10)
ax2.grid()

p3,p4,p5,p6 = ax3.plot(Vspan,Fa,Vspan,Fb,Vspan,Fc,Vspan,Fd)
ax3.legend(['$F_A$','$F_B$','$F_C$','$F_D$'], loc='upper right')
ax3.set_ylim(0,10)
ax3.set_xlim(0,10)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax3.set_ylabel('$F_i$ (mol/min)', fontsize='medium')

p7 = ax4.plot(Vspan, Scd)[0]
ax4.legend(['$S_{C/D}$'], loc='upper right')
ax4.set_ylim(300,5e10)
ax4.set_xlim(0,10)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(dm^3)}$', fontsize='medium')
ax4.set_ylabel('Selectivity', fontsize='medium')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

ax1.axis('off')
ax1.text(-1.17,-1.55,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax1.text(-1.17, -1.25,'Differential Equations'
         '\n'
         r'$\dfrac{dF_A}{dV} = r_A$'
         '\n'
         r'$\dfrac{dF_B}{dV} = r_B$'
         '\n'
         r'$\dfrac{dF_C}{dV} = r_C$'
         '\n'
         r'$\dfrac{dF_D}{dV} = r_D$'
         '\n'
         r'$\dfrac{dT}{dV} = \dfrac{(Q_g -Q_r)}{\sum_{i}F_iC_{P_i}}$'
         '\n'
         r'$\dfrac{dT_a}{dV} = \dfrac{Ua*(T - T_a)}{m_{C}* C_{P_{CO}}}$'
         '\n'
          'Explicit Equations'
                  '\n'
          r'$p=1$'
            '\n'
         r'$F_T=F_A+F_B+F_C+F_D $'
                  '\n'
         r'$k_{1A} = A_1*exp\left(\dfrac{-E_1}{1.987*T}\right)$'  
           '\n'
         r'$k_{2C} = A_2*exp\left(\dfrac{-E_2}{1.987*T}\right)$'  
           '\n'
         r'$\sum_{i}F_iC_{pi} = F_A*C_{P_A} + F_B*C_{P_B} + F_C*C_{P_C}+F_D*C_{P_D}$'
         '\n'
         r'$C_A = C_{T0}*\left(\dfrac{F_A}{F_T}\right)*p*\left(\dfrac{T_0}{T}\right)$'
         '\n'
          r'$C_B = C_{T0}*\left(\dfrac{F_B}{F_T}\right)*p*\left(\dfrac{T_0}{T}\right)$'
         '\n'
          r'$C_C = C_{T0}*\left(\dfrac{F_C}{F_T}\right)*p*\left(\dfrac{T_0}{T}\right)$'
         '\n'
         r'$C_D = C_{T0}*\left(\dfrac{F_D}{F_T}\right)*p*\left(\dfrac{T_0}{T}\right)$'
         '\n'
         r'$r_{1A} = -k_{1A}*C_A *(C_B)^2$'
                  '\n'
         r'$r_{2C} = -k_{2C}*C_A^2 *(C_C)^3$'
                  '\n'
         r'$r_{1B} = 2*r_{1A}$'
                  '\n'
         r'$r_{1C} = -r_{1A}$'
                  '\n'
         r'$r_{2A} = (2/3)*r_{2C}$'
                  '\n'     
         r'$r_{2D} = (-1/3)*r_{2C}$'
                  '\n'    
         r'$r_{A} = r_{1A}+r_{2A}$'
                  '\n' 
         r'$r_{B} = r_{1B}$'
                  '\n' 
         r'$r_{C} = r_{1C}+r_{2C}$'
                  '\n'    
         r'$r_{D} = r_{2D}$'
         '\n'
         r'$Q_{g}=r_{1B}\Delta H_{Rx1B}+r_{2A}\Delta H_{Rx2A}$'
         '\n'
         r'$Q_{r}=Ua* (T-T_a)$'
         '\n'
         r'$S_{C/D}=\dfrac{F_C}{F_D}$'
        , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_E1 = plt.axes([0.32, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_E2 = plt.axes([0.32, 0.79, 0.2, 0.015], facecolor=axcolor)
ax_Cto = plt.axes([0.32, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_mc = plt.axes([0.32, 0.73, 0.2, 0.015], facecolor=axcolor)
ax_DH1b = plt.axes([0.32, 0.70, 0.2, 0.015], facecolor=axcolor)
ax_DH2a = plt.axes([0.32, 0.67, 0.2, 0.015], facecolor=axcolor)
ax_Ua = plt.axes([0.32, 0.64, 0.2, 0.015], facecolor=axcolor)
ax_Cpa = plt.axes([0.32, 0.61, 0.2, 0.015], facecolor=axcolor)
ax_Cpb = plt.axes([0.32, 0.58, 0.2, 0.015], facecolor=axcolor)
ax_Cpc = plt.axes([0.32, 0.55, 0.2, 0.015], facecolor=axcolor)
ax_Cpd = plt.axes([0.32, 0.52, 0.2, 0.015], facecolor=axcolor)


sE1 = Slider(ax_E1, r'$E_1$($\frac{cal}{mol}$)', 5000, 10000, valinit=8000,valfmt='%1.0f')
sE2= Slider(ax_E2, r'$E_2$ ($\frac{cal}{mol}$)', 100, 30000, valinit=12000,valfmt='%1.0f')
sCto = Slider(ax_Cto,r'$C_{T0}$ ($\frac{mol}{dm^3}$)', 0.05, 1, valinit= 0.2,valfmt='%1.2f')
smc = Slider(ax_mc,r'$m_C$ ($\frac{mol}{min}$)', 5, 500, valinit= 50,valfmt='%1.0f')
sDH1b = Slider(ax_DH1b, r'$\Delta H_{Rx1B}$ ($\frac{cal}{mol B}$)', -30000, -5000, valinit=-15000,valfmt='%1.0f')
sDH2a = Slider(ax_DH2a, r'$\Delta H_{Rx2A}$ ($\frac{cal}{mol A}$)',  -5000000, -2000, valinit=-10000,valfmt='%1.0f')
sUa= Slider(ax_Ua, r'Ua ($\frac{cal}{m^3.min.K}$)', 5, 500, valinit=80,valfmt='%1.0f')
sCpa = Slider(ax_Cpa,r'C$_{P_{A}}$ ($\frac{cal}{mol.K}$)', 5, 20, valinit=10,valfmt='%1.1f')
sCpb = Slider(ax_Cpb,r'C$_{P_{B}}$ ($\frac{cal}{mol.K}$)', 5, 20, valinit=12,valfmt='%1.1f')
sCpc = Slider(ax_Cpc,r'C$_{P_{C}}$ ($\frac{cal}{mol.K}$)', 5, 25, valinit=14,valfmt='%1.1f')
sCpd = Slider(ax_Cpd,r'C$_{P_{D}}$ ($\frac{cal}{mol.K}$)', 5, 25, valinit=16,valfmt='%1.1f')

def update_plot2(val):
    E1 = sE1.val
    E2 =sE2.val
    Cto =sCto.val
    mc=smc.val
    DH1b = sDH1b.val
    DH2a= sDH2a.val
    Ua= sUa.val
    Cpa = sCpa.val
    Cpb = sCpb.val
    Cpc = sCpc.val
    Cpd = sCpd.val
    sol = odeint(ODEfun, y0, Vspan, (p,E1,E2,Cto,Cpco,mc,To,R,DH1b,DH2a,Tc,Cpa,Cpb,Cpc,Cpd,Ua,A1,A2))
    Fa =sol[:, 0]
    Fb = sol[:, 1]
    Fc = sol[:, 2]
    Fd = sol[:, 3]
    T = sol[:, 4]
    Ta = sol[:, 5]
    Scd = np.nan_to_num(Fc/Fd);
    Ft = Fa + Fb + Fc + Fd; 
    sumFiCpi = Cpa * Fa + Cpb * Fb + Cpc * Fc + Cpd * Fd; 
    Ca = Cto * Fa / Ft * To / T * p;
    Cb = Cto * Fb / Ft * To / T * p; 
    Cc = Cto * Fc / Ft * To / T * p; 
    k1a = A1*np.exp(-E1 /(R* T)); 
    k2c = A2*np.exp(-E2 / (R* T));
    r1a = 0 - (k1a * Ca * Cb** 2);
    r1c = 0 - r1a; 
    r2c = 0 - (k2c * Ca**2 * Cc**3); 
    r1b = 2 * r1a;
    rb = r1b; 
    r2a = 2 / 3 * r2c;
    rc = r1c + r2c; 
    r2d = -1 / 3 * r2c; 
    ra = r1a + r2a; 
    rd = r2d; 
    Qg = r1b * DH1b + r2a * DH2a; 
    Qr = Ua * (T - Ta);  
    p1.set_ydata(T)
    p2.set_ydata(Ta)
    p3.set_ydata(Fa)
    p4.set_ydata(Fb)
    p5.set_ydata(Fc)
    p6.set_ydata(Fd)
    p7.set_ydata(Scd)
    fig.canvas.draw_idle()

sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)
sCto.on_changed(update_plot2)
smc.on_changed(update_plot2)
sDH1b.on_changed(update_plot2)
sDH2a.on_changed(update_plot2)
sUa.on_changed(update_plot2)
sCpa.on_changed(update_plot2)
sCpb.on_changed(update_plot2)
sCpc.on_changed(update_plot2)
sCpd.on_changed(update_plot2)

resetax = plt.axes([0.37, 0.86, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sE1.reset()
    sE2.reset()
    sCto.reset()
    smc.reset()
    sDH1b.reset()
    sDH2a.reset()
    sUa.reset()
    sCpa.reset()
    sCpb.reset()
    sCpc.reset()
    sCpd.reset()
button.on_clicked(reset)
    
