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
k_a =4.5#Backward rate constant for antivenin adsorption in muscle compartment (1/hr)
ka =3e6#Forward rate constant for Antivenin Adsorption in muscle compartment (L/mol hr)
kv =5e8#Rate constant for adsorption of venom in muscle compartment (L/mol hr)
Ct = 2.2e-9#Total concentration of sites
kvs =1.8e7#Rate constant for reaction of antivenom with venom on site in muscle compartment (L/mol hr)
kas =14#Rate constant for reaction of venom with antivenin on site in muscle compartment (L/mol hr)
vm = 11.16#Blood flow from muscle compartment to central compartment (L/hr)
Vm = 1.62#Tissue water volume of muscle compartment (L)
Vc = .798#Tissue water volume of central compartment (L)
ve = 7.5e-3#Elimination flow rate (L/hr)
kpc = 8.6e4#Rate constant for formation of AV product in central compartment (L/mol hr)

def ODEfun(Yfuncvec, t, k_a, ka, kv, Ct, kvs, kas, vm, Vm, Vc, ve, kpc):  
    Cvm = Yfuncvec[0]
    Cam = Yfuncvec[1]
    Cavm = Yfuncvec[2]
    fvs= Yfuncvec[3]
    fas= Yfuncvec[4]
    Cvc= Yfuncvec[5]
    Cac= Yfuncvec[6]
    Cavc= Yfuncvec[7]
    Ka =ka/k_a#Equilibrium constant for antivenin adsorption reaction in muscle compartment
    fs =1-fvs-fas#Fraction of free sites in muscle compartment
    Cas =fas*Ct#Concentration of sites occupied by antivenin 
    Cs = fs*Ct#Concentration of free sites 
    
    # Differential equations
    dCvmdt =   (vm/Vm)*(Cvc-Cvm)-kv*Cvm*Cs-kas*Cvm*Cas#Venom concentration in muscle compartment
    dCamdt = (vm/Vm)*(Cac-Cam)-ka*(Cam*Cs-Cas/Ka)-kas*Cam*Cs#Antivenin concentration in muscle compartment
    dCavmdt=    (vm/Vm)*(Cavc-Cavm)+(Ct)*(kas*fas*Cvm+kvs*fvs*Cam)#Venom-antivenin product concentration in muscle compartment
    dfvsdt =     kv*fs*Cvm-kvs*fvs*Cam#Fraction of sites occupied by venom in muscle compartment
    dfasdt =     ka*(Cam*fs-fas/Ka)-kas*fas*Cvm#Fraction of sites occupied by antivenin in muscle compartment
    dCvcdt = (vm/Vc)*(Cvm-Cvc)-(ve/Vc)*Cvc-kpc*Cac*Cvc#Venom concentration in central compartment
    dCacdt = (vm/Vc)*(Cam-Cac)-(ve/Vc)*Cac-kpc*Cac*Cvc#Antivenin concentration in central compartment
    dCavcdt =     (vm/Vc)*(Cavm-Cavc)-(ve/Vc)*Cavc+kpc*Cac*Cvc#Venom-antivenin product concentration in central compartment
    return np.array([dCvmdt,dCamdt,dCavmdt,dfvsdt,dfasdt,dCvcdt,dCacdt,dCavcdt])



tspan = np.linspace(0, 18, 100)
y0 = np.array([0, 0, 0, 0, 0, 1.35e-8, 2.5e-8, 0])


#%%
fig, ax = plt.subplots()
fig.suptitle("""Cobra bite problem : Venon - Antivenon""", fontweight='bold', x = 0.25, y=0.98)
plt.subplots_adjust(left  = 0.5)

sol = odeint(ODEfun, y0, tspan, (k_a, ka, kv, Ct, kvs, 
                                 kas, vm, Vm, Vc, ve, kpc))
fvs= sol[:, 3]
fas= sol[:, 4]
fs = 1 - fvs - fas

p1 = plt.plot(tspan, fs)[0]
plt.legend([r'$f_s$'], loc='upper right')
ax.set_xlabel('time (hr)', fontsize='medium', fontweight='bold')
ax.set_ylabel('fs', fontsize='medium', fontweight='bold')
#plt.title('X and Xe Profile')
plt.ylim(0,1)
plt.xlim(0,18)
plt.grid()

ax.text(-21.5, 0.05,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_{VM}}{dt} = \dfrac{v_m(C_{VC} - C_{VM})}{V_m} - k_VC_{VM}C_S - k_{AS}C_{VM}C_{AS}$'
                  '\n\n'
         r'$\dfrac{dC_{AM}}{dT} = \dfrac{v_m(C_{AC} - C_{AM})}{V_m} - k_A(C_{AM}C_S - \dfrac{C_{AS}}{K_A}) - k_{AS}C_{AM}C_S$'
         '\n\n'
         r'$\dfrac{dC_{AVM}}{dT} = \dfrac{v_m(C_{AVC} - C_{AVM})}{V_m} + C_T(k_{AS}f_{AS}C_{VM} + k_{VS}f_{VS}C_{AM})$'
                  '\n\n'
         r'$\dfrac{df_{VS}}{dT} = k_Vf_SC_{VM} - k_{VS}f_{VS}C_{AM}$'
         '\n\n'
         r'$\dfrac{df_{AS}}{dT} = k_A(C_{AM}f_S - \dfrac{f_{AS}}{K_A}) - k_{AS}f_{AS}C_{VM}$'
                  '\n\n'
         r'$\dfrac{dC_{VC}}{dT} = \dfrac{v_m(C_{VM} - C_{VC})}{V_C} - \dfrac{v_eC_{VC}}{V_C} - k_{PC}C_{AC}C_{VC}$'
         '\n\n'
         r'$\dfrac{dC_{AC}}{dt} = \dfrac{v_m(C_{AM} - C_{AC}) }{V_C} - \dfrac{v_eC_{AC}}{V_C} - k_{PC}C_{AC}C_{VC}$'
                  '\n\n'
         r'$\dfrac{dC_{AVC}}{dT} = \dfrac{v_m(C_{AVM} - C_{AVC}) }{V_C} - \dfrac{v_eC_{AVC}}{V_C} + k_{PC}C_{AC}C_{VC}$'
         '\n\n'         
         'Explicit Equations' '\n\n'
         r'$f_S = 1 - f_{VS} - f_{AS}$' '\n\n'
         r'$K_A = \dfrac{k_A}{k_{_A}}$' '\n\n'
         r'$C_{AS} = f_{AS}C_T$' '\n\n'
         r'$C_S = f_SC_T$'
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=10), fontweight='bold')


