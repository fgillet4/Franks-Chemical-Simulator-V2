#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
m = 104.4
Ac = 0.01414
mu = 0.0673
rho = 0.413
Dp = .0208
phi = 0.45
z = np.linspace(0.01, 100, 1000)
def func(m, Ac, mu, rho, Dp, phi):
    G = m/Ac
    vo = m/rho
    gc = 4.17e8
    Po = 10
    beta0 = G*(1-phi)*(150*(1-phi)*mu/Dp + 1.75*G)/(gc*rho*Dp*(phi**3))
    beta0 = beta0/144/14.7
    p = (1 - 2*beta0*z/Po)**0.5
    P = Po*p
    v = vo/p
    return np.array([P, v])

#%%
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("""Example 5- 4 Pressure drop in a Packed Bed""", fontweight='bold', x = 0.2, y= 0.98)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
plt.subplots_adjust(left  = 0.5)

sol = func(m, Ac, mu, rho, Dp, phi)
P = sol[0, :]
v = sol[1, :]


p1 = ax1.plot(z, P)[0]
ax1.legend(['Pressure'], loc='upper right')
ax1.set_xlabel('z (ft)', fontsize='medium')
ax1.set_ylabel('P (atm)', fontsize='medium')
ax1.set_ylim(0,10)
ax1.set_xlim(0,100)
ax1.grid()

p2 = ax2.plot(z, v)[0]
ax2.set_ylabel(r'$v$ ($\dfrac{ft^3}{h}$)', fontsize='medium')
ax2.set_xlabel('z (ft)', fontsize='medium')
ax2.set_ylim(0, 2000)
ax2.set_xlim(0, 100)
ax2.grid()

ax2.text(-77.5, 0.9,
                  
         'Ergun Equation'
                  '\n\n'
         r'$P_0 = 10$'
                 '\n\n'
          r'$\phi = 0.45$'
                 '\n\n'
         r'$p = \sqrt{1 - \dfrac{2\beta_oz}{P_0}}$'   
         '\n\n'
         r'$P = P_0.p$'
                  '\n\n'
         r'$\beta_0 = \dfrac{G(1-\phi)}{g_c \rho_0 D_p \phi^3}\left[\dfrac{150(1-\phi)\mu}{D_p} + 1.75G\right]$'
         '\n\n'
         r'$G = \dfrac{\dot m}{A_c}$'
         '\n\n'
         r'$v_0 = \dfrac{\dot m}{\rho_0}$'
         '\n\n'
         r'$v = \dfrac{v_0}{p}$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_m = plt.axes([0.15, 0.78, 0.2, 0.02], facecolor=axcolor)
ax_Ac = plt.axes([0.15, 0.74, 0.2, 0.02], facecolor=axcolor)
ax_mu = plt.axes([0.15, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Dp = plt.axes([0.15, 0.66, 0.2, 0.02], facecolor=axcolor)

sm = Slider(ax_m, r'$\dot m (\frac{lb_m}{h})$', 0, 1000, valinit=104.4,valfmt='%1.1f')
sAc = Slider(ax_Ac, r'$A_c (ft^2)$', 0.0001, 1, valinit=0.01414,valfmt='%1.5f')
smu= Slider(ax_mu, r'$\mu (\frac{lb_m}{ft.h})$', 0.0001, 1, valinit=0.0673,valfmt='%1.4f')
sDp = Slider(ax_Dp, r'$D_p (ft)$', 0.0001, 5, valinit=.0208,valfmt='%1.4f')

def update_plot2(val):
    m = sm.val
    Ac = sAc.val    
    mu =smu.val
    Dp = sDp.val
    sol = func(m, Ac, mu, rho, Dp, phi)
    P = sol[0, :]
    v = sol[1, :]
    p1.set_ydata(P)
    p2.set_ydata(v)
    fig.canvas.draw_idle()


sm.on_changed(update_plot2)
sAc.on_changed(update_plot2)
smu.on_changed(update_plot2)
sDp.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sm.reset()
    sAc.reset()
    smu.reset()
    sDp.reset()

button.on_clicked(reset)    
