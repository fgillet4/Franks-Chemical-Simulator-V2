#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
k = 0.5
Ca0 = 5
n = 2
U = 4
L = 4
Da = 10 
def ODEfun(Yfuncvec, t, k, Ca0, n, U, L, Da):
    X = Yfuncvec[0]
    theta = t*U/L
    Pe = U*L/Da
    E = np.exp(-(1-theta)**2/(4*theta/Pe))/(2*(np.pi*theta/Pe)**0.5)
    dxdt = k*Ca0**n*(1-X)**n/Ca0
    dXsegdt = X*E
    
    return np.array([dxdt, dXsegdt])

tspan = np.linspace(0.01, 14, 1000)
y0 = np.array([0, 0])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Example : Equation 18-34 coupled with Segregation Model""", fontweight='bold', x = 0.22, y=0.98)
plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (k, Ca0, n, U, L, Da))
X = sol[:, 0]
Xseg = sol[:, 1]
p1, p2 = plt.plot(tspan, X, tspan, Xseg)
plt.legend([r'$X$', r'$X_{seg}$'], loc='upper right')
ax.set_xlabel('time (min)', fontsize='medium', fontweight='bold')
ax.set_ylabel('Conversion, X', fontsize='medium', fontweight='bold')
plt.ylim(0,1)
plt.xlim(0.01,14)
plt.grid()

plt.text(-16.3, 0.3,
            'Equations'      
         '\n\n'
        r'$\dfrac{dX}{dt} = k*(C_{A0})^n*(1-X)^n/C_{A0}$'
                 '\n\n'
         r'$\dfrac{dX_{Seg}}{dt} = X(t)*E(t)$' 
         '\n\n'
         r'$\theta = \dfrac{tU}{L}$'
                  '\n\n'
         r'$Pe_r = \dfrac{U*L}{D_a}$'
                  '\n\n'      
         r'$E(L,t) = \dfrac{1}{2\sqrt{\pi \theta/Pe_r}}*exp\left[\dfrac{-(1-\theta)^2}{4*\theta/Pe_r}\right]$'
                  '\n\n'                  

         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k = plt.axes([0.25, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_Ca0 = plt.axes([0.25, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.6, 0.15, 0.02], facecolor=axcolor)
ax_U = plt.axes([0.25, 0.55, 0.15, 0.02], facecolor=axcolor)
ax_L = plt.axes([0.25, 0.5, 0.15, 0.02], facecolor=axcolor)
ax_Da = plt.axes([0.25, 0.45, 0.15, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k$', 0.01, 3, valinit=0.5, valfmt="%1.2f")
sCa0= Slider(ax_Ca0, r'$C_{A0}$', 0.1, 20, valinit=5, valfmt="%1.2f")
sn = Slider(ax_n, r'$n$', 0, 10, valinit=2, valfmt="%1.1f")
sU = Slider(ax_U, r'$U (\frac{m}{s})$', 1,15, valinit=4)
sL = Slider(ax_L, r'$L (m)$', 1,5, valinit= 4, valfmt="%1.2f")
sDa = Slider(ax_Da, r'$D_a (\frac{m^2}{s})$', 0.2, 30, valinit=10, valfmt="%1.2f")


def update_plot2(val):
    k = sk.val
    Ca0 =sCa0.val
    n = sn.val
    U =sU.val
    L = sL.val
    Da = sDa.val
    sol = odeint(ODEfun, y0, tspan, (k, Ca0, n, U, L, Da))
    X = sol[:, 0]
    Xseg = sol[:, 1]
    p1.set_ydata(X)
    p2.set_ydata(Xseg)
    fig.canvas.draw_idle()


sk.on_changed(update_plot2)
sCa0.on_changed(update_plot2)
sn.on_changed(update_plot2)
sU.on_changed(update_plot2)
sL.on_changed(update_plot2)
sDa.on_changed(update_plot2)
#

resetax = plt.axes([0.28, 0.75, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(eDant):
    sk.reset()
    sCa0.reset()
    sn.reset()
    sU.reset()
    sL.reset()
    sDa.reset()
button.on_clicked(reset)

