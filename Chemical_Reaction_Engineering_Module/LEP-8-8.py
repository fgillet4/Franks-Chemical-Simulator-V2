#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import ScalarFormatter,FormatStrFormatter

#%%
# Explicit Equation
Cto = 0.8
k1a = 2
k2a = 3
Vt = 50
Fbo = 4
def ODEfun1(Yfuncvec, V, Cto, k1a, k2a, Vt, Fbo):
    Fa = Yfuncvec[0] 
    Fb = Yfuncvec[1] 
    Fd = Yfuncvec[2] 
    Fu = Yfuncvec[3]     
    # Explicit equations Inline
    Ft = Fa + Fb + Fd + Fu
    Cb = Cto * Fb / Ft
    Ca = Cto * Fa / Ft
    ra = 0 - (k1a * Ca ** 2 * Cb) - (k2a * Ca * Cb ** 2)
    rb = ra
    rd = k1a * Ca ** 2 * Cb
    ru = k2a * Ca * Cb ** 2
    Rb = Fbo / Vt
    # Differential equations
    dFadV = ra
    dFbdV = rb + Rb
    dFddV = rd
    dFudV = ru
    return np.array([dFadV, dFbdV, dFddV, dFudV])

def ODEfun2(Yfuncvec, V, Cto, k1a, k2a, Vt, Fbo):
    Fa = Yfuncvec[0] 
    Fb = Yfuncvec[1] 
    Fd = Yfuncvec[2] 
    Fu = Yfuncvec[3]     
    # Explicit equations Inline
    Ft = Fa + Fb + Fd + Fu 
    Cb = Cto * Fb / Ft 
    Ca = Cto * Fa / Ft 
    ra = 0 - (k1a * Ca ** 2 * Cb) - (k2a * Ca * Cb ** 2) 
    rb = ra 
    Cd = Cto * Fd / Ft 
    Cu = Cto * Fu / Ft 
    rd = k1a * Ca ** 2 * Cb 
    ru = k2a * Ca * Cb ** 2 
    Sdu = Fd / (Fu + 0.000000001) 
    # Differential equations
    dFadV = ra 
    dFbdV = rb 
    dFddV = rd 
    dFudV = ru 
    return np.array([dFadV, dFbdV, dFddV, dFudV])

