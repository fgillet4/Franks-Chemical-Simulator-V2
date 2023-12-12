#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
vo =  10
ca0 =  1
k1 =  1
k2 =  1
def ODEfun(Yfuncvec, V, k1, k2, vo): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]

    tau =  1.26
    ra =  -k1*ca
    rc =  k2*cb
    X =  1-ca/ca0
    rb =  k1*ca-k2*cb
    # Differential equations
    dcadV = (ra/vo)
    dcbdV = (rb/vo)
    dccdV = (rc/vo)
    return np.array([dcadV,dcbdV,dccdV])

vspan = np.linspace(0, 12.6, 100)
y0 = np.array([1, 0, 0])
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example LEP-WEB17-1 a : Reactions in a Series in a PFR""", fontweight='bold', x = 0.2)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, vspan, (k1, k2, vo))
ca= sol[:, 0]
cb= sol[:, 1]
cc= sol[:, 2]
ra =  -k1*ca
rc =  k2*cb
rb =  k1*ca-k2*cb
X =  1-ca/ca0


p1 = ax2.plot(vspan, X)[0]
ax2.legend(['X'], loc="best")
ax2.set_xlabel(r'$V (dm^3)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 12.6)
ax2.grid()

p2, p3, p4 = ax3.plot(vspan, ca, vspan, cb, vspan, cc)
ax3.legend([r'$C_A$', r'$C_B$', r'$C_C$'], loc="best")
ax3.set_xlabel(r'$V (dm^3)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 1)
ax3.set_xlim(0, 12.6)
ax3.grid()

p5, p6, p7 = ax4.plot(vspan, ra, vspan, rb, vspan, rc)
ax4.legend([r'$r_A$',r'$r_B$',r'$r_C$'], loc="best")
ax4.set_xlabel(r'$V (dm^3)$', fontsize='medium')
ax4.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
ax4.set_ylim(-3,3)
ax4.set_xlim(0, 12.6)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -0.8,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dV} = \dfrac{r_A}{v_0}$'
                  '\n \n'
         r'$\dfrac{dC_B}{dV} = \dfrac{r_B}{v_0}$'
                  '\n \n'
         r'$\dfrac{dC_C}{dV} =\dfrac{r_C}{v_0}$'         
                  '\n\n'
         'Explicit Equations' '\n\n'   
         r'$C_{A0} = 1$'
         '\n\n'

         r'$\tau = 1.26$'
         '\n\n'         
         r'$r_A = -k_1C_A$'
         '\n\n'                
         r'$r_B = k_1C_A - k_2C_B$'
         '\n\n'
         r'$r_C = k_2C_B$'
         '\n\n'         
         r'$X = 1 -\dfrac{C_A}{C_{A0}}$'      
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k1 = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_vo = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)


sk1 = Slider(ax_k1, r'$k_1 (min^{-1})$', 0.01, 15, valinit=1, valfmt='%1.2f')
sk2 = Slider(ax_k2, r'$k_2 (min^{-1})$', 0.01, 15, valinit=1, valfmt='%1.2f') 
svo = Slider(ax_vo, r'$v_0 (\frac{dm^3}{min})$', 1,50, valinit=10, valfmt='%1.2f')

def update_plot(val):
    k1 = sk1.val
    k2 = sk2.val
    vo = svo.val
    sol = odeint(ODEfun, y0, vspan, (k1, k2, vo))
    ca= sol[:, 0]
    cb= sol[:, 1]
    cc= sol[:, 2]
    ra =  -k1*ca
    rc =  k2*cb
    rb =  k1*ca-k2*cb
    X =  1-ca/ca0
    p1.set_ydata(X)
    p2.set_ydata(ca)
    p3.set_ydata(cb)
    p4.set_ydata(cc)
    p5.set_ydata(ra)
    p6.set_ydata(rb)
    p7.set_ydata(rc)    
    fig.canvas.draw_idle()

sk1.on_changed(update_plot)
sk2.on_changed(update_plot)
svo.on_changed(update_plot)

resetax = plt.axes([0.38, 0.75, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')
def reset(event):
    sk1.reset()
    sk2.reset()
    svo.reset()
button.on_clicked(reset)
