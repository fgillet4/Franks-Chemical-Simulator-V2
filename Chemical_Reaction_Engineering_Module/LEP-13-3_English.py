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
UA=16000
Ta1=60
CpW=18
T0=75
mc=1000
dH=-36000
V=66.809
Fa0 = 80
Fb0 = 1000
Fm0 = 100
Cai=0
Ti=75
def ODEfun(Yfuncvec,t,UA,Ta1,CpW,T0,mc,dH,V,Fa0,Fb0,Fm0,Cai):
    Ca= Yfuncvec[0]
    Cb= Yfuncvec[1]
    Cc= Yfuncvec[2]
    Cm= Yfuncvec[3]
    T= Yfuncvec[4]
      #Explicit Equation Inline
    k = 16960000000000 * np.exp(-32400 / 1.987 / (T+460));   
    ra = 0 - (k * Ca)
    rb = 0 - (k * Ca)
    rc = k * Ca
    Na = Ca * V
    Nb = Cb * V
    Nc = Cc * V
    Nm = Cm * V
    ThetaCp = 35 + Fb0 / Fa0 * 18 + Fm0 / Fa0 * 19.5
    v0 = Fa0 /0.923 + Fb0 /3.45 + Fm0 /1.54
    Ta2 = T - ((T - Ta1) *np.exp(0 - (UA / (CpW * mc))))
    Ca0 = Fa0 / v0
    Cb0 = Fb0 / v0
    Cm0 = Fm0 / v0
    Qr2 = mc * CpW * (Ta2 - Ta1)
    Qr1=Fa0*ThetaCp*(T-T0)
    Qr=Qr1+Qr2
    Qg=ra*V*dH
    tau = V / v0
    NCp = Na * 35 + Nb * 18 + Nc * 46 + Nm * 19.5
    # Differential equations
    dCadt = 1 / tau * (Ca0 - Ca) + ra
    dCbdt = 1 / tau * (Cb0 - Cb) + rb
    dCcdt = 1 / tau * (0 - Cc) + rc
    dCmdt = 1 / tau * (Cm0 - Cm)
    dTdt=(Qg-Qr)/NCp
        
    return np.array([dCadt, dCbdt, dCcdt, dCmdt,dTdt])

