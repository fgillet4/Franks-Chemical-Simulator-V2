#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
UA =16000   
Ta1=60
T0 =  70
dH=-36000
mc=1000
Fa0 = 80
Fb0 =  1000
Fm0 = 100 
V=66.809 
Ea=32400

def ODEfun(Yfuncvec, t, UA, Ta1,T0,dH,mc, Fa0,Fb0,Fm0,V,Ea):
    Ca= Yfuncvec[0]
    Cb= Yfuncvec[1]
    Cc= Yfuncvec[2]
    Cm= Yfuncvec[3]
    T=Yfuncvec[4]
    # Explicit equations
    k =  16.96e12*np.exp(-Ea/1.987/(T+460))
    ra =  -k*Ca
    rb =  -k*Ca
    rc =  k*Ca
    Ta2 =  T-(T-Ta1)*np.exp(-UA/(18*mc))
    ThetaCp =35+(Fb0/Fa0)*18+(Fm0/Fa0)*19.5
    v0 =  Fa0/0.923+Fb0/3.45+Fm0/1.54
    Ca0 =  Fa0/v0
    Cb0 =  Fb0/v0
    Cm0 =  Fm0/v0
    tau=V/v0
    Nm =  Cm*V
    Na =  Ca*V
    Nb =  Cb*V
    Nc =  Cc*V
    NCp =  Na*35+Nb*18+Nc*46+Nm*19.5
    Qg=(dH)*ra*V
    Qr=mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)
    # Differential equations
    dCadt =  1/tau*(Ca0-Ca)+ra  
    dCbdt =  1/tau*(Cb0-Cb)+rb  
    dCcdt =  1/tau*(0-Cc)+rc  
    dCmdt =  1/tau*(Cm0-Cm)  
    dTdt =  (Qg-Qr)/NCp
    return np.array([dCadt, dCbdt, dCcdt, dCmdt, dTdt])


