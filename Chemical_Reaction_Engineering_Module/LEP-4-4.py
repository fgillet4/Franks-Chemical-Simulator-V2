import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#Explicit Equations
thetaB=0.54
epsilon=-0.14
k=9.7
KO2=38.5
KSO3=42.5
KP=930
PSO20=4.1
def myFunction(X, W, thetaB, epsilon, k, KO2, KSO3, KP, PSO20):
    Fa0=3
    PSO2=PSO20*(1-X)/(1+epsilon*X)
    PSO3=PSO20*X/(1+epsilon* X)
    PO2=PSO20* (thetaB-X/2)/(1+epsilon* X)
    ra= -k*(PSO2* np.sqrt(PO2)-PSO3/KP)/(1+np.sqrt(PO2* KO2)+PSO3 *KSO3)**2    
    return -ra/Fa0

#Range of W and intial value of X
W = np.linspace(0, 1000, 10000)
X0 = np.array([0])    

#%%
#Example 4-4: Rate Law for SO2 Oxidation
X_sol = odeint(myFunction, X0, W, (thetaB, epsilon, k, 
                                            KO2, KSO3, KP, PSO20))
PSO2=PSO20* (1-X_sol)/(1+epsilon*X_sol)
PSO3=PSO20* X_sol/(1+epsilon* X_sol)
PO2=PSO20*(thetaB-X_sol/2)/(1+epsilon* X_sol)
ra= -k*(PSO2* np.sqrt(PO2)-PSO3/KP)/(1+np.sqrt(PO2* KO2)+PSO3 *KSO3)**2    

fig, ax = plt.subplots()
fig.suptitle("""Example 4-4 Rate law for SO2 Oxidation""", fontweight='bold', x = 0.18, y=0.98)
plt.subplots_adjust(left=0.5)

p1 = plt.plot(X_sol, -ra)[0]
plt.grid()
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.legend(['Rate'], loc="upper right")
ax.set_xlabel('Conversion, X', fontsize='medium')
ax.set_ylabel('$-r^\prime_{SO_2}$ (mol/h.g-cat)', fontsize="medium")

ax.text(-1.17, 0.4,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dW} =-\dfrac{r^\prime_{A} }{F_{A0}}$'

         '\n'
         '\n'
         'Explicit Equations'
         '\n\n'
         r'$F_{A0} = 3$'
                  '\n\n'
         r'$\epsilon = -0.14$'
                  '\n\n'
         r'$P_{SO_2} =  \dfrac{P_{SO_2,0}\thinspace(1-X)}{1 + \epsilon X}$'
                  '\n\n'
         r'$P_{SO_3} =  \dfrac{P_{SO_2,0} \thinspace X}{1 + \epsilon X}$'
                  '\n\n'
         r'$P_{O_2} =  \dfrac{P_{SO_2,0} (\theta_B - \dfrac{X}{2})}{1 + \epsilon X}$'
                  '\n\n'
         r'$-r^\prime_{A}= \dfrac{k(P_{SO_2} \sqrt{P_{O_2}} - \dfrac{P_{SO_3}}{K_P} )}{(1 + \sqrt{P_{O_2}K_{O_2}} +P_{SO_3}K_{SO_3} )^2}$'

         , ha='left', fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=20), fontweight='bold')


axcolor = 'black'
ax_thetaB = plt.axes([0.26, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.26, 0.70, 0.15, 0.02], facecolor=axcolor)
ax_KO2 = plt.axes([0.26, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_KSO3 = plt.axes([0.26, 0.60, 0.15, 0.02], facecolor=axcolor)
ax_KP = plt.axes([0.26, 0.55, 0.15, 0.02], facecolor=axcolor)
ax_PSO20 = plt.axes([0.26, 0.50, 0.15, 0.02], facecolor=axcolor)

sthetaB = Slider(ax_thetaB, r'$\theta_B$', 0., 2., valinit=0.54)
sk = Slider(ax_k, r'$k (\frac{mol\thinspace {SO_2}}{atm^{3/2}.h.g_{cat}})$', 0, 20, valinit=9.7)
sKO2 = Slider(ax_KO2, r'$K_{O_2} (atm^{-1})$', 0, 100, valinit=38.5, valfmt = "%1.1f")
sKSO3 = Slider(ax_KSO3, r'$K_{SO_3} (atm^{-1})$', 0, 100, valinit=42.5, valfmt = "%1.1f")
sKP = Slider(ax_KP, r'$K_P (atm^{-1/2})$', 0, 2500, valinit=930, valfmt = "%1.0f")
sPSO20 = Slider(ax_PSO20, r'$P_{SO_2,0} (atm)$', 0.01, 10, valinit=4.1)

def update_plot(val):
    thetaB = sthetaB.val
    k = sk.val
    KO2 = sKO2.val    
    KSO3 = sKSO3.val
    KP = sKP.val
    PSO20 = sPSO20.val	
    x = odeint(myFunction, X0, W, (thetaB, epsilon, k, 
                                                KO2, KSO3, KP, PSO20))
    PSO2=PSO20* (1-x)/(1+epsilon*x)
    PSO3=PSO20* x/(1+epsilon* x)
    PO2=PSO20* (thetaB-x/2)/(1+epsilon* x)
    ra= -k*(PSO2* np.sqrt(PO2)-PSO3/KP)/(1+np.sqrt(PO2* KO2)+PSO3 *KSO3)**2    
    p1.set_ydata(-ra)
    fig.canvas.draw_idle()

sthetaB.on_changed(update_plot)
sk.on_changed(update_plot)
sKO2.on_changed(update_plot)
sKSO3.on_changed(update_plot)
sKP.on_changed(update_plot)
sPSO20.on_changed(update_plot)

resetax = plt.axes([0.3, 0.81, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sthetaB.reset()
    sk.reset()
    sKO2.reset()
    sKSO3.reset()
    sKP.reset()
    sPSO20.reset()
button.on_clicked(reset)

plt.show()