tspan = np.linspace(0, 4, 500) # Range for the independent variable
y0 = np.array([Cai,3.45,0,0,Ti]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-13-3: Startup of a CSTR  (English units)""", fontweight='bold', x = 0.16, y=0.98)
plt.subplots_adjust(left  = 0.5)
fig.subplots_adjust(wspace=0.35,hspace=0.3)
sol =  odeint(ODEfun, y0, tspan, (UA,Ta1,CpW,T0,mc,dH,V,Fa0,Fb0,Fm0,Cai))
Ca = sol[:, 0]
Cb= sol[:, 1]
Cc= sol[:, 2]
Cm= sol[:, 3]
T=sol[:, 4]
k = 16960000000000 * np.exp(-32400 / 1.987 / (T+460));   
ra = 0 - (k * Ca)
ThetaCp = 35 + Fb0 / Fa0 * 18 + Fm0 / Fa0 * 19.5
Ta2 = T - ((T - Ta1) *np.exp(0 - (UA / (CpW * mc))))
Qr2 = mc * CpW * (Ta2 - Ta1)
Qr1=Fa0*ThetaCp*(T-T0)
Qr=Qr1+Qr2
Qg=ra*V*dH

p1= ax1.plot(tspan, Ca)[0]
ax1.legend([r'$C_A$'], loc='upper right')
ax1.set_xlabel('time $(hr)$', fontsize='medium')
ax1.set_ylabel(r'$C_A$ (lb-mol/$ft^{3}$)', fontsize='medium')
ax1.grid()
ax1.set_ylim(0, 0.2)
ax1.set_xlim(0, 4)

p2 = ax2.plot(tspan, T)[0]
ax2.legend([r'$T$'], loc='upper right')
ax2.set_xlabel('time $(hr)$', fontsize='medium')
ax2.set_ylabel(r'Temperature $(^\circ F)$', fontsize='medium')
ax2.grid()
ax2.set_ylim(60, 200)
ax2.set_xlim(0, 4)

p3 = ax3.plot(T,Ca)[0]
ax3.set_xlabel(r'Temperature $(^\circ F)$', fontsize='medium')
ax3.set_ylabel(r'$C_A$(lb-mol/$ft^{3}$)', fontsize='medium')
ax3.grid()
ax3.set_ylim(0, 0.2)
ax3.set_xlim(60, 250)

p4,p5 = ax4.plot(tspan,Qg,tspan,Qr)
ax4.set_xlabel('time $(hr)$', fontsize='medium')
ax4.legend(['$Q_g$','$Q_r$'], loc='upper right')
ax4.set_ylabel(r'$Q$(Btu/$hr$)', fontsize='medium')
ax4.grid()
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='y')
ax4.set_ylim(0, 8*10**6)
ax4.set_xlim(0, 4)

ax1.text(-11.5,-0.25,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} =r_A +\dfrac{(C_{A0}-C_A)}{V} v_0$'
         '\n'
         r'$\dfrac{dC_B}{dt} =r_B +\dfrac{(C_{B0}-C_B)}{V} v_0$'
         '\n'
         r'$\dfrac{dC_C}{dt} =r_A +\dfrac{-C_C}{V} v_0$'
         '\n'
         r'$\dfrac{dC_M}{dt} =r_A +\dfrac{(C_{M0}-C_M)}{V} v_0$'
         '\n'
         r'$\dfrac{dT}{dt}=\dfrac{(Q_{gs}-Q_{rs})}{\sum_{i} N_iC_{P_i}}$'
         '\n'
         'Explicit Equations'
         '\n\n'
         r'$N_A=C_A *V$'
         '\n'
         r'$N_B=C_B *V$'
         '\n'
         r'$N_C=C_C*V$'
         '\n'
         r'$N_M=C_M*V$'
         '\n'
         r'$NCp=N_A*35+N_B*18+N_C*46+N_M*19.5$'
         '\n'
         r'$k=(16.96*10^{12})*exp\left(\left(\dfrac{-32400}{1.987*(T+460)}\right)\right)$'
         '\n'
         r'$r_A=-k*C_A$'
         '\n'
         r'$r_B=r_A$'
         '\n'
         r'$r_C=-r_A$'
         '\n'
         r'$\sum_{i}\theta_i C_{P_i}=35+18*\dfrac{F_{B0}}{F_{A0}}+19.5*\dfrac{F_{M0}}{F_{A0}}$'
         '\n'
         r'$Q_{gs}=(r_A*V)(\Delta H_{Rx})$'
         '\n'
         r'$Q_{rs1}=(F_{A0}*\sum_{i}\theta_i C_{P_i}*(T-T_0) $'
         '\n'
         r'$Q_{rs2}=m_c* C_{P_W}*(T-T_{a1})\left(1-exp\left(\dfrac{-UA}{m_c*C_{P_W}}\right)\right)$'
         '\n'
         r'$Q_{rs}=Q_{rs1}+Q_{rs2} $'
          , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

axcolor = 'black'
ax_UA = plt.axes([0.295, 0.84, 0.1, 0.015], facecolor=axcolor)
ax_Ta1 = plt.axes([0.295, 0.8, 0.1, 0.015], facecolor=axcolor)
ax_CpW = plt.axes([0.295, 0.76, 0.1, 0.015], facecolor=axcolor)
ax_T0 = plt.axes([0.295, 0.72, 0.1, 0.015], facecolor=axcolor)
ax_mc = plt.axes([0.295, 0.68, 0.1, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.295, 0.64, 0.1, 0.015], facecolor=axcolor)
ax_V = plt.axes([0.295, 0.6, 0.1, 0.015], facecolor=axcolor)
ax_Ti = plt.axes([0.295, 0.56, 0.1, 0.015], facecolor=axcolor)
ax_Fa0 = plt.axes([0.295, 0.52, 0.1, 0.015], facecolor=axcolor)
ax_Fb0 = plt.axes([0.295, 0.48, 0.1, 0.015], facecolor=axcolor)
ax_Fm0 = plt.axes([0.295, 0.44, 0.1, 0.015], facecolor=axcolor)
ax_Cai = plt.axes([0.295, 0.40, 0.1, 0.015], facecolor=axcolor)

sUA = Slider(ax_UA, r'$UA$($\frac{Btu}{h.^\circ F}$)', 1000, 30000, valinit=16000,valfmt='%1.0f')
sTa1= Slider(ax_Ta1, r'$T_{a1}$ ($^\circ F$)',30, 100, valinit=60,valfmt='%1.1f')
sCpW = Slider(ax_CpW,r'$C_{P_W}$($\frac{Btu}{lbmol.^\circ F}$)', 5, 60, valinit=18,valfmt='%1.0f')
sT0 = Slider(ax_T0,r'$T_{0}$($^\circ F$)', 50, 180, valinit= 75,valfmt='%1.0f')
smc = Slider(ax_mc,r'$m_{C}$($\frac{lbmol}{hr}$)', 100, 10000, valinit=1000,valfmt='%1.0f')
sdH = Slider(ax_dH,r'$\Delta H_{Rx}$ ($\frac{Btu}{lbmol\thinspace A}$)', -70000, -10000, valinit= -36000,valfmt='%1.0f')
sV = Slider(ax_V,r'$V$ ($ft^3$)', 20, 100, valinit= 66.809,valfmt='%1.1f')
sTi = Slider(ax_Ti,r'$T_i$ ($^\circ F$)', 20, 250, valinit= 75,valfmt='%1.1f')
sFa0 = Slider(ax_Fa0,r'$F_{A0}$ ($\frac{lbmol}{hr}$)', 30, 150, valinit= 80,valfmt='%1.1f')
sFb0 = Slider(ax_Fb0,r'$F_{B0}$ ($\frac{lbmol}{hr}$)', 200, 2000, valinit=1000,valfmt='%1.0f')
sFm0 = Slider(ax_Fm0,r'$F_{M0}$ ($\frac{lbmol}{hr}$)', 30, 250, valinit= 100,valfmt='%1.1f')
sCai= Slider(ax_Cai,r'$C_{A_i}$ ($\frac{lbmol}{ft^{3}}$)', 0, 0.25, valinit= 0,valfmt='%1.2f')

def update_plot2(val):
    UA = sUA.val
    Ta1 =sTa1.val
    CpW = sCpW.val
    T0 =sT0.val
    mc = smc.val
    dH =sdH.val
    V = sV.val
    Ti=sTi.val
    Fa0 =sFa0.val
    Fb0 =sFb0.val
    Fm0 =sFm0.val
    Cai =sCai.val
    y1 = np.array([Cai,3.45,0,0,Ti])
    sol = odeint(ODEfun, y1, tspan, (UA,Ta1,CpW,T0,mc,dH,V,Fa0,Fb0,Fm0,Cai))
    Ca = sol[:, 0]
    Cb= sol[:, 1]
    Cc= sol[:, 2]
    Cm= sol[:, 3]
    T=sol[:,4]
    k = 16960000000000 * np.exp(-32400 / 1.987 / (T+460));   
    ra = 0 - (k * Ca)
    ThetaCp = 35 + Fb0 / Fa0 * 18 + Fm0 / Fa0 * 19.5
    Ta2 = T - ((T - Ta1) *np.exp(0 - (UA / (CpW * mc))))
    Qr2 = mc * CpW * (Ta2 - Ta1)
    Qr1=Fa0*ThetaCp*(T-T0)
    Qr=Qr1+Qr2
    Qg=ra*V*dH
    p1.set_ydata(Ca)
    p2.set_ydata(T)
    p3.set_ydata(Ca)
    p3.set_xdata(T)
    p4.set_ydata(Qg)
    p5.set_ydata(Qr)
    fig.canvas.draw_idle()

sUA.on_changed(update_plot2)
sTa1.on_changed(update_plot2)
sCpW.on_changed(update_plot2)
sT0.on_changed(update_plot2)
smc.on_changed(update_plot2)
sdH.on_changed(update_plot2)
sV.on_changed(update_plot2)
sTi.on_changed(update_plot2)
sFa0.on_changed(update_plot2)
sFb0.on_changed(update_plot2)
sFm0.on_changed(update_plot2)
sCai.on_changed(update_plot2)

resetax = plt.axes([0.3, 0.89, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sUA.reset()
    sTa1.reset()
    sCpW.reset()
    sT0.reset()
    smc.reset()
    sdH.reset()
    sV.reset()
    sFa0.reset()
    sFb0.reset()
    sFm0.reset()
    sTi.reset()
    sCai.reset()
button.on_clicked(reset)
    
