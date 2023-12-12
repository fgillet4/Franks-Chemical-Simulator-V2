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
kv =5e8# Rate constant for adsorption of venom in muscle compartment (L/mol hr)
Ct =2.2e-9#Total concentration of sites
vm =9.3#Blood flow from muscle compartment to central compartment (L/hr)
Vm =1.35#Tissue water volume of muscle compartment (L)
Vc =.665# Tissue water volume of central compartment (L)
ve =6.3e-3#Elimination flow rate (L/hr)

def ODEfun(Yfuncvec, t, kv, Ct, vm, Vm, Vc, ve):
    Cvm = Yfuncvec[0]
    fvs = Yfuncvec[1]
    Cvc = Yfuncvec[2]
    # Explicit equations Inline
    fs =1-fvs# Fraction of free sites in muscle compartment
    Cs =fs*Ct# Concentration of free sites  
    # Differential equations
    dCvmdt = (vm/Vm)*(Cvc-Cvm)-kv*Cvm*Cs#Venom concentration in muscle compartment
    dfvsdt = kv*fs*Cvm#Fraction of sites occupied by venom in muscle compartment
    dCvcdt = (vm/Vc)*(Cvm-Cvc)-(ve/Vc)*Cvc#Venom concentration in central compartment
    return np.array([dCvmdt, dfvsdt, dCvcdt])

tspan = np.linspace(0, 8, 100)
y0 = np.array([0, 0, 6.79e-9])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Cobra bite problem : Venon only""", fontweight='bold', x = 0.25, y=0.98)
plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (kv, Ct, vm, Vm, Vc, ve))
Cvm = sol[:, 0]
fvs = sol[:, 1]
Cvc = sol[:, 2]
fs =1-fvs


p1 = plt.plot(tspan, fs)[0]
plt.legend([r'$f_s$'], loc='upper right')
ax.set_xlabel('time (hr)', fontsize='medium', fontweight='bold')
ax.set_ylabel('fs', fontsize='medium', fontweight='bold')
#plt.title('X and Xe Profile')
plt.ylim(0,1)
plt.xlim(0,8)
plt.grid()

ax.text(-6.2, 0.02,'Differential Equations'
         '\n\n'
         r'$\dfrac{df_{vs}}{dt} = k_Vf_SC_{VM} $'
                  '\n\n'
         r'$\dfrac{dC_{VM}}{dt} = \dfrac{v_m(C_{VC} - C_{VM})}{V_m} - k_VC_{VM}C_S$'
                  '\n\n'
         r'$\dfrac{dC_{VC}}{dt} = \dfrac{v_m(C_{VM} - C_{VC})}{V_C} - \dfrac{v_eC_{VC}}{V_C}$'
         '\n\n'
         'Explicit Equations' '\n\n'
         r'$f_S = 1 - f_{VS}$' '\n\n'
         r'$C_S = f_S.C_T$'
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')

#%%
axcolor = 'black'
ax_kv = plt.axes([0.1, 0.8, 0.3, 0.02], facecolor=axcolor)
ax_Ct = plt.axes([0.1, 0.75, 0.3, 0.02], facecolor=axcolor)
ax_vm = plt.axes([0.1, 0.7, 0.3, 0.02], facecolor=axcolor)
ax_Vm = plt.axes([0.1, 0.65, 0.3, 0.02], facecolor=axcolor)
ax_Vc = plt.axes([0.1, 0.6, 0.3, 0.02], facecolor=axcolor)
ax_ve = plt.axes([0.1, 0.55, 0.3, 0.02], facecolor=axcolor)

skv = Slider(ax_kv, r'k$_V (\frac{L}{mol.hr})$', 5e7, 5e8, valinit=2e8, valfmt="%1.2E")
sCt= Slider(ax_Ct, r'$C_T (\frac{mol}{L})$', 2e-10, 5.2e-9, valinit=2.2e-9, valfmt="%1.2E")
svm = Slider(ax_vm, r'v$_{m} (\frac{L}{hr})$', 2, 20, valinit=9.3)
sVm = Slider(ax_Vm, r'V$_{m} (L)$', 0.5, 5, valinit=1.35)
sVc = Slider(ax_Vc, r'V$_{C} (L)$', 0.04, 1, valinit= 0.665)
sve = Slider(ax_ve, r'v$_e (\frac{L}{hr})$', 0.0023, 0.0092, valinit=6.3e-3, valfmt="%1.4f")


def update_plot2(val):
    kv = skv.val
    Ct =sCt.val
    vm = svm.val
    Vm =sVm.val
    Vc = sVc.val
    ve = sve.val
    sol = odeint(ODEfun, y0, tspan, (kv, Ct, vm, Vm, Vc, ve))
    fvs = sol[:, 1]
    fs =1-fvs
    p1.set_ydata(fs)
    fig.canvas.draw_idle()


skv.on_changed(update_plot2)
sCt.on_changed(update_plot2)
svm.on_changed(update_plot2)
sVm.on_changed(update_plot2)
sVc.on_changed(update_plot2)
sve.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    skv.reset()
    sCt.reset()
    svm.reset()
    sVm.reset()
    sVc.reset()
    sve.reset()
button.on_clicked(reset)

