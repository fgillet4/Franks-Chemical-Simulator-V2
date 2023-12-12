#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit Equations
k1a = 100 
k2c = 1500 
Cto = 0.2
alpha = 0.0019 
def ODEfun(Yfuncvec, W, k1a, k2c, Cto, alpha): 
    Fa = Yfuncvec[0] 
    Fb = Yfuncvec[1] 
    Fc = Yfuncvec[2] 
    Fd = Yfuncvec[3] 
    p = Yfuncvec[4] 
    # Explicit equations
    Ft = Fa + Fb + Fc + Fd 
     
    Ca = Cto * Fa / Ft * p 
    Cb = Cto * Fb / Ft * p 
    Cc = Cto * Fc / Ft * p 
    r1a = 0 - (k1a * Ca * Cb ** 2) 
    r1b = 2 * r1a 
    rb = r1b 
    r2c = 0 - (k2c * Ca ** 2 * Cc ** 3) 
    r2a = 2 / 3 * r2c 
    r2d = -1 / 3 * r2c 
    r1c = 0 - r1a 
    rd = r2d 
    ra = r1a + r2a 
    rc = r1c + r2c 
    Fto = 20 
    # Differential equations
    dFadW = ra 
    dFbdW = rb 
    dFcdW = rc 
    dFddW = rd 
    dpdW = 0 - (alpha / 2 / p * Ft / Fto) 
    return np.array([dFadW, dFbdW, dFcdW, dFddW, dpdW]) 


