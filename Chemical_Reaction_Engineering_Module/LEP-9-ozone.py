#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import ScalarFormatter

#%%
# Explicit equations
k1 =   1.03e-94  #Rates of reaction (cm3/molecule*s)
k2 =   5.92e-34     
k3 =   4.38e-26     
k4 =   1.22e-11     
k5 =   3.8e-11     
k6 =   2.16e-32     
k7 =   8.53e-15     
k8 =   6.51e-13     
k9 =   1.78e-14     
k10 =  1.05e-11     
k11 =  1e-18     
k12 =  1.18e-12    
k13 =  1.02e-12    
k14 =  1.06e-8  #*Assumed value, pending real value* 

def ODEfun(Yfuncvec, t, k1, k2, k3, k4,k5, k6, k7,
           k8, k9, k10, k11, k12, k13, k14): 
    O2= Yfuncvec[0]
    O= Yfuncvec[1]
    O3= Yfuncvec[2]
    Cl= Yfuncvec[3]
    ClO= Yfuncvec[4]
    Cl2O2= Yfuncvec[5]
    ClO2= Yfuncvec[6]
    NO= Yfuncvec[7]
    NO2=Yfuncvec[8]
    BrCl=Yfuncvec[9]
    Br=Yfuncvec[10]
    BrO=Yfuncvec[11]
    r1 =   k1*O2   # Rate Laws
    r2 =   k2*(O2)*(O)     
    r3 =   k3*(O3)     
    r4 =   k4*(O3)*(Cl)     
    r5 =   k5*(O)*(ClO)     
    r6 =   k6*(ClO)*(ClO)     
    r7 =   k7*(Cl2O2)     
    r8 =   k8*(ClO2)     
    r9 =   k9*(O3)*(NO)     
    r10 =  k10*(NO2)*(O)     
    r11 =  k11*(NO2)*(O3)     
    r12 =  k12*(Br)*(O3)    
    r13 =  k13*(BrO)*(ClO)    
    r14 =  k14*(BrCl)
    # Differential equations
    dO2dt =  -r1-r2+r3+r4+r5+r8+r9+r10+2*r11+r12+r13 #PSSH Equations initial conditions taken from bibliography
    dOdt =    (2*k1*(O2)+k3*(O3))/(k2*(O2)+k5*(ClO)+k10*(NO2))
    dO3dt =    r2-r3-r4-r9-r11-r12
    dCldt =    (k5*(O)*(ClO)+k7*(Cl2O2)+k8*(ClO2)+k14*(BrCl))/(k4*(O3))
    dClOdt =    ((k7*(Cl2O2)+k8*(ClO2))/(2*k6))**0.5
    dCl2O2dt =  r6-r7
    dClO2dt =   r7-r8
    dNOdt =     -r9+r10+r11
    dNO2dt =     r9-r10-r11     
    dBrCldt =    r13-r14    
    dBrdt =    k14*(BrCl)/(k12*(O3))    
    dBrOdt =    k14*(BrCl)/(k13*(ClO))  
    return np.array([dO2dt,dOdt,dO3dt,dCldt,dClOdt,dCl2O2dt,dClO2dt,dNOdt,dNO2dt,dBrCldt,dBrdt,dBrOdt])

tspan = np.linspace(0, 80000, 100000)
y0 = [2e17,1e-6,5e12,6.46e4,7.22e7,1e-6,1e-6,1e9,1e9,1e-6,3.2e5,6.4e6] # Initial values for the dependent variables i.e. fsv,fs,Cv,Ca,fsa,and Cp#%%
#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example Web module: LEP- 9-Ozone""", x = 0.2, y = 0.98, fontweight='bold')
fig.subplots_adjust(wspace=0.25,hspace=0.3)
plt.subplots_adjust(left  = 0.5, wspace=0.3)

sol = odeint(ODEfun, y0, tspan, (k1, k2, k3, k4,k5, k6, k7,
                                 k8, k9, k10, k11, k12, k13, k14))
O2= sol[:, 0]
O3= sol[:, 2]
Cl= sol[:, 3]
Cl2O2= sol[:, 5]

p1 = ax1.plot(tspan, O3)[0]
ax1.legend([r'$O_3$'], loc='best')
ax1.set_xlabel('time (s)', fontsize='medium' )
ax1.set_ylabel('$C(molecules/cm^3)$', fontsize='medium')
ax1.set_ylim(0,6e12)
ax1.set_xlim(0,70000)
ax1.grid()
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))


p2 = ax2.plot(tspan, O2)[0]
ax2.legend([r'$O_2$'], loc='best')
#ax2.set_ylim(0,1)
ax2.set_xlim(0,70000)
ax2.grid()
ax2.set_xlabel('time (s)', fontsize='medium' )
ax2.set_ylabel(r'$C(molecules/cm^3)$', fontsize='medium')
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

