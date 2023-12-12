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
cao=1
k1 =  1
k2 =  1
k3 =  1
def ODEfun(Yfuncvec, t, k1, k2, k3): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]
    cabar=Yfuncvec[3]
    cbbar=Yfuncvec[4]
    ccbar=Yfuncvec[5]
    cd=Yfuncvec[6]
    ce=Yfuncvec[7]
    cdbar=Yfuncvec[8]
    cebar=Yfuncvec[9]
    Xbar=Yfuncvec[10]

    E1 =  0.47219*t**4-1.30733*t**3+0.31723*t**2+0.85688*t+0.20909
    E2 =  3.83999*t**6-58.16185*t**5+366.2097*t**4-1224.66963*t**3+2289.84857*t**2-2265.62125*t+925.46463
    E3 =  0.00410*t**4-0.07593*t**3+0.52276*t**2-1.59457*t+1.84445
    rc =  k1*ca*cb
    re =  k3*cb*cd
    ra =  -k1*ca*cb-k2*ca
    rb =  -k1*ca*cb-k3*cb*cd
    rd =  k2*ca-k3*cb*cd
    X=1-ca/cao
    if t<=1.82:
        E =E1
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
    dcddt =  rd
    dcedt =  re
    dcdbardt =  cd*E
    dcebardt =  ce*E
    dXbardt =  X*E
    return np.array([dcadt,dcbdt,dccdt,dcabardt,dcbbardt,dccbardt,dcddt,dcedt,dcdbardt,dcebardt,dXbardt])
tspan = np.linspace(0, 6, 1000)
y0 = np.array([1, 1, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0])
#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-WEB17-1g : Segregation Model with Bimodal Distribution (Multiple Reactions)""", x = 0.35, y = 0.98, fontweight='bold')
fig.subplots_adjust(wspace=0.25,hspace=0.3)
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, tspan, (k1, k2, k3))
ca= sol[:, 0]
cb= sol[:, 1]
cc= sol[:, 2]
cabar=sol[:, 3]
cbbar=sol[:, 4]
ccbar=sol[:, 5]
cd=sol[:, 6]
ce=sol[:, 7]
cdbar=sol[:, 8]
cebar=sol[:, 9]
Xbar=sol[:, 10]
Scd = cc/(cd+0.00001)
Sde = cd/(ce+0.00001)
X = (cao - ca)/(cao)
rc =  k1*ca*cb
re =  k3*cb*cd
ra =  -k1*ca*cb-k2*ca
rb =  -k1*ca*cb-k3*cb*cd
rd =  k2*ca-k3*cb*cd
    
p1, p14 = ax1.plot(tspan, X, tspan, Xbar)
ax1.legend(['X', '$X_{bar}$'], loc='best')
ax1.set_xlabel('t (mins)', fontsize='medium' )
ax1.set_ylabel('Conversion', fontsize='medium')
ax1.set_ylim(0,1)
ax1.set_xlim(0,6)
ax1.grid()

p2, p3, p4, p5, p6 = ax2.plot(tspan, cabar, tspan, cbbar, tspan, ccbar, tspan, cdbar, tspan, cebar)
ax2.legend([r'$\overline{C_A}$', r'$\overline{C_B}$',r'$\overline{C_C}$',r'$\overline{C_D}$',r'$\overline{C_E}$',], loc='best')
ax2.set_ylim(0,1)
ax2.set_xlim(0,6)
ax2.grid()
ax2.set_xlabel('t (mins)', fontsize='medium' )
ax2.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p7, p8, p9, p10, p11 = ax3.plot(tspan, ra, tspan, rb, tspan, rc, tspan, rd, tspan, re)
ax3.legend([r'$r_A$', r'$r_B$', r'$r_C$', r'$r_D$', r'$r_E$'], loc='best')
ax3.set_ylim(-3, 3)
ax3.set_xlim(0, 6)
ax3.grid()
ax3.set_xlabel('t (mins)', fontsize='medium' )
ax3.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p12, p13 = ax4.plot(tspan, Scd, tspan, Sde)
ax4.legend([r'$S_{C/D}$', r'$S_{D/E}$'], loc='best')
ax4.set_ylim(0,20)
ax4.set_xlim(0,6)
ax4.grid()
ax4.set_xlabel('t (mins)', fontsize='medium' )
ax4.set_ylabel('Selectivity', fontsize='medium' )
#ax4.ticklabel_format(style='sci',scilimits=(-6,-3),axis='y')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax1.text(-4.5, -1.3,'Differential Equations'
         '\n'
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
         r'$\dfrac{dC_D}{dt} = r_D$'
         '\n'
         r'$\dfrac{dC_E}{dt} = r_E$'
         '\n'    
         r'$\dfrac{d\overline{C_D}}{dt} = C_D.E$'
         '\n'
         r'$\dfrac{d\overline{C_E}}{dt} = C_E.E$' 
                  '\n'              
         r'$\dfrac{d\overline{X}}{dt} = X.E$' '\n'

         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
