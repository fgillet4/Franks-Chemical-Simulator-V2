#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
k1 = 1
k2 = 1
k3 = 1
cao=1
def ODEfun(Yfuncvec, t, k1, k2, k3): 
    ca= Yfuncvec[0]
    cb= Yfuncvec[1]
    cc= Yfuncvec[2]
    cabar= Yfuncvec[3]
    cbbar= Yfuncvec[4]
    ccbar= Yfuncvec[5]
    cd= Yfuncvec[6]
    ce= Yfuncvec[7]
    # Explicit equations
    E1 = -2.104*t**4+4.167*t**3-1.596*t**2+0.353*t-0.004
    E2 = -2.104*t**4+17.037*t**3-50.247*t**2+62.964*t-27.402
    rc = k1*ca*cb
    re = k3*cb*cd 
    ra = -k1*ca*cb-k2*ca
    rb = -k1*ca*cb-k3*cb*cd
    rd = k2*ca-k3*cb*cd
    X=(cao-ca)/cao
    E = np.where(t<=1.26, E1, E2)
    # Differential equations
    dcadt = ra
    dcbdt = rb
    dccdt = rc
    dcabardt = ca*E
    dcbbardt = cb*E
    dccbardt = cc*E
    dcddt = rd
    dcedt = re
    dcdbardt = cd*E
    dcebardt = ce*E
    dXbardt=X*E
    return np.array([dcadt,dcbdt,dccdt,dcabardt,dcbbardt,dccbardt,dcddt,dcedt,dcdbardt,dcebardt,dXbardt])

