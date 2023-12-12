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
V0=4000
VH=5000
DHRx1A=-45400
DHRx2S=-3.2*10**5
SumNCp=1.26*10**7
A1A=4*10**14
E1A=128000
A2S=1*10**84
E2S=800000
Cv1=3360
Cv2=53600
UA=0
Pset=28.2
Ta=373.15
def ODEfun(Yfuncvec,t,V0,VH,DHRx1A,DHRx2S,SumNCp,A1A,E1A,A2S,E2S,Cv1,Cv2,UA,Ta,Pset):
    CA= Yfuncvec[0]
    CB= Yfuncvec[1]
    CS= Yfuncvec[2]
    P= Yfuncvec[3]
    T= Yfuncvec[4]
      #Explicit Equation Inline
    k1A = (A1A)* np.exp(-E1A/ (8.31*T))
    k2S = (A2S)* np.exp(-E2S/ (8.31*T))
    r1A = - k1A * CA*CB
    r2S = - k2S * CS
    FD=(-0.5*r1A-3*r2S)*V0
    if (T > 600 or P>45): 
     SW1 = 0
    else:
     SW1=1
    if (FD<11400): 
     Fvent = FD
    elif (P<Pset):
     Fvent=(P-1)*Cv1
    else:
     Fvent=(P-1)*(Cv1+Cv2) 
    Qg=V0*(r1A*DHRx1A+r2S*DHRx2S)
    Qr=UA*(T-Ta)
    # Differential equations
    dCAdt = SW1*r1A 
    dCBdt = SW1*r1A  
    dCSdt = SW1*r2S 
    dPdt = SW1*((FD-Fvent)*0.082*T/VH)
    dTdt=SW1*((Qg-Qr)/SumNCp)
    return np.array([dCAdt, dCBdt, dCSdt,dPdt, dTdt])

