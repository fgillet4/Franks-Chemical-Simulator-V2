#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
# Explicit equations
Fa0 = 80
T0 = 70
V = (1/7.484)*500
Tsp = 138
UA = 16000
Ta1 = 60
kc = 8.5
Fb0 = 1000
Fm0 = 100
mc0 = 1000
Ea=32400
dH=-36000
def ODEfun(Yfuncvec, t, Fa0, T0, V, Tsp, UA, Ta1, kc, Fb0, Fm0, mc0,Ea,dH): 
    Ca= Yfuncvec[0]
    Cb= Yfuncvec[1]
    Cc= Yfuncvec[2]
    Cm= Yfuncvec[3]
    T=Yfuncvec[4]
    I=Yfuncvec[5]
    k = 16.96*10**12*np.exp(-Ea/1.987/(T+460))
    ra = -k*Ca
    NCp = Ca*V*35+Cb*V*18+Cc*V*46+Cm*V*19.5
    ThetaCp = 35+Fb0/Fa0*18+Fm0/Fa0*19.5
    v0 = Fa0/0.923+Fb0/3.45+Fm0/1.54
    Ca0 = Fa0/v0
    Cb0 = Fb0/v0
    Cm0 = Fm0/v0
    tau = V/v0
    X = (Ca0-Ca)/Ca0
    mc = mc0+kc/tau*I
    Ta2 = T-(T-Ta1)*np.exp(-UA/(18*mc))
    Qr = mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)
    Qg=(dH)*ra*V
    # Differential equations
    dCadt = 1/tau*(Ca0-Ca)+ra 
    dCbdt = 1/tau*(Cb0-Cb)+ra 
    dCcdt = 1/tau*(0-Cc)-ra 
    dCmdt = 1/tau*(Cm0-Cm) 
    dTdt = (Qg-Qr)/NCp 
    dIdt = T-Tsp 
    return np.array([dCadt, dCbdt, dCcdt, dCmdt, dTdt, dIdt])


t = np.linspace(0, 4, 1000) # Range for the independent variable
y0 = np.array([0.03789,2.12,0.143,0.2265,138.53,0]) # Initial values for the dependent variables i.e. CO1;CO2;CO3

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
fig.suptitle("""PRS Example CD13-3a: Integral Control of a CSTR""", fontweight='bold', x = 0.4, y=0.98)
sol = odeint(ODEfun, y0, t, (Fa0, T0, V, Tsp, UA, Ta1, kc, Fb0, Fm0, mc0,Ea,dH))

Ca= sol[:, 0]
Cb= sol[:, 1]
Cc= sol[:, 2]
Cm= sol[:, 3]
T=sol[:, 4]
I=sol[:, 5]

v0 = Fa0/0.923+Fb0/3.45+Fm0/1.54
Ca0 = Fa0/v0
X = (Ca0-Ca)/Ca0
k = 16.96*10**12*np.exp(-Ea/1.987/(T+460))
ra = -k*Ca
ThetaCp = 35+Fb0/Fa0*18+Fm0/Fa0*19.5
tau = V/v0
mc = mc0+kc/tau*I
Ta2 = T-(T-Ta1)*np.exp(-UA/(18*mc))
Qr = mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)
Qg=(dH)*ra*V

p1 = ax2.plot(X, T)[0]
ax2.legend(['Conversion-Temperature'], loc='best')
ax2.set_ylabel('$T (^\circ F)$', fontsize='medium')
ax2.set_xlabel('Conversion', fontsize='medium')
ax2.set_ylim(110, 180)
ax2.set_xlim(0, 1)
ax2.grid()

p5 = ax3.plot(t, T)[0]
ax3.legend(['T'], loc='best')
ax3.set_ylim(110,180)
ax3.set_xlim(0,4)
ax3.grid()
ax3.set_xlabel('time (hr)', fontsize='medium')
ax3.set_ylabel('$Temperature (^\circ F)$', fontsize='medium')

