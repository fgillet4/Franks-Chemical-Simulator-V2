#%%
#Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
k1 = 1
k2 = 1
Cao = 1
Cbo = 0
Cco = 0
def func(tau, k1, k2,Cao, Cbo, Cco): 
    Ca = Cao/(1 + k1*tau)
    Cb = (Cbo + k1*Ca*tau)/(1 + k2*tau)
    Cc = Cco + k2*Cb*tau    
    ra = -k1*Ca
    rb = k1*Ca - k2*Cb
    rc = k2*Cb
    X  = (Cao - Ca)/Cao
    return np.array([X, Ca, Cb, Cc, ra, rb, rc])

vspan = np.linspace(0, 1.26, 100)

 
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example LEP-WEB17-1 b : Reactions in a Series in a CSTR""", fontweight='bold', x = 0.2)
plt.subplots_adjust(left  = 0.3)

sol = func(vspan, k1, k2,Cao, Cbo, Cco)
X = sol[0, :]
Ca = sol[1, :]
Cb = sol[2, :]
Cc = sol[3, :]
ra = sol[4, :]
rb = sol[5, :]
rc = sol[6, :]

 
p1 = ax2.plot(vspan, X)[0]
ax2.legend(['X'], loc="best")
ax2.set_xlabel(r'$\tau (min)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 1.26)
ax2.grid()

p2, p3, p4 = ax3.plot(vspan, Ca, vspan, Cb, vspan, Cc)
ax3.legend([r'$C_A$', r'$C_B$', r'$C_C$'], loc="best")
ax3.set_xlabel(r'$\tau (min)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 5)
ax3.set_xlim(0, 1.26)
ax3.grid()

p5, p6, p7 = ax4.plot(vspan, ra, vspan, rb, vspan, rc)
ax4.legend([r'$r_A$',r'$r_B$',r'$r_C$'], loc="best")
ax4.set_xlabel(r'$\tau (min)$', fontsize='medium')
ax4.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
ax4.set_ylim(-3,3)
ax4.set_xlim(0, 1.26)
ax4.grid()

ax1.axis('off')
ax1.text(-0.8, -0.3,         
         'Equations'
                  '\n\n'
         r'$C_A = \dfrac{C_{A0}}{1+k_1\tau}$'
         '\n\n'         
         r'$C_B = \dfrac{C_{B0} + k_1C_{A}\tau}{1+k_2\tau}$'
         '\n\n'
         r'$C_C = C_{C0} + k_2C_B\tau$'
         '\n\n'
         r'$r_A = -k_1C_A$'
         '\n\n'
         r'$r_B = k_1C_A - k_2C_B$'
         '\n\n'
         r'$r_C = k_2C_B$'
         '\n\n'
         r'$X = \dfrac{(C_{A0} - C_{A})}{C_{A0}}$'
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k1 = plt.axes([0.32, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.32, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cbo = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Cco = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1 (min^{-1})$', .01, 15, valinit=1,valfmt='%1.2f')
sk2= Slider(ax_k2, r'$k_2 (min^{-1})$', .01, 15, valinit=1,valfmt='%1.2f')
sCao = Slider(ax_Cao, r'$C_{Ao} (\frac{mol}{dm^3})$', 0.1, 2.5, valinit=1, valfmt="%1.2f")
sCbo = Slider(ax_Cbo, r'$C_{Bo} (\frac{mol}{dm^3})$', 0, 2.5, valinit=0, valfmt="%1.2f")
sCco = Slider(ax_Cco, r'$C_{Co} (\frac{mol}{dm^3})$', 0, 2.5, valinit=0, valfmt="%1.2f")


def update_plot2(val):
    k1 = sk1.val
    k2 =sk2.val
    Cao =sCao.val
    Cbo = sCbo.val
    Cco = sCco.val
    sol = func(vspan, k1, k2,Cao, Cbo, Cco)
    X = sol[0, :]
    Ca = sol[1, :]
    Cb = sol[2, :]
    Cc = sol[3, :]
    ra = sol[4, :]
    rb = sol[5, :]
    rc = sol[6, :]
    p1.set_ydata(X)
    p2.set_ydata(Ca)
    p3.set_ydata(Cb)
    p4.set_ydata(Cc)
    p5.set_ydata(ra)
    p6.set_ydata(rb)
    p7.set_ydata(rc)    
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sCao.on_changed(update_plot2)
sCbo.on_changed(update_plot2)
sCco.on_changed(update_plot2)


resetax = plt.axes([0.36, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk1.reset()
    sk2.reset()
    sCao.reset()
    sCbo.reset()
    sCco.reset()
button.on_clicked(reset)
