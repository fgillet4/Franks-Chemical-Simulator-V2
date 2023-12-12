#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})

from matplotlib.widgets import Slider, Button

phi = 0.4
CF = 0.8
DAB = 10**-6
t = np.linspace(1, 20, 1000)

De = phi*CF*DAB/t

#%%
fig, ax1 = plt.subplots()
plt.subplots_adjust(left=0.4, bottom = 0.2)
fig.suptitle("""LEP-15-1: Finding the Effective Diffusivity""", fontweight='bold', x = 0.2, y=0.97)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

p1 = ax1.plot(t, De)[0]
ax1.grid()
ax1.set_ylabel('$D_e (m^2/s)$', fontsize='medium', fontweight='bold')
ax1.set_xlabel('tortousity', fontsize='medium',)
ax1.set_ylim(10**-8, 10**-6)
ax1.set_xlim(1, 20)
ax1.text(-11, 10**-8,r'$The\thickspace formula\thickspace for\thickspace\thickspace effective\thickspace diffusivity\thickspace D_e\thickspace is$'
         '\n\n'
         r'$D_e = \dfrac{\phi_P \hspace{0.5} \sigma_C}{\tau}.D_{AB}$'
                  '\n\n'
         r'$\phi_P = pellet\thickspace porosity$'
                  '\n\n'
         r'$\sigma_C = constriction\thickspace factor$'
         '\n\n'
         r'$\tau = tortuosity$'
         '\n\n'
         r'$D_{AB} = bulk\thickspace diffusivity$'
         '\n'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


axcolor = 'black'
ax_phi = plt.axes([0.07, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_CF = plt.axes([0.07, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_DAB = plt.axes([0.07, 0.7, 0.2, 0.02], facecolor=axcolor)

sphi = Slider(ax_phi, r'$\phi_p$', 0.01, 0.99, valinit=0.4, valfmt='%1.2f')
sCF = Slider(ax_CF, r'$\sigma_c$', 0.1, 0.99, valinit=0.8,  valfmt='%1.2f')
sDAB = Slider(ax_DAB, r'$D_{AB} (\frac{m^2}{s})$', 10**-7, 10**-5, valinit=10**-6,  valfmt='%1.1E')

def update_plot(val):
    phi = sphi.val
    CF = sCF.val
    DAB = sDAB.val    
    De = phi*CF*DAB/t

    p1.set_ydata(De)
    fig.canvas.draw_idle()

sphi.on_changed(update_plot)
sCF.on_changed(update_plot)
sDAB.on_changed(update_plot)

resetax = plt.axes([0.13, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sphi.reset()
    sCF.reset()
    sDAB.reset()

button.on_clicked(reset)