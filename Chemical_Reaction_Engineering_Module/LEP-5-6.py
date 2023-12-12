#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
Cao = 0.1
mu = 0.1
Po = 1013
rhoc = 1923
vo = 7.15
MW = 65.5
gc = 1.296e7
Ac = 0.0013
voidfrac = 0.45
Dp = 0.006
k = 12
W = np.linspace(0, 27, 1000)
def func(Cao, voidfrac, Dp, Po, Ac, vo, k, MW):
    Fao = Cao*vo
    alphamax = (1 - 0.01)/27
    rho = Po*MW/(8.314*1206)
    G = MW*Fao/Ac
    Beta0 = (G*(1 - voidfrac)*((150*(1 - voidfrac)*mu/Dp) + 1.75*G)/(gc*rho*Dp*(voidfrac)**3))/1000
    alpha1 = 2*Beta0/(Ac*(1-voidfrac)*rhoc*Po)
    alpha = np.where(alpha1<alphamax, alpha1, alphamax)
    p = (1 - alpha*W)**0.5
    a = (k*Cao*W/vo)*(1 - alpha*W/2)
    X = a/(1+a)
    return np.array([p, X])

#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 5 - 6 Robert Worries what if...""", fontweight='bold', x = 0.15, y= 0.98)

plt.subplots_adjust(left  = 0.5)

sol = func(Cao, voidfrac, Dp, Po, Ac, vo, k, MW)
p = sol[0, :]
X = sol[1, :]


p1, p2 = plt.plot(W, p, W, X)
plt.legend(['Pressure ratio', 'Conversion'], loc='upper right')
plt.xlabel('Catalyst Weight (kg)', fontsize='medium', fontweight='bold')
plt.ylabel('X, p', fontsize='medium', fontweight='bold')
plt.ylim(0,1.1)
plt.xlim(0,27)
plt.grid()


plt.text(-32.5, -0.05,
                  
         'Explicit Equations'
                  '\n\n'
         r'$\mu = 0.1$'
                 '\n\n'
         r'$\rho_c = 1923$'   
         '\n\n'
         r'$g_c = 1.296*10^7$'
                  '\n\n'
         r'$C_{A0} = 0.1$'
          '\n\n'
          r'$MW = 65.5$'
          '\n\n'
          r'$\phi = 0.45$'
          '\n\n'
         r'$F_{A0} = C_{A0}*v_0$'
                  '\n\n'      
         r'$\alpha_{max} = \dfrac{1 - 0.01}{27}$'
                  '\n\n'                  
         r'$\rho_o = \dfrac{P_0 MW}{8.314*1206}$'
                  '\n\n'                  
         r'$G = \dfrac{MW F_{A0}}{A_c}$'
                  '\n\n'                  
         r'$\beta_o = \dfrac{G(1-\phi)}{1000 g_c \rho_o D_p (\phi)^3}\left[\dfrac{150(1-\phi)\mu}{D_p} + 1.75G\right]$'
         '\n\n'
         r'$\alpha_1 = \dfrac{2 \beta_0}{A_c(1-\phi)\rho_c P_o}$'
         '\n\n'
         r'$\alpha = IF(\alpha_1 < \alpha_{max}) then (\alpha_1) else (\alpha_{max})$'
         '\n\n'
         r'$p = \sqrt{1-\alpha W}$' 
        '\n\n'
         r'$X = \dfrac{\left(kC_{A0}\dfrac{W}{v_0}\right)\left(1 - \alpha \dfrac{W}{2}\right)}{1+\left(kC_{A0}\dfrac{W}{v_0}\right)\left(1 - \alpha \dfrac{W}{2}\right)}$'
         '\n'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'

ax_Dp = plt.axes([0.28, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_Po = plt.axes([0.28, 0.70, 0.15, 0.02], facecolor=axcolor)
ax_Ac = plt.axes([0.28, 0.65, 0.15, 0.02], facecolor=axcolor)
ax_vo = plt.axes([0.28, 0.60, 0.15, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.28, 0.55, 0.15, 0.02], facecolor=axcolor)

sDp= Slider(ax_Dp, r'$D_p$ (m)', 0.0006, 1, valinit=0.006)
sPo = Slider(ax_Po, r'$P_o (kPa)$', 101.325, 10000, valinit=1013,valfmt = '%1.0f')
sAc = Slider(ax_Ac, r'$A_c (m^2)$', 0.001, 0.005, valinit=0.0013, valfmt = '%1.4f')
svo = Slider(ax_vo, r'$v_o (\frac{m^3}{h})$', 1,30, valinit= 7.15)
sk = Slider(ax_k, r'$k (\frac{m^6}{kmol.kgcat.h})$', 1, 40, valinit=12)

def update_plot2(val):
    Dp =sDp.val
    Po = sPo.val
    Ac =sAc.val
    vo = svo.val
    k = sk.val
    sol = func(Cao, voidfrac, Dp, Po, Ac, vo, k, MW)
    p = sol[0, :]
    X = sol[1, :]
    p1.set_ydata(p)
    p2.set_ydata(X)
    fig.canvas.draw_idle()


sDp.on_changed(update_plot2)
sPo.on_changed(update_plot2)
sAc.on_changed(update_plot2)
svo.on_changed(update_plot2)
sk.on_changed(update_plot2)
#
resetax = plt.axes([0.31, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sDp.reset()
    sPo.reset()
    sAc.reset()
    svo.reset()
    sk.reset()
button.on_clicked(reset)
    
