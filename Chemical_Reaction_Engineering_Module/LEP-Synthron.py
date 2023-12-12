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
Cao=3.99
Cco= 1.94
Cto= 2.09
Vo= 2.38
vo= 6
Cai= 2.38
Nci= 7.76
Nti=7.09
UA=5
def ODEfun(Yfuncvec,t,Cao,Cco,Cto,Vo,vo,Cai,Nci,Nti,UA):
    Ca= Yfuncvec[0]
    Nc= Yfuncvec[1]
    Nt= Yfuncvec[2]
    Can= Yfuncvec[3]
    T= Yfuncvec[4]
    Cas= Yfuncvec[5]
    Ncs= Yfuncvec[6]
    Nts= Yfuncvec[7]
    Cans= Yfuncvec[8]
    Ts= Yfuncvec[9]
      #Explicit Equation Inline
    V = Vo + (vo*10**-5*t);
    Na= Ca*V;
    Nan= Can*V;
    Fao = Cao*vo*10**-5;
    Fco = Cco*vo*10**-5;
    Fto = Cto*vo*10**-5;
    Cpa = 245.75;
    Cpc = 161.3;
    Cpt = 165.60;
    Cpan = 231;
    k= (4.01*10**3)*np.exp(-29000/(8.314*T))
    ra= -k*(Ca)**2;
    Qgs= -ra*V*64512;
    Qrs1= ((Fao*Cpa) + (Fco*Cpc) + (Fto*Cpt))*(T - 310);
    Qrs2= UA*(T - 298);
    Qrs= Qrs1 + Qrs2 + 8.3;
    NCp= (Na*Cpa) + (Nc*Cpc) + (Nt*Cpt) + (Nan*Cpan);
    Caos = 2.22;
    Ccos = 3.52;
    Ctos = 2.92;
    Vos = 0.73;
    vos = 1.5*10**-4;
    UAS = 5;
    Vs = Vos + (vos*t);
    Nas= Cas*Vs;
    Nans= Cans*Vs;
    Faos = Caos*vos;
    Fcos = Ccos*vos;
    Ftos = Ctos*vos;
    ks= (4.01*10**3)*np.exp(-29000/(8.314*Ts))
    ras= -ks*(Cas)**2
    Qgss= -ras*Vs*64512;
    Qrs1s= ((Faos*Cpa) + (Fcos*Cpc) + (Ftos*Cpt))*(Ts - 310);
    Qrs2s= UAS*(Ts - 298);
    Qrss= Qrs1s + Qrs2s + 8.3;
    NCps= (Nas*Cpa) + (Ncs*Cpc) + (Nts*Cpt) + (Nans*Cpan);
    # Differential equations
    dCadt = (vo*10**-5/V)*(Cao - Ca) + ra
    dNcdt = Cco*vo*10**-5
    dNtdt = Cto*vo*10**-5 
    dCandt = -ra - (Can*(vo*10**-5/V))
    dTdt=((Qgs-Qrs)/NCp)
    dCasdt = (vos/Vs)*(Caos - Cas) + ras
    dNcsdt = Ccos*vos
    dNtsdt = Ctos*vos
    dCansdt = -ras - (Cans*(vos/V))
    dTsdt=((Qgss-Qrss)/NCps)
    return np.array([dCadt, dNcdt, dNtdt,dCandt, dTdt,dCasdt, dNcsdt, dNtsdt,dCansdt, dTsdt])

