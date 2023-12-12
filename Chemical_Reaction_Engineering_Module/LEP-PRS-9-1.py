#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
k5 = 3980000000 #
T = 1000 #
E1=87500
E2=13000
E4=9700
E3=40000
def ODEfun(Yfuncvec, t, k5,T,E1,E2,E3,E4): 
    C1= Yfuncvec[0]
    C2= Yfuncvec[1]
    C3= Yfuncvec[2]
    C4= Yfuncvec[3]
    C5= Yfuncvec[4]
    C6= Yfuncvec[5]
    C7= Yfuncvec[6]
    C8= Yfuncvec[7]
    CP1= Yfuncvec[8]
    CP5= Yfuncvec[9]
    # Explicit equations Inline
    k1 = 10*np.exp((E1/1.987)*(1/1250-1/T)) #
    k2 = 8450000*np.exp((E2/1.987)*(1/1250-1/T)) #
    k4 = 2530000000*np.exp((E4/1.987)*(1/1250-1/T)) #
    k3 = 3200000*np.exp((E3/1.987)*(1/1250-1/T)) #
    r1=-k1*C1-k2*C1*C2-k4*C1*C6
    r2=2*k1*C1-k2*C2*C1
    r3=k2*C1*C2
    r4=k2*C1*C2-k3*C4+k4*C1*C6-k5*C4**2
    r5=k3*C4
    r6=k3*C4-k4*C1*C6    
    r7=k4*C1*C6
    r8=0.5*k5*C4**2
    rCP5=k3*((2*k1/k5)**0.5)*(CP1**0.5)
    rCP1= -3*k1*CP1-(k3*(2*k1/k5)**0.5)*(CP1**0.5)
   
    # Differential equations
    dC1dt = r1
    dC2dt = r2
    dC3dt = r3
    dC4dt = r4
    dC5dt = r5
    dC6dt = r6
    dC7dt = r7
    dC8dt = r8
    dCP1dt = rCP1
    dCP5dt = rCP5
    return np.array([dC1dt, dC2dt, dC3dt,dC4dt,dC5dt,dC6dt,dC7dt,dC8dt,dCP1dt,dCP5dt]) 

tspan = np.linspace(0, 12.1, 100) # Range for the independent variable
y0 = np.array([0.1,0,0,0,0,0,0,0,0.1,0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP PRS-9-1 PSSH Applied to Thermal Cracking of Ethane""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.35,hspace=0.35)
sol = odeint(ODEfun, y0, tspan, (k5,T,E1,E2,E3,E4))
C1= sol[:,0]
C2= sol[:,1]
C3= sol[:,2]
C4= sol[:,3]
C5= sol[:,4]
C6= sol[:,5]
C7= sol[:,6]
C8= sol[:,7]
CP1= sol[:,8]
CP5= sol[:,9]

p1= ax1.plot(tspan, C2)[0]
ax1.legend(["$CH3* (C_2)$"], loc='best')
ax1.set_xlabel('time (s)', fontsize='medium')
ax1.set_ylabel(r'$Concentration (mol/dm^3)$', fontsize='medium')
ax1.set_ylim(0,10**-9)
ax1.set_xlim(0,12.1)
ax1.grid()

p2,p3 = ax2.plot(tspan, C1, tspan, CP1)
ax2.legend(["$Ethane (C_1)$"] ,loc='best')
ax2.set_xlabel('time (s)', fontsize='medium')
ax2.set_ylabel(r'$Concentration (mol/dm^3)$', fontsize='medium')
ax2.set_ylim(0,0.1)
ax2.set_xlim(0,12.1)
ax2.grid()

p4,p5 = ax3.plot(tspan, C5, tspan, CP5)
ax3.legend(["$Ethylene (C_5)$"], loc='best')
ax3.set_xlabel('time (s)', fontsize='medium')
ax3.set_ylabel(r'$Concentration (mol/dm^3)$', fontsize='medium')
ax2.set_ylim(0,0.1)
ax3.set_xlim(0,12.1)
ax3.grid()

p6,p7 = ax4.plot(tspan, C3, tspan, C8)
ax4.legend(['$Methane (C_3)$', '$Butane (C_8)$'], loc='best')
ax4.set_xlabel('time (s)', fontsize='medium')
ax4.set_ylabel(r'$Concentration (mol/dm^3)$', fontsize='medium')
ax4.set_ylim(0,0.002)
ax4.set_xlim(0,12.1)
ax4.grid()

ax3.text(-19.0, -0.03,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_1}{dt} = -k_1*C_1-k_2*C_1*C_2-k_4*C_1*C_6$'
                  '\n'
         r'$\dfrac{dC_2}{dt} = 2*k_1*C_1-k_2*C_2*C_1$'
                  '\n'
         r'$\dfrac{dC_3}{dt} = k_2*C_1*C_2$'
                  '\n'
         r'$\dfrac{dC_4}{dt} = k_2*C_1*C_2-k_3*C_4+k_4*C_1*C_6-k_5*C_4^2$'
                  '\n'
         r'$\dfrac{dC_5}{dt} = k_3*C_4$'
                  '\n'
         r'$\dfrac{dC_6}{dt} = k_3*C_4-k_4*C_1*C_6 $'
                           '\n'
         r'$\dfrac{dC_7}{dt} = k_4*C_1*C_6$'
                           '\n'
         r'$\dfrac{dC_8}{dt} = 0.5*k_5*C_4^2$'
                  '\n\n'                  
         'Explicit Equations'
                  '\n\n'
         r'$k_1=(10)*exp\left(\left(\dfrac{E_1}{1.987}\right)\left(\dfrac{1}{1250} - \dfrac{1}{T}\right)\right)$'
         '\n'
         r'$k_2=(8450000)*exp\left(\left(\dfrac{E_2}{1.987}\right)\left(\dfrac{1}{1250} - \dfrac{1}{T}\right)\right)$'
         '\n'
               '\n'
         r'$k_3=(3200000)*exp\left(\left(\dfrac{E_3}{1.987}\right)\left(\dfrac{1}{1250} - \dfrac{1}{T}\right)\right)$'
               '\n'
         r'$k_4=(2530000000)*exp\left(\left(\dfrac{E_4}{1.987}\right)\left(\dfrac{1}{1250} - \dfrac{1}{T}\right)\right)$'
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=15), fontweight='bold')

