#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
n = 2
k = 0.00493
Cao = 0.75
tau = 1000
def ODEfun(Yfuncvec, t, k, Cao, n, tau): 
    X= Yfuncvec[0]
    Xbar = Yfuncvec[1]
    # Explicit equations
    t1 = tau/2
    E2 = tau**2/2/(t**3+0.00001)
    E = np.where(t<t1, 0, E2)
#    XPFR=tau*k/(1+tau*k)
    # Differential equations
    dxdt = (k*(Cao**n)*((1-X)**n))/(Cao)
    dXbardt = X*E
    return np.array([dxdt, dXbardt])

tspan = np.linspace(0, 20000, 50000)
y0 = np.array([0, 0])

#%%
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("""Example 17-3: Mean Conversion in a Laminar Flow Reactor""", fontweight='bold', x = 0.25, y= 0.98)
plt.subplots_adjust(left  = 0.5)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, tspan, (k, Cao, n, tau))
X = sol[:, 0]
Xbar = sol[:, 1]
t1 = tau/2
E2 = tau**2/2/(tspan**3+0.00001)
E = np.where(tspan<t1, 0, E2)
#XPFR=tau*k/(1+tau*k)

p1, p2 = ax1.plot(tspan, X, tspan, Xbar)
ax1.legend(['X', r'$\overline{X}$'], loc='lower right')
ax1.set_xlabel('t (sec)', fontsize='medium', fontweight='bold')
ax1.set_ylabel('Conversion', fontsize='medium', fontweight='bold')
ax1.set_ylim(0,1)
ax1.set_xlim(0,20000)
ax1.grid()

p3 = ax2.plot(tspan, E)[0]
ax2.legend(['E'], loc='upper right')
ax2.set_ylabel(r'E(t)', fontsize='medium', fontweight='bold')
ax2.set_xlabel('t (sec)', fontsize='medium', fontweight='bold')
ax2.set_ylim(0, 0.005)
ax2.set_xlim(0, 20000)
ax2.grid()

ax1.text(-16000, -1.2,
            'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dt} = \dfrac{kC_{A0}^n(1-X)^n}{C_{A0}}$'
                  '\n \n'
         r'$\dfrac{\overline{X}}{dt} = X.E$'
                  '\n \n'                  
         'Explicit Equations'
                  '\n\n'
            
         r'$t_1 = \dfrac{\tau}{2}$'
                  '\n\n'
         r'$E_2 = \dfrac{\tau^2}{2(t^3 + 0.00001)}$'
       
         '\n\n'
         r'$E = IF\hspace{0.5}(t<=4) \hspace{0.5}then \hspace{0.5}(0) \hspace{0.5}else \hspace{0.2}(E_2)$',
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k = plt.axes([0.15, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.15, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.15, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_tau = plt.axes([0.15, 0.6, 0.2, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k (\frac{mol^{1-n}}{dm^{3(1-n)}.s})$', 0.0001, 0.01, valinit=0.00493,valfmt='%1.5f')
sCao= Slider(ax_Cao, r'$C_{A0} (\frac{mol}{dm^3})$', 0.05,20, valinit= 0.75,valfmt='%1.2f')
sn = Slider(ax_n, r'$n $', 0.5, 10 , valinit=2, valfmt='%1.1f')
stau = Slider(ax_tau, r'$\tau (s)$', 100, 2000, valinit=1000,valfmt='%1.0f')


def update_plot2(val):
    k = sk.val    
    Cao =sCao.val
    n = sn.val
    tau = stau.val
    sol = odeint(ODEfun, y0, tspan, (k, Cao, n, tau))
    X = sol[:, 0]
    Xbar = sol[:, 1]
    t1 = tau/2
    E2 = tau**2/2/(tspan**3+0.00001)
#    XPFR=tau*k/(1+tau*k)
    E = np.where(tspan<t1, 0, E2)
    p1.set_ydata(X)
    p2.set_ydata(Xbar)
    p3.set_ydata(E)
    fig.canvas.draw_idle()


sk.on_changed(update_plot2)
sCao.on_changed(update_plot2)
sn.on_changed(update_plot2)
stau.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk.reset()
    sCao.reset()
    sn.reset()
    stau.reset()
button.on_clicked(reset)    

