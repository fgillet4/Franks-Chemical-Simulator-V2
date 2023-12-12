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
kf = 7.2e7
kr = .34
keR = .03
keC = .165
krec = .058
kdeg = .0022
Vs = .013
fR = .5
fL = .5
L = 1e-8
Navgo = 6.02e23
kfP = 0
def ODEfun(Yfuncvec, t, kf, kr,keR, keC, krec,
           kdeg, fR, fL, L, kfP): 
    Rs= Yfuncvec[0]
    RTi= Yfuncvec[1]
    Cs= Yfuncvec[2]
    LTi= Yfuncvec[3]
    # Differential equations
    dRsdt = -kf*Rs*L+kr*Cs-keC*Rs+(krec*(1-fR)*RTi)+Vs
    dRTidt = keR*Rs+keC*Cs-(krec*(1-fR)*RTi)-kdeg*fR*RTi
    dCsdt = kf*L*Rs-kr*Cs-keC*Cs
    dLTidt = keC*Cs+kfP*L*Navgo-(krec*(1-fL)*LTi)-kdeg*fR*RTi
    return np.array([dRsdt,dRTidt,dCsdt,dLTidt])




tspan = np.linspace(0, 50, 1000) # Range for the independent variable
y0 = np.array([5e4, 0, 0, 0]) # Initial values for the dependent variables

#%%
fig, ax = plt.subplots()
fig.suptitle("""PRS-9-5 Receptor Kinetics : Endocytosis""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, tspan, (kf, kr,keR, keC, krec,
                                 kdeg, fR, fL, L, kfP))
Rs= sol[:,0]
RTi= sol[:,1]
Cs= sol[:,2]
LTi= sol[:,3]

p1, p2, p3, p4 = plt.plot(tspan, Rs, tspan, RTi,tspan,Cs,
                                  tspan, LTi)
plt.legend([r"Surface Receptors, $R_S$", r"Internal Receptors, $R_{Ti}$", r"Surface complexes, $C_S$", r"Internal Ligands, $L_{Ti}$"], loc='best')
ax.set_xlabel('Time (min)', fontsize='medium')
ax.set_ylabel('Concentration (M)', fontsize='medium')
plt.ylim(0,50000)
plt.xlim(0,50)
plt.grid()

plt.text(-30, 2500,'Differential Equations'
         '\n\n'
         r'$\dfrac{dR_S}{dt} = -k_fR_SL+k_rC_S - k_{eC}R_S+K_{rec}(1-f_R)R_{Ti}+V_S$'
                  '\n \n'
         r'$\dfrac{dR_{Ti}}{dt} = k_{eR}R_S + k_{eC}C_S - k_{rec}(1-f_R)R_{Ti} - k_{deg}f_RR_{Ti}$'
                  '\n \n'
         r'$\dfrac{dC_S}{dt} = k_fLR_S - k_rC_S - k_{eC}C_S$'
                  '\n \n'   
         r'$\dfrac{dC_S}{dt} = k_{eC}C_S + k_{fP}LN_{avgo} - k_{rec}(1-f_R)L_{Ti} - k_{deg}f_RR_{Ti}$'
                  '\n \n'                     
         'Explicit Equations'
                  '\n\n'
         r'$N_{avgo} = 6.02*10^{23}$'
                  '\n\n'
         r'$V_S = 0.013$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_kf = plt.axes([0.1, 0.85, 0.2, 0.02], facecolor=axcolor)
ax_kr = plt.axes([0.1, 0.82, 0.2, 0.02], facecolor=axcolor)
ax_keR = plt.axes([0.1, 0.79, 0.2, 0.02], facecolor=axcolor)
ax_keC = plt.axes([0.1, 0.76, 0.2, 0.02], facecolor=axcolor)
ax_krec = plt.axes([0.1, 0.73, 0.2, 0.02], facecolor=axcolor)
ax_kdeg = plt.axes([0.1, 0.70, 0.2, 0.02], facecolor=axcolor)
ax_fR = plt.axes([0.1, 0.67, 0.2, 0.02], facecolor=axcolor)
ax_fL = plt.axes([0.1, 0.64, 0.2, 0.02], facecolor=axcolor)
ax_L = plt.axes([0.1, 0.61, 0.2, 0.02], facecolor=axcolor)
ax_kfP = plt.axes([0.1, 0.58, 0.2, 0.02], facecolor=axcolor)

skf = Slider(ax_kf, r'$k_{f} (M^{-1}.min^{-1})$', 1.2e7, 1.22e8, valinit=7.2e7,valfmt='%1.0f')
skr= Slider(ax_kr, r'$k_{r} (min^{-1})$', 0.05, 1, valinit=0.34)
skeR = Slider(ax_keR, r'$k_{eR} (min^{-1})$', 0.005, 0.2, valinit=0.03,valfmt='%1.2f')
skeC = Slider(ax_keC, r'$k_{eC} (min^{-1})$', 0.01, 0.5, valinit=0.165,valfmt='%1.3f')
skrec = Slider(ax_krec, r'$k_{rec} (min^{-1})$', 0.01, 0.2, valinit= 0.058,valfmt='%1.3f')
skdeg = Slider(ax_kdeg, r'$k_{deg} (min^{-1})$', 0.0005, 0.02, valinit=0.0022,valfmt='%1.4f')
sfR = Slider(ax_fR, r'$f_{R}$', 0.02, 1., valinit=.5)
sfL = Slider(ax_fL, r'$f_{L}$', 0.02, 1, valinit=.5)
sL = Slider(ax_L, r'$L (\frac{mol}{dm^3})$', 2e-9, 3e-8, valinit=1e-8,valfmt='%1.2E')
skfP = Slider(ax_kfP, r'$k_{fP} (min^{-1})$', 0, 0.2, valinit=0,valfmt='%1.2f')


def update_plot2(val):
    kf = skf.val
    kr =skr.val
    keR = skeR.val
    keC =skeC.val
    krec = skrec.val
    kdeg = skdeg.val
    fR = sfR.val
    fL = sfL.val
    L = sL.val
    kfP = skfP.val
    sol = odeint(ODEfun, y0, tspan, (kf, kr,keR, keC, krec,
                                     kdeg, fR, fL, L, kfP))
    Rs= sol[:,0]
    RTi= sol[:,1]
    Cs= sol[:,2]
    LTi= sol[:,3]
    p1.set_ydata(Rs)
    p2.set_ydata(RTi)
    p3.set_ydata(Cs)
    p4.set_ydata(LTi)
    fig.canvas.draw_idle()


skf.on_changed(update_plot2)
skr.on_changed(update_plot2)
skeR.on_changed(update_plot2)
skeC.on_changed(update_plot2)
skrec.on_changed(update_plot2)
skdeg.on_changed(update_plot2)
sfR.on_changed(update_plot2)
sfL.on_changed(update_plot2)
sL.on_changed(update_plot2)
skfP.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    skf.reset()
    skr.reset()
    skeR.reset()
    skeC.reset()
    skrec.reset()
    skdeg.reset()
    sfR.reset()
    sfL.reset()
    sL.reset()
    skfP.reset()
button.on_clicked(reset)
    