Vspan = np.linspace(0, 50, 1000) # Range for the independent variable
y0 = np.array([4 , 0, 0, 0]) # Initial values for the dependent variables
y1 = np.array([4 , 4, 0, 0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-8 Membrane Reactor to improve Selectivity in Multiple Reactions""", x = 0.25, y = 0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.35,hspace=0.35)

#MR solution
sol = odeint(ODEfun1, y0, Vspan, (Cto, k1a, k2a, Vt, Fbo))
Fa = sol[:, 0] 
Fb = sol[:, 1] 
Fd = sol[:, 2] 
Fu = sol[:, 3] 
Sdu = Fd / (Fu + 0.0000000000001)
X=1-Fa/4

#PFR Solution
sol1 = odeint(ODEfun2, y1, Vspan, (Cto, k1a, k2a, Vt, Fbo))
Fa1 = sol1[:, 0] 
Fb1 = sol1[:, 1] 
Fd1 = sol1[:, 2] 
Fu1 = sol1[:, 3] 
Sdu1 = Fd1 / (Fu1 + 0.000000001)
X1=1-Fa1/4

p1, p2, p3, p4 = ax1.plot(Vspan, Fa, Vspan, Fb, Vspan, Fd, Vspan, Fu)
ax1.legend([r'$F_A$', r'$F_B$', r'$F_D$', r'$F_U$'], loc='upper right')
ax1.set_ylim(0,4)
ax1.set_xlim(0,50)
ax1.grid()
ax1.set_title('MR')

ax1.set_xlabel(r'V ($dm^3$)', fontsize='medium')
ax1.set_ylabel(r'$F_i (mol/s)$', fontsize='medium')

p5, p6, p7, p8 = ax2.plot(Vspan, Fa1, Vspan, Fb1, Vspan, Fd1, Vspan, Fu1)
ax2.legend([r'$F_A$', r'$F_B$', r'$F_D$', r'$F_U$'], loc='upper right')
ax2.set_ylim(0,4)
ax2.set_xlim(0,50)
ax2.grid()
ax2.set_title('PFR')
ax2.set_xlabel(r'V ($dm^3$)', fontsize='medium')
ax2.set_ylabel(r'$F_i (mol/s)$', fontsize='medium')
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p9,p10 = ax3.plot(Vspan, Sdu,Vspan,Sdu1)
ax3.legend([r'$MR$',r'$PFR$'], loc='upper right')
ax3.set_ylim(0,60)
ax3.set_xlim(0,50)
ax3.grid()
ax3.set_xlabel(r'V ($dm^3$)', fontsize='medium')
ax3.set_ylabel(r'$S_{D/U}$', fontsize='medium')
ax3.set_title('Selectivity profile')



p11,p12 = ax4.plot(Vspan,X,Vspan,X1)
ax4.legend([r'$MR$',r'$PFR$'], loc='upper right')
#ax4.set_ylim(0,60)
ax4.set_xlim(0,50)
ax4.set_ylim(0,1)
ax4.set_title('Conversion Profile')
ax4.grid()
ax4.set_xlabel(r'V ($dm^3$)', fontsize='medium')
ax4.set_ylabel('Conversion', fontsize='medium')
ax4.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.text(-70, -6.2,'Membrane Reactor'
         '\n\n'
         'Differential Equations'
         '\n'
         r'$\dfrac{dF_A}{dV} = r_A$'
                  '\n'
         r'$\dfrac{dF_B}{dV} = r_B + R_B$'
                  '\n'
                           r'$\dfrac{dF_D}{dV} = r_D$'
                  '\n'
                           r'$\dfrac{dF_U}{dV} = r_U$'
                  '\n\n'
         'Explicit Equations'
                  '\n'
         r'$F_T = F_A + F_B + F_D + F_U$'
         '\n'         
         r'$C_B = \dfrac{C_{T0}F_B}{F_T}$'
         '\n'
         r'$C_A = \dfrac{C_{T0}F_A}{F_T}$'
         '\n'
         r'$r_A = -k_{1A}C_A^2C_B - k_{2A}C_AC_B^2$'
         '\n'
         r'$r_B = r_A$'
         '\n'
         r'$C_D = \dfrac{C_{T0}F_D}{F_T}$'
         '\n'
         r'$C_U = \dfrac{C_{T0}F_U}{F_T}$'
         '\n'    
         r'$r_D = k_{1A}C_A^2C_B $'
         '\n'
         r'$r_U = k_{2A}C_AC_B^2$'
         '\n'         
         r'$R_B = \dfrac{F_{B0}}{V_t}$'
         '\n'         
         r'$S_{D/U} = \dfrac{F_D}{F_U}$'         '\n'         
         r'$F_{A0} = 4$'         '\n'         
         r'$X = 1 - \dfrac{F_A}{F_{A0}}$'         
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')

ax1.text(-40, -6.1, 'Plug Flow Reactor'
         '\n\n'
         'Differential Equations'
         '\n\n'
         r'$\dfrac{dF_A}{dV} = r_A$'
                  '\n'
         r'$\dfrac{dF_B}{dV} = r_B$'
                  '\n'
                           r'$\dfrac{dF_D}{dV} = r_D$'
                  '\n'
                           r'$\dfrac{dF_U}{dV} = r_U$'
                  '\n\n'
         'Explicit Equations'
                  '\n\n'
         r'$F_T = F_A + F_B + F_D + F_U$'
         '\n'         
         r'$C_B = \dfrac{C_{T0}F_B}{F_T}$'
         '\n'
         r'$C_A = \dfrac{C_{T0}F_A}{F_T}$'
         '\n'
         r'$r_A = -k_{1A}C_A^2C_B - k_{2A}C_AC_B^2$'
         '\n'
         r'$r_B = r_A$'
         '\n'
         r'$C_D = \dfrac{C_{T0}F_D}{F_T}$'
         '\n'
         r'$C_U = \dfrac{C_{T0}F_U}{F_T}$'
         '\n'    
         r'$r_D = k_{1A}C_A^2C_B $'
         '\n'
         r'$r_U = k_{2A}C_AC_B^2$'
         '\n'                 
         r'$S_{D/U} = \dfrac{F_D}{F_U}$'         '\n'         
         r'$F_{A0} = 4$'         '\n'         
         r'$X = 1 - \dfrac{F_A}{F_{A0}}$'         
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')

ax2.text(3.2,3.3, r'$F_{A}= F_{B}$')

#%%
axcolor = 'black'
ax_Vt = plt.axes([0.1, 0.85, 0.2, 0.015], facecolor=axcolor)
ax_k1a = plt.axes([0.1, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_k2a = plt.axes([0.1, 0.79, 0.2, 0.015], facecolor=axcolor)
ax_Cto = plt.axes([0.1, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_Fbo = plt.axes([0.1, 0.73, 0.2, 0.015], facecolor=axcolor)


sVt = Slider(ax_Vt, r'V$_t$  ($dm^3$)', 10, 500, valinit=50, valfmt="%1.0f")
sk1a= Slider(ax_k1a, r'k$_{1A}$ ($\frac{dm^6}{mol^2.s}$)', 1, 100, valinit=2, valfmt="%1.0f")
sk2a = Slider(ax_k2a, r'k$_{2A}$ ($\frac{dm^6}{mol^2.s}$)', 1, 100, valinit=3, valfmt="%1.0f")
sCto = Slider(ax_Cto, r'C$_{To} (\frac{mol}{dm^3})$ ', 0.1, 2, valinit=0.8)
sFbo = Slider(ax_Fbo, r'F$_{Bo} (\frac{mol}{sec})$', 1, 50, valinit=4, valfmt="%1.0f")


def update_plot2(val):
    Vt = sVt.val
    k1a =sk1a.val
    k2a =sk2a.val
    Cto = sCto.val
    Fbo = sFbo.val
    
    sol = odeint(ODEfun1, y0, Vspan, (Cto, k1a, k2a, Vt, Fbo))
    Fa = sol[:, 0] 
    Fb = sol[:, 1] 
    Fd = sol[:, 2] 
    Fu = sol[:, 3] 
    Sdu = Fd / (Fu + 0.0000000000001)
    X=1-Fa/4
    
    sol1 = odeint(ODEfun2, y1, Vspan, (Cto, k1a, k2a, Vt, Fbo))
    Fa1 = sol1[:, 0] 
    Fb1 = sol1[:, 1] 
    Fd1 = sol1[:, 2] 
    Fu1 = sol1[:, 3] 
    Sdu1 = Fd1 / (Fu1 + 0.000000001)
    X1=1-Fa1/4
    
    p1.set_ydata(Fa)
    p2.set_ydata(Fb)
    p3.set_ydata(Fd)
    p4.set_ydata(Fu)
    p5.set_ydata(Fa1)  
    p6.set_ydata(Fb1)
    p7.set_ydata(Fd1)
    p8.set_ydata(Fu1)
    p9.set_ydata(Sdu)
    p10.set_ydata(Sdu1)    
    p11.set_ydata(X)
    p12.set_ydata(X1)  
    fig.canvas.draw_idle()


sVt.on_changed(update_plot2)
sk1a.on_changed(update_plot2)
sk2a.on_changed(update_plot2)
sCto.on_changed(update_plot2)
sFbo.on_changed(update_plot2)

#

resetax = plt.axes([0.15, 0.88, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sVt.reset()
    sk1a.reset()
    sk2a.reset()
    sCto.reset()
    sFbo.reset()

button.on_clicked(reset)