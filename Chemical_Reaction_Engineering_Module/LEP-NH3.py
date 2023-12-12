#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
k1A = 5
k2A = 2
k3B = 10
k4C = 5
Cto = 2
def ODEfun(Yfuncvec, V, k1A, k2A, k3B, k4C, Cto): 
    FA =Yfuncvec[0]
    FB =Yfuncvec[1]
    FC = Yfuncvec[2]
    FD = Yfuncvec[3]
    FE = Yfuncvec[4]
    FF = Yfuncvec[5]
    # Explicit equations
    
    Ft = FA+FB+FC+FD+FE+FF 
    r1A = -k1A*Cto**3*(FA/Ft)*(FB/Ft)**2
    r2A = -k2A*Cto**2*(FA/Ft)*(FB/Ft)
    r4C = -k4C*Cto**(5/3)*(FC/Ft)*(FA/Ft)**(2/3)
    r3B = -k3B*Cto**3*(FC/Ft)**2*(FB/Ft)
    CA = 2*FA/Ft
    rA = r1A+r2A+2*r4C/3
    rB = 1.25*r1A+.75*r2A+r3B
    rC = -r1A+2*r3B+r4C
    rD = -1.5*r1A-1.5*r2A-r4C
    rE = -.5*r2A-5*r4C/6
    rF = -2*r3B
    # Differential equations
    dFAdV = rA
    dFBdV = rB
    dFCdV = rC
    dFDdV = rD
    dFEdV = rE
    dFFdV = rF
    return np.array([dFAdV,dFBdV,dFCdV,dFDdV,dFEdV,dFFdV])






tspan = np.linspace(0, 10, 1000)
y0 = np.array([10,10, 0, 0, 0, 0])


#%%
fig, ax = plt.subplots()
fig.suptitle("""LEP-NH3:Calculating Concentrations as a Function of Position for NH3 Oxidation in a PFR""", x = 0.35, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (k1A, k2A, k3B, k4C, Cto))
FA = sol[:, 0]
FB = sol[:, 1]
FC = sol[:, 2]
FD = sol[:, 3]
FE = sol[:, 4]
FF = sol[:, 5]

p1, p2, p3, p4, p5, p6 = plt.plot(tspan, FA, tspan, FB,tspan,FC,
                                  tspan, FD,tspan, FE,tspan, FF)
plt.legend([r'$F_A$', r'$F_B$', r'$F_C$' ,r'$F_D$' ,r'$F_E$' ,r'$F_F$'], loc='best')
ax.set_xlabel(r'V ($dm^3$)', fontsize='medium')
ax.set_ylabel(r'F$_i$ (mol/min)', fontsize='medium')
plt.ylim(0,14)
plt.xlim(0,10)
plt.grid()

ax.text(-12, -0.5,'Differential Equations'
         '\n\n'
         r'$\dfrac{dF_{A}}{dV} = r_A$'
                  '\n'
         r'$\dfrac{dF_{B}}{dV} = r_B$'
                  '\n'
         r'$\dfrac{dF_{C}}{dV} = r_C$'
                  '\n'
         r'$\dfrac{dF_{D}}{dV} = r_D$'
                  '\n'
         r'$\dfrac{dF_{E}}{dV} = r_E$'
                  '\n'
         r'$\dfrac{dF_{F}}{dV} = r_F$'
                  '\n\n'                  
         'Explicit Equations' '\n\n'
         r'$F_T = F_A + F_B + F_C + F_D + F_E + F_F $'
         '\n\n'
         r'$r_{1A} = -k_{1A}\thinspaceC_{T0}^3\thinspace\dfrac{F_A}{F_T} \thinspace \left (\dfrac{F_B}{F_T}\right)^2$'
         '\n\n'
         r'$r_{2A} = -k_{2A}\thinspaceC_{T0}^2 \thinspace\dfrac{F_A}{F_T} \thinspace \dfrac{F_B}{F_T}$'
         '\n\n'
         r'$r_{4C} = -k_{4C}\thinspaceC_{T0}^{\frac{5}{3}} \thinspace \dfrac{F_C}{F_T} \left(\dfrac{F_A}{F_T}\right)^{\frac{2}{3}} $'
         '\n\n'
         r'$r_{3B} = -k_{3B}\thinspace C_{T0}^3 \thinspace\dfrac{F_B}{F_T} \thinspace \left (\dfrac{F_C}{F_T}\right)^2$'
         '\n\n'
         r'$C_A = \dfrac{2F_A}{F_T} $'
         '\n'
         r'$r_A =  r_{1A} + r_{2A} + 2r_{4C}/3$'
         '\n'  
         r'$r_B = 1.25r_{1A} + 0.75r_{2A} + r_{3B} $'
         '\n'  
         r'$r_C = -r_{1A} + 2r_{3B} + r_{4C} $'
         '\n'  
         r'$r_D = -1.5r_{1A}-1.5r_{2A} -r_{4C} $'
         '\n'  
         r'$r_E = -0.5r_{2A} - 5r_{4C}/6 $'
         '\n'  
         r'$r_F = -2r_{3B} $'
         
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')

#%%

# Slider Code
axcolor = 'black'
ax_k1A = plt.axes([0.26, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_k2A = plt.axes([0.26, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_k3B = plt.axes([0.26, 0.6, 0.15, 0.02], facecolor=axcolor)
ax_k4C = plt.axes([0.26, 0.55, 0.15, 0.02], facecolor=axcolor)
ax_Cto = plt.axes([0.26, 0.5, 0.15, 0.02], facecolor=axcolor)

sk1A = Slider(ax_k1A, r'k$_{1A} (\frac{m^6}{kmol^2.min})$', 1, 20., valinit=5)
sk2A = Slider(ax_k2A, r'k$_{2A} (\frac{m^3}{kmol.min})$', 1, 20, valinit=2)
sk3B = Slider(ax_k3B, r'k$_{3B} (\frac{m^6}{kmol^2.min}) $', 1, 50, valinit=10)
sk4C = Slider(ax_k4C, r'k$_{4C} (\frac{m^2}{kmol^{2/3}.min})$', 1, 20, valinit=5)
sCto = Slider(ax_Cto, r'C$_{T0} (\frac{mol}{dm^3})$', 1, 20, valinit=2)

def update_plot1(val):
    k1A = sk1A.val
    k2A =sk2A.val
    k3B = sk3B.val
    k4C = sk4C.val
    Cto = sCto.val
    sol = odeint(ODEfun, y0, tspan, (k1A, k2A, k3B, k4C, Cto))
    FA = sol[:, 0]
    FB = sol[:, 1]
    FC = sol[:, 2]
    FD = sol[:, 3]
    FE = sol[:, 4]
    FF = sol[:, 5]
    p1.set_ydata(FA)
    p2.set_ydata(FB)
    p3.set_ydata(FC)
    p4.set_ydata(FD)
    p5.set_ydata(FE)
    p6.set_ydata(FF)
    fig.canvas.draw_idle()

sk1A.on_changed(update_plot1)
sk2A.on_changed(update_plot1)
sk3B.on_changed(update_plot1)
sk4C.on_changed(update_plot1)
sCto.on_changed(update_plot1)

resetax = plt.axes([0.29, 0.75, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk1A.reset()
    sk2A.reset()
    sk3B.reset()
    sk4C.reset()
    sCto.reset()
button.on_clicked(reset)
