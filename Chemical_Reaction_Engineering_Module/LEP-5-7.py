#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
alpha = 0.0367
Fa0 = 0.1362
Fb0 = 0.068
FI = 0.256 
kprime=0.0074
def ODEfun(Yfuncvec, W, alpha, Fa0, Fb0, FI, kprime): 
    X = Yfuncvec[0]
    p= Yfuncvec[1] 
    # Explicit equations
    FT0 =  Fa0 + Fb0 + FI
    yA0 = Fa0/FT0
    eps = yA0*(-0.5)
    raprime = -(kprime * (1 - X) / (1 + eps * X) * p) 
    # Differential equations
    dXdW = -(raprime / Fa0) 
    dpdW = -(alpha * (1 + eps * X) / 2 / p) 
    return np.array([dXdW, dpdW]) 

W = np.linspace(0, 27,1000) # Range for the weight of the catalyst. 
y0 = np.array([0, 1]) # Initial values for the dependent variables X and y. 


#%%
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("""Example 5-7 Calculating X in a Reactor with Pressure Drop""", fontweight='bold', x = 0.2)
fig.subplots_adjust(wspace=0.5,hspace=0.3)
plt.subplots_adjust(left = 0.5)
sol = odeint(ODEfun, y0, W, (alpha, Fa0, Fb0, FI, kprime))
X = sol[:, 0]
p= sol[:, 1] 
FT0 =  Fa0 + Fb0 + FI
yA0 = Fa0/FT0
eps = yA0*(-0.5)
f = (1 + eps * X) / p 
raprime = -(kprime * (1 - X) / (1 + eps * X) * p) 
rate = -raprime

p1, p2, p3 = ax1.plot (W, X, W, p, W, f)
ax1.legend(['X', 'p', 'f'], loc="upper left")
ax1.set_xlabel('Catalyst Weight (Kg)', fontsize='medium')
ax1.set_ylabel('X, p, f', fontsize='medium')
ax1.set_ylim(0, 3)
ax1.set_xlim(0, 27)
ax1.grid()
##

p4 = ax2.plot (W, rate)[0]
ax2.legend(['$-r_A\prime$'], loc="upper right")
ax2.set_xlabel('Catalyst Weight (Kg)', fontsize='medium')
ax2.set_ylabel('Rate (mol/s.kg-cat)', fontsize='medium')
ax2.set_ylim(0, 0.1)
ax2.set_xlim(0, 27)
ax2.grid()

ax1.text(-24.5, -3.7,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dW} = -\dfrac{r_A^\prime}{F_{A0}}$'
                  '\n \n'
         r'$\dfrac{dp}{dW} = \dfrac{-\alpha(1+\epsilon X)}{2.p}}$'
                  '\n \n'                  
         'Explicit Equations'
                  '\n\n'    
         r'$F_{T0} = F_{A0}+ F_{B0} + F_{I}$'         
         '\n\n'
         r'$y_{A0} = \dfrac{F_{A0}}{F_{T0}}$'    
                  '\n\n'   
         r'$\epsilon = y_{A0}(-0.5)$'
         '\n\n'
         r'$k^\prime = 0.0074$'
         '\n\n'
         r'$r_A^\prime = \dfrac{-k^\prime(1-X)p}{1+\epsilon X}$'
         '\n\n'
         r'$rate = -r_A^\prime$'

         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_kprime = plt.axes([0.1, 0.84 , 0.2, 0.015], facecolor=axcolor)
ax_Fa0 = plt.axes([0.1, 0.80, 0.2, 0.015], facecolor=axcolor)
ax_FI = plt.axes([0.1, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_alpha = plt.axes([0.1, 0.72, 0.2, 0.015], facecolor=axcolor)


skprime = Slider(ax_kprime, r'$kprime (\frac{mol}{kg_{cat}.s})$', 0.0005, 0.1, valinit=0.0074, valfmt="%1.4f")
sFa0 = Slider(ax_Fa0, r'$F_{A0} (\frac{mol}{s})$', 0.01, 1, valinit=0.1362) 
sFI = Slider(ax_FI, r'$F_{I} (\frac{mol}{s})$', 0.01, 1, valinit=0.256) 
salpha = Slider(ax_alpha, r'$\alpha (kg^{-1})$', 0, 0.039, valinit=0.0367, valfmt="%1.4f")

def update_plot1(val):
    kprime = skprime.val
    Fa0 = sFa0.val
    FI = sFI.val
    alpha = salpha.val
    sol = odeint(ODEfun, y0, W, (alpha, Fa0, Fb0, FI, kprime))
    X = sol[:, 0]
    p= sol[:, 1] 
    FT0 =  Fa0 + Fb0 + FI
    yA0 = Fa0/FT0
    eps = yA0*(-0.5)
    f = (1 + eps * X) / p 
    raprime = -(kprime * (1 - X) / (1 + eps * X) * p) 
    rate = -raprime
    p1.set_ydata(X)
    p2.set_ydata(p)
    p3.set_ydata(f)
    p4.set_ydata(rate)
    fig.canvas.draw_idle()

skprime.on_changed(update_plot1)
sFa0.on_changed(update_plot1)
sFI.on_changed(update_plot1)
salpha.on_changed(update_plot1)

resetax = plt.axes([0.16, 0.88, 0.08, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    skprime.reset()
    sFa0.reset()
    sFI.reset()
    salpha.reset()

button.on_clicked(reset)


