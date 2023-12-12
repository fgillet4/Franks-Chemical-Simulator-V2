#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
     
#%%
#Explicit equations
T = 698 
Ea = 24000
Fao = 0.0000226
P0=1641
A=8.988*10**9
def ODEfun(Yfuncvec, V, T, Ea,P0,A): 
    Fa= Yfuncvec[0]
    Fb= Yfuncvec[1]
    Fc= Yfuncvec[2]
    #Explicit equations Inline
    Cto = P0 / 8.314 / T 
    Ft = Fa + Fb + Fc 
    Ca = Cto * Fa / Ft 
    k = A * np.exp(-Ea/ (1.987* T))      
    vo = Fao / Cto 
    Tau = V / vo 
    ra =-(k * Ca**2) 
    X = 1 -(Fa / Fao) 
    rb = -ra 
    rc = -(ra / 2) 
    #Differential equations
    dFadV = ra 
    dFbdV = rb 
    dFcdV = rc 
    return np.array([dFadV, dFbdV, dFcdV]) 

Vspan = np.linspace(0, 1e-5, 10000)
y0 = np.array([2.26e-5, 0, 0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

fig.suptitle("""Example 6-1 Gas-Phase Reaction in a Microreactor - Molar Flow Rates""", fontweight='bold', x = 0.25, y= 0.98)
plt.subplots_adjust(left=0.38)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, Vspan, (T, Ea,P0,A))
Fa= sol[:, 0]
Fb= sol[:, 1]
Fc= sol[:, 2]
X = 1 -(Fa / Fao)
k = A * np.exp(-Ea/ (1.987* T))  
Cto = P0 / 8.314 / T 
Ft = Fa + Fb + Fc 
Ca = Cto * Fa / Ft 
ra =-(k * Ca**2) 

p1,p2,p3 = ax2.plot(Vspan, Fa, Vspan, Fb, Vspan, Fc)
ax2.legend([r'F$_A$', r'F$_B$', r'F$_C$'], loc='best')
ax2.set_xlabel(r'V( $dm^{3}$)', fontsize='medium')
ax2.set_ylabel(r'Flow Rates(mol/sec)', fontsize='medium')
ax2.grid()
ax2.set_xlim(0, 1e-5)
ax2.set_ylim(0, 0.00003)
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

p4 = ax3.plot(Vspan, X)[0]
ax3.legend(['X'], loc='upper right')
ax3.set_xlabel(r'V( $dm^{3}$)', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium' )
ax3.grid()
ax3.set_xlim(0, 1e-5)
ax3.set_ylim(0, 1.2)
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

p5 = ax4.plot(Vspan, -ra)[0]
ax4.legend([r'$-r_A$'], loc='upper right')
ax4.set_xlabel(r'V( $dm^{3}$)', fontsize='medium')
ax4.set_ylabel(r'Rate($ mol/dm^3.s)$', fontsize='medium' )
ax4.grid()
ax4.set_xlim(0, 1e-5)
ax4.set_ylim(0, 40)
ax4.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


ax1.axis('off')
ax1.text(-1.5, -1.3,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n           in the textbook, in python we have to use k=A*exp(-E/RT) \n           in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))

ax1.text(-1.4, -0.9,
'Differential Equations'
         '\n'
         r'$\dfrac{dF_A}{dV} = r_A$'
         '\n'
         r'$\dfrac{dF_B}{dV} = r_B$'
         '\n'
         r'$\dfrac{dF_C}{dV} = r_C$'

                  '\n \n'           
         'Explicit Equations'
                  '\n\n'
         r'$A = 8.988*10^{9} \thinspace dm^{3}/(mol.s)$'
         '\n'
         r'$F_{A0} = 2.26*10^{-5}$'
         '\n \n'         
         r'$C_{T0} = \dfrac{P_0}{8.314.T}$'
                  '\n \n'
         r'$F_T = F_A + F_B + F_C$'
         '\n \n'
         r'$C_A = \dfrac{C_{T0} F_A}{F_T}$'
         '\n'
         r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'
         '\n'
         r'$v_0 = \dfrac{F_{A0}}{C_{T0}}$'
                  '\n'
         r'$\tau = \dfrac{V}{v_0}$'
         '\n'
         r'$r_A = -kC_A^2$'
         '\n'
         r'$X = 1 - \dfrac{F_A}{F_{A0}}$'
         '\n'
         r'$r_B = -r_A$'
                  '\n'
         r'$r_C = \dfrac{-r_A}{2}$'
                  '\n'
         r'$rate = -r_A$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%

axcolor = 'black'
ax_T = plt.axes([0.35, 0.76, 0.15, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.35, 0.72, 0.15, 0.015], facecolor=axcolor)
ax_P0 = plt.axes([0.35, 0.68, 0.15, 0.015], facecolor=axcolor)

sT = Slider(ax_T, 'T (K)', 300, 1200, valinit=698, valfmt = "%1.1f")
sEa = Slider(ax_Ea, r'E$ (\frac{cal}{mol})$', 10000, 40000, valinit=24000, valfmt = "%1.0f")
sP0 = Slider(ax_P0, r'$P_0 (kPa)$', 100, 5000, valinit=1641, valfmt = "%1.0f")

def update_plot(val):
    T = sT.val
    Ea = sEa.val
    P0 = sP0.val
    sol = odeint(ODEfun, y0, Vspan, (T, Ea,P0,A))
    Fa= sol[:, 0]
    Fb= sol[:, 1]
    Fc= sol[:, 2]
    X = 1 -(Fa / Fao) 
    k = A * np.exp(-Ea/ (1.987* T))  
    Cto = P0 / 8.314 / T 
    Ft = Fa + Fb + Fc 
    Ca = Cto * Fa / Ft 
    ra =-(k * Ca**2)
    p1.set_ydata(Fa)
    p2.set_ydata(Fb) 
    p3.set_ydata(Fc)
    p4.set_ydata(X)
    p5.set_ydata(-ra)
    fig.canvas.draw_idle()

sT.on_changed(update_plot)
sEa.on_changed(update_plot)
sP0.on_changed(update_plot)

resetax = plt.axes([0.37, 0.82, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sT.reset()
    sEa.reset() 
    sP0.reset() 
button.on_clicked(reset)
plt.show()