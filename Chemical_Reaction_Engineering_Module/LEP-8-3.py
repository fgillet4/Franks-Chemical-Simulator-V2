#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
A1 = 1.913
A2 = 0.547
E1 = 800
E2 = 600
T = 300
Cao = 2
R = 1.987
def ODEfun(Yfuncvec, t, A1, A2, E1, E2, T): 
    Ca = Yfuncvec[0] 
    Cb = Yfuncvec[1] 
    Cc = Yfuncvec[2]  
    # Explicit equations Inline
    k1=A1*np.exp(-E1/(R*T))
    k2=A2*np.exp(-E2/(R*T))
    ra=-k1*Ca
    rb=k1*Ca-k2*Cb
    rc=k2*Cb
    # Differential equations
    dCadt = ra 
    dCbdt = rb 
    dCcdt = rc 
    return np.array([dCadt, dCbdt, dCcdt]) 

t = np.linspace(0, 20, 1000)
y0 = np.array([2, 0, 0])

#Making E1 and E2 extremely Small solves the problem
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-3: Series Reactions in a Batch Reactor""", x = 0.2, y = 0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.3,hspace=0.3)

sol = odeint(ODEfun, y0, t, (A1,A2, E1, E2, T))
Ca = sol[:, 0]
Cb = sol[:, 1]
Cc = sol[:, 2]
selectivity = np.nan_to_num(Cb/Cc)
Yield = np.nan_to_num(Cb/(Cao - Ca))
X = (Cao - Ca)/Cao

p1,p2,p3  = ax1.plot(t, Ca, t, Cb, t, Cc)
ax1.legend(['$C_A$', '$C_B$', '$C_C$'], loc='center right')
ax1.set_xlabel('time(h)', fontsize='medium', )
ax1.set_ylabel('$Concentration(mol/dm^3)$', fontsize='medium', )
ax1.grid()
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 2)
p4 = ax2.plot(t, X)[0]
ax2.legend(['X'], loc='upper left')
ax2.set_xlabel('time(h)', fontsize='medium', )
ax2.set_ylabel('Conversion', fontsize='medium', )
ax2.grid()
ax2.set_xlim(0, 20)
ax2.set_ylim(0, 1.05)

p5 = ax3.plot(t, selectivity)[0]
ax3.legend(['$S_{B/C}$'], loc='upper right')
ax3.set_xlabel('time(h)', fontsize='medium', )
ax3.set_ylabel('Selectivity of B', fontsize='medium', )
ax3.grid()
ax3.set_xlim(0, 20)
ax3.set_ylim(0, 20)

p6 = ax4.plot(t, Yield)[0]
ax4.legend(['$Y_B$'], loc='upper right')
ax4.set_xlabel('time(h)', fontsize='medium', )
ax4.set_ylabel('Yield of B', fontsize='medium', )
ax4.grid()
ax4.set_xlim(0, 20)
ax4.set_ylim(0, 1)

ax3.text(-32, -4.2,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))
ax3.text(-26, 2.5,
'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dt} = r_A$'
         '\n'
         r'$\dfrac{dC_B}{dt} = r_B$'
         '\n'
         r'$\dfrac{dC_C}{dt} = r_C$'

                  '\n \n'           
         'Explicit Equations'
                  '\n'
         r'$C_{A0} = 2$'
         '\n'
          r'$T = 300 \thinspace K$'
         '\n'
          r'$A_1 = 1.913 \thinspace hr^{-1}$'
         '\n'
          r'$A_2 = 0.547 \thinspace hr^{-1}$'
         '\n'
         r'$X = \dfrac{(C_{A0} - C_A)}{C_{A0}}$'
         '\n'
         r'$Selectivity = \dfrac{C_B}{C_C}$'
                  '\n'
         r'$Yield = \dfrac{C_B}{(C_{A0} - C_A)}$'
                '\n'
         r'$k_1 = A_1*exp\left(\dfrac{-E_1}{1.987*T}\right)$'       
        '\n\n'
        r'$k_2 = A_2*exp\left(\dfrac{-E_2}{1.987*T}\right)$' 
                  '\n'
         r'$r_A = -k_1C_A$'
         '\n'
         r'$r_B = k_1C_A - k_2C_B$'
         '\n'
         r'$r_C = k_2C_B$'
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
#ax1.axis('off')
axcolor = 'black'

ax_E1 = plt.axes([0.09, 0.84, 0.15, 0.015], facecolor=axcolor)
ax_E2 = plt.axes([0.09, 0.80, 0.15, 0.015], facecolor=axcolor)
ax_T = plt.axes([0.09, 0.76, 0.15, 0.015], facecolor=axcolor)

sE1 = Slider(ax_E1, r'E$_{1} (\frac{cal}{mol})$', 0, 5000, valinit=800, valfmt = "%1.1f")
sE2 = Slider(ax_E2, r'E$_{2} (\frac{cal}{mol})$',   0,   5000, valinit=600, valfmt = "%1.1f")
sT = Slider(ax_T, r'T (K)',   280, 500, valinit=300, valfmt = "%1.1f")

def update_plot2(val):
    E1 = sE1.val
    E2 = sE2.val
    T=sT.val
    sol = odeint(ODEfun, y0, t, (A1,A2,E1, E2, T))
    Ca = sol[:, 0]
    Cb = sol[:, 1]
    Cc = sol[:, 2]
    selectivity = np.nan_to_num(Cb/Cc)
    yeild = np.nan_to_num(Cb/(Cao - Ca))
    X = (Cao - Ca)/Cao
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(X)
    p5.set_ydata(selectivity)
    p6.set_ydata(yeild)
    fig.canvas.draw_idle()


sE1.on_changed(update_plot2)
sE2.on_changed(update_plot2)
sT.on_changed(update_plot2)

resetax = plt.axes([0.13, 0.87, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sE1.reset()
    sE2.reset()
    sT.reset()

button.on_clicked(reset)
