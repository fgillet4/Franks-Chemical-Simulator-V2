#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
CB0 = 20.2
V = .01
dHrx =  -44432
A =  3.7e7
E =  15400
R =  1.987
def ODEfun(Yfuncvec, t, CB0, V,dHrx, A, E): 
    CA= Yfuncvec[0]
    T= Yfuncvec[1]
    Sumcpi=28.0
    Tedot = np.where(T > 85.7+273, 0, 2)
    ra = -A*np.exp(-E/R/T)*CA*CB0
    Tsdot =  (-dHrx)*(-ra*V)/Sumcpi
    # Differential equations
    dCAdt = ra
    dTdt =  Tedot+Tsdot 
    return np.array([dCAdt, dTdt])

tspan = np.linspace(0, 25, 1000) #Range for the time of the reaction 
y0 = np.array([6.7,298.6]) #Initial values for the dependent variables



#%%
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.suptitle("""LEP-RE-13.1: Use of ARSST""", fontweight='bold', x = 0.14, y= 0.98)

plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (CB0,V,dHrx, A, E))
CA= sol[:, 0]
T= sol[:, 1]
Sumcpi=28.0
Tedot = np.where(T > 85.7+273, 0, 2)
ra = -A*np.exp(-E/R/T)*CA*CB0
Tsdot =  (-dHrx)*(-ra*V)/Sumcpi

p1 = ax1.plot(tspan, T)[0]
ax1.legend(['Temperature'], loc='best')
ax1.set_xlabel('t (min)', fontsize='medium')
ax1.set_ylabel('T (K)', fontsize='medium')
ax1.set_ylim(280, 480)
ax1.set_xlim(0,25)
ax1.grid()

p2 = ax2.plot(tspan, Tsdot)[0]
ax2.legend(['Heating - Rate'], loc='best')
ax2.set_ylabel(r'Heating Rate$\left(\dfrac{k}{min}\right)$', fontsize='medium')
ax2.set_xlabel('t (min)', fontsize='medium')
ax2.set_ylim(0, 100)
ax2.set_xlim(0, 25)
ax2.grid()

ax2.text(-22.5, 15.5,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} = r_A$'
                  '\n'
         r'$\dfrac{dT}{dt} = \dot T_E + \dot T_S$'
                  '\n\n'                  
         'Explicit Equations'
                  '\n\n'
         r'$R = 1.987$'
                  '\n'
         r'$\dot T_E = If\thinspace(T>85.7+273)\thinspace then(0)\thinspace else \thinspace (2)$'
         '\n'  
         r'$r_A = -Aexp \left(\dfrac{-E_a}{R.T} \right)\thinspace C_A\thinspace C_{B0}$'
         '\n'

         r'$\sum{N_iC_{P_i}}=28.0$'
         '\n'
         r'$\dot T_S = \dfrac{(\Delta H_{RX})(-r_A.V)}{\sum{N_iC_{P_i}}}$'

         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=20), fontweight='bold')
#%%
axcolor = 'black'
ax_CBo = plt.axes([0.15, 0.84, 0.2, 0.02], facecolor=axcolor)
ax_V = plt.axes([0.15, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_dHrx = plt.axes([0.15, 0.76, 0.2, 0.02], facecolor=axcolor)
ax_A = plt.axes([0.15, 0.72, 0.2, 0.02], facecolor=axcolor)
ax_E = plt.axes([0.15, 0.68, 0.2, 0.02], facecolor=axcolor)


sCBo = Slider(ax_CBo, r'$C_{B0} (\frac{mol}{dm^3})$', 10, 30, valinit=20.2, valfmt='%1.2f')
sV = Slider(ax_V, r'$V (dm^3)$', 0.0005, 0.05, valinit=0.01,valfmt='%1.3f')
sdHrx = Slider(ax_dHrx, r'$\Delta H_{RX} (\frac{J}{mol})$', -60000, -20000 , valinit=-44432, valfmt='%1.0f')
sA = Slider(ax_A, r'$A (\frac{dm^3}{mol.min})$', 1.734e7, 5.734e7, valinit=3.7e7,valfmt='%1.2E')
sE = Slider(ax_E, r'$E_a (\frac{cal}{mol})$', 10000, 20000, valinit=15400,valfmt='%1.0f')


def update_plot2(val):
    CB0 = sCBo.val
    V = sV.val    
    dHrx = sdHrx.val
    A = sA.val
    E = sE.val
    sol = odeint(ODEfun, y0, tspan, (CB0, V,dHrx, A, E))
    CA= sol[:, 0]
    T= sol[:, 1]
    Sumcpi=28.0
    ra = -A*np.exp(-E/R/T)*CA*CB0
    Tsdot =  (-dHrx)*(-ra*V)/Sumcpi
    p1.set_ydata(T)   
    p2.set_ydata(Tsdot)
    fig.canvas.draw_idle()


sCBo.on_changed(update_plot2)
sV.on_changed(update_plot2)
sdHrx.on_changed(update_plot2)
sA.on_changed(update_plot2)
sE.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCBo.reset()
    sV.reset()
    sdHrx.reset()
    sA.reset()
    sE.reset()
button.on_clicked(reset)    
