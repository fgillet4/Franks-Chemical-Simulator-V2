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
cao =  1
tau =  1.26
cbo =  0
cco =  0
def ODEfun(Yfuncvec, z, k1, k2): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]
    F=Yfuncvec[3]
    # Explicit equations
    ra =   -k1*ca
    rc =   k2*cb
    rb =   k1*ca-k2*cb

    lam =  6-z
    E1 =  0.47219*lam**4-1.30733*lam**3+0.31723*lam**2+0.85688*lam+0.20909;
    E2 =  3.83999*lam**6-58.16185*lam**5+366.20970*lam**4-1224.66963*lam**3+2289.84857*lam**2-2265.62125*lam+925.46463;
    E3 =  0.00410*lam**4-0.07593*lam**3+0.52276*lam**2-1.59457*lam+1.84445;
    if lam<=1.82:
        E=E1
    elif lam<=2.8:
        E=E2
    else:
        E=E3
    EF =  E/(1-F)
    # Differential equations
    dcadz =  -(-ra+(ca-cao)*EF)
    dcbdz =  -(-rb+(cb-cbo)*EF)
    dccdz =  -(-rc+(cc-cco)*EF)
    dFdz =  -E
    return np.array([dcadz, dcbdz, dccdz, dFdz])
    
zspan = np.linspace(0, 6, 1000)
y0 = np.array([1, 0, 0, 0.99])    
    
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-WEB17-1 f : Maximum Mixedness Model with Bimodal Distribution""", fontweight='bold', x = 0.3)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)

sol = odeint(ODEfun, y0, zspan, (k1, k2))
ca= sol[:, 0]
cb= sol[:, 1]
cc= sol[:, 2]
F=sol[:, 3]
ra =   -k1*ca
rc =   k2*cb
rb =   k1*ca-k2*cb
X = 1 - ca/cao


p1 = ax2.plot(zspan, X)[0]
ax2.legend([r'$\overline{X}$'], loc="best")
ax2.set_xlabel(r'$z (mins)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 6)
ax2.grid()

p3, p4, p5 = ax3.plot(zspan, ca, zspan, cb, zspan, cc)
ax3.legend([r'${C_A}$', r'${C_B}$', r'${C_C}$'], loc="best")
ax3.set_xlabel(r'$z (mins)$', fontsize='medium')
ax3.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_ylim(0, 1)
ax3.set_xlim(0, 6)
ax3.grid()

p6, p7, p8 = ax4.plot(zspan, ra, zspan, rb, zspan, rc)
ax4.legend([r'$r_A$',r'$r_B$',r'$r_C$'], loc="best")
ax4.set_xlabel(r'$z (mins)$', fontsize='medium')
ax4.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
ax4.set_ylim(-3,3)
ax4.set_xlim(0, 6)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -1.5,'Differential Equations'
         '\n\n'
         r'$\dfrac{dC_A}{dz} = -(-r_A + (C_A - C_{A0})EF )$'
         '\n\n'
         r'$\dfrac{dC_B}{dz} = -(-r_B + (C_B - C_{B0})EF )$'
         '\n\n'
         r'$\dfrac{dC_C}{dz} = -(-r_C + (C_C - C_{C0})EF )$'       
         '\n\n'
         r'$\dfrac{dF}{dz} = -E$'
         '\n\n'
         'Explicit Equations'
         '\n\n'   
         r'$C_{A0} = 1$'
         '\n'
         r'$C_{C0} = 0$'
         '\n'
         r'$C_{B0} = 0$'
         '\n'         
         r'$\tau = 1.26$'
         '\n'         
         r'$r_A = -k_1C_A$'
         '\n'         
         r'$r_B = k_1C_A - k_2C_B$'
         '\n'         
         r'$r_C = k_2C_B$'
         '\n\n'         
         r'$X = 1 -\dfrac{C_A}{C_{A0}}$' 
         '\n\n'
         r'$\lambda = 6 - z$'
         '\n'          
         r'$E_1 = +0.47219\lambda^4 - 1.30733\lambda^3$' '\n\t' 
         r'$+ 0.31723\lambda^2 + 0.85688\lambda$''\n\t'
         r'$  + 0.20909$'
         '\n'
         r'$E_2 = +3.83999\lambda^6 - 58.16185\lambda^5   $' '\n\t' 
         r'$+ 366.2097\lambda^4 - 1224.6696\lambda^3$''\n\t'
         r'$+ 2289.84857\lambda^2 - 2265.62125\lambda$''\n\t'
         r'$+ 925.46463$'
         '\n'
         r'$E_3 = 0.00410\lambda^4 - 0.07593\lambda^3  $' '\n\t' 
         r'$+ + 0.52276\lambda^2 - 1.59457\lambda$''\n\t'
         r'$  + 1.84445$' '\n'         
         r'$E = IF (\lambda<=1.82) then (E_1)$''\n\t' 
         r'$else if (\lambda<=2.8) then(E_2) else (E_3)$''\n'
         r'$EF = \dfrac{E}{1-F}$'
         
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
    sol = odeint(ODEfun, y0, zspan, (k1, k2))
    ca= sol[:, 0]
    cb= sol[:, 1]
    cc= sol[:, 2]
    ra =   -k1*ca
    rc =   k2*cb
    rb =   k1*ca-k2*cb
    X = 1 - ca/cao    
    p1.set_ydata(X)
    p3.set_ydata(ca)
    p4.set_ydata(cb)
    p5.set_ydata(cc)
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
