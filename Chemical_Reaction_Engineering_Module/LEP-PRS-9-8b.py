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
ke =  2.0  
kr =  3.0  
kcp = 1.0 
kpc = 1.0 
ka =  4.0  
def ODEfun(Yfuncvec, t, kpc, kcp, kr, ke, ka): 
    Cc= Yfuncvec[0]
    Cp= Yfuncvec[1]
    Co= Yfuncvec[2]
    # Differential equations
    dCcdt =  -(ke+kr+kcp)*Cc + kpc*Cp + ka*Co # Concentration of drug in Central Compartment
    dCpdt =  -kpc*Cp + kcp*Cc  # Concentration of drug in Peripheral Compartment
    dCodt =  -ka * Co  # Concentration of drug in Oral Compartment
    return np.array([dCcdt, dCpdt, dCodt])

tspan = np.linspace(0, 7, 1000)
y0 = np.array([0, 0, 40])

#%%
fig, ax = plt.subplots()
fig.suptitle("""PRS 9 - 8 : Pharmacokinetics in Drug Delivery : Three Compartment model""", x = 0.3, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, tspan, (kpc, kcp, kr, ke,ka))
Cc = sol[:, 0]
Cp = sol[:, 1]
Co = sol[:, 2]
p1, p2, p3 = plt.plot(tspan, Cc, tspan, Cp, tspan, Co)
plt.legend([r"C$_c$", r"C$_p$", r"C$_o$"], loc='best')
ax.set_xlabel('time (hr)', fontsize='medium')
ax.set_ylabel('Concentration (mg/ml)', fontsize='medium')
plt.ylim(0, 40)
plt.xlim(0,7)
plt.grid()

ax.text(-4, 8,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = -(k_R + k_e + k_{CP})C_C + k_{PC}C_P + k_AC_0$'
                  '\n\n'
         r'$\dfrac{dC_p}{dt} = k_{CP}C_C - k_{PC}C_P$'
         '\n\n'
         r'$\dfrac{dC_0}{dt} = -k_{A}C_0$'


         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_kpc = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_kcp = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_kr = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_ke = plt.axes([0.1, 0.6, 0.2, 0.02], facecolor=axcolor)
ax_ka = plt.axes([0.1, 0.55, 0.2, 0.02], facecolor=axcolor)

skpc = Slider(ax_kpc, r'$k_{PC} (hr^{-1})$', 0.02,5, valinit=1)
skcp = Slider(ax_kcp, r'$k_{CP} (hr^{-1})$', 0.02,5, valinit=1)
skr = Slider(ax_kr, r'$k_R (hr^{-1})$', 0.05, 8, valinit= 3)
ske = Slider(ax_ke, r'$k_e (hr^{-1})$', 0.05, 7, valinit=2)
ska = Slider(ax_ka, r'$k_A (hr^{-1})$', 0.2, 9, valinit=4)


def update_plot2(val):
    kpc = skpc.val
    kcp =skcp.val
    kr = skr.val
    ke = ske.val
    ka = ska.val
    
    sol = odeint(ODEfun, y0, tspan, (kpc, kcp, kr, ke ,ka))
    Cc = sol[:, 0]
    Cp = sol[:, 1]
    Co = sol[:, 2]
    p1.set_ydata(Cc)
    p2.set_ydata(Cp)
    p3.set_ydata(Co)
    fig.canvas.draw_idle()


skpc.on_changed(update_plot2)
skcp.on_changed(update_plot2)
skr.on_changed(update_plot2)
ske.on_changed(update_plot2)
ska.on_changed(update_plot2)

#

resetax = plt.axes([0.15, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    skpc.reset()
    skcp.reset()
    skr.reset()
    ske.reset()
    ska.reset()
    
button.on_clicked(reset)
    
