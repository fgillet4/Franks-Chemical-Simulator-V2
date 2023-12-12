#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
k = 0.1
Cao = 1
n = 1
def ODEfun(Yfuncvec,t, k, Cao, n): 
    X= Yfuncvec[0]
    Xseg= Yfuncvec[1]
    tm= Yfuncvec[2]
    F= Yfuncvec[3]
    Xseglfr= Yfuncvec[4]
    # Explicit equations
    C1= 0.0038746 + 0.2739782*t + 1.574621*t**2 - 0.2550041*t**3
    C2= -33.43818 + 37.18972*t - 11.58838*t**2 + 1.695303*t**3 - 0.1298667*t**4 + 0.005028*t**5 - 7.743*10**-5*t**6
    C = np.where(t<=4, C1, C2)
    E=C/51
    Elfr = np.where(t<5.1/2, 0, (5.1**2)/(2*t**3 + 0.0001))
    # Differential equations
    dXdt=(k*(Cao**n)*((1-X)**n))/Cao
    dXsegdt = X*E 
    dtmdt = t*E 
    dFdt = E
    dXseglfrdt = X*Elfr
    return np.array([dXdt,dXsegdt,dtmdt,dFdt, dXseglfrdt])

tspan = np.linspace(0, 14, 100)
y0 = np.array([0, 0, 0, 0, 0])
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 17-2: Mean Conversion Calculation in a Real Reactor""", fontweight='bold', x = 0.24)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
X= sol[:, 0]
Xseg= sol[:, 1]
tm= sol[:, 2]
F= sol[:, 3]
Xseglfr= sol[:, 4]

p1, p2, p3 = ax2.plot(tspan, X, tspan, Xseg, tspan, Xseglfr)
ax2.legend([r'$X$', r'$X_{seg}$', r'$X_{seg} (for\hspace{0.5} LFR\hspace{0.5} RTD)$'], loc="best")
ax2.set_xlabel('t (min)', fontsize='medium', fontweight='bold')
ax2.set_ylabel('Conversion', fontsize='medium', fontweight='bold')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 14)
ax2.grid()

p4 = ax3.plot(tspan, tm)[0]
ax3.legend([r'$t_m$'], loc="best")
ax3.set_xlabel('t (min)', fontsize='medium', fontweight='bold')
ax3.set_ylabel(r'$t_m (min)$', fontsize='medium', fontweight='bold')
ax3.set_ylim(0, 6)
ax3.set_xlim(0, 14)
ax3.grid()

p5 = ax4.plot(tspan, F)[0]
ax4.legend(['F'], loc="best")
ax4.set_xlabel('t (min)', fontsize='medium', fontweight='bold')
ax4.set_ylabel('F(t)', fontsize='medium', fontweight='bold')
ax4.set_ylim(0, 1)
ax4.set_xlim(0, 14)
ax4.grid()

ax1.axis('off')
ax1.text(-1, -1.2,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dt} = \dfrac{kC_{A0}^n(1-X)^n}{C_{A0}}$'
                  '\n \n'
         r'$\dfrac{dX_{seg}}{dt} = X.E$'
                  '\n \n'
         r'$\dfrac{dF}{dt} = E$'
                  '\n \n'
         r'$\dfrac{dt_m}{dt} = t.E$'
                  '\n \n'
         r'$\dfrac{dX_{seg\hspace{0.5} LFR}}{dt} = X.E_{LFR}$'
                  '\n \n'                  
         'Explicit Equations'
                  '\n\n'
         r'$C_1 = + 0.0038746 + 0.2739782t$''\n \t'
         r'$ + 1.574621t^2 - 0.2550041t^3$'
         '\n\n'
         
         r'$C_2 = -33.43818 + 37.18972*t$''\n \t' r'$- 11.58838*t^2 + 1.695303*t^3$''\n \t'
         r'$ - 0.1298667*t^4 + 0.005028*t^5$''\n \t'
         r'$ - 7.743*10^{-5}*t^6$'
         '\n\n'    
         
         r'$Area = 51$'
         '\n\n'
          r'$C = If\hspace{0.5} (t<=t1)\hspace{0.5} then\hspace{0.5} (C_1) \hspace{0.5}else\hspace{0.5} (C_2)$'
         '\n\n'
         r'$E = \dfrac{C}{Area}$'
         '\n\n'
         r'$\tau = 5.1$'
         '\n\n'
         r'$E_{LFR} = IF\hspace{0.5}(t<\frac{\tau}{2})\hspace{0.5} then \hspace{0.5}(0)\hspace{0.5} else (\frac{\tau^2}{2t^3 + 0.0001})$'
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)


sk = Slider(ax_k, r'$k (\frac{mol^{1-n}}{dm^{3(1-n)}.min})$', 0.01, 1, valinit=0.1, valfmt='%1.2f')
sCao = Slider(ax_Cao, r'$C_{A0} (\frac{mol}{dm^3})$', 0.1, 20, valinit=1, valfmt='%1.1f') 
sn = Slider(ax_n, r'$n$', 0.5, 10, valinit=1, valfmt='%1.1f')

def update_plot(val):
    k = sk.val
    Cao = sCao.val
    n = sn.val
    sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
    X= sol[:, 0]
    Xseg= sol[:, 1]
    tm= sol[:, 2]
    F= sol[:, 3]
    Xseglfr= sol[:, 4]
    p1.set_ydata(X)
    p2.set_ydata(Xseg)
    p3.set_ydata(Xseglfr)
    p4.set_ydata(tm)
    p5.set_ydata(F)    
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






