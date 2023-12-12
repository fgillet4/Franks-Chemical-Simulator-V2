#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
# Explicit equations
vo = 0.1 
Vo = 10 
Kc = 16 
k = 0.15
Cbo = 0.1 
Cao=0.04
def ODEfun(Yfuncvec, t, vo, Kc, k): 
    Ca = Yfuncvec[0] 
    Cb = Yfuncvec[1] 
    Cc = Yfuncvec[2] 
    # Explicit equations Inline
    ra = -k*(Ca*Cb-Cc**2/Kc) 
    V = Vo+vo*t 
    X=(Vo*Cao-V*Ca)/(Vo* Cao)
    # Differential equations
    dCadt = ra-vo*Ca/V 
    dCbdt = ra+vo*(Cbo-Cb)/V
    dCcdt = -2*ra-vo*Cc/V 
    return np.array([dCadt, dCbdt, dCcdt])

t = np.linspace(0, 200, 1000)
y0 = np.array([0.04, 0.1, 0.0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 6-5 Algorithm for the Liquid Phase Reaction""", fontweight='bold', x = 0.2, y=0.99)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, t, (vo, Kc, k))
Ca = sol[:, 0]
Cb = sol[:, 1]
Cc = sol[:, 2]
V = Vo+vo*t 
X=(Vo*Cao-V*Ca)/(Vo* Cao)
ra = -k*(Ca*Cb-Cc**2/Kc) 
V = Vo+vo*t 

p1, p2, p3 = ax2.plot(t, Ca, t, Cb, t, Cc)
ax2.legend(['$C_A$', '$C_B$', '$C_C$'], loc='best')
ax2.set_xlabel('time(s)', fontsize='medium', )
ax2.set_ylabel(r'Concentration (mol/$dm^{3}$)', fontsize='medium', )
ax2.grid()
ax2.set_xlim(0, 200)
ax2.set_ylim(0, 0.1)
 
p4 = ax3.plot(t, X)[0]
ax3.legend(['X'], loc='best')
ax3.set_xlabel('time(s)', fontsize='medium', )
ax3.set_ylabel('Conversion', fontsize='medium', )
ax3.grid()
ax3.set_xlim(0, 200)
ax3.set_ylim(0, 1.1)

p5,p6 = ax4.plot(t, -ra,t,2*ra)
ax4.legend(['$-r_A$','$-r_C$'], loc='best')
ax4.set_xlabel('time(s)', fontsize='medium', )
ax4.set_ylabel(r'Reaction Rate (mol/$dm^{3}.s)$', fontsize='medium', )
ax4.grid()
ax4.set_xlim(0, 200)
ax4.set_ylim(-0.003, 0.003)
ax4.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.axis('off')
ax1.text(-0.8, -1.1,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dt} = r_A - \dfrac{v_0C_A}{V}$'
         '\n\n'
         r'$\dfrac{dC_B}{dt} = r_A + \dfrac{v_0(C_{B0} - C_B)}{V}$'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = -2r_A - \dfrac{v_0C_C}{V}$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$C_{A0} = 0.04$'
         '\n\n'  
         r'$C_{B0} = 0.1$'
         '\n\n'          
          r'$V_0 = 10$'
         '\n\n'  
         r'$V = V_0 + v_0.t$'
         '\n\n'
         r'$r_A = -k\left(C_{A}C_B - \dfrac{C_C^2}{K_C}\right)$'
         '\n\n'
         r'$X = \dfrac{C_{A0}V_0 - C_AV}{C_{A0}V_0}$'
         '\n\n'
         r'$rate = -r_A$'
         '\n\n'
         r'$C_{B} (0) = 0.1$'
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_vo = plt.axes([0.32, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Kc = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)

svo = Slider(ax_vo, r'$v_0 (\frac{dm^3}{s})$', 0.001, 10, valinit=0.1 )
sk = Slider(ax_k, r'$k (\frac{dm^3}{s.mol})$', 0.05, 10, valinit=0.15)
sKc = Slider(ax_Kc, '$K_C$', 0.01, 100, valinit=16)


def update_plot(val):
    vo = svo.val
    k = sk.val
    Kc = sKc.val
    sol = odeint(ODEfun, y0, t, (vo, Kc, k))
    Ca = sol[:, 0]
    Cb = sol[:, 1]
    Cc = sol[:, 2]
    V = Vo+vo*t 
    X=(Vo*Cao-V*Ca)/(Vo* Cao)
    ra = -k*(Ca*Cb-Cc**2/Kc) 
    V = Vo+vo*t 	
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(X)
    p5.set_ydata(-ra)
    p6.set_ydata(2*ra)
    fig.canvas.draw_idle()

svo.on_changed(update_plot)
sk.on_changed(update_plot)
sKc.on_changed(update_plot)

resetax = plt.axes([0.38, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    svo.reset()
    sk.reset()     
    sKc.reset()    
	
button.on_clicked(reset)
plt.show()


 


