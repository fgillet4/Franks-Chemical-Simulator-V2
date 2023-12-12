#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
P=6
T=1100
R = 1.987
Ea = 82000
yao = 1
Fao=193
def ODEfun(Yfuncvec, V,P,T,Ea, yao, Fao): 
    X = Yfuncvec
    # Differential equations
    Cto=P*10**5/(8.314*T)/1000
    Cao=yao*Cto;
    epsilon = yao*(1+1-1) 
    A= 6.024*10**16
    k = A*(np.exp(-Ea/(R*T)))
    Ca = Cao*(1-X)/(1+epsilon*X) 
    ra = -k*Ca 
    return -ra/Fao 

Vspan = np.linspace(0, 2130, 10000) # Range for the Volume of the reactor. 
y0 = np.array([0]) # Initial values for the dependent variables Ca and Cb

 
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""Example 5-3 Plug Flow Reactor""", fontweight='bold', x = 0.14)
plt.subplots_adjust(left  = 0.38)

sol = odeint(ODEfun, y0, Vspan, (P,T,Ea, yao, Fao))
Cto=P*10**5/(8.314*T)/1000
epsilon = yao*(1+1-1)
A= 6.024*10**16
k = A*(np.exp(-Ea/(R*T)))
Cao=yao*Cto
Ca = Cao*(1-sol)/(1+epsilon*sol) 
Cb = Cao*sol/(1+epsilon*sol) 
Cc = Cb
ra = -k*Ca 

p1, p2, p3 = ax2.plot(Vspan, Ca, Vspan, Cb, Vspan, Cc)
ax2.legend(['$C_A$', '$C_B$', '$C_C$'], loc="upper right")
ax2.set_xlabel('V ($dm^3$)', fontsize='medium')
ax2.set_ylabel('Concentration ($mol/dm^3$)', fontsize='medium')
ax2.set_ylim(0, 0.1)
ax2.set_xlim(0, 2130)
ax2.grid()


p4= ax3.plot(Vspan, odeint(ODEfun, y0, Vspan, (P,T,Ea, yao, Fao)))[0]

ax3.legend(['X'], loc="upper right")
ax3.set_xlabel('V ($dm^3$)', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium')
ax3.set_ylim(0, 1.0)
ax3.set_xlim(0, 2130)
ax3.grid()

p5 = ax4.plot(Vspan, -ra)[0]
ax4.legend(['$-r_A$'], loc="upper right")
ax4.set_xlabel('V ($dm^3$)', fontsize='medium')
ax4.set_ylabel('Reaction Rate($mol/dm^3.s$)', fontsize='medium')

ax4.set_ylim(0, 1)
ax4.set_xlim(0, 2130)
ax4.grid()

ax1.axis('off')
ax1.text(-1.5, -1.45,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n           in the textbook, in python we have to use k=A*exp(-E/RT) \n           in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax2.text(650,0.082, r'$C_{B}= C_{C}$')
ax1.text(-1.3, -1.1,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dV} = \dfrac{-r_A}{F_{A0}}$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$P = 6$'
         '\n'    
         r'$y_{A0} = 1$'
        '\n'
         r'$C_{T0} = P*10^5/(8.314*T)/1000 $'
         '\n\n'  
         r'$C_{A0} = y_{A0}*C_{T0}$'
         '\n\n' 
         r'$R = 1.987$'
         '\n\n'
         r'$\epsilon = y_{A0}(1+1-1)$'
         '\n\n'
          r'$F_{A0} = 193$'
         '\n\n'
         r'$A = 6.024*10^{16}$'
         '\n\n'
         r'$C_A = \dfrac{C_{A0}(1-X)}{1+\epsilon X}$'
         '\n'
         r'$C_B = \dfrac{C_{A0} X}{1+\epsilon X}$'
         '\n'
         r'$C_C = C_B$'
         '\n'
         r'$r_A = -k C_A$'
         '\n'
         r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'
         '\n'
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_yao = plt.axes([0.33, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_T = plt.axes([0.33, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Ea = plt.axes([0.33, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Fao = plt.axes([0.33, 0.60, 0.2, 0.02], facecolor=axcolor)

syao = Slider(ax_yao, r'$y_{A0} $', 0, 1, valinit=1, valfmt='%1.1f')
sT = Slider(ax_T, 'T (K)', 500, 1500, valinit=1100, valfmt='%1.0f')
sEa = Slider(ax_Ea, r'$E (\frac{cal}{mol})$', 60000, 100000, valinit=82000, valfmt='%1.0f')
sFao = Slider(ax_Fao, r'$F_{A0} (\frac{mol}{s})$', 10, 500, valinit=193, valfmt='%1.1f')

def update_plot(val):
    yao = syao.val
    T = sT.val
    Ea = sEa.val
    Fao=sFao.val
    sol = odeint(ODEfun, y0, Vspan, (P,T,Ea, yao, Fao))
    Cto=P*10**5/(8.314*T)/1000
    Cao=yao*Cto
    epsilon = yao*(1+1-1)
    A=6.024*10**16
    k = A*(np.exp(-Ea/(R*T)))
    Ca = Cao*(1-sol)/(1+epsilon*sol) 
    Cb = Cao*sol/(1+epsilon*sol) 
    Cc = Cb
    ra = -k*Ca     
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(sol)
    p5.set_ydata(-ra)    
    fig.canvas.draw_idle()

syao.on_changed(update_plot)
sT.on_changed(update_plot)
sEa.on_changed(update_plot)
sFao.on_changed(update_plot)
resetax = plt.axes([0.38, 0.8, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    syao.reset()
    sT.reset()
    sEa.reset()
    sFao.reset()

button.on_clicked(reset)


    