p6,p7 = ax4.plot(t, Qg, t, Qr)
ax4.legend(['$Q_g$','$Q_r$'], loc='best')
ax4.set_xlim(0,4)
ax4.set_ylim(0,5e6)
ax4.grid()
ax4.set_xlabel('time (hr)', fontsize='medium')
ax4.set_ylabel('Q (Btu/hr)', fontsize='medium')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

ax1.axis('off')


ax1.text(-1.05, -1.55,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} = \dfrac{1}{\tau}(C_{A0}-C_A)+r_A $'
                  '\n '
         r'$\dfrac{dC_B}{dt} = \dfrac {1}{\tau}(C_{B0}-C_B)+r_B $'
                  '\n ' 
         r'$\dfrac{dC_C}{dt} = \dfrac{1}{\tau}(0-C_C)+r_C$'
                  '\n '
         r'$\dfrac{dC_M}{dt} = \dfrac{1}{\tau}(C_{M0}-C_M) $'
                  '\n '  
         r'$\dfrac{dT}{dt} = \dfrac{Q_g-Q_r}{N_{Cp}}$'
         '\n'
         r'$\dfrac{dI}{dt} = T - T_{SP}$'
         '\n'
         '\n'
         'Explicit Equations'
             
         '\n\n'
          r'$Q_g=r_A.V*\Delta H_{Rx}$'
          '\n'
          r'$Q_r=18m_C(T_{a2}-T_{a1})+F_{A0}\theta_{C_p}(T-T_0)$'
         '\n'
         r'$k = 16.96*10^12exp\left (-\dfrac{E_a}{1.987(T+460)} \right)$'
         '\n\n'
         r'$r_A = -kC_A$'
         '\n\n'
         r'$N_{Cp} = 35*C_A*V + 18*C_B*V+ 46*C_C*V + 19.5*C_M*V$'
         '\n\n'
         r'$\theta_{Cp} = 35+ \dfrac{18F_{B0}}{F_{A0}}+ \dfrac{19.5F_{M0}}{F_{A0}}$'
         '\n\n'
         r'$v_0 =  \dfrac{F_{A0}}{0.923} + \dfrac{F_{B0}}{3.45} + \dfrac{F_{M0}}{1.54}$'
         '\n\n'
         r'$C_{A0} = \dfrac{F_{A0}}{v_0}$'
         '\n'
         r'$C_{B0} = \dfrac{F_{B0}}{v_0}$'
         '\n'
         r'$C_{M0} = \dfrac{F_{M0}}{v_0}$'
         '\n'     
         r'$\tau = \dfrac{V}{v_0}$'
         '\n'     
         r'$X = 1-\dfrac{C_A}{C_{A0}}$'
         '\n\n'     
         r'$m_C = m_{C0} + \dfrac{k_C.I}{\tau}$'  
         '\n\n'     
         r'$T_{a2} = T - (T - T_{a1})exp \left( -\dfrac{U_A}{18m_C} \right)$' 
         '\n'              
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