tspan = np.linspace(0, 4, 1000) # Range for the independent variable
y0 = np.array([0.03789,2.12,0.143,0.2265,138.53]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""PRS Example R13-2 Falling Off the Steady State""", fontweight='bold', x = 0.3, y = 0.98)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
plt.subplots_adjust(left  = 0.45)

sol = odeint(ODEfun, y0, tspan, ( UA, Ta1,T0,dH,mc, Fa0,Fb0,Fm0,V,Ea))
Ca= sol[:, 0]
Cb= sol[:, 1]
Cc= sol[:, 2]
Cm= sol[:, 3]
T=sol[:, 4]
v0 =  Fa0/0.923+Fb0/3.45+Fm0/1.54
Ca0 =  Fa0/v0
X=(Ca0-Ca)/Ca0
k =  16.96e12*np.exp(-Ea/1.987/(T+460))
ra =  -k*Ca
ThetaCp =35+Fb0/Fa0*18+Fm0/Fa0*19.5
Ta2 =  T-(T-Ta1)*np.exp(-UA/(18*mc))
Qg=(dH)*ra*V
Qr=mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)

p1 = ax1.plot(tspan, T)[0]
ax1.legend(['T'], loc='best')
ax1.set_xlabel('t (hr)', fontsize='medium')
ax1.set_ylabel('$T (^\circ F)$', fontsize='medium')
ax1.set_ylim(60,200)
ax1.set_xlim(0,4)
ax1.grid()

p2= ax2.plot(tspan, X)[0]
ax2.legend(['X'], loc='best')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0,1)
ax2.set_xlim(0,4)
ax2.grid()
ax2.set_xlabel('t (hr)', fontsize='medium')

p3,p4= ax3.plot(tspan, Qg, tspan, Qr)
ax3.legend(['$Q_g$','$Q_r$'], loc='best')
ax3.set_ylabel('Q (Btu/hr)', fontsize='medium')
ax3.set_ylim(0,8e6)
ax3.set_xlim(0,4)
ax3.grid()
ax3.set_xlabel('t (hr)', fontsize='medium')

p5= ax4.plot(T, Ca)[0]
ax4.set_ylim(0, 0.2)
ax4.set_xlim(0, 250)
ax4.grid()
ax4.set_xlabel('$T (^\circ F)$', fontsize='medium')
ax4.set_ylabel('$C_{A}  (lb-mol/ft^3)$', fontsize='medium')


ax2.text(-14.0, -1.5,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} =  \dfrac{1}{\tau}(C_{A0}-C_A)+r_A $'
                  '\n \n'
         r'$\dfrac{dC_B}{dt} = \dfrac {1}{\tau}(C_{B0}-C_B)+r_B $'
                  '\n \n' 
         r'$\dfrac{dC_C}{dt} =  \dfrac{1}{\tau}(0-C_C)+r_C$'
                  '\n \n'
         r'$\dfrac{dC_M}{dt} =  \dfrac{1}{\tau}(C_{M0}-C_M) $'
                  '\n \n'  
        
         r'$\dfrac{dT}{dt} =  \dfrac{(Q_g-Q_r)}{N_{C_p}}$'
                  '\n \n'     
         'Explicit Equations'
                  '\n\n'
         r'$k =  16.96.10^{12}.exp\left(\dfrac{-E_a}{1.987.(T+460)} \right)$'
         '\n'
         r'$r_A =  -kC_A$'
         '\n'
         r'$r_B =  -kC_A$'
         '\n'
         r'$r_C =  k*Ca$'         '\n\n'
          r'$Q_g=r_A.V*\Delta H_{Rx}$'
         '\n'
         r'$T_{a2} =  T-(T-T_{a1})*exp(-UA/(18*mc)) $' '\n'
         r'$Q_r=m_c*18*(T_{a2}-T_{a1})+F_{A0}\theta_{C_p}(T-T_0)$'
         '\n'
         r'$\theta_{Cp} = 35+\dfrac{F_{B0}}{F_{A0}}*18+\dfrac{F_{M0}}{F_{A0}}*19.5$'         '\n\n'
         r'$ v_{0} =  \dfrac{F_{A0}}{0.923}+\dfrac{F_{B0}}{3.45}+\dfrac{F_{M0}}{1.54}$'   '\n\n'
         r'$C_{A0} =  \dfrac{F_{A0}}{v_{0}}$'         '\n'
         r'$C_{B0} =  \dfrac{F_{B0}}{v_{0}}$'         '\n'
         r'$C_{M0} =  \dfrac{F_{M0}}{v_{0}}$'         '\n'
         r'$N_M =  C_M \thinspace V$'         '\n'
         r'$N_A =  Ca\thinspace V$'         '\n'
         r'$N_B =  Cb\thinspace V$'         '\n'
         r'$N_C =  Cc\thinspace V$'         '\n'
         r'$N_{Cp} =  N_A\thinspace* 35+N_B\thinspace * 18+N_C\thinspace * 46+N_M\thinspace* 19.5$'         
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')
    
#%%
axcolor = 'black'
ax_V = plt.axes([0.26, 0.8, 0.1, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.26, 0.76, 0.1, 0.015], facecolor=axcolor)
ax_Ta1 = plt.axes([0.26, 0.72, 0.1, 0.015], facecolor=axcolor)
ax_Fa0 = plt.axes([0.26, 0.68, 0.1, 0.015], facecolor=axcolor)
ax_T0 = plt.axes([0.26, 0.64, 0.1, 0.015], facecolor=axcolor)
ax_Fb0 = plt.axes([0.26, 0.60, 0.1, 0.015], facecolor=axcolor)
ax_Fm0 = plt.axes([0.26, 0.56, 0.1, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.26, 0.52, 0.1, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.26, 0.48, 0.1, 0.015], facecolor=axcolor)

sV = Slider(ax_V, r'$V (ft^3)$', 10,150, valinit=66.809,valfmt='%1.2f')
sUA = Slider(ax_UA, r'$U_A (\frac{Btu}{hr. ^\circ F})$', 1000, 30000, valinit=16000,valfmt='%1.0f')
sTa1= Slider(ax_Ta1, r'$T_a (^\circ F)$', 20, 80, valinit=60,valfmt='%1.2f')
sFa0 = Slider(ax_Fa0, r'$F_{A0} (\frac{lb mol}{hr})$', 30, 150, valinit=80,valfmt='%1.1f')
sT0 = Slider(ax_T0, r'$T_0 (^\circ F)$',30, 250, valinit=70,valfmt='%1.2f')
sFb0 = Slider(ax_Fb0, r'$F_{B0} (\frac{lb mol}{hr})$', 200, 2000, valinit= 1000,valfmt='%1.0f')
sFm0 = Slider(ax_Fm0, r'$F_{M0} (\frac{lb mol}{hr})$', 30, 250, valinit=100,valfmt='%1.2f')
sEa = Slider(ax_Ea, r'$E_{a} (\frac{Btu}{lb mol})$', 20000, 75000, valinit=32400,valfmt='%1.0f')
sdH = Slider(ax_dH, r'$\Delta H_{Rx} (\frac{Btu}{lb mol})$', -70000, -10000, valinit=-36000,valfmt='%1.0f')

def update_plot2(val):
    V = sV.val
    UA =sUA.val
    Ta1 =sTa1.val
    Fa0 = sFa0.val
    T0 =sT0.val
    Fb0 = sFb0.val
    Fm0 = sFm0.val
    Ea = sEa.val
    dH=  sdH.val
    sol = odeint(ODEfun, y0, tspan, (UA, Ta1,T0,dH,mc, Fa0,Fb0,Fm0,V,Ea))
    Ca= sol[:, 0]
    T=sol[:, 4]
    v0 =  Fa0/0.923+Fb0/3.45+Fm0/1.54
    Ca0 =  Fa0/v0
    X=(Ca0-Ca)/Ca0
    k =  16.96e12*np.exp(-Ea/1.987/(T+460))
    ra =  -k*Ca
    ThetaCp =35+Fb0/Fa0*18+Fm0/Fa0*19.5
    Qg=(dH)*ra*V
    Ta2 =  T-(T-Ta1)*np.exp(-UA/(18*mc))
    Qr=mc*18*(Ta2-Ta1)+Fa0*ThetaCp*(T-T0)

    p1.set_ydata(T)
    p2.set_ydata(X)
    p3.set_ydata(Qg)
    p4.set_ydata(Qr)
    p5.set_ydata(Ca)
    p5.set_xdata(T)  
    fig.canvas.draw_idle()


sV.on_changed(update_plot2)
sUA.on_changed(update_plot2)
sTa1.on_changed(update_plot2)
sFa0.on_changed(update_plot2)
sT0.on_changed(update_plot2)
sFb0.on_changed(update_plot2)
sFm0.on_changed(update_plot2)
sEa.on_changed(update_plot2)
sdH.on_changed(update_plot2)
#

resetax = plt.axes([0.27, 0.85, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sV.reset()
    sUA.reset()
    sTa1.reset()
    sFa0.reset()
    sT0.reset()
    sFb0.reset()
    sFm0.reset()
    sEa.reset()
    sdH.reset()
button.on_clicked(reset)
    