tspan = np.linspace(0, 4, 100) # Range for the independent variable
y0 = np.array([4.3,5.1,3,4.4,422]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-13-6: T2 Laboratories Explosion""", fontweight='bold', x = 0.15, y=0.98)
plt.subplots_adjust(left=0.45)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol =  odeint(ODEfun, y0, tspan, (V0,VH,DHRx1A,DHRx2S,SumNCp,A1A,E1A,A2S,E2S,Cv1,Cv2,UA,Ta,Pset))
CA = sol[:, 0]
CB= sol[:, 1]
CS= sol[:, 2]
P= sol[:, 3]
T= sol[:, 4]
k1A = (A1A)* np.exp(-E1A/ (8.31*T))
k2S = (A2S)* np.exp(-E2S/ (8.31*T))
r1A = - k1A * CA*CB
r2S = - k2S * CS
Qg=V0*(r1A*DHRx1A+r2S*DHRx2S)
Qr=UA*(T-Ta)

p1,p2,p3= ax1.plot(tspan, CA,tspan, CB,tspan, CS)
ax1.legend([r'$C_A$',r'$C_B$',r'$C_S$'], loc='upper right')
ax1.set_xlabel('time $(hr)$', fontsize='medium')
ax1.set_ylabel(r'$C_i$ (mol/$dm^{3}$)', fontsize='medium')
ax1.grid()
ax1.set_ylim(0, 6)
ax1.set_xlim(0, 4)

p4 = ax2.plot(tspan, T)[0]
ax2.legend([r'$T$'], loc='upper right')
ax2.set_xlabel('time $(hr)$', fontsize='medium')
ax2.set_ylabel(r'Temperature $(K)$', fontsize='medium')
ax2.grid()
ax2.set_ylim(400, 600)
ax2.set_xlim(0, 4)

p5 = ax3.plot(tspan,P)[0]
ax3.legend([r'$P$'], loc='upper left')
ax3.set_xlabel('time $(hr)$', fontsize='medium')
ax3.set_ylabel(r'P $(atm)$', fontsize='medium')
ax3.grid()
ax3.set_ylim(0, 50)
ax3.set_xlim(0, 4)

p6,p7 = ax4.plot(tspan,Qg,tspan,Qr)
ax4.legend(['$Q_g$', '$Q_r$'], loc='upper left')
ax4.set_xlabel('time $(hr)$', fontsize='medium')
ax4.set_ylabel(r'Q $(J/hr)$', fontsize='medium')
ax4.grid()
ax4.set_ylim(0, 2*10**16)
ax4.set_xlim(0, 4)








ax1.text(-8.75,-6.3,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} =r_{1A}$'
         '\n'
         r'$\dfrac{dC_B}{dt} =r_{1A}$'
         '\n'
         r'$\dfrac{dC_S}{dt} =r_{2S}$'
         '\n'
         r'$\dfrac{dT}{dt}=\dfrac{(Q_g-Q_r)}{\sum_{i} N_iC_{P_i}}$'
         '\n'
          r'$\dfrac{dP}{dt}=(F_D-F_{vent})\dfrac{R*T_H}{V_H}$'
         '\n\n'
         'Explicit Equations'
         '\n\n'
         r'$Q_r=UA*(T-T_a)$'
         '\n'
         r'$k_{1A}=(A_{1A})*exp\left(\dfrac{-E_{1A}}{R T}\right)$'
         '\n'
         r'$k_{2S}=(A_{2S})*exp\left(\dfrac{-E_{2S}}{R T}\right)$'
         '\n'
        r'$-r_{1A}=k_{1A}* C_A*C_B$'
         '\n'
        r'$-r_{2S}=k_{2S}* C_S$'
         '\n\n'
         r'$F_D=[(-0.5 r_{1A})+(-3 r_{2S})] V_0$'
         '\n\n'
         r'$F_{vent}=F_D \hspace{0.5} if\hspace{0.5} F_D <11,400  $'
         '\n'
         r'$else, \thinspace F_{vent}=(P-1)C_{v1} \hspace{0.5}when\hspace{0.5} P<P_{set} $'
         '\n'
         r'$else,\hspace{0.5} F_{vent}= (P-1)(C_{v1}+C_{v2})$'
         '\n\n'
         r'$Q_g=V_0\left[r_{1A} \Delta H_{Rx1A}+r_{2S} \Delta H_{Rx2S}\right] $'
          , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


axcolor = 'black'
ax_E1A = plt.axes([0.26, 0.82, 0.1, 0.015], facecolor=axcolor)
ax_E2S = plt.axes([0.26, 0.78, 0.1, 0.015], facecolor=axcolor)
ax_DHRx1A = plt.axes([0.26, 0.74, 0.1, 0.015], facecolor=axcolor)
ax_DHRx2S = plt.axes([0.26, 0.7, 0.1, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.26, 0.66, 0.1, 0.015], facecolor=axcolor)
ax_VH = plt.axes([0.26, 0.62, 0.1, 0.015], facecolor=axcolor)
ax_Pset = plt.axes([0.26, 0.58, 0.1, 0.015], facecolor=axcolor)
ax_Cv1 = plt.axes([0.26, 0.54, 0.1, 0.015], facecolor=axcolor)
ax_Cv2 = plt.axes([0.26, 0.5, 0.1, 0.015], facecolor=axcolor)
ax_V0 = plt.axes([0.26, 0.46, 0.1, 0.015], facecolor=axcolor)
ax_Ta = plt.axes([0.26, 0.42, 0.1, 0.015], facecolor=axcolor)

sE1A = Slider(ax_E1A, r'$E_{1A}$($\frac{J}{mol.K}$)', 50000, 200000, valinit=128000,valfmt='%1.0f')
sE2S= Slider(ax_E2S, r'$E_{2S}$($\frac{J}{mol.K}$)', 400000, 1600000, valinit=800000,valfmt='%1.0f')
sDHRx1A = Slider(ax_DHRx1A,r'$\Delta H_{Rx1A}$ ($\frac{J}{mol}$)',-100000, -10000, valinit=-45400,valfmt='%1.0f')
sDHRx2S = Slider(ax_DHRx2S,r'$\Delta H_{Rx2S}$ ($\frac{J}{mol}$)', -5*10**5,-0.2*10**5, valinit= -3.2*10**5,valfmt='%1.0E')
sUA = Slider(ax_UA,r'$UA$ ($\frac{J}{hr.K}$)',0, 5000000, valinit=0,valfmt='%1.0f')
sVH = Slider(ax_VH,r'$V_H$ ($dm^3$)', 10, 8000, valinit= 5000,valfmt='%1.0f')
sPset = Slider(ax_Pset,r'$P_{set}$ ($atm$)', 1, 80, valinit= 28.2,valfmt='%1.0f')
sCv1 = Slider(ax_Cv1,r'$C_{v1}$ ($\frac{mol}{atm.hr}$)', 1, 8000, valinit= 3360,valfmt='%1.0f')
sCv2 = Slider(ax_Cv2,r'$C_{v2}$ ($\frac{mol}{atm.hr}$)', 1000,80000, valinit= 53600,valfmt='%1.0f')
sV0 = Slider(ax_V0,r'$V_0$ ($dm^3$)', 0, 10000, valinit= 4000,valfmt='%1.0f')
sTa = Slider(ax_Ta,r'$T_a$ ($K$)', 273, 500, valinit= 373.15,valfmt='%1.0f')


def update_plot2(val):
    E1A = sE1A.val
    E2S =sE2S.val
    DHRx1A = sDHRx1A.val
    DHRx2S =sDHRx2S.val
    UA = sUA.val
    VH =sVH.val
    Pset = sPset.val
    Cv1 =sCv1.val
    Cv2 =sCv2.val
    V0 =sV0.val
    Ta =sTa.val
    sol = odeint(ODEfun, y0, tspan, (V0,VH,DHRx1A,DHRx2S,SumNCp,A1A,E1A,A2S,E2S,Cv1,Cv2,UA,Ta,Pset))
    CA = sol[:, 0]
    CB= sol[:, 1]
    CS= sol[:, 2]
    P= sol[:, 3]
    T= sol[:, 4]
    k1A = (A1A)* np.exp(-E1A/ (8.31*T))
    k2S = (A2S)* np.exp(-E2S/ (8.31*T))
    r1A = - k1A * CA*CB
    r2S = - k2S * CS
    Qg=V0*(r1A*DHRx1A+r2S*DHRx2S)
    Qr=UA*(T-Ta)
    p1.set_ydata(CA)
    p2.set_ydata(CB)
    p3.set_ydata(CS)
    p4.set_ydata(T)
    p5.set_ydata(P)
    p6.set_ydata(Qg)
    p7.set_ydata(Qr)
    fig.canvas.draw_idle()

sE1A.on_changed(update_plot2)
sE2S.on_changed(update_plot2)
sDHRx1A.on_changed(update_plot2)
sDHRx2S.on_changed(update_plot2)
sUA.on_changed(update_plot2)
sVH.on_changed(update_plot2)
sPset.on_changed(update_plot2)
sCv1.on_changed(update_plot2)
sCv2.on_changed(update_plot2)
sV0.on_changed(update_plot2)
sTa.on_changed(update_plot2)

resetax = plt.axes([0.27, 0.87, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sE1A.reset()
    sE2S.reset()
    sDHRx1A.reset()
    sDHRx2S.reset()
    sUA.reset()
    sVH.reset()
    sPset.reset()
    sCv1.reset()
    sCv2.reset()
    sV0.reset()
    sTa.reset()
button.on_clicked(reset)
    
