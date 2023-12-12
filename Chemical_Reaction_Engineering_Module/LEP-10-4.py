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
A=3.7256*10**12
Ad=4.3851*10**53
E = 20000
Ed = 75000
T = 300
R = 1.987
def ODEfun(Y, t, A, Ad, E, Ed, T): 
    X = Y[0]
    Xd=Y[1]
    # Explicit equations Inline
    k = A*np.exp(-E/(R*T))
    kd = Ad*np.exp(-Ed/(R*T))
    # Differential equations
    dXdt= k*(1-X) 
    dXddt=k*(1-Xd)/(1+kd*t)
    return np.array([dXdt, dXddt]) 



tspan = np.linspace(0, 500, 10000)
y0 = np.array([0, 0])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 10-4 Calculating Conversion with Catalyst Decay in Batch Reactors""", x = 0.3, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)

p1, p2 = plt.plot(tspan, odeint(ODEfun, y0, tspan, (A, Ad, E, Ed, T)))

plt.legend([r'X', r'X$_d$'], loc='best')
ax.set_xlabel(r'time (s)', fontsize='medium')
ax.set_ylabel('Conversion', fontsize='medium')
plt.ylim(0,1)
plt.xlim(0,500)
plt.grid()

ax.text(-450, -0.02,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))

ax.text(-370, 0.15,'Differential Equations' '\n' r'$\dfrac{dX}{dt} = k(1 - X)$ '
        "\n"
        r'$\dfrac{dX_d}{dt} = k\dfrac{(1-X_d)}{(1+k_dt)}$ '

        '\n \n'
        'Explicit Equations'
        '\n\n'
        r'$A = 3.7256*10^{12}\thinspace s^{-1}$'
                '\n\n'
        r'$A_d = 4.3851*10^{53}\thinspace s^{-1}$'
                '\n\n'
        r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'       
        '\n\n'
        r'$k_d = A_d*exp\left(\dfrac{-E_d}{1.987*T}\right)$' 

        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')

#%%
# Slider Code
axcolor = 'black'

ax_E = plt.axes([0.1, 0.75, 0.3, 0.02], facecolor=axcolor)
ax_Ed = plt.axes([0.1, 0.70, 0.3, 0.02], facecolor=axcolor)
ax_T = plt.axes([0.1, 0.65, 0.3, 0.02], facecolor=axcolor)


sE = Slider(ax_E, r'$E (\frac{cal}{mol})$', 15000, 30000, valinit=20000, valfmt = "%1.0f")
sEd = Slider(ax_Ed, r'$E_d (\frac{cal}{mol})$', 65000, 85000, valinit=75000, valfmt = "%1.0f")
sT = Slider(ax_T, 'T (K)', 295, 400, valinit=300, valfmt = "%1.1f")

def update_plot1(val):
    E = sE.val
    Ed = sEd.val
    T = sT.val
    sol = odeint(ODEfun, y0, tspan, (A, Ad, E, Ed, T))

    p1.set_ydata(sol[:, 0])
    p2.set_ydata(sol[:, 1])

    fig.canvas.draw_idle()

sE.on_changed(update_plot1)
sEd.on_changed(update_plot1)
sT.on_changed(update_plot1)

resetax = plt.axes([0.2, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sE.reset()
    sEd.reset()
    sT.reset()
button.on_clicked(reset)
