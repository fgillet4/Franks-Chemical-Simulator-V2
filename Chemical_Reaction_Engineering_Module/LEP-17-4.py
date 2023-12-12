#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
k = 0.01
Cao = 8
n = 2
def ODEfun(Yfuncvec, t, k ,Cao, n): 
    Xseg= Yfuncvec[0]
    X= Yfuncvec[1]
    # Explicit equations
    
    Ca = Cao*(1-X)
    
    ra = -k*Ca**n
    E1 = 4.44658e-10*t**4-1.1802e-7*t**3+1.35358e-5*t**2 -0.000865652*t+0.028004
    E2 = -2.64e-9*t**3+1.3618e-6*t**2-0.00024069*t+0.015011
    E = np.where(t<=70, E1, E2)
    # Differential equations
    dXsegdt = X*E
    dXdt=-ra/Cao
    return np.array([dXsegdt,dXdt])
tspan = np.linspace(0, 200, 1000)
y0 = np.array([0, 0])
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 17-4 Conversion Bounds for a Nonideal Reactor""", fontweight='bold', x = 0.2)
plt.subplots_adjust(left  = 0.3)

sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
Xseg= sol[:, 0]
X= sol[:, 1]
Ca = Cao*(1-X)
ra = -k*Ca**n

p1, p2 = ax2.plot(tspan, X, tspan, Xseg)
ax2.legend([r'$X_{seg}$', r'$X$'], loc="best")
ax2.set_xlabel('t (mins)', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 200)
ax2.grid()

p3 = ax3.plot(tspan, Ca)[0]
ax3.legend([r'$C_A$'], loc="best")
ax3.set_xlabel('t (mins)', fontsize='medium')
ax3.set_ylabel(r'$C_A (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 8)
ax3.set_xlim(0, 200)
ax3.grid()

p4 = ax4.plot(tspan, -ra)[0]
ax4.legend([r'$-r_A$'], loc="best")
ax4.set_xlabel('t (mins)', fontsize='medium')
ax4.set_ylabel(r'$-r_A$', fontsize='medium')
ax4.set_ylim(0, 0.7)
ax4.set_xlim(0, 200)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -0.8,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dt} = \dfrac{-r_A}{C_{A0}}$'
                  '\n \n'
         r'$\dfrac{dX_{seg}}{dt} = X.E$'
                  '\n\n'
         'Explicit Equations' '\n\n'   
         
           
         r'$E_1 = +4.44658.10^{-10}t^4 - 1.1802.10^{-7}t^3$''\n \t'
         r'$ +1.35358.10^{-5}t^2 - 8.65652.10^{-4}t$''\n \t'
         r'$+ 0.028004$'
         '\n\n'
          
         r'$E_2 = -2.64.10^{-9}t^3 + 1.3618.10^{-6}t^2$''\n \t'
         r'$- 2.4069.10^{-4}t + 0.015011$'
         '\n\n'    
         r'$E = IF\hspace{0.5}(t<=70)\hspace{0.5} then \hspace{0.5}(E_1) \hspace{0.5} else\hspace{0.5} (E_2)$'
         '\n\n'
         r'$C_A = C_{A0}(1-X)$'
         '\n\n'
         r'$r_A = -kC_A^n$'
         '\n\n'
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)


sk = Slider(ax_k, r'$k (\frac{mol^{1-n}}{dm^{3(1-n)}.s})$', 0.0001, 0.1, valinit=0.01, valfmt='%1.4f')
sCao = Slider(ax_Cao, r'$C_{A0} (\frac{mol}{dm^3})$', 0.5, 30, valinit=8) 
sn = Slider(ax_n, r'$n$', 0.5, 10, valinit=1, valfmt='%1.1f')

def update_plot(val):
    k = sk.val
    Cao = sCao.val
    n = sn.val
    sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
    Xseg= sol[:, 0]
    X= sol[:, 1]
    Ca = Cao*(1-X)
    ra = -k*Ca**n
    p1.set_ydata(X)
    p2.set_ydata(Xseg)
    p3.set_ydata(Ca)
    p4.set_ydata(-ra)
    fig.canvas.draw_idle()

sk.on_changed(update_plot)
sCao.on_changed(update_plot)
sn.on_changed(update_plot)

resetax = plt.axes([0.38, 0.75, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')
def reset(event):
    sk.reset()
    sCao.reset()
    sn.reset()
button.on_clicked(reset)






