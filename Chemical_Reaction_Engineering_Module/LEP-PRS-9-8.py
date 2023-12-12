#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
kpc = 3.0651 
kcp = 3.936  
kr =  1.0  
ke =  1.0 
def ODEfun(Yfuncvec, t, kpc, kcp, kr, ke): 
    Cc= Yfuncvec[0]
    Cp= Yfuncvec[1]
     
    k0 =  kr+ke+kcp  
    # Differential equations
    dCcdt = -k0*Cc+kpc*Cp
    dCpdt = kcp*Cc-kpc*Cp
    return np.array([dCcdt, dCpdt])

tspan = np.linspace(0, 5, 1000)
y0 = np.array([40, 0])

#%%
fig, ax = plt.subplots()
fig.suptitle("""PRS-9-8 : Pharmacokinetics in Drug Delivery: Two compartment model""", x = 0.3, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, tspan, (kpc, kcp, kr, ke))
Cc = sol[:, 0]
Cp = sol[:, 1]
p1, p2 = plt.plot(tspan, Cc, tspan, Cp)
plt.legend([r"C$_c$", r"C$_p$"], loc='best')
ax.set_xlabel('time (hr)', fontsize='medium')
ax.set_ylabel('Concentration (mg/ml)', fontsize='medium')
plt.ylim(0, 40)
plt.xlim(0,5)
plt.grid()

ax.text(-2.6, 10,'Differential Equations'
         '\n'
         r'$\dfrac{dC_C}{dt} = -k_0C_C+k_{PC}C_P$'
                  '\n'
         r'$\dfrac{dC_p}{dt} = k_{CP}C_C - k_{PC}C_P$'
         '\n'
         '\n'
         'Explicit Equations'
         '\n'
         r'$k_0 = k_R + k_e + k_{CP}$'

         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_kpc = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_kcp = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_kr = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_ke = plt.axes([0.1, 0.6, 0.2, 0.02], facecolor=axcolor)

skpc = Slider(ax_kpc, r'$k_{PC} (hr^{-1})$', 1,10, valinit=3.936 )
skcp = Slider(ax_kcp, r'$k_{CP} (hr^{-1})$', 1,10, valinit=0.165)
skr = Slider(ax_kr, r'$k_R (hr^{-1})$', 0.02, 5, valinit= 1)
ske = Slider(ax_ke, r'$k_e (hr^{-1})$', 0.02, 3, valinit=1)


def update_plot2(val):
    kpc = skpc.val
    kcp =skcp.val
    kr = skr.val
    ke = ske.val
    sol = odeint(ODEfun, y0, tspan, (kpc, kcp, kr, ke))
    Cc = sol[:, 0]
    Cp = sol[:, 1]
    p1.set_ydata(Cc)
    p2.set_ydata(Cp)
    fig.canvas.draw_idle()


skpc.on_changed(update_plot2)
skcp.on_changed(update_plot2)
skr.on_changed(update_plot2)
ske.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    skpc.reset()
    skcp.reset()
    skr.reset()
    ske.reset()
button.on_clicked(reset)
    