#%%
axcolor = 'black'
ax_Fa0 = plt.axes([0.32, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_T0 = plt.axes([0.32, 0.79, 0.2, 0.015], facecolor=axcolor)
ax_V = plt.axes([0.32, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_Tsp = plt.axes([0.32, 0.73, 0.2, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.32, 0.7, 0.2, 0.015], facecolor=axcolor)
ax_Ta1 = plt.axes([0.32, 0.67, 0.2, 0.015], facecolor=axcolor)
ax_kc = plt.axes([0.32, 0.64, 0.2, 0.015], facecolor=axcolor)
ax_Fb0 = plt.axes([0.32, 0.61, 0.2, 0.015], facecolor=axcolor)
ax_Fm0 = plt.axes([0.32, 0.58, 0.2, 0.015], facecolor=axcolor)
ax_mc0 = plt.axes([0.32, 0.55, 0.2, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.32, 0.52, 0.2, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.32, 0.49, 0.2, 0.015], facecolor=axcolor)

sFa0 = Slider(ax_Fa0, r'$F_{a0} (\frac{mol}{hr})$', 75, 120, valinit=80, valfmt="%1.0f")
sT0= Slider(ax_T0, r'$T_0 (F)$', 69, 100, valinit=70, valfmt="%1.0f")
sV = Slider(ax_V, r'$V$', 60, 95, valinit=(1/7.484)*500, valfmt="%1.1f")
sTsp = Slider(ax_Tsp, r'$T_{SP}(^\circ F)$', 100, 200, valinit=138, valfmt="%1.0f")
sUA = Slider(ax_UA, r'$U_A (\frac{ hr.mol}{K.gm})$', 9000, 22000, valinit=16000, valfmt="%1.0f")
sTa1 = Slider(ax_Ta1, r'$T_{a1} (^\circ F)$', 40, 100, valinit=60, valfmt="%1.0f")
skc = Slider(ax_kc, r'$k_c (hr^{-1})$', 4, 13, valinit=8.5, valfmt="%1.2f")
sFb0 = Slider(ax_Fb0, r'$F_{B0} (\frac{mol}{hr})$', 400, 1200, valinit= 1000, valfmt="%1.0f")
sFm0 = Slider(ax_Fm0, r'$F_{M0} (\frac{mol}{hr})$', 50, 200, valinit=100, valfmt="%1.0f")
smc0 = Slider(ax_mc0, r'$m_{C0} (\frac{K}{hr})$', 800, 2000, valinit=1000, valfmt="%1.0f")
sEa = Slider(ax_Ea, r'$E_{a} (\frac{Btu}{lb mol})$', 5000, 100000, valinit=32400,valfmt='%1.0f')
sdH = Slider(ax_dH, r'$\Delta H_{Rx} (\frac{Btu}{lb mol})$', -70000, -1000, valinit=-36000,valfmt='%1.0f')


def update_plot(val):
    Fa0 =sFa0.val
    T0 =sT0.val
    V = sV.val
    Tsp =sTsp.val
    UA = sUA.val
    Ta1 = sTa1.val
    kc = skc.val
    Fb0 = sFb0.val
    Fm0 = sFm0.val
    mc0 = smc0.val
    Ea = sEa.val
    dH = sdH.val
    sol = odeint(ODEfun, y0, t, (Fa0, T0, V, Tsp, UA, Ta1, kc, Fb0, Fm0, mc0,Ea,dH))
    Ca= sol[:, 0]
    T=sol[:, 4]
    I=sol[:, 5]
    v0 = Fa0/0.923+Fb0/3.45+Fm0/1.54
    Ca0 = Fa0/v0
    X = (Ca0-Ca)/Ca0  
    k = 16.96*10**12*np.exp(-Ea/1.987/(T+460))
    ra = -k*Ca
    ThetaCp = 35+Fb0/Fa0*18+Fm0/Fa0*19.5
    tau = V/v0
    mc = mc0+kc/tau*I
    Ta2 = T-(T-Ta1)*np.exp(-UA/(18*mc))
    Qr = mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)
    Qg=(dH)*ra*V
    p1.set_ydata(T)
    p1.set_xdata(X)
    p5.set_ydata(T)
    p6.set_ydata(Qg)
    p7.set_ydata(Qr)
    fig.canvas.draw_idle()


sFa0.on_changed(update_plot)
sT0.on_changed(update_plot)
sV.on_changed(update_plot)
sTsp.on_changed(update_plot)
sUA.on_changed(update_plot)
sTa1.on_changed(update_plot)
skc.on_changed(update_plot)
sFb0.on_changed(update_plot)
sFm0.on_changed(update_plot)
smc0.on_changed(update_plot)
sEa.on_changed(update_plot)
sdH.on_changed(update_plot)

resetax = plt.axes([0.4, 0.85, 0.09, 0.03])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sFa0.reset()
    sT0.reset()
    sV.reset()
    sTsp.reset()
    sUA.reset()
    sTa1.reset()
    skc.reset()
    sFb0.reset()
    sFm0.reset()
    smc0.reset()
    sEa.reset()
    sdH.reset()
button.on_clicked(reset)


plt.show()
