#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
k1 =1.485  
k2 =0.1485 
k3 =0.00891
k5 =0.00111
Qy = 12964 # quantum yield (overall height)
def ODEfun(Yfuncvec, t, k1, k2, k3, k5, Qy): 
    Ca= Yfuncvec[0]
    Cb= Yfuncvec[1]
    Cc= Yfuncvec[2]
    Cd= Yfuncvec[3]
    Ce= Yfuncvec[4]
    Ch= Yfuncvec[5]
    Cf= Yfuncvec[6]
    Ck= Yfuncvec[7]
    r5 =k5*Ck     
    r3 = k3*Cf*Ce
    rEMIT =r3*Qy  #light as a function of time
    r1 = k1*Ca*Cb   
    r2 = k2*Cd   
    # Differential equations
    dCadt = -r1 # tcpo
    dCbdt = -r1  # h2o2
    dCcdt = (r1+r2)# PhOH
    dCddt = (r1-r2) # peroxyacid
    dCedt = (r2-r3) # 1,2-dioxetanedione
    dChdt =  2*r3# CO2
    dCfdt =  r5-r3# dye
    dCkdt =  r3-r5 # complex
    return np.array([dCadt, dCbdt, dCcdt, dCddt, dCedt, dChdt, dCfdt, dCkdt])


tspan = np.linspace(0, 50, 1000)
tspan2 = np.linspace(0, 3600, 10000)
y0 = np.array([0.7,0.8,0,0,0,0,0.0005,0])


#%%
fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle("""Example Web module : Glowsticks""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, tspan, (k1, k2, k3, k5, Qy))
sol2 = odeint(ODEfun, y0, tspan2, (k1, k2, k3, k5, Qy))
Ca= sol[:, 0]
Cb= sol[:, 1]
Cc= sol[:, 2]
Cd= sol[:, 3]
Ce= sol[:, 4]
Ce2= sol2[:, 4]
Ch= sol[:, 5]
Cf= sol[:, 6]
Cf2= sol2[:, 6]
Ck= sol[:, 7]
r3 = k3*Cf2*Ce2
rEMIT =r3*Qy

p1, p2, p3, p4, p5, p6, p7, p8 = ax1.plot(tspan, odeint(ODEfun, y0, tspan, (k1, k2, k3, k5, Qy)))
ax1.legend(["$C_A$","$C_B$","$C_C$","$C_D$","$C_E$","$C_H$","$C_F$","$C_K$",], loc='best')
ax1.set_xlabel('time (sec)', fontsize='medium')
ax1.set_ylabel(r'$Concentration (mol/dm^3)$', fontsize='medium')
ax1.set_ylim(0,1.5)
ax1.set_xlim(0,50)
ax1.grid()

p9 = ax2.plot(tspan2, rEMIT)[0]
ax2.legend(["rEMIT"], loc='best')
ax2.set_xlabel('time (sec)', fontsize='medium')
ax2.set_ylabel('Absorbance', fontsize='medium')
ax2.set_ylim(0,0.09)
ax2.set_xlim(0,3600)
ax2.grid()
ax1.text(-26, -2.2,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dt} = -r_1$'
                  '\n'
         r'$\dfrac{dC_B}{dt} = -r_1$'
                  '\n'
         r'$\dfrac{dC_C}{dt} = r_1 + r_2$'
                  '\n'
         r'$\dfrac{dC_D}{dt} = r_1 - r_2$'
                  '\n'   
         r'$\dfrac{dC_E}{dt} = r_2 - r_3$'
                  '\n'
         r'$\dfrac{dC_H}{dt} = 2r_3$'
                  '\n'
         r'$\dfrac{dC_F}{dt} = r_5 - r_3$'
                  '\n'
         r'$\dfrac{dC_K}{dt} = -r_5 + r_3$'
                  '\n\n'                   
         'Explicit Equations'
                  '\n\n'
         r'$r_3 = k_3C_F*C_E$'
         '\n'         
         r'$r_1 = k_1C_A*C_B$'
         '\n'
         r'$r_2 = k_2*C_D$'
         '\n'
         r'$r_{EMIT} = r_3.QY$'
         '\n'
         r'$r_5 = k_5C_K$'         
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_k1 = plt.axes([0.09, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.09, 0.76, 0.2, 0.02], facecolor=axcolor)
ax_k3 = plt.axes([0.09, 0.72, 0.2, 0.02], facecolor=axcolor)
ax_k5 = plt.axes([0.09, 0.68, 0.2, 0.02], facecolor=axcolor)
ax_Qy = plt.axes([0.09, 0.64, 0.2, 0.02], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1 (\frac{dm^3}{mol.s})$', 0.05, 5, valinit=1.485, valfmt = '%1.3f')
sk2 = Slider(ax_k2, r'$k_2 \left(\frac{1}{s^{-1}}\right)$', 0.005, 0.5, valinit=0.1485, valfmt = '%1.4f')
sk3 = Slider(ax_k3, r'$k_3 (\frac{dm^3}{mol.s})$', 0.000001, 0.9, valinit=0.00891, valfmt = '%1.5f')
sk5 = Slider(ax_k5, r'$k_5 \left(\frac{1}{s^{-1}}\right)$',0.0005, 0.9, valinit= 0.00111, valfmt = '%1.5f')
sQy = Slider(ax_Qy, r'$QY$', 5000, 20000, valinit=12964, valfmt = '%1.0f')


def update_plot2(val):
    k1 = sk1.val
    k2 = sk2.val
    k3 =sk3.val
    k5 = sk5.val
    Qy = sQy.val
    sol = odeint(ODEfun, y0, tspan, (k1, k2, k3, k5, Qy))
    Ca= sol[:, 0]
    Cb= sol[:, 1]
    Cc= sol[:, 2]
    Cd= sol[:, 3]
    Ce= sol[:, 4]
    Ce2= sol2[:, 4]
    Ch= sol[:, 5]
    Cf= sol[:, 6]
    Cf2= sol2[:, 6]
    Ck= sol[:, 7]
    r3 = k3*Cf2*Ce2
    rEMIT =r3*Qy
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(Cd)
    p5.set_ydata(Ce)
    p6.set_ydata(Ch)
    p7.set_ydata(Cf)
    p8.set_ydata(Ck)
    p9.set_ydata(rEMIT)    
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
sk5.on_changed(update_plot2)
sQy.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
    sk5.reset()
    sQy.reset()
button.on_clicked(reset)
    
