#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit Equations
k1 =  1
k2 =  1   
ca0 =  1
tau =  1.26

def ODEfun(Yfuncvec, t, k1, k2): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]
    cabar= Yfuncvec[3]
    cbbar= Yfuncvec[4]
    ccbar= Yfuncvec[5]
    Xbar=Yfuncvec[6]
    # Explicit equations
    ra =  -k1*ca
    rc =  k2*cb
    X =  1-ca/ca0
    rb =  k1*ca-k2*cb
    E1 =  -2.104*t**4+4.167*t**3-1.596*t**2+0.353*t-0.004
    E2 =  -2.104*t**4+17.037*t**3-50.247*t**2+62.964*t-27.402
    E = np.where(t<=tau, E1, E2)
    # Differential equations
    dcadt =  ra
    dcbdt =  rb 
    dccdt =  rc 
    dcabardt =  ca*E
    dcbbardt =  cb*E
    dccbardt =  cc*E
    dXbardt =  X*E
    return np.array([dcadt,dcbdt,dccdt,dcabardt,dcbbardt,dccbardt,dXbardt])
    
tspan = np.linspace(0,2.52, 100)
y0 = np.array([1,0,0,0,0,0,0])    
    
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example LEP- WEB17-1c : Segregation Model with Asymmetric RTD""", fontweight='bold', x = 0.25)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, tspan, (k1, k2))
ca= sol[:, 0]
cb= sol[:, 1]
cc= sol[:, 2]
cabar= sol[:, 3]
cbbar= sol[:, 4]
ccbar= sol[:, 5]
Xbar=sol[:, 6]
ra =  -k1*ca
rc =  k2*cb
X =  1-ca/ca0
rb =  k1*ca-k2*cb


p1, p2 = ax2.plot(tspan, X, tspan, Xbar)
ax2.legend([r'$X$', r'$\overline{X}$'], loc="best")
ax2.set_xlabel(r'$t (mins)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 2.52)
ax2.grid()

p3, p4, p5 = ax3.plot(tspan, cabar, tspan, cbbar, tspan, ccbar)
ax3.legend([r'$\overline{C_A}$', r'$\overline{C_B}$', r'$\overline{C_C}$'], loc="best")
ax3.set_xlabel(r'$t (mins)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 1)
ax3.set_xlim(0, 2.52)
ax3.grid()

p6, p7, p8 = ax4.plot(tspan, ra, tspan, rb, tspan, rc)
ax4.legend([r'$r_A$',r'$r_B$',r'$r_C$'], loc="best")
ax4.set_xlabel(r'$t (mins)$', fontsize='medium')
ax4.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
ax4.set_ylim(-3,3)
ax4.set_xlim(0, 2.52)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -1.5,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dt} = r_A$'
         '\n\n'
         r'$\dfrac{dC_B}{dt} = r_B$'
         '\n\n'
         r'$\dfrac{dC_C}{dt} = r_C$'       
         '\n\n'
         r'$\dfrac{d\overline{C_A}}{dt} = C_A.E$'
         '\n\n'
         r'$\dfrac{d\overline{C_B}}{dt} = C_B.E$' 
                  '\n\n'
         r'$\dfrac{d\overline{C_C}}{dt} = C_C.E$'
                  '\n\n'
         r'$\dfrac{d\overline{X}}{dt} = X.E$' '\n\n'
         'Explicit Equations' '\n\n'   
         r'$C_{A0} = 1$'
         '\n'
         r'$\tau = 1.26$'
         '\n'         
         r'$r_A = -k_1C_A$'
         '\n'
         r'$r_B = k_1C_A - k_2C_B$'
         '\n'
         r'$r_C = k_2C_B$'
         '\n'         
         r'$X = 1 -\dfrac{C_A}{C_{A0}}$' 
         '\n\n'
         r'$E_1 = -2.104t^4 + 4.167t^3$' '\n\t' 
         r'$- 1.596t^2 + 0.353t $''\n\t'
         r'$- 0.004$'
         '\n'
         r'$E_2 = -2.104t^4 + 17.037t^3 $' '\n\t' 
         r'$- 50.247t^2 + 62.964t $''\n\t'
         r'$- 27.402$'
         '\n'
         r'$E = IF (t<=\tau) then (E_1) else (E_2)$'
         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k1 = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)


sk1 = Slider(ax_k1, r'$k_1 (min^{-1})$', 0.01, 15, valinit=1, valfmt='%1.2f')
sk2 = Slider(ax_k2, r'$k_2 (min^{-1})$', 0.01, 15, valinit=1, valfmt='%1.2f') 

def update_plot(val):
    k1 = sk1.val
    k2 = sk2.val
    sol = odeint(ODEfun, y0, tspan, (k1, k2))
    ca= sol[:, 0]
    cb= sol[:, 1]
    cabar= sol[:, 3]
    cbbar= sol[:, 4]
    ccbar= sol[:, 5]
    Xbar=sol[:, 6]
    ra =  -k1*ca
    rc =  k2*cb
    X =  1-ca/ca0
    rb =  k1*ca-k2*cb
    
    p1.set_ydata(X)
    p2.set_ydata(Xbar)
    p3.set_ydata(cabar)
    p4.set_ydata(cbbar)
    p5.set_ydata(ccbar)
    p6.set_ydata(ra)
    p7.set_ydata(rb)
    p8.set_ydata(rc)    
    fig.canvas.draw_idle()

sk1.on_changed(update_plot)
sk2.on_changed(update_plot)

resetax = plt.axes([0.38, 0.75, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')
def reset(event):
    sk1.reset()
    sk2.reset()
button.on_clicked(reset)
