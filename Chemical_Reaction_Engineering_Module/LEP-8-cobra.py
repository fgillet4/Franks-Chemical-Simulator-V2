#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
kv = 3e9
ksv =6e8
ka = 2e8
kia = 1
Cso = 5e-9
ksa = 6e8
kp =  1.2e9
kov = 0
koa = 0.3
kop = 0.3

def ODEfun(Yfuncvec, t, kv, ksv, ka, kia, Cso, ksa, kp, kov, koa, kop): 
    fsv = Yfuncvec[0]
    fs = Yfuncvec[1]
    Cv = Yfuncvec[2]
    Ca = Yfuncvec[3]
    fsa = Yfuncvec[4]
    Cp = Yfuncvec[5]
    # Explicit equations Inline
    g =   ksa * fsa * Cv + ksv * fsv * Ca   
    h =   -kp * Cv * Ca - kov * Cv  
    m =   kp * Cv * Ca - kop * Cp  
    j =   -Cso * ksv * fsv * Ca - kp * Cv * Ca - koa * Ca 
    # Differential equations
    dfsvdt =   kv * fs * Cv - ksv * fsv * Ca
    dfsdt =  -kv*fs*Cv - ka * fs * Ca + kia * fsa + g
    dCvdt =  Cso * (-kv * fs * Cv - ksa * fsa * Cv) + h
    dCadt =   Cso*(-ka * fs * Ca + kia * fsa) + j
    dfsadt =   ka * fs * Ca - kia * fsa - ksa * fsa * Cv
    dCpdt =   Cso * (ksv * fsv * Ca + ksa * fsa * Cv) + m
    return np.array([dfsvdt, dfsdt, dCvdt, dCadt, dfsadt, dCpdt])
    
tspan = np.linspace(0, 0.5, 100)
y0 = [0, 1, 5e-9, 0, 0, 0]


#%%
fig, ax = plt.subplots()
fig.suptitle("""Cobra bite problem : Single compartment""", fontweight='bold', x = 0.22, y=0.96)
plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (kv, ksv, ka, kia, Cso, 
                                 ksa, kp, kov, koa, kop))
fsv = sol[:, 0]
fs = sol[:, 1]
Cv = sol[:, 2]
Ca = sol[:, 3]
fsa = sol[:, 4]
Cp = sol[:, 5]


p1,p2 = plt.plot(tspan, fs,tspan,fsv)
plt.legend([r'$f_S$',r'$f_{SV}$'], loc='upper right')
ax.set_xlabel('time (hr)', fontsize='medium', fontweight='bold')
ax.set_ylabel('fraction', fontsize='medium', fontweight='bold')
#plt.title('X and Xe Profile')
plt.ylim(0,1)
plt.xlim(0,0.5)
plt.grid()
plt.title('No Antivenon given')

