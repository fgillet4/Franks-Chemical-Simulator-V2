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
k = 5000 
Cao = 0.01
alpha = 0.01 
yao = 0.33
Kc = 0.05 
vo=1500

def ODEfun(Yfuncvec, W, k, Cao, alpha, yao, Kc, vo): 
    X = Yfuncvec[0]
    p= Yfuncvec[1] 
    epsilon = yao*1 
    thetaB = (1-yao)/yao 
    Fa0 = Cao*vo
    Ca = Cao*(1-X)*p/(1+epsilon*X)
    Cb = Cao*(thetaB-X)*p/(1+epsilon*X)
    Cc = Cao*3*X*p/(1+epsilon*X)
    ra = -k*(Ca*Cb -Cc**3/Kc)
    # Differential equations
    dXdW = -ra/Fa0 
    dpdW = -alpha*(1+epsilon*X)/2/p 
    return np.array([dXdW, dpdW]) 

Wspan = np.linspace(0, 80, 1000)
y0 = np.array([0, 1])

 
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 5-8 Reversible gas phase reaction in a packed bed with pressure drop""", fontweight='bold', x = 0.3)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, Wspan, (k, Cao, alpha, yao, Kc, vo))
epsilon = yao*1 
thetaB = (1-yao)/yao 
X = sol[:, 0]
p = sol[:, 1]
Ca = Cao*(1-X)*p/(1+epsilon*X)
Cb = Cao*(thetaB-X)*p/(1+epsilon*X)
Cc = Cao*3*X*p/(1+epsilon*X)
ra = -k*(Ca*Cb -Cc**3/Kc)

p1, p2, p3 = ax2.plot(Wspan, Ca,Wspan, Cb,Wspan, Cc)
ax2.legend(['$C_A$', '$C_B$', '$C_C$'], loc='upper right')
ax2.set_xlabel('Catalyst Weight (kg)', fontsize='medium')
ax2.set_ylabel('Concentration ($mol/dm^3$) ', fontsize='medium')
ax2.set_xlim(0, 80)
ax2.set_ylim(0,0.1)
ax2.grid()


p4, p5 = ax3.plot(Wspan, odeint(ODEfun, y0, Wspan, (k, Cao, alpha, yao, Kc, vo)))
ax3.legend(['X', 'p'], loc='upper right')
ax3.set_xlabel('Catalyst Weight (kg)', fontsize='medium')
ax3.set_ylabel('X, p', fontsize='medium')
ax3.set_xlim(0, 80)
ax3.set_ylim(0,1.2)
ax3.grid()


p6 = ax4.plot(Wspan, -ra)[0]
ax4.legend(['$-r_A^\prime$'], loc='upper right')
ax4.set_xlabel('Catalyst Weight (kg)', fontsize='medium')
ax4.set_ylabel('Reaction Rate (mol/s.kg-cat)', fontsize='medium')
ax4.set_ylim(0,5)
ax4.set_xlim(0, 80)
ax4.grid()

ax1.axis('off')
ax1.text(-0.8, -0.9,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dW} = -\dfrac{r_A^\prime}{F_{A0}}$'
                  '\n \n'
         r'$\dfrac{dp}{dW} = \dfrac{-\alpha(1+\epsilon X)}{2.p}}$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$C_A = \dfrac{C_{Ao}(1-X) p}{1+\epsilon X}$'
         '\n\n'
         r'$\theta_B = \dfrac{1-y_{A0}}{y_{A0}}$'
         '\n\n'
         r'$C_B = \dfrac{C_{Ao}(\theta_B - X)p}{1+\epsilon X}$'
         '\n\n'
         r'$C_C = \dfrac{3.C_{A0}.X.p}{1+\epsilon X}$'
         '\n\n'
         r'$-r_A^\prime = k(C_AC_B - \dfrac{C_C^3}{K_c})$'
         '\n\n'
         r'$F_{A0} = C_{A0}v_0$'
         
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_alpha = plt.axes([0.32, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.32, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_yao = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Kc = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)
ax_vo = plt.axes([0.32, 0.55, 0.2, 0.02], facecolor=axcolor)

salpha = Slider(ax_alpha, r'$\alpha (kg^{-1})$', .0001, 0.01, valinit=0.01,valfmt='%1.3f')
sk= Slider(ax_k, r'$k (\frac{dm^6}{mol.kgcat.s})$', 100, 15000, valinit=5000,valfmt='%1.0f')
sCao = Slider(ax_Cao, r'$C_{A0} (\frac{mol}{dm^3})$', 0.0001, 0.1, valinit=0.01, valfmt="%1.3f")
syao = Slider(ax_yao, r'$y_{A0}$', 0.01, 1, valinit=0.33,valfmt='%1.2f')
sKc = Slider(ax_Kc, r'$K_c (\frac{mol}{dm^3})$', 0.001, 0.6, valinit=0.05,valfmt='%1.3f')
svo = Slider(ax_vo, r'$v_0 (\frac{dm^3}{s})$', 100, 3000, valinit=1500,valfmt='%1.0f')


def update_plot2(val):
    alpha = salpha.val
    k =sk.val
    Cao =sCao.val
    yao = syao.val
    Kc = sKc.val
    vo = svo.val
    sol = odeint(ODEfun, y0, Wspan, (k, Cao, alpha, yao, Kc, vo))
    epsilon = yao*1 
    thetaB = (1-yao)/yao 
    X = sol[:, 0]
    p = sol[:, 1]
    Ca = Cao*(1-X)*p/(1+epsilon*X)
    Cb = Cao*(thetaB-X)*p/(1+epsilon*X)
    Cc = Cao*3*X*p/(1+epsilon*X) 
    ra = -k*(Ca*Cb -Cc**3/Kc)
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(X)
    p5.set_ydata(p)
    p6.set_ydata(-ra)    
    fig.canvas.draw_idle()


salpha.on_changed(update_plot2)
sk.on_changed(update_plot2)
sCao.on_changed(update_plot2)
syao.on_changed(update_plot2)
sKc.on_changed(update_plot2)
svo.on_changed(update_plot2)


resetax = plt.axes([0.36, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    salpha.reset()
    sk.reset()
    sCao.reset()
    syao.reset()
    sKc.reset()
    svo.reset()
button.on_clicked(reset)
