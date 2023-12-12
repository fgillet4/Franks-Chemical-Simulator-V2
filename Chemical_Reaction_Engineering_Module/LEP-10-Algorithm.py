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
k=0.1
KA=1.5
kd=0.75
FA0=10
PA0=20
Us=2
alpha=0.0019
def ODEfun(Y, W, k,KA,kd,FA0,PA0,Us,alpha): 
    X = Y[0]
    a = Y[1]
    p = Y[2]
    #Explicit Equation Inline
    PA=PA0*(1-X)*p
    PB=PA0*X*p
    raprime=-a*k*PA/(1+KA*PA)
    # Differential equations
    dXdW=(-raprime)/FA0
    dadW= -kd*a**2*PB/Us 
    dpdW=-alpha/2*p
    return np.array([dXdW, dadW,dpdW]) 

Wspan = np.linspace(0, 500, 1000)
y0 = np.array([0, 1,1])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Algorithm for decaying catalyst in a moving bed reactor""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)

p1, p2,p3 = plt.plot(Wspan, odeint(ODEfun, y0, Wspan, (k,KA,kd,FA0,PA0,Us,alpha)))
plt.legend(['X','a' ,'p'], loc='best')
ax.set_xlabel('Weight (kg)', fontsize='medium')
ax.set_ylabel('X, a, p', fontsize='medium')
plt.ylim(0,1)
plt.xlim(0,500)
plt.grid()

ax.text(-450, -0.05,'Differential Equations' '\n\n'
        r'$\dfrac{dX}{dW} = \dfrac{(-r_A^\prime)}{F_{A0}}$ '
        '\n \n'
         r'$\dfrac{da}{dW} = -\dfrac{k_d.a^2* P_B}{U_s}$ '
        "\n\n"
        r'$\dfrac{dp}{dW} = -\dfrac{\alpha}{2*p}$'
        '\n\n'
        'Explicit Equations'
        '\n\n'
        r'$P_A = P_{A0}(1-X)*p$'
                '\n\n'
        r'$P_B = P_{A0}(X)*p$'
                '\n\n'
        r'$-r_A^\prime =-\dfrac{a*k*P_A}{1+K_A*P_A}$ '
        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')

#%%
# Slider Code
axcolor = 'black'
ax_k = plt.axes([0.1, 0.82, 0.3, 0.02], facecolor=axcolor)
ax_KA = plt.axes([0.1, 0.78, 0.3, 0.02], facecolor=axcolor)
ax_kd = plt.axes([0.1, 0.74, 0.3, 0.02], facecolor=axcolor)
ax_FA0 = plt.axes([0.1, 0.7, 0.3, 0.02], facecolor=axcolor)
ax_PA0 = plt.axes([0.1, 0.66, 0.3, 0.02], facecolor=axcolor)
ax_Us = plt.axes([0.1, 0.62, 0.3, 0.02], facecolor=axcolor)
ax_alpha = plt.axes([0.1, 0.58, 0.3, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k$ ($\frac{mol}{kg-cat.s.atm}$)', 0.002, 0.5, valinit=0.1,valfmt='%1.2f')
sKA = Slider(ax_KA, '$K_A$ ($atm^{-1}$)', 0.005, 20, valinit=1.5,valfmt='%1.1f')
skd = Slider(ax_kd, r'k$_{d}$ ($\frac{1}{s.atm}$)',0.001, 5, valinit=0.75,valfmt='%1.2f')
sFA0 = Slider(ax_FA0, r'F$_{A0}$ ($\frac{mol}{s}$)', 1, 50, valinit=10,valfmt='%1.1f')
sPA0 = Slider(ax_PA0, r'P$_{A0}$ (atm)', 1, 50, valinit=20,valfmt='%1.1f')
sUs = Slider(ax_Us, r'U$_s$ ($\frac{kg-cat}{s}$)', 0.1, 10, valinit=2,valfmt='%1.1f')
salpha = Slider(ax_alpha, r'$\alpha$ ($kg^{-1}$)', 0.0001,0.5, valinit=0.0019,valfmt='%1.4f')

def update_plot1(val):
    k = sk.val
    KA =sKA.val
    kd = skd.val
    FA0 = sFA0.val
    PA0 = sPA0.val
    Us = sUs.val
    alpha = salpha.val
    sol = odeint(ODEfun, y0, Wspan, (k,KA,kd,FA0,PA0,Us,alpha))
    p1.set_ydata(sol[:, 0])
    p2.set_ydata(sol[:, 1])
    p3.set_ydata(sol[:, 2])
    fig.canvas.draw_idle()

sk.on_changed(update_plot1)
sKA.on_changed(update_plot1)
skd.on_changed(update_plot1)
sFA0.on_changed(update_plot1)
sPA0.on_changed(update_plot1)
sUs.on_changed(update_plot1)
salpha.on_changed(update_plot1)

resetax = plt.axes([0.2, 0.87, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk.reset()
    sKA.reset()
    skd.reset()
    sFA0.reset()
    sPA0.reset()
    sUs.reset()
    salpha.reset()
button.on_clicked(reset)
