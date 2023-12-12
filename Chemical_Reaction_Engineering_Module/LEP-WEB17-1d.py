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
    E1 =  0.47219*t**4-1.30733*t**3+0.31723*t**2+0.85688*t+0.20909;
    E2 =  3.83999*t**6-58.16185*t**5+366.20970*t**4-1224.66963*t**3+2289.84857*t**2-2265.62125*t+925.46463;
    E3 =  0.00410*t**4-0.07593*t**3+0.52276*t**2-1.59457*t+1.84445;
    if t<=1.82:
        E=E1
    elif t<=2.8:
        E=E2
    else:
        E=E3
    # Differential equations
    dcadt =  ra
    dcbdt =  rb 
    dccdt =  rc 
    dcabardt =  ca*E
    dcbbardt =  cb*E
    dccbardt =  cc*E
    dXbardt =  X*E
    return np.array([dcadt,dcbdt,dccdt,dcabardt,dcbbardt,dccbardt,dXbardt])
    
tspan = np.linspace(0,7,1000)
y0 = np.array([1.0,0,0,0,0,0,0])    
    
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example LEP-WEB17-1d : Segregation Model with Bimodal Distribution""", fontweight='bold', x = 0.25)
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
ax2.set_xlim(0, 7)
ax2.grid()

p3, p4, p5 = ax3.plot(tspan, cabar, tspan, cbbar, tspan, ccbar)
ax3.legend([r'$\overline{C_A}$', r'$\overline{C_B}$', r'$\overline{C_C}$'], loc="best")
ax3.set_xlabel(r'$t (mins)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 1)
ax3.set_xlim(0, 7)
ax3.grid()

p6, p7, p8 = ax4.plot(tspan, ra, tspan, rb, tspan, rc)
ax4.legend([r'$r_A$',r'$r_B$',r'$r_C$'], loc="best")
ax4.set_xlabel(r'$t (mins)$', fontsize='medium')
ax4.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
ax4.set_ylim(-3,3)
ax4.set_xlim(0, 7)
ax4.grid()

ax1.axis('off')
ax1.text(-1.08, -1.3,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dt} = r_A$'
         '\n'
         r'$\dfrac{dC_B}{dt} = r_B$'
         '\n'
         r'$\dfrac{dC_C}{dt} = r_C$'       
         '\n'
         r'$\dfrac{d\overline{C_A}}{dt} = C_A.E$'
         '\n'
         r'$\dfrac{d\overline{C_B}}{dt} = C_B.E$' 
                  '\n'
         r'$\dfrac{d\overline{C_C}}{dt} = C_C.E$'
                  '\n'
         r'$\dfrac{d\overline{X}}{dt} = X.E$' '\n\n'
         'Explicit Equations' '\n\n'   
         r'$C_{A0} = 1$'
         '\n'         
        r'$r_A = -k_1C_A$'
         '\n'
         r'$r_B = k_1C_A - k_2C_B$'
         '\n'
         r'$r_C = k_2C_B$'
         '\n'         
         r'$X = 1 -\dfrac{C_A}{C_{A0}}$' 
         '\n'
         r'$E_1 = +0.47219t^4 - 1.30733t^3$' '\n\t' 
         r'$+ 0.31723t^2 + 0.85688t+ 0.20909$'
         '\n\n'
         r'$E_2 = +3.83999t^6 - 58.16185t^5   $' '\n\t' 
         r'$+ 366.2097t^4 - 1224.6696t^3$''\n\t'
         r'$+ 2289.84857t^2 - 2265.62125t+ 925.46463$'
         '\n\n'
         r'$E_3 = 0.00410t^4 - 0.07593t^3  $' '\n\t' 
         r'$+ + 0.52276t^2 - 1.59457t + 1.84445$' '\n\n'         
         r'$E = IF (t<=1.82) then (E_1) else (if(t<=2.8)then(E_2)else(E_3)) $'
         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k1 = plt.axes([0.34, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.34, 0.65, 0.2, 0.02], facecolor=axcolor)


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

resetax = plt.axes([0.40, 0.75, 0.09, 0.04])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')
def reset(event):
    sk1.reset()
    sk2.reset()
button.on_clicked(reset)
