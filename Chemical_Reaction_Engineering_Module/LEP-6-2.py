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
Kc = 0.05 
k = 0.7 
Cto = 0.2 
kc = 0.2 

def ODEfun(Yfuncvec, V, Kc, k, Cto, kc): 
    Fa = Yfuncvec[0]
    Fb = Yfuncvec[1] 
    Fc = Yfuncvec[2]

    # Explicit equations Inline
    Ft = Fa + Fb + Fc 
    ra = 0 - (k * Cto * (Fa / Ft - (Cto / Kc * Fb / Ft * Fc / Ft))) 
    
    # Differential equations
    dFadV = ra 
    dFbdV = 0 - ra - (kc * Cto * Fb / Ft) 
    dFcdV = 0 - ra 
    return np.array([dFadV, dFbdV, dFcdV]) 

Vspan = np.linspace(0, 500, 1000)
y0 = np.array([10, 0, 0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 6-2 Membrane Reactor""", fontweight='bold', x = 0.15, y=0.98)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, Vspan, (Kc, k, Cto, kc))
Fa = sol[:, 0]
Fb = sol[:, 1]
Fc = sol[:, 2]
Ft = Fa + Fb + Fc
Rb = kc*Cto*(Fb/Ft)
X = (10 - Fa)/10


p1,p2,p3= ax2.plot(Vspan, odeint(ODEfun, y0, Vspan, (Kc, k, Cto, kc)))
ax2.legend([r'$F_A$', r'$F_B$',r'$F_C$'], loc='upper right')
ax2.set_xlabel(r'V( $dm^{3}$)', fontsize='medium', )
ax2.set_ylabel(r'Flow Rates(mol/min)', fontsize='medium', )
ax2.grid()
ax2.set_xlim(0, 500)


p4 = ax3.plot(Vspan, X)[0]
ax3.legend(['X'], loc='upper right')
ax3.set_xlabel(r'V( $dm^{3}$)', fontsize='medium', )
ax3.set_ylabel('Conversion', fontsize='medium', )
ax3.grid()
ax3.set_xlim(0, 500)
ax3.set_ylim(0, 1.1)


p5 = ax4.plot(Vspan, Rb)[0]
ax4.legend([r'$R_b$'], loc='upper right')
ax4.set_xlabel(r'V( $dm^{3}$)', fontsize='medium', )
ax4.set_ylabel(r'$R_b ($mol/$dm^{3}$.min$)$', fontsize='medium' )
ax4.grid()
ax4.set_xlim(0, 500)
ax4.set_ylim(0, 0.1)
ax1.axis('off')
ax1.text(-0.9, -1.2,'Differential Equations'
         '\n\n'
         r'$\dfrac{dF_A}{dV} = r_A$'
         '\n\n'
         r'$\dfrac{dF_B}{dV} = r_B - R_B$'
         '\n\n'
         r'$\dfrac{dF_C}{dV} = r_C$'
      
                  '\n \n'
                  
         'Explicit Equations'
                  '\n\n'
         r'$F_{A0} = 10$'
         '\n\n'         
         r'$F_T = F_A + F_B + F_C$'
         '\n\n'
         r'$r_B=-r_A$'
         '\n'
         r'$r_C=-r_A$'
         '\n'
         r'$-r_A = kC_{T0}\left[\dfrac{F_A}{F_T} - \dfrac{C_{T0} F_B F_C}{K_C F_T^2}\right]$'
         '\n\n'
         r'$Rate = -r_A$'
                  '\n\n'
         r'$R_B = \dfrac{k_CC_{T0}F_B}{F_T}$'
                  '\n\n'
         r'$X = \dfrac{F_{A0} - F_A}{F_{A0}}$'

         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_Kc = plt.axes([0.32, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cto = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_kc = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)

sKc= Slider(ax_Kc, r'$K_C (\frac{mol}{dm^3})$', 0.001, 1, valinit=0.05)
sk = Slider(ax_k, r'$k (min^{-1})$', 0.1, 4, valinit=0.7)
sCto = Slider(ax_Cto, r'$C_{T0} (\frac{mol}{dm^3})$', 0, 2, valinit=0.2)
skc = Slider(ax_kc, r'$k_C (min^{-1})$', 0.01, 2, valinit=0.2)


def update_plot(val):
    Kc = sKc.val
    k = sk.val
    Cto = sCto.val
    kc = skc.val
	
    sol = odeint(ODEfun, y0, Vspan, (Kc, k, Cto, kc))
    Fa = sol[:, 0]
    Fb = sol[:, 1]
    Fc = sol[:, 2]
    Ft = Fa + Fb + Fc
    Rb = kc*Cto*(Fb/Ft)
    X = (10 - Fa)/10
    p1.set_ydata(Fa)
    p2.set_ydata(Fb)
    p3.set_ydata(Fc)
    p4.set_ydata(X)
    p5.set_ydata(Rb)    
    fig.canvas.draw_idle()

sKc.on_changed(update_plot)
sk.on_changed(update_plot)
sCto.on_changed(update_plot)
skc.on_changed(update_plot)

resetax = plt.axes([0.38, 0.8, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sKc.reset()
    sk.reset()   
    sCto.reset()    
    skc.reset()    
	
button.on_clicked(reset)