Wspan = np.linspace(0, 1000, 10000) # Range for the independent variable
y0 = np.array([10, 10, 0, 0, 1]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-5 Multiple Gas Phase Reactions in a PBR""", x = 0.2, y = 0.98, fontweight='bold')
fig.subplots_adjust(wspace=0.3,hspace=0.3)
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, Wspan, (k1a, k2c, Cto, alpha))
#sol=sol[1:]
#Wspan=Wspan[1:]
Fa = sol[:, 0] 
Fb = sol[:, 1] 
Fc = sol[:, 2] 
Fd = sol[:, 3] 
p = sol[:, 4] 
Ft = Fa + Fb + Fc + Fd 
Ca = Cto * Fa / Ft * p 
Cb = Cto * Fb / Ft * p 
Cc = Cto * Fc / Ft * p 
r1a = 0 - (k1a * Ca * Cb ** 2) 
r1b = 2 * r1a 
rb = r1b 
r2c = 0 - (k2c * Ca ** 2 * Cc ** 3) 
r2a = 2 / 3 * r2c 
r2d = -1 / 3 * r2c 
r1c = 0 - r1a 
rd = r2d 
ra = r1a + r2a 
rc = r1c + r2c 
Cd = Cto * Fd / Ft * p 
Fao = 10
Fbo = 10 
Fto = Fao+Fbo 
Scd = np.nan_to_num(Fc / Fd)
Xa = (Fao - Fa)/Fao
Xb = (Fbo - Fb)/Fbo
Yc = Fc / (Fao- Fa)
Yd = Fd / (Fao- Fa) 

p1, p2, p3, p4 = ax1.plot(Wspan, Fa, Wspan, Fb, Wspan, Fc,Wspan, Fd )
ax1.legend([r'$F_A$', r'$F_B$', r'$F_C$', r'$F_D$'], loc='upper right')
ax1.set_xlabel('W (kg)', fontsize='medium' )
ax1.set_ylabel(r'$F_i (mol/min)$', fontsize='medium')
ax1.set_ylim(0,10)
ax1.set_xlim(0,1000)
ax1.grid()

p5, p6, p7 = ax2.plot(Wspan, Xa, Wspan, Xb, Wspan, p)
ax2.legend(['X$_A$', 'X$_B$', 'p'], loc='lower right')
ax2.set_ylim(0,1)
ax2.set_xlim(0,1000)
ax2.grid()
ax2.set_xlabel('W (kg)', fontsize='medium')
ax2.set_ylabel('X,p', fontsize='medium')
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p8 = ax3.plot(Wspan, Scd)[0]
ax3.legend([r'$S_{C/D}$'], loc='upper right')
ax3.set_ylim(0,10000)
ax3.set_xlim(0,1000)
ax3.grid()
ax3.set_xlabel('W (kg)', fontsize='medium' )
ax3.set_ylabel('Selectivity', fontsize='medium')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p9, p10 = ax4.plot(Wspan, Yc, Wspan, Yd)
ax4.legend([r'$Y_C$', r'$Y_D$'], loc='upper right')
ax4.set_ylim(0,1)
ax4.set_xlim(0,1000)
ax4.grid()
ax4.set_xlabel('W (kg)', fontsize='medium' )
ax4.set_ylabel('Yield', fontsize='medium' )
#ax4.ticklabel_format(style='sci',scilimits=(-6,-3),axis='y')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax1.text(-1750, -14,'Differential Equations'
         '\n' r'$\dfrac{dF_A}{dW} = r_A^\prime$ '
        "\n"
        r'$\dfrac{dF_B}{dW} = r_B^\prime$ '
                "\n"
        r'$\dfrac{dF_C}{dW} = r_C^\prime$ '
                "\n"
        r'$\dfrac{dF_D}{dW} = r_D^\prime$ '
                "\n"
        r'$\dfrac{dp}{dW} = -\dfrac{\alpha F_T}{2.p.F_{To}}$ '
        '\n \n'
        'Explicit Equations'
        '\n'
        r'$F_{T0} = 20$'
                '\n'
        r'$F_{B0} = 10$'
                '\n'
        r'$F_{A0} = 10$'        
        '\n'

        r'$F_T = F_A + F_B + F_C + F_D$'
        '\n'

        r'$C_A = C_{T0}(F_A/F_T)p$'
                        '\n'
        r'$C_B = C_{T0}(F_B/F_T)p$'
                        '\n'
        r'$C_C = C_{T0}(F_C/F_T)p$'
        '\n'
        r'$C_D = C_{T0}(F_D/F_T)p$'
        '\n'
        r'$r_{1A}^\prime = -k_{1A}C_AC_B^2$'
                '\n'
        r'$r_{1B}^\prime = 2r_{1A}^\prime$'
                '\n'
        r'$r_B^\prime = r_{1B}^\prime$'
                '\n'
        r'$r_{2C}^\prime = -k_{2C}C_A^2C_C^3$'
                '\n'
        r'$r_{2A}^\prime = (2/3)r_{2C}^\prime$'
                '\n'
        r'$r_{2D}^\prime = -(1/3)r_{2C}^\prime$'
                '\n'
        r'$r_{1C}^\prime = -r_{1A}^\prime$'
                '\n'
        r'$r_D^\prime = r_{2D}^\prime$'
                '\n'
        r'$r_A^\prime = r_{1A}^\prime+ r_{2A}^\prime$'
                '\n'
        r'$r_C^\prime = r_{1C}^\prime + r_{2C}^\prime$'
                '\n'
        r'$X_A = (F_{A0} - F_A)/F_{A0}$'
        '\n'
        r'$X_B = (F_{B0} - F_B)/F_{B0}$'       
        '\n'
        r'$S_{C/D}=\dfrac{F_C}{F_D}$'
        '\n'
        r'$Y_{C}=\dfrac{F_C}{(F_{A0}-F_A)}$'
                '\n'
        r'$Y_{D}=\dfrac{F_D}{(F_{A0}-F_A)}$'

        , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


axcolor = 'black'
ax_alpha = plt.axes([0.22, 0.65, 0.1, 0.02], facecolor=axcolor)
ax_k1a = plt.axes([0.22, 0.6, 0.1, 0.02], facecolor=axcolor)
ax_k2c = plt.axes([0.22, 0.55, 0.1, 0.02], facecolor=axcolor)
ax_Cto = plt.axes([0.22, 0.5, 0.1, 0.02], facecolor=axcolor)

salpha = Slider(ax_alpha, r'$\alpha$ ($kg^{-1}$)', 0.0005, 0.002, valinit=0.0019,valfmt='%1.5f', valstep=0.000001)
sk1a= Slider(ax_k1a, r'k$_{1A} (\frac{dm^9}{mol^2.kgcat.min})$', 90, 500, valinit=100,valfmt='%1.0f', valstep=1)
sk2c = Slider(ax_k2c, r'k$_{2C} (\frac{dm^{15}}{mol^4.kgcat.min})$', 700, 2500, valinit=1500,valfmt='%1.0f', valstep=1)
sCto = Slider(ax_Cto, r'C$_{T0} (\frac{mol}{dm^3})$', 0.19, 1, valinit=0.2, valstep=0.001)


def update_plot2(val):
    alpha = salpha.val
    k1a =sk1a.val
    k2c =sk2c.val
    Cto = sCto.val
    sol = odeint(ODEfun, y0, Wspan, (k1a, k2c, Cto, alpha))
    Fa = sol[:, 0] 
    Fb = sol[:, 1] 
    Fc = sol[:, 2] 
    Fd = sol[:, 3] 
    p = sol[:, 4] 
    Fao = 10
    Fbo = 10 
    Scd = np.nan_to_num(Fc / Fd)
    Xa = (Fao - Fa)/Fao
    Xb = (Fbo - Fb)/Fbo
    Yc = Fc / (Fao- Fa)
    Yd = Fd / (Fao- Fa)
    p1.set_ydata(Fa)
    p2.set_ydata(Fb)
    p3.set_ydata(Fc)
    p4.set_ydata(Fd)
    p5.set_ydata(Xa)
    p6.set_ydata(Xb)
    p7.set_ydata(p)
    p8.set_ydata(Scd)
    p9.set_ydata(Yc)
    p10.set_ydata(Yd)    
    fig.canvas.draw_idle()


salpha.on_changed(update_plot2)
sk1a.on_changed(update_plot2)
sk2c.on_changed(update_plot2)
sCto.on_changed(update_plot2)
#

resetax = plt.axes([0.22, 0.7, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    salpha.reset()
    sk1a.reset()
    sk2c.reset()
    sCto.reset()
button.on_clicked(reset)