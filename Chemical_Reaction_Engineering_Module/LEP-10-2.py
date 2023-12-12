#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
FTo=50
k=0.00087
KT=1.038
KB=1.39
alpha = 0.000098 
Po = 40
yH2=0.45
yT=0.3
def ODEfun(Y, W, FTo, k, KT, KB, alpha, Po,yH2,yT): 
    X = Y[0]
    PTo = yT*Po 
    p = (1-alpha*W)**0.5
    P = p*Po 
    ThetaH2=yH2/yT
    PH2 = PTo*(ThetaH2-X)*p 
    PB = PTo*X*p 
    PT = PTo*(1-X)*p 
    rt = -k*PT*PH2/(1+KB*PB+KT*PT) 
    RATE = -rt 
    # Differential equations
    dXdW= -rt/FTo 
    return dXdW 

Wspan = np.linspace(0, 10000, 10000)
y0 = np.array([0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 10-2 Catalytic Reactor Design""", fontweight='bold', x = 0.16, y=0.96)
plt.subplots_adjust(left  = 0.35)
fig.subplots_adjust(wspace=0.35,hspace=0.35)
sol = odeint(ODEfun, y0, Wspan, (FTo, k, KT, KB, alpha, Po,yH2,yT))
X = sol[:, 0]
PTo = yT*Po 
p = (1-alpha*Wspan)**0.5
P = p*Po 
ThetaH2=yH2/yT
PH2 = PTo*(ThetaH2-X)*p 
PB = PTo*X*p 
PT = PTo*(1-X)*p 
rt = -k*PT*PH2/(1+KB*PB+KT*PT) 
RATE = -rt 
p1, p2 = ax2.plot(Wspan, X, Wspan, p)
ax2.legend(['X', 'p'], loc='lower right')
ax2.set_xlabel('Weight (kg)', fontsize='medium')
ax2.set_ylabel('X, p', fontsize='medium')
ax2.set_ylim(0,1.05)
ax2.set_xlim(0,10000)
ax2.grid()
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p3, p4, p5 = ax3.plot(Wspan, PH2, Wspan, PB, Wspan, PT)
ax3.legend([r'P$_{H2}$', r'P$_B$', r'P$_T$'], loc='upper right')
ax3.set_ylim(0,50)
ax3.set_xlim(0,10000)
ax3.grid()
ax3.set_xlabel('Weight (kg)', fontsize='medium')
ax3.set_ylabel(r'P$_i$ (atm)', fontsize='medium')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')


p6 = ax4.plot(Wspan, RATE)[0]
ax4.legend([r'$-r_T^\prime$'], loc='upper right')
ax4.set_ylim(0,0.02)
ax4.set_xlim(0,10000)
ax4.grid()
ax4.set_xlabel('Weight (kg)', fontsize='medium')
ax4.set_ylabel('Rate (mol/kg-cat.min)', fontsize='medium')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

ax1.axis('off')
ax1.text(-1.2, -1,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dW} = \dfrac{-r_T^\prime}{F_{T0}}$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$P_{T0} = y_{T0}P_0$'
                  '\n\n'
         r'$p = \sqrt{1-\alpha W}$'
         '\n\n'
         r'$P = p.P_0$'
         '\n\n'
         r'$P_{H_2} = P_{T0}(\theta_{H2}-X)p$'
         '\n\n'
         r'$\theta_{H2}=\dfrac{y_{H2}}{y_{T0}}$'
         '\n\n'
         r'$P_B = P_{T0}(X)p$'
                  '\n\n'
         r'$P_T = P_{T0}(1-X)p$'
         '\n\n'
         r'$-r_T^\prime = \dfrac{kP_TP_{H_2}}{1+K_BP_B+K_TP_T}$'
         '\n\n'
         r'$Rate = -r_t^\prime$'
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
ax1.text(-1.4, -1.2,
         'Instructions: Make sure $y_{H2}$ +$y_{T0}$ is never greater than 1'
        , ha='left', wrap = True, fontsize=13, fontweight='bold',color='red')
#%%
axcolor = 'black'
ax_FTo = plt.axes([0.3, 0.8, 0.25, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.3, 0.76, 0.25, 0.02], facecolor=axcolor)
ax_KT = plt.axes([0.3, 0.72, 0.25, 0.02], facecolor=axcolor)
ax_KB = plt.axes([0.3, 0.68, 0.25, 0.02], facecolor=axcolor)
ax_alpha = plt.axes([0.3, 0.64, 0.25, 0.02], facecolor=axcolor)
ax_Po = plt.axes([0.3, 0.60, 0.25, 0.02], facecolor=axcolor)
ax_yH2 = plt.axes([0.3, 0.56, 0.25, 0.02], facecolor=axcolor)
ax_yT = plt.axes([0.3, 0.52, 0.25, 0.02], facecolor=axcolor)


sFTo = Slider(ax_FTo, r'$F_{T0} (\frac{mol}{min})$', 10,200, valinit=50)
sk = Slider(ax_k, r'$k (\frac{mol}{atm^2.kg_{cat}.min})$', 0.00001, 0.01, valinit=0.00087,valfmt = "%1.5f")
sKT= Slider(ax_KT, r'$K_T (atm^{-1})$', 0.1, 10, valinit=1.038)
sKB = Slider(ax_KB, r'$K_B (atm^{-1})$', 0.1, 10, valinit=1.39)
salpha = Slider(ax_alpha, r'$\alpha (kg^{-1})$', 0.00001,0.0003, valinit=.000098,valfmt = "%1.6f")
sPo = Slider(ax_Po, r'$P_0 (atm)$', 1, 150, valinit= 40)
syH2 = Slider(ax_yH2, r'$y_{H2}$', 0,1, valinit=0.45)
syT = Slider(ax_yT, r'$y_{T0}$', 0, 1, valinit= 0.3)




def update_plot2(val):
    FTo = sFTo.val
    k =sk.val
    KT =sKT.val
    KB = sKB.val
    alpha =salpha.val
    Po = sPo.val
    yH2 = syH2.val
    yT = syT.val
    sol = odeint(ODEfun, y0, Wspan, (FTo, k, KT, KB, alpha, Po,yH2,yT))
    X = sol[:, 0]
    PTo = yT*Po 
    p = (1-alpha*Wspan)**0.5
    P = p*Po 
    ThetaH2=yH2/yT
    PH2 = PTo*(ThetaH2-X)*p 
    PB = PTo*X*p 
    PT = PTo*(1-X)*p 
    rt = -k*PT*PH2/(1+KB*PB+KT*PT) 
    RATE = -rt 

    p1.set_ydata(X)
    p2.set_ydata(p)
    p3.set_ydata(PH2)
    p4.set_ydata(PB)
    p5.set_ydata(PT)
    p6.set_ydata(RATE)    
    fig.canvas.draw_idle()


sFTo.on_changed(update_plot2)
sk.on_changed(update_plot2)
sKT.on_changed(update_plot2)
sKB.on_changed(update_plot2)
salpha.on_changed(update_plot2)
sPo.on_changed(update_plot2)
syH2.on_changed(update_plot2)
syT.on_changed(update_plot2)

#

resetax = plt.axes([0.37, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sFTo.reset()
    sk.reset()
    sKT.reset()
    sKB.reset()
    salpha.reset()
    sPo.reset()
    syH2.reset()
    syT.reset()
	
button.on_clicked(reset)
    