p3 = ax3.plot(tspan, Cl)[0]
ax3.legend([r'$Cl$'], loc='best')
ax3.set_ylim(0, 2e7)
ax3.set_xlim(0, 70000)
ax3.grid()
ax3.set_xlabel('time (s)', fontsize='medium' )
ax3.set_ylabel('$C(molecules/cm^3)$', fontsize='medium')
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

p4 = ax4.plot(tspan, Cl2O2)[0]
ax4.legend([r'$Cl_2O_2$'], loc='best')
#ax4.set_ylim(0,20)
ax4.set_xlim(0,70000)
ax4.set_ylim(0,0.00008)
ax4.grid()
ax4.set_xlabel('time (s)', fontsize='medium' )
ax4.set_ylabel('$C(molecules/cm^3)$', fontsize='medium' )
ax4.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

ax1.text(-195000, -7.5e12,'Differential Equations'
         '\n\n'
         r'$\dfrac{dO_2}{dt} = -r_1 - r_2 + r_3 + r_4 + r_5 + r_8$' '\n\t'
         r'$+ r_9 + r_{10} + 2r_{11} + r_{12} + r_{13}$'
         '\n\n'
         r'$\dfrac{dO}{dt} = \dfrac{2k_1O_2 + k3O_3}{k2O_2 + k_5ClO + k_{10}NO_2}$'
         '\n\n'
         r'$\dfrac{dO_3}{dt} = r_2 - r_3 - r_4 - r_9 - r_{11} - r_{12}$'          
         '\n\n'
         r'$\dfrac{dCl}{dt} = \dfrac{k_5*O*ClO + k_7Cl_2O_2 + k_8ClO_2 + k_{14}BrCl}{k_4O_3}$'
         '\n\n'
         r'$\dfrac{dClO}{dt} = \sqrt{\dfrac{k_7Cl_2O_2 + k_8ClO_2}{2k_6}}$'
         '\n\n' 
         r'$\dfrac{dCl_2O_2}{dt} = r_6 - r_7$'
         '\n\n'
         r'$\dfrac{dClO_2}{dt} = r_7 - r_8$'
         '\n\n'     
         r'$\dfrac{dNO}{dt} = -r_9 + r_{10} + r_{11}$'
         '\n\n'
         r'$\dfrac{dNO_2}{dt} = r_9 - r_{10} - r_{11} $'
         '\n\n' 
         r'$\dfrac{dBrCl}{dt} = r_{13} - r_{14}$'
         '\n\n'
         r'$\dfrac{dBr}{dt} = \dfrac{k_{14}BrCl}{k_{12}O_3}$'
         '\n\n' 
         r'$\dfrac{dBrO}{dt} = \dfrac{k_{14}BrCl}{k_{13}ClO}$'       
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

ax1.text( -89200, -9e12 ,'Explicit Equations' '\n'   
         '\n' 
         r'$r_1 = k_1*O_2 $' 
         '\n' 
         r'$r_2 = k_2*O_2*O $'    
         '\n' 
         r'$r_3 = k_3*O_3 $' 
         '\n' 
         r'$r_4 = k_4*O_3*Cl $'      
         '\n' 
         r'$r_5 = k_5*O*ClO $' 
         '\n' 
         r'$r_6 = k_6*ClO^2 $'    
         '\n' 
         r'$r_7 = k_7*Cl_2O_2 $' 
         '\n' 
         r'$r_8 = k_8*ClO_2 $' 
         '\n' 
         r'$r_9 = k_9*O_3*NO $' 
         '\n' 
         r'$r_{10} = k_{10}NO_2*O $'    
         '\n' 
         r'$r_{11} = k_{11}NO_2*O_3 $' 
         '\n' 
         r'$r_{12} = k_{12}Br*O_3 $' 
         '\n' 
         r'$r_{13} = k_{13}BrO*ClO $' 
         '\n' 
         r'$r_{14} = k_{14}*BrCl $'        
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k1 = plt.axes([0.3, 0.85, 0.1, 0.015], facecolor=axcolor)
ax_k2 = plt.axes([0.3, 0.82, 0.1, 0.015], facecolor=axcolor)
ax_k3 = plt.axes([0.3, 0.79, 0.1, 0.015], facecolor=axcolor)
ax_k4 = plt.axes([0.3, 0.76, 0.1, 0.015], facecolor=axcolor)
ax_k5 = plt.axes([0.3, 0.73, 0.1, 0.015], facecolor=axcolor)
ax_k6 = plt.axes([0.3, 0.70, 0.1, 0.015], facecolor=axcolor)
ax_k7 = plt.axes([0.3, 0.67, 0.1, 0.015], facecolor=axcolor)
ax_k8 = plt.axes([0.3, 0.64, 0.1, 0.015], facecolor=axcolor)
ax_k9 = plt.axes([0.3, 0.61, 0.1, 0.015], facecolor=axcolor)
ax_k10 = plt.axes([0.3, 0.58, 0.1, 0.015], facecolor=axcolor)
ax_k11 = plt.axes([0.3, 0.55, 0.1, 0.015], facecolor=axcolor)
ax_k12 = plt.axes([0.3, 0.52, 0.1, 0.015], facecolor=axcolor)
ax_k13 = plt.axes([0.3, 0.49, 0.1, 0.015], facecolor=axcolor)
ax_k14 = plt.axes([0.3, 0.46, 0.1, 0.015], facecolor=axcolor)



sk1 = Slider(ax_k1, r'$k_1(\frac{cm^3}{molecule.s})$', 0.05*10**-96, 2*10**-93, valinit=1.03e-94,valfmt='%1.2E')
sk2 = Slider(ax_k2, r'$k_2(\frac{cm^3}{molecule.s})$', 2*10**-35, 9*10**-33, valinit=5.92e-34,valfmt='%1.2E')
sk3= Slider(ax_k3, r'$k_3(\frac{cm^3}{molecule.s})$', 2*10**-27, 7*10**-25, valinit=4.38e-26,valfmt='%1.2E')
sk4 = Slider(ax_k4, r'$k_4(\frac{cm^3}{molecule.s})$', 0.22*10**-11, 4.22*10**-11, valinit=1.22e-11,valfmt='%1.2E')
sk5 = Slider(ax_k5, r'$k_5(\frac{cm^3}{molecule.s})$', 1*10**-12, 7*10**-10, valinit=3.8e-11,valfmt='%1.2E')
sk6 = Slider(ax_k6, r'$k_6(\frac{cm^3}{molecule.s})$', 0.5*10**-32, 5*10**-32, valinit= 2.16e-32 ,valfmt='%1.2E')
sk7 = Slider(ax_k7, r'$k_7(\frac{cm^3}{molecule.s})$', 4.53*10**-16, 12.53*10**-14, valinit=8.53e-15,valfmt='%1.2E')
sk8 = Slider(ax_k8, r'$k_{8}(\frac{cm^3}{molecule.s})$',3.51*10**-13, 10.51*10**-13, valinit=6.51e-13 ,valfmt='%1.2E')
sk9 = Slider(ax_k9, r'$k_{9}(\frac{cm^3}{molecule.s})$', 0.5*10**-15, 3*10**-13, valinit=1.78e-14,valfmt='%1.2E')
sk10 = Slider(ax_k10, r'$k_{10}(\frac{cm^3}{molecule.s})$', 0.5*10**-12, 2*10**-10, valinit=1.05e-11,valfmt='%1.2E')
sk11 = Slider(ax_k11, r'$k_{11}(\frac{cm^3}{molecule.s})$', 0.4*10**-19, 2*10**-17, valinit=1e-18 ,valfmt='%1.2E')
sk12 = Slider(ax_k12, r'$k_{12}(\frac{cm^3}{molecule.s})$', 0.4*10**-13, 3*10**-11, valinit=1.18e-12 ,valfmt='%1.2E')
sk13 = Slider(ax_k13, r'$k_{13}(\frac{cm^3}{molecule.s})$',0.5*10**-13, 1.7*10**-11, valinit= 1.02e-12 ,valfmt='%1.2E')
sk14 = Slider(ax_k14, r'$k_{14}(\frac{cm^3}{molecule.s})$', 0.5*10**-9, 1.2*10**-7, valinit=1.06e-8,valfmt='%1.2E')


def update_plot2(val):
    k1 = sk1.val
    k2 =sk2.val
    k3 =sk3.val
    k4 = sk4.val
    k5 =sk5.val
    k6 = sk6.val
    k7 = sk7.val
    k8 = sk8.val
    k9 = sk9.val
    k10 = sk10.val
    k11 = sk11.val
    k12 = sk12.val
    k13 = sk13.val
    k14 = sk14.val   
    sol = odeint(ODEfun, y0, tspan, (k1, k2, k3, k4,k5, k6, k7,
                                     k8, k9, k10, k11, k12, k13, k14))
    O2= sol[:, 0]
    O3= sol[:, 2]
    Cl= sol[:, 3]
    Cl2O2= sol[:, 5]
    p1.set_ydata(O3)
    p2.set_ydata(O2)
    p3.set_ydata(Cl)
    p4.set_ydata(Cl2O2)
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
sk4.on_changed(update_plot2)
sk5.on_changed(update_plot2)
sk6.on_changed(update_plot2)
sk7.on_changed(update_plot2)
sk8.on_changed(update_plot2)
sk9.on_changed(update_plot2)
sk10.on_changed(update_plot2)
sk11.on_changed(update_plot2)
sk12.on_changed(update_plot2)
sk13.on_changed(update_plot2)
sk14.on_changed(update_plot2)
#

resetax = plt.axes([0.3, 0.88, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
    sk4.reset()
    sk5.reset()
    sk6.reset()
    sk7.reset()
    sk8.reset()
    sk9.reset()
    sk10.reset()
    sk11.reset()
    sk12.reset()
    sk13.reset()
    sk14.reset()    
button.on_clicked(reset)
    
