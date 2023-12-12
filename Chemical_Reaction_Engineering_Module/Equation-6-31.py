#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
Kc = 0.05
Fbo = 0.05
Nao = 0.1
def func(t, Kc, Fbo, Nao):
    Xe = (Kc*(1+ (Fbo*t)/(Nao)) - np.sqrt((Kc*(1+ (Fbo*t)/(Nao)))**2 - 4*(Kc-1)*Kc*t*Fbo/Nao))/(2*(Kc-1))
    return Xe

tspan = np.linspace(0, 250, 100)

#%%
fig, ax = plt.subplots()
fig.suptitle("""Equation:6-31 (Calculating Equilibrium Conversion in a Semibatch Reactor)""", fontweight='bold', x = 0.25)
plt.subplots_adjust(left  = 0.4)

sol = func(tspan, Kc, Fbo, Nao)
p1 = ax.plot(tspan, sol)[0]
ax.legend([r'$X_e$'], loc="best")
ax.set_xlabel('time (min)', fontsize='medium', fontweight='bold')
ax.set_ylabel('Conversion', fontsize='medium', fontweight='bold')
ax.set_ylim(0, 1)
ax.set_xlim(0, 250)
ax.grid()
plt.text(-165, 0.4,
         'Equation:'
                  '\n\n'
         r'$X_e = \dfrac{K_C \left(1+ \dfrac{F_{B0}t}{N_{A0}}\right) - \sqrt{\left[K_C (1+ \dfrac{F_{B0}t}{N_{A0}})\right]^2 - 4(K_C-1)K_C\dfrac{t\thinspace F_{B0}}{N_{A0}}}}{2(K_C-1)}$'

         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
axcolor = 'black'
ax_Kc = plt.axes([0.08, 0.75, 0.25, 0.02], facecolor=axcolor)
ax_Fbo = plt.axes([0.08, 0.7, 0.25, 0.02], facecolor=axcolor)
ax_Nao = plt.axes([0.08, 0.65, 0.25, 0.02], facecolor=axcolor)

sKc = Slider(ax_Kc, r'$K_c$', .001, 0.9, valinit = 0.05,valfmt='%1.3f')
sFbo = Slider(ax_Fbo, r'$F_{B0}$', 0.001, 0.1, valinit=0.05,valfmt='%1.3f')
sNao= Slider(ax_Nao, r'$N_{A0}$', 0.01, 10, valinit=0.1)


def update_plot2(val):
    Kc = sKc.val
    Fbo =sFbo.val
    Nao =sNao.val
    sol = func(tspan, Kc, Fbo, Nao)
    p1.set_ydata(sol)
    fig.canvas.draw_idle()


sKc.on_changed(update_plot2)
sFbo.on_changed(update_plot2)
sNao.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKc.reset()
    sFbo.reset()
    sNao.reset()
button.on_clicked(reset)
    