ax.text(-0.5, -0.04,'Differential Equations'
         '\n'
         r'$\dfrac{df_{sv}}{dt} = k_Vf_sC_V - k_{SV}f_{SV}C_A$'
                  '\n'
         r'$\dfrac{df_S}{dt} = -k_Vf_sC_V - k_Af_SC_A + k_{IA}f_{SA} + g$'
         '\n'
         r'$\dfrac{dC_V}{dt} = C_{SO}(-k_Vf_sC_V - k_{SA}f_{SA}C_V) + h$'
                  '\n'
         r'$\dfrac{dC_A}{dt} = C_{SO}(-k_Af_SC_A + k_{IA}f_{SA}) + j$'         '\n'
         r'$\dfrac{df_{SA}}{dt} = k_A*f_S*C_A - k_{IA}f_{SA} - k_{SA}f_{SA}C_V$'
                  '\n'
         r'$\dfrac{dC_P}{dt} = C_{SO}(k_{SV}f_{SV}C_A + k_{SA}f_{SA}C_V)$'
         '\n\n'
         'Explicit Equations' '\n\n'
         r'$g = k_{SA}*f_{SA}*C_V + k_{SV}*f_{SV}*C_A$' '\n'
         r'$h = -k_P*C_V*C_A - k_{OV}*C_V$' '\n'
         r'$m = k_P*C_V*C_A - k_{OP}*C_P$' '\n'
         r'$j = - C_{SO}*k_{SV}*f_{SV}*C_A - k_P*C_V*C_A - k_{OA}*C_A $'
        , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')
#%%

axcolor = 'black'
ax_kv = plt.axes([0.08, 0.85, 0.3, 0.015], facecolor=axcolor)
ax_ksv = plt.axes([0.08, 0.82, 0.3, 0.015], facecolor=axcolor)
ax_ka = plt.axes([0.08, 0.79, 0.3, 0.015], facecolor=axcolor)
ax_kia = plt.axes([0.08, 0.76, 0.3, 0.015], facecolor=axcolor)
ax_Cso = plt.axes([0.08, 0.73, 0.3, 0.015], facecolor=axcolor)
ax_ksa = plt.axes([0.08, 0.70, 0.3, 0.015], facecolor=axcolor)
ax_kp = plt.axes([0.08, 0.67, 0.3, 0.015], facecolor=axcolor)
ax_kov = plt.axes([0.08, 0.64, 0.3, 0.015], facecolor=axcolor)
ax_koa = plt.axes([0.08, 0.61, 0.3, 0.015], facecolor=axcolor)
ax_kop = plt.axes([0.08, 0.58, 0.3, 0.015], facecolor=axcolor)

skv = Slider(ax_kv, r'k$_V (\frac{dm^3}{mol.hr})$', 0.5e8, 8e9, valinit=3e9,  valfmt="%1.1E")
sksv= Slider(ax_ksv, r'k$_{SV} (\frac{dm^3}{mol.hr})$', 1e8, 1e9, valinit=6e8, valfmt="%1.1E")
ska = Slider(ax_ka, r'k$_A (\frac{dm^3}{mol.hr})$', 5e7, 5e8, valinit=2e8, valfmt="%1.1E")
skia = Slider(ax_kia, r'k$_{iA} (hr^{-1})$', 0.2, 5, valinit=1)
sCso = Slider(ax_Cso, r'C$_{S0} (\frac{mol}{dm^3})$', 1e-9, 1e-8, valinit= 5e-9, valfmt="%1.1E")
sksa = Slider(ax_ksa, r'k$_{SA} (\frac{dm^3}{mol.hr})$', 1e8, 1.1e9, valinit=6e8, valfmt="%1.1E")
skp = Slider(ax_kp, r'k$_{P} (\frac{dm^3}{mol.hr})$', 2e8, 7e9, valinit=1.2e9, valfmt="%1.1E")
skov = Slider(ax_kov, r'k$_{OV} (hr^{-1})$', 0, 5, valinit=0)
skoa = Slider(ax_koa, r'k$_{OA} (hr^{-1})$', 0.05, 0.8, valinit=0.3)
skop = Slider(ax_kop, r'k$_{OP} (hr^{-1})$', 0.05, 0.8, valinit=0.3)


def update_plot2(val):
    kv = skv.val
    ksv =sksv.val
    ka = ska.val
    kia =skia.val
    Cso = sCso.val
    ksa = sksa.val
    kp = skp.val
    kov = skov.val
    koa = skoa.val
    kop = skop.val
    sol = odeint(ODEfun, y0, tspan, (kv, ksv, ka, kia, Cso, 
                                     ksa, kp, kov, koa, kop))
    fsv = sol[:, 0]
    fs = sol[:, 1]
    Cv = sol[:, 2]
    Ca = sol[:, 3]
    fsa = sol[:, 4]
    Cp = sol[:, 5]
    p1.set_ydata(fs)
    p2.set_ydata(fsv)
    fig.canvas.draw_idle()


skv.on_changed(update_plot2)
sksv.on_changed(update_plot2)
ska.on_changed(update_plot2)
skia.on_changed(update_plot2)
sCso.on_changed(update_plot2)
sksa.on_changed(update_plot2)
skp.on_changed(update_plot2)
skov.on_changed(update_plot2)
skoa.on_changed(update_plot2)
skop.on_changed(update_plot2)
#

resetax = plt.axes([0.18, 0.88, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    skv.reset()
    sksv.reset()
    ska.reset()
    skia.reset()
    sCso.reset()
    sksa.reset()
    skp.reset()
    skov.reset()
    skoa.reset()
    skop.reset()
button.on_clicked(reset)

