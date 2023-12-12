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
Us=10
kd=0.72
Fao=30
Cao=0.075
k=600
def ODEfun(Y, W, Us, kd, Fao, Cao, k): 
    a = Y[0]
    X = Y[1]
    #Explicit Equation Inline
    Ca=Cao*(1-X)
    raprime=-k*Ca**2
    # Differential equations
    dadW= -kd*a/Us 
    dXdW=a*(-raprime)/Fao
    return np.array([dadW, dXdW]) 

Wspan = np.linspace(0, 22, 1000)
y0 = np.array([1, 0])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 10-5 Catalytic Cracking in a Moving-Bed Reactor""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)

p1, p2 = plt.plot(Wspan, odeint(ODEfun, y0, Wspan, (Us, kd, Fao, Cao, k)))
plt.legend(['a', 'X'], loc='best')
ax.set_xlabel('Weight (kg)', fontsize='medium')
ax.set_ylabel('a, X', fontsize='medium')
plt.ylim(0,1)
plt.xlim(0,22)
plt.grid()

ax.text(-16, 0.1,'Differential Equations' '\n\n'
        r'$\dfrac{da}{dW} = -\dfrac{k_d.a}{U_s}$ '
        "\n\n"
        r'$\dfrac{dX}{dW} = \dfrac{a.(-r_A^\prime)}{F_{A0}}$ '
        '\n \n'
        'Explicit Equations'
        '\n\n'
        r'$C_A = C_{A0}(1-X)$'
                '\n\n'
        r'$-r_A^\prime = kC_A^2$'
        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')

#%%
# Slider Code
axcolor = 'black'
ax_Us = plt.axes([0.1, 0.75, 0.3, 0.02], facecolor=axcolor)
ax_kd = plt.axes([0.1, 0.7, 0.3, 0.02], facecolor=axcolor)
ax_Fao = plt.axes([0.1, 0.65, 0.3, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.1, 0.6, 0.3, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.1, 0.55, 0.3, 0.02], facecolor=axcolor)

sUs = Slider(ax_Us, '$U_s$ (kg/min)', 1, 20, valinit=10,valfmt='%1.1f')
skd = Slider(ax_kd, '$k_d$ ($min^{-1}$)', 0.1, 1.5, valinit=0.72)
sFao = Slider(ax_Fao, r'F$_{A0}$ ($\frac{mol}{min}$)',5, 60, valinit=30,valfmt='%1.1f')
sCao = Slider(ax_Cao, r'C$_{A0}$ ($\frac{mol}{dm^3}$)', 0, 1, valinit=0.075,valfmt='%1.3f')
sk = Slider(ax_k, r'$k$ ($\frac{dm^{6}}{kg cat.mol.min}$)', 100, 1000, valinit=600,valfmt='%1.0f')

def update_plot1(val):
    Us = sUs.val
    kd =skd.val
    Fao = sFao.val
    Cao = sCao.val
    k = sk.val
    sol = odeint(ODEfun, y0, Wspan, (Us, kd, Fao, Cao, k))
    p1.set_ydata(sol[:, 0])
    p2.set_ydata(sol[:, 1])
    fig.canvas.draw_idle()

sUs.on_changed(update_plot1)
skd.on_changed(update_plot1)
sFao.on_changed(update_plot1)
sCao.on_changed(update_plot1)
sk.on_changed(update_plot1)

resetax = plt.axes([0.2, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sUs.reset()
    skd.reset()
    sFao.reset()
    sCao.reset()
    sk.reset()
button.on_clicked(reset)
