#%%
#Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
taus = 1
k = 1
taup = 1
def func(Cao, taus, k, taup):
    Cai = ((1+4*taus*k*Cao)**0.5 - 1)/(2*taus*k)
    Ca = 1/((1/Cai) + taup*k)
    X = (Cao - Ca)/Cao
    
    Caip = 1/((1/Cao) + taup*k)    
    Cap = ((1 + 4*taus*k*Caip)**0.5 - 1)/(2*taus*k)
    Xp = np.nan_to_num((Cao - Cap)/Cao)
    
    return np.array([X, Xp])

Cao = np.linspace(0, 10, 100)

#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 16-3 Comparing Second-Order Reaction Systems""", x = 0.25, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)
X, Xp = func(Cao, taus, k, taup)
p1, p2 = plt.plot(Cao, X, Cao, Xp)
plt.legend(['Early mixing', 'Late mixing'], loc='best')
ax.set_xlabel('$Initial \hspace{0.5} Concentration, C_{A0} \hspace{0.5} (kmol/m^3)$', fontsize='medium')
ax.set_ylabel('Conversion, X', fontsize='medium')
plt.ylim(0,1)
plt.xlim(0,10)
plt.grid()

ax.text(-8, 0.05,'For the case of Early Mixing'
        '\n\n'
        r'$C_{Ai} = \dfrac{\sqrt{1+4\tau_skC_{A0}} - 1}{2\tau_s k}$ '
        "\n\n"
        r'$\dfrac{1}{C_A} - \dfrac{1}{C_{Ai}} = \tau_p k$ '
        "\n\n"
        r'$X = \dfrac{C_{A0} - C_{A}}{C_{A0}}$ '        
        '\n \n'
        'For the case of Late Mixing'
        "\n\n"
        r'$\dfrac{1}{C_{Ai}} - \dfrac{1}{C_{A0}}= \tau_p k$ '
        '\n\n'
        r'$C_{A} = \dfrac{\sqrt{1+4\tau_skC_{Ai}} - 1}{2\tau_s k}$ '
        '\n\n'
        r'$X = \dfrac{C_{A0} - C_{A}}{C_{A0}}$ '                
        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')

#%%
# Slider Code
axcolor = 'black'
ax_taus = plt.axes([0.1, 0.8, 0.3, 0.02], facecolor=axcolor)
ax_taup = plt.axes([0.1, 0.75, 0.3, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.1, 0.7, 0.3, 0.02], facecolor=axcolor)

staus = Slider(ax_taus, r'$\tau_s (min)$', 0.1, 10, valinit=1)
staup = Slider(ax_taup, r'$\tau_p (min)$', 0.1, 10, valinit=1)
sk = Slider(ax_k, r'$k (\frac{m^3}{kmol.min})$', 0.1, 10, valinit=1)

def update_plot1(val):
    taus = staus.val
    taup =staup.val
    k = sk.val
    X, Xp = func(Cao, taus, k, taup)
    p1.set_ydata(X)
    p2.set_ydata(Xp)
    fig.canvas.draw_idle()

staus.on_changed(update_plot1)
staup.on_changed(update_plot1)
sk.on_changed(update_plot1)

resetax = plt.axes([0.2, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    staus.reset()
    staup.reset()
    sk.reset()
button.on_clicked(reset)
