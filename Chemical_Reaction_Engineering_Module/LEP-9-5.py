#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button
#%%
#Explicit Equations
kd = 0.01
Ysc = 12.5
Ypc = 5.6
Ks = 33.5
m = 0.03
umax = 0.46
Cso = 250
Cco = 1
def ODEfun(Yfuncvec, t, kd, Ysc, Ypc, Ks, m, umax):
    Cc= Yfuncvec[0]
    Cs= Yfuncvec[1]
    Cp= Yfuncvec[2]
    #Explicit Equation Inline
    rd = Cc*kd
    rsm = m*Cc
    kobs = umax*(1-Cp/93)**(0.52)
    rg = kobs*Cc*Cs/(Ks+Cs)
    
    #Differential Equations
    dCcdt = rg-rd
    dCsdt = Ysc*(-rg) - rsm
    dCpdt = rg*Ypc
    return np.array([dCcdt, dCsdt, dCpdt])

tspan = np.linspace(0, 12, 1000)
y0 = np.array([1, 250, 0])

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.4)
fig.suptitle("""Example 9-5 Bacteria Growth in a Batch Reactor""", x = 0.22, y=0.98, fontweight='bold')
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, tspan, (kd, Ysc, Ypc, Ks, m, umax))
Cc= sol[:, 0]
Cs= sol[:, 1]
Cp= sol[:, 2]
kobs = umax*(1-Cp/93)**(0.52)
rd = Cc*kd
rsm = m*Cc
kobs = umax*(1-Cp/93)**(0.52)
rg = kobs*Cc*Cs/(Ks+Cs)

p1 = ax1.plot(tspan, Cc)[0]
ax1.legend([r'C$_c$'], loc='lower right')
ax1.set_xlabel('time (hr)', fontsize='medium')
ax1.set_ylabel(r'C$_c (g/dm^3)$ ', fontsize='medium')
ax1.set_ylim(0,20)
ax1.set_xlim(0,12)
ax1.grid()

p2, p3 = ax2.plot(tspan, Cs, tspan, Cp)
ax2.legend([r'C$_s$', r'C$_p$'], loc='upper right')
ax2.set_ylim(0,250)
ax2.set_xlim(0,12)
ax2.grid()
ax2.set_xlabel('time (hr)', fontsize='medium')
ax2.set_ylabel(r'$Concentration (g/dm^3)$ ', fontsize='medium')

p4 = ax3.plot(tspan, kobs)[0]
ax3.legend([r'k$_{obs}$'], loc='upper right')
ax3.set_ylim(0,0.5)
ax3.set_xlim(0,12)
ax3.grid()
ax3.set_xlabel('time (hr)', fontsize='medium')
ax3.set_ylabel(r'k$_{obs} (hr^{-1})$', fontsize='medium')

p5, p6, p7 = ax4.plot(tspan, rg, tspan, rsm, tspan, rd)
ax4.legend([r'r$_g$', r'r$_{sm}$', r'r$_d$'], loc='upper right')
ax4.set_ylim(0,6)
ax4.set_xlim(0,12)
ax4.grid()
ax4.set_xlabel('time (hr)', fontsize='medium')
ax4.set_ylabel(r'Rates ($g/(dm^3.hr)$)', fontsize='medium')

ax1.text(-13, -26,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = r_g - r_d$'
                  '\n \n'
         r'$\dfrac{dC_S}{dt} = Y_{s/c}(-r_g) - r_{sm}$'
                  '\n \n'
         r'$\dfrac{dC_P}{dt} = Y_{p/c}r_g$'
                  '\n \n'                  
         'Explicit Equations'
                  '\n\n'
         r'$r_d = k_d*C_C$'
         '\n\n'         
         r'$r_{sm} = m*C_C$'
         '\n\n'
         r'$K_{obs} = u_{max}\left(1-\dfrac{C_P}{93}\right)^{0.52}$'
         '\n\n'
         r'$r_g = \dfrac{K_{obs}*C_C*C_S}{(K_S + C_S)}$'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')

#%%
axcolor = 'black'
ax_kd = plt.axes([0.1, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_Ysc = plt.axes([0.1, 0.79, 0.2, 0.015], facecolor=axcolor)
ax_Ypc = plt.axes([0.1, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_Ks = plt.axes([0.1, 0.73, 0.2, 0.015], facecolor=axcolor)
ax_m = plt.axes([0.1, 0.70, 0.2, 0.015], facecolor=axcolor)
ax_umax = plt.axes([0.1, 0.67, 0.2, 0.015], facecolor=axcolor)

skd = Slider(ax_kd, r'$k_d (h^{-1})$', 0, 0.1, valinit=.01,valfmt='%1.2f')
sYsc= Slider(ax_Ysc, r'$Y_{s/c} (\frac{g}{g})$', 12.4, 30., valinit=12.5,valfmt='%1.1f')
sYpc = Slider(ax_Ypc, r'$Y_{p/c} (\frac{g}{g})$', 1, 5.6, valinit=5.6)
sKs = Slider(ax_Ks, r'$K_s (\frac{g}{dm^3}) $', 33.5, 200, valinit=33.5,valfmt='%1.1f')
sm = Slider(ax_m, r'$m (g/g.hr)$', 0.01, 0.5, valinit= 0.03,valfmt='%1.2f')
sumax = Slider(ax_umax, r'$u_{max} (h^{-1})$', 0.1, 0.47, valinit=0.46)


def update_plot2(val):
    kd = skd.val
    Ysc =sYsc.val
    Ypc = sYpc.val
    Ks =sKs.val
    m = sm.val
    umax = sumax.val
    sol = odeint(ODEfun, y0, tspan, (kd, Ysc, Ypc, Ks, m, umax))
    Cc= sol[:, 0]
    Cs= sol[:, 1]
    Cp= sol[:, 2]
    kobs = umax*(1-Cp/93)**(0.52)
    rd = Cc*kd
    rsm = m*Cc
    kobs = umax*(1-Cp/93)**(0.52)
    rg = kobs*Cc*Cs/(Ks+Cs)
    p1.set_ydata(Cc)
    p2.set_ydata(Cs)
    p3.set_ydata(Cp)
    p4.set_ydata(kobs)
    p5.set_ydata(rg)
    p6.set_ydata(rsm)
    p7.set_ydata(rd)
    fig.canvas.draw_idle()


skd.on_changed(update_plot2)
sYsc.on_changed(update_plot2)
sYpc.on_changed(update_plot2)
sKs.on_changed(update_plot2)
sm.on_changed(update_plot2)
sumax.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.87, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    skd.reset()
    sYsc.reset()
    sYpc.reset()
    sKs.reset()
    sm.reset()
    sumax.reset()
button.on_clicked(reset)
    
