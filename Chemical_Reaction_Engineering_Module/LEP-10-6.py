#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
Ka=0.05
Kb=0.15
Pao=12
eps=1
A=7.6
R=0.082
T=400+273
rho=80
kprime=0.0014
Dia=1.5
Uo=2.5
Kc=0.1
def ODEfun(Y, z, Ka, Kb, Pao, eps, A, T, rho, kprime, Dia, Uo, Kc): 
    X=Y[0]
    #Explicit Equation Inline
    U=Uo*(1+eps*X)
    Pa=Pao*(1-X)/(1+eps*X)
    Pb=Pao*X/(1+eps*X)
    Cao=Pao/R/T
    Pc=Pb
    a=1/(1+A*(z/U)**0.5)
    raprime=a*(-kprime*Pa/(1+Ka*Pa+Kb*Pb+Kc*Pc))
    ra=rho*raprime
    # Differential equations
    dXdz = -ra/Uo/Cao
    return dXdz 

zspan = np.linspace(0, 10, 1000)
y0 = [0]


#%%
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.suptitle("""Example 10-6 Decay in a Straight-Through Transport Reactor""", fontweight='bold', x = 0.25, y= 0.98)

plt.subplots_adjust(left  = 0.55)

sol = odeint(ODEfun, y0, zspan, (Ka, Kb, Pao, eps, A, 
                                 T, rho, kprime, Dia, Uo, Kc))
X = sol[:, 0]
U=Uo*(1+eps*X) 
Pa=Pao*(1-X)/(1+eps*X)
Pb=Pao*X/(1+eps*X)
Cao=Pao/R/T
Pc=Pb
a=1/(1+A*(zspan/U)**0.5)
raprime=a*(-kprime*Pa/(1+Ka*Pa+Kb*Pb+Kc*Pc))
ra=rho*raprime

p1, p2 = ax1.plot(zspan, X, zspan, a)
ax1.legend(['X', 'a'], loc='upper right')
ax1.set_xlabel('z (m)', fontsize='medium')
ax1.set_ylabel('X, a', fontsize='medium')
plt.ylim(0,1)
plt.xlim(0,10)
ax1.grid()

p3 = plt.plot(zspan, -ra)[0]
ax2.legend(['$-r_A$'], loc='upper right')
plt.ylim(0,0.8)
plt.xlim(0, 10)
ax2.grid()
ax2.set_xlabel('z (m)', fontsize='medium')
ax2.set_ylabel('Rate ($kmol/m^3.s$)', fontsize='medium')

ax2.text(-15.2, 0.15,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dz} = \dfrac{-r_A}{U_0 C_{A0}}$'

                  '\n \n'
                  
         'Explicit Equations'
                  '\n\n'
         r'$R = 0.082$'
                  '\n\n'
         r'$U = U_0(1+\epsilon X)$'
         '\n\n'
         r'$P_A = \dfrac{P_{A0}(1-X)}{1+ \epsilon X}$'
         '\n\n'
         r'$P_B = \dfrac{P_{A0}X}{1+ \epsilon X}$'
         '\n\n'
         r'$v_0 = \dfrac{U_0 \pi D^2}{4}$'
                  '\n\n'
         r'$C_{A0} = \dfrac{P_{A0}}{R T}$'
         '\n\n'
         r'$P_C = P_B$'
         '\n\n'
         r'$a = \dfrac{1}{1+A \sqrt{\dfrac{z}{U}}}$'
                  '\n\n'
         r'$-r_A^{\prime} = \dfrac{k^{\prime} P_A}{1+K_AP_A+K_BP_B+K_CP_C}$'
                  '\n\n'
         r'$-r_A = a\rho_B r_A^{\prime}$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
#%%
axcolor = 'black'
ax_Ka = plt.axes([0.25, 0.8, 0.15, 0.02], facecolor=axcolor)
ax_Kb = plt.axes([0.25, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_Pao = plt.axes([0.25, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_eps = plt.axes([0.25, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_A = plt.axes([0.25, 0.6, 0.15, 0.02], facecolor=axcolor)
ax_T = plt.axes([0.25, 0.55, 0.15, 0.02], facecolor=axcolor)
ax_rho = plt.axes([0.25, 0.5, 0.15, 0.02], facecolor=axcolor)
ax_kprime = plt.axes([0.25, 0.45, 0.15, 0.02], facecolor=axcolor)
ax_Uo = plt.axes([0.25, 0.4, 0.15, 0.02], facecolor=axcolor)
ax_Kc = plt.axes([0.25, 0.35, 0.15, 0.02], facecolor=axcolor)

sKa = Slider(ax_Ka, '$K_A$ ($atm^{-1}$)', 0.01, 1, valinit=.05,valfmt='%1.2f')
sKb = Slider(ax_Kb, '$K_B$ ($atm^{-1}$)', 0.01, 1, valinit=0.15,valfmt='%1.2f')
sPao= Slider(ax_Pao, '$P_{A0}$ (atm)', 1,50, valinit=12,valfmt='%1.0f')
seps = Slider(ax_eps, '$\epsilon$', 0.1,10, valinit=1)
sA = Slider(ax_A, 'A ($s^{-1/2}$)', 1,20, valinit=7.6)
sT = Slider(ax_T, 'T (K)', 400,1000, valinit= 400+273,valfmt='%1.1f')
srho = Slider(ax_rho, r'$\rho$$_{b}$($\frac{kg-cat}{m^3}$)', 5,200, valinit=80)
skprime = Slider(ax_kprime, r'$k^\prime$($\frac{kmol}{kg-cat.s.atm}$)', 0.0001, 0.01, valinit=0.0014)
sUo = Slider(ax_Uo, r'$U_0$($\frac{m}{s})$', 0.5,5, valinit=2.5)
sKc = Slider(ax_Kc, '$K_C$ ($atm^{-1}$)', 0.01, 1, valinit=0.1)


def update_plot2(val):
    Ka = sKa.val
    Kb = sKb.val
    Pao =sPao.val
    eps = seps.val
    A =sA.val
    T = sT.val
    rho = srho.val
    kprime = skprime.val
    Uo = sUo.val
    Kc = sKc.val
    sol = odeint(ODEfun, y0, zspan, (Ka,Kb, Pao, eps, A, T, rho, kprime, 
                                     Dia, Uo, Kc))
    X = sol[:, 0]
    U=Uo*(1+eps*X)
    Pa=Pao*(1-X)/(1+eps*X)
    Pb=Pao*X/(1+eps*X)
    Cao=Pao/R/T
    Pc=Pb
    a=1/(1+A*(zspan/U)**0.5)
    raprime=a*(-kprime*Pa/(1+Ka*Pa+Kb*Pb+Kc*Pc))
    ra=rho*raprime
    
    p1.set_ydata(X)
    p2.set_ydata(a)
    p3.set_ydata(-ra)
    fig.canvas.draw_idle()


sKa.on_changed(update_plot2)
sKb.on_changed(update_plot2)
sPao.on_changed(update_plot2)
seps.on_changed(update_plot2)
sA.on_changed(update_plot2)
sT.on_changed(update_plot2)
srho.on_changed(update_plot2)
skprime.on_changed(update_plot2)
sUo.on_changed(update_plot2)
sKc.on_changed(update_plot2)
#

resetax = plt.axes([0.28, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKa.reset()
    sKb.reset()
    sPao.reset()
    seps.reset()
    sA.reset()
    sT.reset()
    srho.reset()
    skprime.reset()
    sUo.reset()
    sKc.reset()
button.on_clicked(reset)
    
