#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
ko = 0.001
ku = 0.01
k1 = 2.5e9
k2 = 1
Cpo = 0.01
def ODEfun(Yfuncvec, t, ko, ku, k1, k2): 
    Cp =Yfuncvec[0]
    Ca =Yfuncvec[1]
    Cb = Yfuncvec[2]
    Cc = Yfuncvec[3]
    # Differential equations
    dCpdt = -ko*Cp
    dCadt = ko*Cp - ku*Ca - k1*Ca*Cb**2
    dCbdt = ku*Ca + k1*Ca*Cb**2 - k2*Cb 
    dCcdt = k2*Cb

    return np.array([dCpdt, dCadt, dCbdt, dCcdt])

tspan = np.linspace(0, 200, 1000)
y0 = np.array([0.01, 2.5e-5, 1e-5, 0])


#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP P8-G1 : Oscillating Reactions""", fontweight='bold', x = 0.3, y=0.96)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.3,hspace=0.3)

sol = odeint(ODEfun, y0, tspan, (ko, ku, k1, k2))
Cp = sol[:, 0]
Ca =sol[:, 1]
Cb = sol[:, 2]
Cc = sol[:, 3]
X = 1- Cp/Cpo
p1, p2 = ax2.plot(tspan, Ca, tspan, Cb)
ax2.legend([r'$C_A$', r'$C_B$'], loc='best')
ax2.set_xlabel('time (mins)', fontsize='medium')
ax2.set_ylabel(r'C$_i$ (moles/dm$^3$)', fontsize='medium')
ax2.set_ylim(0,0.0002)
ax2.set_xlim(0, 200)
ax2.grid()
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p3, p4 = ax3.plot(tspan, Cp, tspan, Cc)
ax3.legend([r'$C_P$', r'$C_C$'], loc='best')
ax3.set_xlabel('time (mins)', fontsize='medium')
ax3.set_ylabel(r'C$_i$ (moles/dm$^3$)', fontsize='medium')
ax3.set_ylim(0,0.01)
ax3.set_xlim(0, 200)
ax3.grid()
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')


p5 = ax4.plot(tspan, X)[0]
ax4.legend(['$X_P$'], loc='upper right')
ax4.set_ylim(0,1)
ax4.set_xlim(0,200)
ax4.grid()
ax4.set_xlabel('time (mins)', fontsize='medium')
ax4.set_ylabel('Conversion', fontsize='medium')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

ax1.axis('off')

ax1.text(-0.8, -0.5,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_{P}}{dt} = -k_0C_P$'
                  '\n\n'
         r'$\dfrac{dC_{A}}{dt} = k_0C_P - k_uC_A - k_1C_AC_B^2$'
                  '\n\n'
         r'$\dfrac{dC_{B}}{dt} = k_uC_A + k_1C_AC_B^2 - k_2C_B$'
                  '\n\n'
         r'$\dfrac{dC_{C}}{dt} = k_2C_B$'
                  '\n\n'                  
         'Explicit Equations' '\n\n'
         r'$C_{P0} = 0.01$'
         '\n\n'
         r'$X = 1 - \dfrac{C_P}{C_{P0}}$'
        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')


#%%
# Slider Code
axcolor = 'black'
ax_k0 = plt.axes([0.35, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_ku = plt.axes([0.35, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_k1 = plt.axes([0.35, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.35, 0.6, 0.15, 0.02], facecolor=axcolor)
#ax_k3.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
#ax_k3.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
sko = Slider(ax_k0, r'k$_0 (min^{-1})$', 0.0001, 0.01, valinit=0.001,valfmt="%1.4f")
sku = Slider(ax_ku, r'k$_u (min^{-1})$', 0.00001, 0.1, valinit=0.01,valfmt="%1.3f")
sk1 = Slider(ax_k1, r'k$_1 (\frac{dm^6}{mol^2.min})$', 25, 1e10, valinit=2.5e9, valfmt="%1.2E")
sk2 = Slider(ax_k2, r'k$_2 (min^{-1})$', 0.1, 10, valinit=1)

def update_plot1(val):
    ko = sko.val
    ku =sku.val
    k1 = sk1.val
    k2 = sk2.val
    sol = odeint(ODEfun, y0, tspan, (ko, ku, k1, k2))
    Cp = sol[:, 0]
    Ca =sol[:, 1]
    Cb = sol[:, 2]
    Cc = sol[:, 3]
    X = 1- Cp/Cpo
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cp)
    p4.set_ydata(Cc)
    p5.set_ydata(X)
    fig.canvas.draw_idle()

sko.on_changed(update_plot1)
sku.on_changed(update_plot1)
sk1.on_changed(update_plot1)
sk2.on_changed(update_plot1)

resetax = plt.axes([0.38, 0.8, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sko.reset()
    sku.reset()
    sk1.reset()
    sk2.reset()
button.on_clicked(reset)
