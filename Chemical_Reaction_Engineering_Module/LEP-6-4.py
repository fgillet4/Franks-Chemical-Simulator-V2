#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
# Explicit equations
alpha = 0.009 
k = 5000 
Cb0 = 0.01 
Ca0 = 0.01 
def ODEfun(Yfuncvec, W, alpha, k, Ca0, Cb0): 
    Fa = Yfuncvec[0] 
    Fb = Yfuncvec[1] 
    Fc = Yfuncvec[2] 
    p = Yfuncvec[3] 
    #Explicit Equation Inline
    Ct0 = Ca0 + Cb0
    Ft0 = 30
    Fao=15
    X=1-Fa/Fao
    Ft=Fa+Fb+Fc
    Ca = Ct0*(Fa/Ft)*p
    Cb = Ct0*(Fb/Ft)*p 
    Cc = Ct0*(Fc/Ft)*p 
    ra = -k*Ca*Cb 
    rb = ra 
    rc = 3*(-ra) 
    # Differential equations
    dFadW = ra 
    dFbdW = rb 
    dFcdW = rc 
    dpdW = -(alpha/(2*p))*(Ft/Ft0) 
    return np.array([dFadW, dFbdW, dFcdW, dpdW]) 

Wspan = np.linspace(0, 80, 1000)
y0 = np.array([15, 15, 0, 1])
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 6-4 Algorithm for the Gas Phase Reaction""", fontweight='bold', x = 0.2, y=0.99)
plt.subplots_adjust(left  = 0.35)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol =  odeint(ODEfun, y0, Wspan, (alpha, k, Ca0, Cb0))
Fa = sol[:, 0]
Fb = sol[:, 1]
Fc = sol[:, 2]
p = sol[:, 3]
Ct0 = Ca0 + Cb0
Ft0 = 30
Ft=Fa+Fb+Fc
Ca = Ct0*(Fa/Ft)*p
Cb = Ct0*(Fb/Ft)*p 
Cc = Ct0*(Fc/Ft)*p 
X = (15-Fa)/15
ra = -k*Ca*Cb 
rb = ra 
rc = 3*(-ra) 

p1, p2, p3 = ax1.plot(Wspan, Fa, Wspan, Fb, Wspan, Fc)
ax1.legend([r'$F_A$',r'$F_B$',r'$F_C$'],  loc='best')
ax1.set_xlabel('Catalyst Weight (kg)', fontsize='medium', )
ax1.set_ylabel(r'Molar flow rates (mol/s)', fontsize='medium', )
ax1.grid()
ax1.set_xlim(0, 80)
ax1.set_ylim(0, 40)


p4, p5, p6 = ax2.plot(Wspan, Ca, Wspan, Cb, Wspan, Cc)
ax2.legend([r'$C_{A}$', r'$C_{B}$', r'$C_{C}$'], loc='best')
ax2.set_xlabel('Catalyst Weight(kg)', fontsize='medium', )
ax2.set_ylabel(r'Concentration (mol/$dm^{3}$)', fontsize='medium', )
ax2.grid()
ax2.set_xlim(0, 80)
ax2.set_ylim(0, 0.04)


p7, p8= ax3.plot(Wspan, X, Wspan, p)
ax3.legend(['X', 'p'], loc='best')
ax3.set_xlabel('Catalyst Weight(kg)', fontsize='medium', )
ax3.set_ylabel('Conversion, pressure drop', fontsize='medium', )
ax3.grid()
ax3.set_xlim(0, 80)
ax3.set_ylim(0, 1.1)

p9, p10, p11 = ax4.plot(Wspan, -ra, Wspan, -rb, Wspan, -rc)
ax4.legend([r'$-r_A^\prime$',r'$-r_B^\prime$',r'$-r_C^\prime$'], loc='best')
ax4.set_xlabel('Catalyst Weight(kg)', fontsize='medium', )
ax4.set_ylabel(r'Reaction Rate (mol/$dm^{3}.s)$', fontsize='medium', )
ax4.grid()
ax4.set_xlim(0, 80)
ax4.set_ylim(-2, 1)

ax2.text(11.7,0.03, r'$C_{A}= C_{B}$',fontsize=15)
ax3.text(-80, -0.1,'Differential Equations'
         '\n'
         r'$\dfrac{dF_A}{dW} = r_A^\prime$'
         '\n'
         r'$\dfrac{dF_B}{dW} = r_B^\prime$'
         '\n'
         r'$\dfrac{dF_C}{dW} = r_C^\prime$'
         '\n'
         r'$\dfrac{dp}{dW} = \dfrac{-\alpha F_T}{2p\thinspace F_{T0}}$'      
                  '\n \n'
         'Explicit Equations'
                  '\n'
         r'$C_{T0} = C_{A0}+C_{B0}$'
         '\n \n'   
         r'$F_{T0} = 30$'
         '\n \n'          
         r'$F_T = F_A + F_B + F_C$'
         '\n \n'
         r'$C_A = C_{T0}\left(\dfrac{F_A}{F_T}\right) p$'
         '\n'
          r'$C_B = C_{T0}\left(\dfrac{F_B}{F_T}\right) p$'
         '\n'
          r'$C_C = C_{T0}\left(\dfrac{F_C}{F_T}\right) p$'         
         '\n'
         r'$r_A^\prime = -kC_AC_B$'
         '\n'
         r'$r_B^\prime = r_A^\prime$'
         '\n'
         r'$r_C^\prime = 3(-r_A^\prime)$'
        
         , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_alpha = plt.axes([0.07, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_k = plt.axes([0.07, 0.78, 0.2, 0.015], facecolor=axcolor)
ax_Ca0 = plt.axes([0.07, 0.74, 0.2, 0.015], facecolor=axcolor)
ax_Cb0 = plt.axes([0.07, 0.7, 0.2, 0.015], facecolor=axcolor)

salpha = Slider(ax_alpha, r'$\alpha (kg^{-1})$', 0.0, 0.01, valinit=0.009, valfmt = '%1.3f')
sk = Slider(ax_k, r'$k (\frac{dm^6}{mol.kgcat.s})$', 100, 15000, valinit=5000, valfmt = '%1.0f')
sCa0 = Slider(ax_Ca0, r'$C_{A0} (\frac{mol}{dm^3})$', 0.0001, 0.05, valinit=0.01, valfmt = '%1.3f')
sCb0 = Slider(ax_Cb0, r'$C_{B0} (\frac{mol}{dm^3})$', 0.0001, 0.05, valinit=0.01, valfmt = '%1.3f')


def update_plot(val):
    alpha = salpha.val
    k = sk.val
    Ca0 = sCa0.val
    Cb0 = sCb0.val
    sol =  odeint(ODEfun, y0, Wspan, (alpha, k, Ca0, Cb0))
    Fa = sol[:, 0]
    Fb = sol[:, 1]
    Fc = sol[:, 2]
    p = sol[:, 3]
    Ct0 = Ca0 + Cb0
    Ft0 = 30
    Ft=Fa+Fb+Fc
    Ca = Ct0*(Fa/Ft)*p
    Cb = Ct0*(Fb/Ft)*p 
    Cc = Ct0*(Fc/Ft)*p 
    X = (15-Fa)/15
    ra = -k*Ca*Cb 
    rb = ra 
    rc = 3*(-ra) 
    p1.set_ydata(Fa)
    p2.set_ydata(Fb)
    p3.set_ydata(Fc)
    p4.set_ydata(Ca)
    p5.set_ydata(Cb)
    p6.set_ydata(Cc)
    p7.set_ydata(X)
    p8.set_ydata(p)
    p9.set_ydata(-ra)
    p10.set_ydata(-rb)
    p11.set_ydata(-rc)
    fig.canvas.draw_idle()

salpha.on_changed(update_plot)
sk.on_changed(update_plot)
sCa0.on_changed(update_plot)
sCb0.on_changed(update_plot)

resetax = plt.axes([0.1, 0.87, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    salpha.reset()
    sk.reset()   
    sCa0.reset()    
    sCb0.reset()    
	
button.on_clicked(reset)
plt.show()