ax1.text( -9.5, -1.45 ,'Explicit Equations' '\n'   
         r'$C_{A0} = 1$'
         '\n'        
         r'$r_A = -k_1C_AC_B - k_2C_A$'
         '\n'         
         r'$r_B = -k_1C_AC_B - k_3C_BC_D$'
         '\n'         
         r'$r_C = k_1C_AC_B$'
         '\n'    
         r'$r_D = k_2C_A - k_3C_BC_D$'
         '\n'         
         r'$r_E = k_3C_BC_D$'
         '\n'            
         r'$X = 1 -\dfrac{C_A}{C_{Ao}}$' 
         '\n'
         r'$S_{C/D} = \dfrac{C_C}{C_{D}}$' 
         '\n'
         r'$S_{D/E} = \dfrac{C_D}{C_{E}}$' 
         '\n'        
         r'$E_1 = +0.47219t^4 - 1.30733t^3$' '\n\t' 
         r'$+ 0.31723t^2 + 0.85688t$''\n\t'
         r'$  + 0.20909$'
         '\n'
         r'$E_2 = +3.83999t^6 - 58.16185t^5   $' '\n\t' 
         r'$+ 366.2097t^4 - 1224.6696t^3$''\n\t'
         r'$+ 2289.84857t^2 - 2265.62125t$''\n\t'
         r'$+ 925.46463$'
         '\n'
         r'$E_3 = 0.00410t^4 - 0.07593t^3  $' '\n\t' 
         r'$+ + 0.52276t^2 - 1.59457t$''\n\t'
         r'$  + 1.84445$' '\n'         
         r'$E = IF (t<=1.82) then (E_1)$''\n\t' 
         r'$else if (t<=2.8) then(E_2) else (E_3)$''\n'
         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k1 = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k3 = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=0.000001)
sk2 = Slider(ax_k2, r'$k_2 (min^{-1})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=1)
sk3 = Slider(ax_k3, r'$k_3 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=1)


def update_plot2(val):
    k1 = sk1.val
    k2 =sk2.val
    k3 =sk3.val
    sol = odeint(ODEfun, y0, tspan, (k1, k2, k3))
    ca= sol[:, 0]
    cb= sol[:, 1]
    cc= sol[:, 2]
    cabar=sol[:, 3]
    cbbar=sol[:, 4]
    ccbar=sol[:, 5]
    cd=sol[:, 6]
    ce=sol[:, 7]
    cdbar=sol[:, 8]
    cebar=sol[:, 9]
    Xbar=sol[:, 10]
    rc =  k1*ca*cb
    re =  k3*cb*cd
    ra =  -k1*ca*cb-k2*ca
    rb =  -k1*ca*cb-k3*cb*cd
    rd =  k2*ca-k3*cb*cd    
    Scd = cc/(cd+0.00001)
    Sde = cd/(ce+0.00001)
    X = (cao - ca)/(cao)

    p1.set_ydata(X)
    p2.set_ydata(cabar)
    p3.set_ydata(cbbar)
    p4.set_ydata(ccbar)
    p5.set_ydata(cdbar)
    p6.set_ydata(cebar)
    p7.set_ydata(ra)
    p8.set_ydata(rb)
    p9.set_ydata(rc)
    p10.set_ydata(rd) 
    p11.set_ydata(re)
    p12.set_ydata(Scd)
    p13.set_ydata(Sde) 
    p14.set_ydata(Xbar)
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
#

resetax = plt.axes([0.15, 0.85, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
button.on_clicked(reset)	