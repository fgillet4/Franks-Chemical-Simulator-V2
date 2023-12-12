#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import ScalarFormatter

#%%
# Explicit Equation
k1a = 10 
k2c = 15 
Vo = 1000 
vo = 10 
Fao = 3
def ODEfun(Yfuncvec, t, k1a, k2c, Vo, vo, Fao):
    Nb = Yfuncvec[0] 
    Na = Yfuncvec[1] 
    Nd = Yfuncvec[2]
    Nc = Yfuncvec[3]
    # Explicit equations
    V = Vo + vo * t 
    Ca = Na / V 
    Cb = Nb / V 
    r1a = 0 - (k1a * Ca * Cb ** 2) 
    Cc = Nc / V 
    r1b = 2 * r1a 
    rb = r1b 
    r2c = 0 - (k2c * Ca ** 2 * Cc ** 3) 
 
    r2a = 2 / 3 * r2c 
    r2d = -1 / 3 * r2c 
    r1c = 0 - r1a 
    rd = r2d 
    ra = r1a + r2a 
    Cd = Nd / V 
    rc = r1c + r2c 
#    if (t > 0.0001) 
#        Scd = Nc / Nd
#    else
#        Scd = 0
#    end 
    # Differential equations
    dNbdt = rb * V 
    dNadt = ra * V + Fao 
    dNddt = rd * V 
    dNcdt = rc * V 
    return np.array([dNbdt, dNadt, dNddt, dNcdt]) 

tspan = np.linspace(0, 100, 1000) # Range for the independent variable
y0 = np.array([200, 0, 0, 0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-7 Complex Reactions in a Semibatch Reactor""", x = 0.3, y = 0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
sol = odeint(ODEfun, y0, tspan, (k1a, k2c, Vo, vo, Fao))
Nb = sol[:, 0]
Na = sol[:, 1]
Nd = sol[:, 2]
Nc = sol[:, 3]
Scd = np.nan_to_num(Nc/Nd)
Nbo = 200
X = 1 - Nb/Nbo

p1, p2, p3, p4 = ax2.plot(tspan, Na, tspan, Nb, tspan, Nc, tspan, Nd )
ax2.legend([r'$N_A$', r'$N_B$', r'$N_C$', r'$N_D$'], loc='upper right')
ax2.set_xlabel('time(min)', fontsize='medium',)
ax2.set_ylabel('$N_i (moles)$', fontsize='medium',)
ax2.set_ylim(0,300)
ax2.set_xlim(0,100)
ax2.grid()
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p5 = ax3.plot(tspan, Scd)[0]
ax3.legend(['$S_{C/D}$'], loc='upper right')
ax3.set_ylim(0 , 8e9)
ax3.set_xlim(0,100)
ax3.grid()
ax3.set_xlabel('time(min)', fontsize='medium', )
ax3.set_ylabel('Selectivity', fontsize='medium', )
ax3.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))

#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p6= ax4.plot(tspan, X)[0]
ax4.legend(['X'], loc='upper left')
ax4.set_ylim(0,1)
ax4.set_xlim(0,100)
ax4.grid()
ax4.set_xlabel('time(min)', fontsize='medium', )
ax4.set_ylabel('Conversion', fontsize='medium', )
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

ax1.axis('off')
ax1.text(-1.0, -1.4,'Differential Equations'
         '\n\n'
         r'$\dfrac{dN_B}{dt} = r_BV$'
                  '\n '
         r'$\dfrac{dN_A}{dt} = r_AV + F_{A0}$'
                  '\n '
                           r'$\dfrac{dN_D}{dt} = r_DV$'
                  '\n '
                           r'$\dfrac{dN_C}{dt} = r_CV$'
                  '\n\n '
         'Explicit Equations'
                  '\n\n'
         r'$V = V_0 + v_0.t$'
         '\n'         
         r'$C_A = \dfrac{N_A}{V}$'
         '\n'
         r'$C_B = \dfrac{N_B}{V}$'
         '\n'
         r'$V_0 = 1000$'
         '\n'
          r'$v_o = 10$'
         '\n'
         r'$r_{1A} = -k_{1A}C_AC_B^2$'
         '\n'
         r'$C_C = \dfrac{N_C}{V}$'
         '\n'
         r'$r_{1B} = 2.r_{1A}$'         '\n'
         r'$r_B = r_{1B}$'         '\n'
         r'$r_{2C} = -k_{2C}C_A^2C_C^3$'         '\n'
         r'$r_{2A} = \dfrac{2.r_{2C}}{3}$'         '\n'
         r'$r_{2D} = \dfrac{-r_{2C}}{3}$'         '\n'
         r'$r_{1C} = -r_{1A}$'  '\n'     
         r'$r_D = r_{2D}$'  '\n'  
         r'$r_A = r_{1A} + r_{2A}$'  '\n'  
         r'$C_D = \dfrac{N_D}{V}$'  '\n'  
         r'$r_C = r_{1C}+r_{2C}$'  '\n'  
          r'$S_{C/D} = \dfrac{N_C}{N_D}$'  '\n'  
           r'$N_{B0} = 200$'  '\n'  
            r'$X = 1 - \dfrac{N_B}{N_{B0}}$'  
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
axcolor = 'black'
ax_k1a = plt.axes([0.35, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_k2c = plt.axes([0.35, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Fao = plt.axes([0.35, 0.60, 0.2, 0.02], facecolor=axcolor)

sk1a= Slider(ax_k1a, r'k$_{1A} (\frac{dm^6}{mol^2.min})$', 5, 50, valinit=10,valfmt="%1.1f")
sk2c = Slider(ax_k2c, r'k$_{2C} (\frac{dm^{12}}{mol^4.min})$', 5, 100, valinit=15,valfmt="%1.1f")
sFao = Slider(ax_Fao, r'F$_{Ao}$ ($\frac{mol}{min}$)', 0.5, 50, valinit=3,valfmt="%1.1f")


def update_plot2(val):
    k1a =sk1a.val
    k2c =sk2c.val
    Fao = sFao.val
    
    sol = odeint(ODEfun, y0, tspan, (k1a, k2c, Vo, vo, Fao))
    Nb = sol[:, 0]
    Na = sol[:, 1]
    Nd = sol[:, 2]
    Nc = sol[:, 3]
    Scd = np.nan_to_num(Nc/Nd)
    Nbo = 200
    X = 1 - Nb/Nbo
    p1.set_ydata(Na)
    p2.set_ydata(Nb)
    p3.set_ydata(Nc)
    p4.set_ydata(Nd)
    p5.set_ydata(Scd)
    p6.set_ydata(X)
  
    fig.canvas.draw_idle()

sk1a.on_changed(update_plot2)
sk2c.on_changed(update_plot2)
sFao.on_changed(update_plot2)

resetax = plt.axes([0.4, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1a.reset()
    sk2c.reset()
    sFao.reset()
    
button.on_clicked(reset)