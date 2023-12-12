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
Ycs = .4
alpha = .0001
beta = .05
Ks = .1 
mumax = .9

def ODEfun(Yfuncvec, t, Ycs, alpha, beta, Ks, mumax): 
    Cc= Yfuncvec[0]
    Cs= Yfuncvec[1]
    e= Yfuncvec[2]
    # Explicit equations Inline
    emax = alpha/(mumax+beta)
    ER = e/emax
    mu = mumax * ER*Cs/(Ks + Cs)
    # Differential equations
    dCcdt = mu * Cc
    dCsdt = -1/Ycs * mu * Cc
    dedt = alpha * Cs/(Ks + Cs) - beta*e - mu*e
    return np.array([dCcdt, dCsdt, dedt])
    

tspan = np.linspace(0, 4, 100) # Range for the independent variable
y0 = np.array([0.1, 4, 8.3e-5]) # Initial values for the dependent variables

#%%
fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle("""LEP PRS-9-6 Single Substrate""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, tspan, (Ycs, alpha, beta, Ks, mumax))
Cc= sol[:,0]
Cs= sol[:,1]
e= sol[:,2]

p1, p2 = ax1.plot(tspan, Cc, tspan, Cs)
ax1.legend(["Cell Concentration, $C_C(g/L)$", "Substrate Concentration, $C_S(g/L)$"], loc='best')
ax1.set_xlabel('time (hr)', fontsize='medium')
ax1.set_ylabel('Concentration (M)', fontsize='medium')
ax1.set_ylim(0,5)
ax1.set_xlim(0,4)
ax1.grid()

p3 = ax2.plot(tspan, e)[0]
ax2.legend(["Enzyme content, $e(g_{enzyme}/g_{cell mass})$"], loc='best')
ax2.set_xlabel('time (hr)', fontsize='medium')
ax2.set_ylabel('Concentration (M)', fontsize='medium')
ax2.set_ylim(0,0.0012)
ax2.set_xlim(0,4)
ax2.grid()
ax1.text(-2, -6.1,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = \mu C_C$'
                  '\n \n'
         r'$\dfrac{dC_S}{dt} = \dfrac{-\mu C_C}{Y_{cs}}$'
                  '\n \n'
         r'$\dfrac{de}{dt} = \dfrac{\alpha C_s}{K_S+C_S} - e(\beta + \mu)$'
                  '\n \n'                  
         'Explicit Equations'
                  '\n\n'
         r'$e_{max} = \dfrac{\alpha}{\mu_{max} + \beta}$'
         '\n\n'         
         r'$ER = \dfrac{e}{e_{max}}$'
         '\n\n'
         r'$\mu = \dfrac{ER \mu_{max}C_s}{K_S+C_S}$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_Ycs = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_alpha = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_beta = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Ks = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_mumax = plt.axes([0.1, 0.6, 0.2, 0.02], facecolor=axcolor)

sYcs = Slider(ax_Ycs, r'$Y_{cs}$', 0.05, 0.8, valinit=0.4)
salpha = Slider(ax_alpha, r'$\alpha (\frac{g_{enzyme}}{g_{cell mass}.s})$', 5e-6, 0.001, valinit=0.0001, valfmt = '%1.4f')
sbeta = Slider(ax_beta, r'$\beta (hr^{-1})$', 0.01, 0.2, valinit=0.05)
sKs = Slider(ax_Ks, r'$K_s (\frac{g}{L})$',0.02, 0.3, valinit= 0.1)
smumax = Slider(ax_mumax, r'$\mu_{max} (hr^{-1})$', 0.2, 1, valinit=0.9)


def update_plot2(val):
    Ycs = sYcs.val
    alpha = salpha.val
    beta =sbeta.val
    Ks = sKs.val
    mumax = smumax.val
    sol = odeint(ODEfun, y0, tspan, (Ycs, alpha, beta, Ks, mumax))
    Cc= sol[:,0]
    Cs= sol[:,1]
    e= sol[:,2]
    p1.set_ydata(Cc)
    p2.set_ydata(Cs)
    p3.set_ydata(e)
    fig.canvas.draw_idle()


sYcs.on_changed(update_plot2)
salpha.on_changed(update_plot2)
sbeta.on_changed(update_plot2)
sKs.on_changed(update_plot2)
smumax.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sYcs.reset()
    salpha.reset()
    sbeta.reset()
    sKs.reset()
    smumax.reset()
button.on_clicked(reset)
    