#%%
# Slider Code
axcolor = 'black'
ax_k_a = plt.axes([0.3, 0.8, 0.12, 0.015], facecolor=axcolor)
ax_ka = plt.axes([0.3, 0.75, 0.12, 0.015], facecolor=axcolor)
ax_kv = plt.axes([0.3, 0.7, 0.12, 0.015], facecolor=axcolor)
ax_Ct = plt.axes([0.3, 0.65, 0.12, 0.015], facecolor=axcolor)
ax_kvs = plt.axes([0.3, 0.6, 0.12, 0.015], facecolor=axcolor)
ax_kas = plt.axes([0.3, 0.55, 0.12, 0.015], facecolor=axcolor)
ax_vm = plt.axes([0.3, 0.5, 0.12, 0.015], facecolor=axcolor)
ax_Vm = plt.axes([0.3, 0.45, 0.12, 0.015], facecolor=axcolor)
ax_Vc = plt.axes([0.3, 0.4, 0.12, 0.015], facecolor=axcolor)
ax_ve = plt.axes([0.3, 0.35, 0.12, 0.015], facecolor=axcolor)
ax_kpc = plt.axes([0.3, 0.3, 0.12, 0.015], facecolor=axcolor)


sk_a = Slider(ax_k_a, r'k$_{_A} (hr^{-1})$', 0.5, 10., valinit=4.5)
ska= Slider(ax_ka, r'k$_A (\frac{dm^3}{mol.hr})$', 500000., 9e6, valfmt="%1.0E")
skv = Slider(ax_kv, r'k$_V (\frac{dm^3}{mol.hr})$', 5e7, 1e9, valinit=5e8,valfmt="%1.0E")
sCt = Slider(ax_Ct, r'$C_T (\frac{mol}{dm^3})$', 2e-10, 7.2e-9, valinit=2.2e-9, valfmt="%1.0E")
skvs = Slider(ax_kvs, r'k$_{VS} (\frac{dm^3}{mol.hr})$', 8e6, 6.8e7, valinit=1.8e7,valfmt="%1.0E")
skas = Slider(ax_kas, r'k$_{SA} (\frac{dm^3}{mol.hr})$', 3, 20, valinit=14)
svm = Slider(ax_vm, r'v$_m (\frac{dm^3}{hr})$', 2, 25, valinit=11.16)
sVm = Slider(ax_Vm, r'V$_{m} (dm^3)$', 0.5, 8.5, valinit=1.62)
sVc = Slider(ax_Vc, r'V$_{C} (dm^3)$', 0.2, 2, valinit=0.798)
sve = Slider(ax_ve, r'v$_e (\frac{dm^3}{hr})$', 0.0025, 0.012, valinit=7.5e-3)
skpc = Slider(ax_kpc, r'k$_{PC} (\frac{dm^3}{mol.hr})$', 36000, 126000, valinit=8.6e4,valfmt="%1.0f")

def update_plot1(val):
    k_a = sk_a.val
    ka =ska.val
    kv = skv.val
    Ct =sCt.val
    kvs = skvs.val
    kas = skas.val
    vm = svm.val
    Vm = sVm.val
    Vc = sVc.val
    ve = sve.val
    kpc = skpc.val
    sol = odeint(ODEfun, y0, tspan, (k_a, ka, kv, Ct, kvs, 
                                     kas, vm, Vm, Vc, ve, kpc))
    fvs= sol[:, 3]
    fas= sol[:, 4]
    fs = 1 - fvs - fas
    p1.set_ydata(fs)
    fig.canvas.draw_idle()

sk_a.on_changed(update_plot1)
ska.on_changed(update_plot1)
skv.on_changed(update_plot1)
sCt.on_changed(update_plot1)
skvs.on_changed(update_plot1)
skas.on_changed(update_plot1)
svm.on_changed(update_plot1)
sVm.on_changed(update_plot1)
sVc.on_changed(update_plot1)
sve.on_changed(update_plot1)
skpc.on_changed(update_plot1)

resetax = plt.axes([0.3, 0.85, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk_a.reset()
    ska.reset()
    skv.reset()
    sCt.reset()
    skvs.reset()
    skas.reset()
    svm.reset()
    sVm.reset()
    sVc.reset()
    sve.reset()
    skpc.reset()
button.on_clicked(reset)