#%%
# Slider
axcolor = 'black'
ax_E1 = plt.axes([0.08, 0.84, 0.2, 0.015], facecolor=axcolor)
ax_E2 = plt.axes([0.08, 0.81, 0.2, 0.015], facecolor=axcolor)
ax_E3 = plt.axes([0.08, 0.78, 0.2, 0.015], facecolor=axcolor)
ax_E4 = plt.axes([0.08, 0.75, 0.2, 0.015], facecolor=axcolor)
ax_k5 = plt.axes([0.08, 0.72, 0.2, 0.015], facecolor=axcolor)
ax_T = plt.axes([0.08, 0.69, 0.2, 0.015], facecolor=axcolor)

sE1 = Slider(ax_E1, r'$E_{1}$ ($\frac{cal}{mol}$)', 25000, 150000, valinit=87500, valfmt = '%1.0f')
sE2 = Slider(ax_E2,  r'$E_{2}$ ($\frac{cal}{mol}$)', 5000, 30000, valinit=13000, valfmt = '%1.0f')
sE3 = Slider(ax_E3,  r'$E_{3}$ ($\frac{cal}{mol}$)', 10000, 80000, valinit=40000, valfmt = '%1.0f')
sE4 = Slider(ax_E4, r'$E_{4}$ ($\frac{cal}{mol}$)',2000, 25000, valinit= 9700, valfmt = '%1.0f')
sk5 = Slider(ax_k5, r'$k_5$  ($\frac{dm^3}{mol.s}$)', 2*10**8, 10**11, valinit=3980000000, valfmt = '%1.0E')
sT = Slider(ax_T, r'$T (K)$', 500, 1500, valinit=1000, valfmt = '%1.0f')

def update_plot2(val):
    E1 = sE1.val
    E2 = sE2.val
    E3 =sE3.val
    E4 = sE4.val
    k5 = sk5.val
    T = sT.val
    sol = odeint(ODEfun, y0, tspan, (k5,T,E1,E2,E3,E4))
    C1= sol[:,0]
    C2= sol[:,1]
    C3= sol[:,2]
    C4= sol[:,3]
    C5= sol[:,4]
    C6= sol[:,5]
    C7= sol[:,6]
    C8= sol[:,7]
    CP1= sol[:,8]
    CP5= sol[:,9]
    p1.set_ydata(C2)
    p2.set_ydata(C1)
    p3.set_ydata(CP1)
    p4.set_ydata(C5)
    p5.set_ydata(CP5)
    p6.set_ydata(C3)
    p7.set_ydata(C8)
    fig.canvas.draw_idle()

sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)
sE3.on_changed(update_plot2)
sE4.on_changed(update_plot2)
sk5.on_changed(update_plot2)
sT.on_changed(update_plot2)
#
resetax = plt.axes([0.15, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sE1.reset()
    sE2.reset()
    sE3.reset()
    sE4.reset()
    sk5.reset()
    sT.reset()
button.on_clicked(reset)
    
