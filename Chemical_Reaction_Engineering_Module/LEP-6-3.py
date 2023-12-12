#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
#Explicit equations
vo = 0.05 
k = 2.2
Vo = 5 
Cbo = 0.025  
Cao = 0.05  
def ODEfun(Yfuncvec, t, vo, k, Vo, Cbo): 
    Ca = Yfuncvec[0] 
    Cb = Yfuncvec[1] 
    Cc = Yfuncvec[2] 
    Cd = Yfuncvec[3] 
    V = Vo + vo * t  
    ra = 0 - (k * Ca * Cb) 
     
    rate = -ra 
    X = (Cao * Vo - (Ca * V)) / (Cao * Vo) 
    #Differential equations
    dCadt = ra - (vo * Ca / V) 
    dCbdt = ra + (Cbo - Cb) * vo / V 
    dCcdt = 0 - ra - (vo * Cc / V) 
    dCddt = 0 - ra - (vo * Cd / V) 
    return np.array([dCadt, dCbdt, dCcdt, dCddt]) 

t = np.linspace(0, 500, 1000)
y0 = np.array([0.05,0, 0, 0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 6 - 3 Isothermal Semibatch Reactor with Second - Order Reaction""", fontweight='bold', x = 0.25, y=0.98)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, t, (vo, k, Vo, Cbo))
Ca = sol[:, 0]
Cb = sol[:, 1]
Cc = sol[:, 2]
Cd = sol[:, 3]
ra = -k*Ca*Cb
V = Vo + vo * t
Ca = sol[:, 0]
X = (Cao * Vo - (Ca * V)) / (Cao * Vo) 

p1,p2,p3,p4 = ax2.plot(t, odeint(ODEfun, y0, t, (vo, k, Vo, Cbo)))
ax2.legend([r'$C_{A}$', r'$C_{B}$', r'$C_{C}$', '$C_{D}$'], loc='upper right')
ax2.set_xlabel('time(s)', fontsize='medium')
ax2.set_ylabel(r'Concentration (mol/$dm^{3}$)', fontsize='medium')
ax2.grid()
ax2.set_xlim(0, 500)
ax2.set_ylim(0, 0.05)

p5 = ax3.plot(t, X)[0]
ax3.legend(['X'], loc='upper right')
ax3.set_xlabel('time(s)', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium')
ax3.grid()
ax3.set_xlim(0, 500)
ax3.set_ylim(0, 1.2)

p6 = ax4.plot(t, -ra)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_xlabel('time(s)', fontsize='medium')
ax4.set_ylabel(r'Rate (mol/$dm^{3}$.s)', fontsize='medium')
ax4.grid()
ax4.set_xlim(0, 500)
ax4.set_ylim(0, 0.0005)

ax1.axis('off')
ax1.text(-1.0, -0.8,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dt} = r_A - \dfrac{v_0C_A}{V}$'
         '\n\n'
         r'$\dfrac{dC_B}{dt} = r_B + \dfrac{v_0(C_{B0} - C_B)}{V}$'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = r_C - \dfrac{v_0C_C}{V}$'
         '\n\n'
         r'$\dfrac{dC_D}{dt} = r_D - \dfrac{v_0C_D}{V}$'      
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$C_{A0} = 0.05$'
         '\n\n'         
         r'$V = V_0 + v_0.t$'
         '\n\n'
         r'$-r_A = kC_{A}C_B$'
         '\n\n'
         r'$X = \dfrac{C_{A0}V_0 - C_AV}{C_{A0}V_0}$'
         '\n\n'
         r'$-r_A =-r_B =r_C =r_D$'

         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_vo = plt.axes([0.32, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Vo = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Cbo = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)

svo = Slider(ax_vo, r'$v_o (\frac{dm^3}{s})$', 0.001, 1, valinit=0.05 )
sk = Slider(ax_k, r'$k (\frac{dm^3}{s.mol})$', 0.2, 5, valinit=2.2)
sVo = Slider(ax_Vo, r'$V_o (dm^3)$', 1, 40, valinit=5)
sCbo = Slider(ax_Cbo, r'$C_{Bo} (\frac{mol}{dm^3})$', 0, 0.1, valinit=0.025, valfmt = "%1.3f")


def update_plot(val):
    vo = svo.val
    k = sk.val
    Vo = sVo.val
    Cbo = sCbo.val
	
    sol = odeint(ODEfun, y0, t, (vo, k, Vo, Cbo))
    Ca = sol[:, 0]
    Cb = sol[:, 1]
    Cc = sol[:, 2]
    Cd = sol[:, 3]
    ra = -k*Ca*Cb
    V = Vo + vo * t
    X = (Cao * Vo - (Ca * V)) / (Cao * Vo) 
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(Cd)
    p5.set_ydata(X)
    p6.set_ydata(-ra)


    fig.canvas.draw_idle()

svo.on_changed(update_plot)
sk.on_changed(update_plot)
sVo.on_changed(update_plot)
sCbo.on_changed(update_plot)

resetax = plt.axes([0.38, 0.8, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    svo.reset()
    sk.reset()   
    sVo.reset()    
    sCbo.reset()    
	
button.on_clicked(reset)
plt.show()