tspan = np.linspace(0, 3000, 100) # Range for the independent variable
y0 = np.array([Cai,Nci,Nti,0,355,2.12,2.64,2.20,0,355]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-Synthron Explosion""", fontweight='bold', x = 0.15, y=0.98)
plt.subplots_adjust(left=0.45)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol =  odeint(ODEfun, y0, tspan, (Cao,Cco,Cto,Vo,vo,Cai,Nci,Nti,UA))
Ca = sol[:, 0]
Nc= sol[:, 1]
Nt= sol[:, 2]
Can= sol[:, 3]
T= sol[:, 4]
Cas = sol[:, 5]
Ncs= sol[:, 6]
Nts= sol[:, 7]
Cans= sol[:, 8]
Ts= sol[:, 9]
Vos = 0.73;
vos = 1.5*10**-4;
Vs = Vos + (vos*tspan)
V = Vo + (vo*10**-5*tspan);
k= (4.01*10**3)*np.exp(-29000/(8.314*T))
ra= -k*(Ca)**2;
Qgs= -ra*V*64512;
ks= (4.01*10**3)*np.exp(-29000/(8.314*Ts))
ras= -ks*(Cas)**2
Qgss= -ras*Vs*64512
p1,p2= ax2.plot(tspan, Ts,tspan,T)
ax2.legend([r'$T_{Original\hspace{0.5} Recipe}$',r'$T_{Modified \hspace{0.5} Recipe}$'], loc='upper right')
ax2.set_xlabel('time $(sec)$', fontsize='medium')
ax2.set_ylabel(r'$Temp$ (K)', fontsize='medium')
ax2.grid()
ax2.set_ylim(300, 600)
ax2.set_xlim(0, 3000)

p3,p4 = ax3.plot(tspan, Cas,tspan,Ca)
ax3.legend([r'$Ca_{\hspace{0.5} Original\hspace{0.5} Recipe}$',r'$Ca_{\hspace{0.5} Modified\hspace{0.5} Recipe}$'], loc='upper right')
ax3.set_xlabel('time $(sec)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration (kmol/m^3)$', fontsize='medium')
ax3.grid()
ax3.set_ylim(0, 0.5)
ax3.set_xlim(0, 3000)

p7,p8 = ax4.plot(tspan,Qgss,tspan,Qgs)
ax4.legend([r'$Qg_{\hspace{0.5}  Original\hspace{0.5} Recipe}$',r'$Qg_{\hspace{0.5}  Modified\hspace{0.5} Recipe}$'], loc='upper right')
ax4.set_xlabel('time $(sec)$', fontsize='medium')
ax4.set_ylabel(r'Heat gen $(J/s)$', fontsize='medium')
ax4.grid()
ax4.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
ax4.set_ylim(0, 2e5)
ax4.set_xlim(0, 100)

ax1.text(-2,-1.2,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} =(v_{0}/V)*(Cao-Ca)+ra$'
         '\n'
         r'$\dfrac{dN_C}{dt} =C_{C0}*v_0$'
         '\n'
         r'$\dfrac{dN_t}{dt} =C_{T0}*v_0$'
         '\n'
         r'$\dfrac{C_{AN}}{dt}=-r_A -(C_{AN}*(v_0/V))$'
         '\n'
          r'$\dfrac{dT}{dt}=(Q_{gs}-Q_{rs})/NCp$'
         '\n\n'
         'Explicit Equations'
         '\n\n'
         r'$V=V_0+(v_0*t)$'
         '\n\n'
         r'$N_{A}=C_A*V$'
        '\n'
         r'$N_{AN}=C_{AN}*V$'
        '\n\n'
         r'$F_{A0}=C_{A0}*v_0$'
         '\n'
         r'$F_{C0}=C_{C0}*v_0$'
         '\n'
         r'$F_{T0}=C_{T0}*v_0$'
         '\n\n'
         r'$k=4.01*10^3*exp(-29000/(8.314*T))$'
         '\n'
         r'$r_{A}=-k*(C_A)^2  $'
         '\n\n'
         r'$Q_{gs}=-r_A*V*64512 $'
         '\n\n'
         r'$Q_{rs1}=(F_{A0}*C_{PA}+F_{C0}*C_{PC}+F_{T0}*C_{PT})*(T-310)$'
         '\n'
         r'$Q_{rs2}=UA*(T-298)$'
         '\n'
         r'$Q_{rs}=Q_{rs1}+Q_{rs2}+8.3$'
         '\n\n'
         r'$N_{CP}=N_{A}*C_{PA}+N_{C}*C_{PC}+N_{T}*C_{PT}+N_{AN}*C_{PAN}$'
          , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

ax1.axis('off')
axcolor = 'black'
ax_Cao = plt.axes([0.45, 0.82, 0.15, 0.015], facecolor=axcolor)
ax_Vo = plt.axes([0.45, 0.78, 0.15, 0.015], facecolor=axcolor)
ax_vo = plt.axes([0.45, 0.74, 0.15, 0.015], facecolor=axcolor)
ax_Cai = plt.axes([0.45, 0.70, 0.15, 0.015], facecolor=axcolor)
ax_Nci = plt.axes([0.45, 0.66, 0.15, 0.015], facecolor=axcolor)
ax_Nti = plt.axes([0.45, 0.62, 0.15, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.45, 0.58, 0.15, 0.015], facecolor=axcolor)


sCao = Slider(ax_Cao, r'$C_{A0}$($\frac{kmol}{m^3}$)', 0.5, 20, valinit=3.99,valfmt='%1.2f')
sVo = Slider(ax_Vo,r'$V_{0}$ ($m^3$)', 0.1,3, valinit= 2.38,valfmt='%1.2f')
svo = Slider(ax_vo,r'$v_0*10^{-5}$ ($\frac{m^3}{s}$)',10**-3, 10**3, valinit=6,valfmt='%1.2f')
sCai = Slider(ax_Cai,r'$C_{A}(0)$($\frac{kmol}{m^3}$)', 0.5, 10, valinit= 2.38,valfmt='%1.2f')
sNci = Slider(ax_Nci,r'$N_{C}(0)$ ($kmol$)', 0.5, 20, valinit= 7.76,valfmt='%1.2f')
sNti = Slider(ax_Nti,r'$N_{T}(0)$ ($kmol$)', 0.5, 20, valinit= 7.09,valfmt='%1.2f')
sUA = Slider(ax_UA,r'$UA$ ($\frac{J}{s.K}$)', 0,15, valinit= 5,valfmt='%1.1f')

def update_plot2(val):
    Cao = sCao.val
    Vo =sVo.val
    vo = svo.val
    Cai =sCai.val
    Nci = sNci.val
    Nti =sNti.val
    UA =sUA.val
    y0 = np.array([Cai,Nci,Nti,0,355,2.12,2.64,2.20,0,355])
    sol = odeint(ODEfun, y0, tspan, (Cao,Cco,Cto,Vo,vo,Cai,Nci,Nti,UA))
    Ca = sol[:, 0]
    T= sol[:, 4]
    Cas = sol[:, 5]
    Ts= sol[:, 9]
    V = Vo + (vo*10**-5*tspan);
    k= (4.01*10**3)*np.exp(-29000/(8.314*T))
    ra= -k*(Ca)**2;
    Qgs= -ra*V*64512;

    p1.set_ydata(Ts)
    p2.set_ydata(T)
    p3.set_ydata(Cas)
    p4.set_ydata(Ca)
    p7.set_ydata(Qgss)
    p8.set_ydata(Qgs)
    fig.canvas.draw_idle()

sCao.on_changed(update_plot2)
sVo.on_changed(update_plot2)
svo.on_changed(update_plot2)
sCai.on_changed(update_plot2)
sNci.on_changed(update_plot2)
sNti.on_changed(update_plot2)
sUA.on_changed(update_plot2)

resetax = plt.axes([0.48, 0.87, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCao.reset()
    sVo.reset()
    svo.reset()
    sCai.reset()
    sNci.reset()
    sNti.reset()
    sUA.reset()

button.on_clicked(reset)
    