tspan = np.linspace(0, 2.52, 100) # Range for the independent variable
y0 = np.array([1,1,0,0,0,0,0,0,0,0,0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 17-6a Segregation model with Asymmetric RTD (Multiple Reactions)""", x = 0.28, y = 0.98, fontweight='bold')
fig.subplots_adjust(wspace=0.25,hspace=0.3)
plt.subplots_adjust(left  = 0.4)

sol = odeint(ODEfun, y0, tspan, (k1, k2, k3))
ca= sol[:,0]
cb= sol[:,1]
cc= sol[:,2]
cabar= sol[:,3]
cbbar= sol[:,4]
ccbar= sol[:,5]
cd= sol[:,6]
ce= sol[:,7]
cdbar= sol[:,8]
cebar= sol[:,9]
Xbar= sol[:,10]
E1 = -2.104*tspan**4+4.167*tspan**3-1.596*tspan**2+0.353*tspan-0.004
E2 = -2.104*tspan**4+17.037*tspan**3-50.247*tspan**2+62.964*tspan-27.402
rc = k1*ca*cb
re = k3*cb*cd 
ra = -k1*ca*cb-k2*ca
rb = -k1*ca*cb-k3*cb*cd
rd = k2*ca-k3*cb*cd
X=(cao-ca)/cao
E = np.where(tspan<=1.26, E1, E2)
Scd = ccbar/(cdbar+0.00001)
Sde = cdbar/(cebar+0.00001)

p1, p2 = ax1.plot(tspan, X, tspan, Xbar)
ax1.legend([r'$X$', r'$\overline{X}$'], loc='best')
ax1.set_xlabel('t (mins)', fontsize='medium' )
ax1.set_ylabel(r'$Conversion$', fontsize='medium')
ax1.set_ylim(0,1)
ax1.set_xlim(0,2.52)
ax1.grid()

p3, p4, p5, p6, p7 = ax2.plot(tspan, cabar, tspan, cbbar, tspan, ccbar, tspan, cdbar, tspan, cebar)
ax2.legend([r'$\overline{C_A}$', r'$\overline{C_B}$',r'$\overline{C_C}$',r'$\overline{C_D}$',r'$\overline{C_E}$'], loc='best')
ax2.set_ylim(0,1)
ax2.set_xlim(0,2.52)
ax2.grid()
ax2.set_xlabel('t (mins)', fontsize='medium' )
ax2.set_ylabel(r'$Concentration \thinspace (\frac{mol}{dm^3})$', fontsize='medium')
#ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p8 ,p9, p10, p11, p12 = ax3.plot(tspan, ra, tspan, rb, 
                                tspan, rc, tspan, rd, 
                                tspan, re )
ax3.legend([r'$r_A$',r'$r_B$',r'$r_C$',r'$r_D$',r'$r_E$',], loc='best')
ax3.set_ylim(-3,3)
ax3.set_xlim(0,2.52)
ax3.grid()
ax3.set_xlabel('t (mins)', fontsize='medium' )
ax3.set_ylabel(r'$Rate \thinspace (\frac{mol}{dm^3.min })$', fontsize='medium')
#ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p13, p14 = ax4.plot(tspan, Scd, tspan, Sde)
ax4.legend([r'$S_{C/D}$', r'$S_{D/E}$'], loc='best')
ax4.set_ylim(0,20)
ax4.set_xlim(0,2.52)
ax4.grid()
ax4.set_xlabel('t (mins)', fontsize='medium' )
ax4.set_ylabel('Selectivity', fontsize='medium' )
#ax4.ticklabel_format(style='sci',scilimits=(-6,-3),axis='y')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax1.text(-2.1, -1.3,'Differential Equations'
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

ax1.text( -4.4, -1.1,
         'Explicit Equations'
         '\n\n'   
         r'$C_{A0} = 1$'
         '\n\n'
         r'$\tau = 1.26$'
         '\n\n'         
         r'$r_A = -k_1C_AC_B - k_2C_A$'
         '\n\n'         
         r'$r_B = -k_1C_AC_B - k_3C_BC_D$'
         '\n\n'         
         r'$r_C = k_1C_AC_B$'
         '\n\n'    
         r'$r_D = k_2C_A - k_3C_BC_D$'
         '\n\n'         
         r'$r_E = k_3C_BC_D$'

         '\n\n'         
         r'$X = 1 -\dfrac{C_A}{C_{A0}}$' 
         '\n\n'          
         r'$E_1 = -2.104t^4 + 4.167t^3$' '\n\t' 
         r'$- 1.596t^2 + 0.353t $''\n\t'
         r'$- 0.004$'
         '\n'
         r'$E_2 = -2.104t^4 + 17.037t^3 $' '\n\t' 
         r'$- 50.247t^2 + 62.96t $''\n\t'
         r'$- 27.402$'
         '\n'
         r'$E = IF\hspace{0.5} (t<\tau) \hspace{0.5}then\hspace{0.5} (E_1)\hspace{0.5} else\hspace{0.5} (E_2)$''\n\n'
         r'$S_{C/D} = \dfrac{C_C}{C_{D}}$' 
         '\n\n'
         r'$S_{D/E} = \dfrac{C_D}{C_{E}}$' 
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

#%%
axcolor = 'black'
ax_k1 = plt.axes([0.22, 0.8, 0.1, 0.02], facecolor=axcolor)
ax_k2 = plt.axes([0.22, 0.75, 0.1, 0.02], facecolor=axcolor)
ax_k3 = plt.axes([0.22, 0.7, 0.1, 0.02], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=0.000001)
sk2= Slider(ax_k2, r'$k_2 (min^{-1})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=1)
sk3 = Slider(ax_k3, r'$k_3 (\frac{dm^3}{mol.min})$', 0.01, 15, valinit=1,valfmt='%1.2f', valstep=1)


def update_plot2(val):
    k1 = sk1.val
    k2 =sk2.val
    k3 =sk3.val
    sol = odeint(ODEfun, y0, tspan, (k1, k2, k3))
    ca= sol[:,0]
    cb= sol[:,1]
    cc= sol[:,2]
    ccbar= sol[:,5]
    cd= sol[:,6]
    ce= sol[:,7]
    cdbar= sol[:,8]
    cebar= sol[:,9]
    Xbar= sol[:,10]
    rc = k1*ca*cb
    re = k3*cb*cd 
    ra = -k1*ca*cb-k2*ca
    rb = -k1*ca*cb-k3*cb*cd
    rd = k2*ca-k3*cb*cd
    X=(cao-ca)/cao
    Scd = ccbar/(cdbar+0.00001)
    Sde = cdbar/(cebar+0.00001)
    p1.set_ydata(X)
    p2.set_ydata(Xbar)
    p3.set_ydata(ca)
    p4.set_ydata(cb)
    p5.set_ydata(cc)
    p6.set_ydata(cd)
    p7.set_ydata(ce)
    p8.set_ydata(ra)
    p9.set_ydata(rb)
    p10.set_ydata(rc)
    p11.set_ydata(rd)    
    p12.set_ydata(re)
    p13.set_ydata(Scd)
    p14.set_ydata(Sde)     
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
#

resetax = plt.axes([0.2, 0.85, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
button.on_clicked(reset)