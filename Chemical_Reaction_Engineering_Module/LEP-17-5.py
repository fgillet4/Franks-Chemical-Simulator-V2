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
def ODEfun(Yfuncvec, z, k, Cao, n): 
    X= Yfuncvec
    # Explicit equations
    lam = 200-z
    Ca = Cao*(1-X)
    E1 = 4.44658e-10*lam**4-1.1802e-7*lam**3+1.35358e-5*lam**2-.000865652*lam+.028004
    E2 = -2.64e-9*lam**3+1.3618e-6*lam**2-.00024069*lam+.015011
    F1 = 4.44658e-10/5*lam**5-1.1802e-7/4*lam**4+1.35358e-5/3*lam**3-.000865652/2*lam**2+.028004*lam
    F2 = -(-9.30769e-8*lam**3+5.02846e-5*lam**2-.00941*lam+.618231-1)
    ra = -k*Ca**n
    E = np.where(lam<=70, E1, E2)
    F = np.where(lam<=70, F1, F2)
    EF=E/(1-F)
    # Differential equations
    dXdz = -(ra/Cao+EF*X)
    return dXdz 

tspan = np.linspace(0, 200, 1000)
y0 = 0
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 17-5 Using Software to Make Maximum Mixedness Model Calculations""", fontweight='bold', x = 0.3)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
X= sol
Ca = Cao*(1-X)
ra = -k*Ca**n

p1 = ax2.plot(tspan, X)[0]
ax2.legend([r'$X$'], loc="best")
ax2.set_xlabel('t (mins)', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 200)
ax2.grid()

p2 = ax3.plot(tspan, Ca)[0]
ax3.legend([r'$C_A$'], loc="best")
ax3.set_xlabel('t (mins)', fontsize='medium')
ax3.set_ylabel(r'$C_A (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 8)
ax3.set_xlim(0, 200)
ax3.grid()

p3 = ax4.plot(tspan, -ra)[0]
ax4.legend([r'$-r_A$'], loc="best")
ax4.set_xlabel('t (mins)', fontsize='medium')
ax4.set_ylabel(r'$-r_A$', fontsize='medium')
ax4.set_ylim(0, 0.7)
ax4.set_xlim(0, 200)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -1,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dz} = -\left(\dfrac{r_A}{C_{A0}} + \dfrac{E.X}{(1-F)}\right)$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$\lambda = 200-z$'         
                  '\n\n'
         r'$C_A = C_{A0}(1-X)$'
         '\n\n'
         r'$r_A = -kC_A^n$'
         '\n\n'  
         
         r'$E_1 = +4.44658.10^{-10}\lambda^4-1.1802.10^{-7}\lambda^3$''\n \t'
         r'$ +1.35358.10^{-5}\lambda^2-.000865652\lambda$''\n \t'
         r'$+.028004$'
         '\n\n'
         
         r'$E_2 = -2.64.10^{-9}\lambda^3+1.3618.10^{-6}\lambda^2$''\n \t'
         r'$-.00024069\lambda+.015011$'
         '\n \n'
         
         r'$F_1 = 4.44658.10^{-10}/5\lambda^5-1.1802.10^{-7}/4\lambda^4$''\n \t'
         r'$+1.35358.10^{-5}/3\lambda^3-.000865652/2\lambda^2$''\n \t'
         r'$+.028004*\lambda$'
         '\n\n'  
         
         r'$F_2 = +9.30769.10^{-8}\lambda^3-5.02846.10^{-5}\lambda^2$''\n \t'
         r'$+.00941*\lambda-.618231+1$'
         '\n\n'    
         r'$E = IF \hspace{0.5}(\lambda<=70)\hspace{0.5} then \hspace{0.5}(E_1) \hspace{0.5}else\hspace{0.5} (E_2)$'
         '\n\n'    
         r'$F = IF\hspace{0.5}(\lambda<=70)\hspace{0.5} then\hspace{0.5} (F_1)\hspace{0.5} else \hspace{0.5} (F_2)$'  
         '\n\n'  
         r'$EF = \dfrac{E}{(1-F)}$'
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k (\frac{mol^{1-n}}{dm^{3(1-n)}.s})$', 0.0001, 0.1, valinit=0.01, valfmt='%1.5f')
sCao = Slider(ax_Cao, r'$C_{A0} (\frac{mol}{dm^3})$', 0.5, 30, valinit=8) 
sn = Slider(ax_n, r'$n$', 0.5, 10, valinit=1)

def update_plot(val):
    k = sk.val
    Cao = sCao.val
    n = sn.val
    sol = odeint(ODEfun, y0, tspan, (k, Cao, n))
    X= sol
    Ca = Cao*(1-X)
    ra = -k*Ca**n
    p1.set_ydata(X)
    p2.set_ydata(Ca)
    p3.set_ydata(-ra)
   
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






