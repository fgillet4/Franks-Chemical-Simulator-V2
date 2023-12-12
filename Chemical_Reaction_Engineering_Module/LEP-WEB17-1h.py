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
k1 =  1
k2 =  1
k3 =  1 
cao = 1
cbo = 1
cco = 0
cdo = 0  
ceo = 0
def ODEfun(Yfuncvec, z, k1, k2, k3): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]
    cd=Yfuncvec[3]
    ce=Yfuncvec[4]
    F=Yfuncvec[5]
    # Explicit equations
    ra =  -k1*ca*cb-k2*ca
    rc =  k1*ca*cb
    rb =  -k1*ca*cb-k3*cb*cd
    rd =  k2*ca-k3*cb*cd
    re =  k3*cb*cd
    lam =   2.52-z
    E1 =  -2.104*lam**4+4.167*lam**3-1.596*lam**2+0.353*lam-0.004
    E2 =  -2.104*lam**4+17.037*lam**3-50.247*lam**2+62.964*lam-27.402
    E = np.where(lam<=1.26, E1, E2)
    EF =   E/(1-F)
    # Differential equations
    dcadz = -(-ra+(ca-cao)*EF)
    dcbdz = -(-rb+(cb-cbo)*EF)
    dccdz = -(-rc+(cc-cco)*EF)
    dcddz = -(-rd+(cd-cdo)*EF)
    dcedz = -(-re+(ce-ceo)*EF)
    dFdz =  -E
    return np.array([dcadz,dcbdz,dccdz,dcddz,dcedz,dFdz])

zspan = np.linspace(0, 2.52, 1000)
y0 = np.array([1, 1, 0, 0, 0 ,0.99])
#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-WEB17-1h : Maximum Mixedness Model with Asymmetric RTD (Multiple Reactions)""", x = 0.4, y = 0.98, fontweight='bold')

plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, zspan, (k1, k2, k3))
ca= sol[:, 0]
cb= sol[:, 1]
cc= sol[:, 2]
cd=sol[:, 3]
ce=sol[:, 4]
F=sol[:, 5]
Scd = cc/(cd+0.00001)
Sde = cd/(ce+0.00001)
X = (cao - ca)/(cao)
ra =  -k1*ca*cb-k2*ca
rc =  k1*ca*cb
rb =  -k1*ca*cb-k3*cb*cd
rd =  k2*ca-k3*cb*cd
re =  k3*cb*cd
    
p1 = ax1.plot(zspan, X)[0]
ax1.legend([r'$\overline{X}$'], loc='best')
ax1.set_xlabel('z (mins)', fontsize='medium' )
ax1.set_ylabel('Conversion', fontsize='medium')
ax1.set_ylim(0,1)
ax1.set_xlim(0,2.52)
ax1.grid()

p2, p3, p4, p5, p6 = ax2.plot(zspan, ca, zspan, cb, zspan, cc, zspan, cd, zspan, ce)
ax2.legend([r'${C_A}$', r'${C_B}$',r'${C_C}$',r'${C_D}$',r'${C_E}$',], loc='best')
ax2.set_ylim(0,1)
ax2.set_xlim(0,2.52)
ax2.grid()
ax2.set_xlabel('z (mins)', fontsize='medium' )
ax2.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$',fontsize='medium')
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p7, p8, p9, p10, p11 = ax3.plot(zspan, ra, zspan, rb, zspan, rc, zspan, rd, zspan, re)
ax3.legend([r'$r_A$', r'$r_B$', r'$r_C$', r'$r_D$', r'$r_E$'], loc='best')
ax3.set_ylim(-3, 3)
ax3.set_xlim(0, 2.52)
ax3.grid()
ax3.set_xlabel('z (mins)', fontsize='medium' )
ax3.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p12, p13 = ax4.plot(zspan, Scd, zspan, Sde)
ax4.legend([r'$S_{C/D}$', r'$S_{D/E}$'], loc='best')
ax4.set_ylim(0,20)
ax4.set_xlim(0,2.52)
ax4.grid()
ax4.set_xlabel('z (mins)', fontsize='medium' )
ax4.set_ylabel('Selectivity', fontsize='medium' )
#ax4.ticklabel_format(style='sci',scilimits=(-6,-3),axis='y')
#ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax1.text(-4, -0.8,'Differential Equations'
         '\n'
         r'$\dfrac{dC_A}{dz} = -(-r_A + (C_A - C_{A0})EF )$'
         '\n\n'
         r'$\dfrac{dC_B}{dz} = -(-r_B + (C_B - C_{B0})EF )$'
         '\n\n'
         r'$\dfrac{dC_C}{dz} = -(-r_C + (C_C - C_{C0})EF )$'          
         '\n'
         r'$\dfrac{dC_D}{dt} = -(-r_D + (C_D - C_{D0})EF )$'
         '\n'
         r'$\dfrac{dC_E}{dt} = -(-r_E + (C_E - C_{E0})EF )$'
         '\n'    
         r'$\dfrac{dF}{dz} = -E$' '\n'

         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
ax1.text( -2.2, -1.5 ,'Explicit Equations' '\n'   
         r'$C_{A0} = 1$'
         '\n'
                  r'$C_{B0} = 1$'
         '\n'
                  r'$C_{C0} = 0$'
         '\n'
                  r'$C_{D0} = 0$'
         '\n'
                  r'$C_{E0} = 0$'
         '\n'
         r'$\tau = 1.26$'
         '\n' 
         r'$\lambda = 2.52 - z$'
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
         r'$E_1 = -2.104\lambda^4 + 4.167\lambda^3$' '\n\t' 
         r'$- 1.596\lambda^2 + 0.353\lambda $''\n\t'
         r'$- 0.004$'
         '\n'
         r'$E_2 = -2.104\lambda^4 + 17.037\lambda^3 $' '\n\t' 
         r'$- 50.247\lambda^2 + 62.964\lambda $''\n\t'
         r'$- 27.402$'
         '\n'
         r'$E = IF (\lambda<=\tau) then (E_1) else (E_2)$'
         '\n'
         r'$EF = \dfrac{E}{1-F}$'
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k1 = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k3 = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f')
sk2 = Slider(ax_k2, r'$k_2 (min^{-1})$', 0.01, 15, valinit=1,valfmt='%1.2f')
sk3 = Slider(ax_k3, r'$k_3 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f')


def update_plot2(val):
    k1 = sk1.val
    k2 =sk2.val
    k3 =sk3.val
    sol = odeint(ODEfun, y0, zspan, (k1, k2, k3))
    ca= sol[:, 0]
    cb= sol[:, 1]
    cc= sol[:, 2]
    cd=sol[:, 3]
    ce=sol[:, 4]
    Scd = cc/(cd+0.00001)
    Sde = cd/(ce+0.00001)
    X = (cao - ca)/(cao)
    ra =  -k1*ca*cb-k2*ca
    rc =  k1*ca*cb
    rb =  -k1*ca*cb-k3*cb*cd
    rd =  k2*ca-k3*cb*cd
    re =  k3*cb*cd

    p1.set_ydata(X)
    p2.set_ydata(ca)
    p3.set_ydata(cb)
    p4.set_ydata(cc)
    p5.set_ydata(cd)
    p6.set_ydata(ce)
    p7.set_ydata(ra)
    p8.set_ydata(rb)
    p9.set_ydata(rc)
    p10.set_ydata(rd) 
    p11.set_ydata(re)
    p12.set_ydata(Scd)
    p13.set_ydata(Sde) 
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