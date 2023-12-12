#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
U = 1; 
DAB = 10**-8; 
dp = 10**-3; 
kr = 0.5; 
rho = 1000; 
mu = 10**-3;
Ca0 = 1; 
phi = 0.4;
y = 1; 
Ac = 0.05;
rhoc = 3000; 
def ODEfun(Yfuncvec,W,U,DAB,dp,kr,rho,mu,Ca0,phi,y,Ac,rhoc):
    X= Yfuncvec[0]
    #Explicit Equation Inline
    Ca = Ca0*(1-X) 
    acprime=6*(1-phi)/(dp*rhoc)
    nu=mu/rho
    Sc = nu/DAB 
    Re = dp*U/nu
    Reprime=Re/((1-phi)*y)
    Shprime = (Reprime**(1/2))*(Sc**(1/3)) 
    kc = Shprime*DAB*(1-phi)*y/(dp*phi) 
    k = kc*kr/ (kc+kr) 
    ra = -k*Ca 
    raprime=acprime*ra
    Fa0=Ca0*U*Ac
    
        # Differential equations
    dXdW = -raprime/Fa0; 
    return np.array([dXdW])

Wspan = np.linspace(0, 100, 1000) # Range for the independent variable
y0 = np.array([0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.4)
fig.suptitle("""LEP-14-7: Flow, Diffusion and Reaction in a Packed Bed """, fontweight='bold', x = 0.5,y=0.97)
plt.subplots_adjust(left  = 0.3)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, Wspan, (U,DAB,dp,kr,rho,mu,Ca0,phi,y,Ac,rhoc))
X =sol[:, 0]

Ca = Ca0*(1-X) 
acprime=6*(1-phi)/(dp*rhoc)
nu=mu/rho
Sc = nu/DAB 
Re = dp*U/nu
Reprime=Re/((1-phi)*y)
Shprime = (Reprime**(1/2))*(Sc**(1/3)) 
kc = Shprime*DAB*(1-phi)*y/(dp*phi) 
k=[]
ra=[]
WA=[]
for i in range(len(Wspan)):
    k.append(kc*kr/ (kc+kr))
    ra=(-k[i]*Ca[i]) 
    WA.append(-ra)

p1= ax2.plot(Wspan,X)[0]
ax2.legend(['X'], loc='upper right')
ax2.set_xlabel(r'$W(kg)$', fontsize='medium')
ax2.set_ylabel('Conversion', fontsize='medium')
ax2.set_ylim(0,1)
ax2.set_xlim(0,100)
ax2.grid()

p2 = ax3.plot(Wspan,WA)[0]
ax3.legend(['$W_A$'], loc='upper right')
ax3.set_ylim(0,0.005)
ax3.set_xlim(0,100)
ax3.grid()
ax3.set_xlabel(r'$W(kg)$', fontsize='medium')
ax3.set_ylabel('Molar Flux ($mol/m^2.s$)', fontsize='medium')


p3 = ax4.plot(Wspan,k)[0]
ax4.legend(['$k$'], loc='upper right')
ax4.set_ylim(0,0.01)
ax4.set_xlim(0,100)
ax4.grid()
ax4.set_xlabel(r'$W(kg)$', fontsize='medium')
ax4.set_ylabel(r'Rate Constant (m/s)', fontsize='medium')

ax1.axis('off')
ax1.text(-1.05, -1.35,'Differential Equations'
         '\n\n'
         r'$\dfrac{dX}{dW} = -\dfrac{r_A^\prime}{F_{A0}}$'
         '\n\n'
          'Explicit Equations'
                  '\n\n'
         r'$C_{A}=C_{A0}*(1-X)$'
                  '\n\n'         
         r'$\nu=\dfrac{\mu}{\rho}$'
                  '\n\n'
         r'$S_{c} = \dfrac{\nu}{D_{AB}}$'   
           '\n\n'
         r'$R_{e} = \dfrac{d_{p}*U}{\nu}$'   
           '\n\n'
         r'$R_{e}^\prime = \dfrac{R_{e}}{(1-\phi)*y}$'
         '\n\n'
         r'$S_{h}^\prime =1.0*(R_{e}^\prime)^{(1/2)}*(S_{c})^{(1/3)}$'
         '\n\n'
          r'$k_c = D_{AB}*\dfrac{(1-\phi)}{d_p* \phi}*y*\left(S_{h}^\prime \right)$'
         '\n\n'
          r'$k = \dfrac{k_c* k_r}{k_{c}+ k_{r}}$'
         '\n\n'
         r'$-r_A ^{\prime \prime} = k*C_A$'
         '\n\n'
         r'$F_{A0} = C_{A0}*U*A_{c}$'
                  '\n\n'
         r'$W_{A} = -r_A ^{\prime \prime}$'
                  '\n\n'
         r'$a_{c}^\prime = 6*\dfrac{(1-\phi)}{d_p*\rho_{C}}$'
                  '\n\n'
         r'$-r_{A}^\prime= a_{c}^\prime *(-r_A ^{\prime \prime}) $'
                  '\n\n'
        , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
axcolor = 'black'
ax_U = plt.axes([0.32, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_DAB = plt.axes([0.32, 0.79, 0.2, 0.015], facecolor=axcolor)
ax_dp = plt.axes([0.32, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_kr = plt.axes([0.32, 0.73, 0.2, 0.015], facecolor=axcolor)
ax_rho = plt.axes([0.32, 0.70, 0.2, 0.015], facecolor=axcolor)
ax_mu = plt.axes([0.32, 0.67, 0.2, 0.015], facecolor=axcolor)
ax_Ca0 = plt.axes([0.32, 0.64, 0.2, 0.015], facecolor=axcolor)
ax_phi = plt.axes([0.32, 0.61, 0.2, 0.015], facecolor=axcolor)
ax_y = plt.axes([0.32, 0.58, 0.2, 0.015], facecolor=axcolor)
ax_Ac = plt.axes([0.32, 0.55, 0.2, 0.015], facecolor=axcolor)
ax_rhoc = plt.axes([0.32, 0.52, 0.2, 0.015], facecolor=axcolor)

sU = Slider(ax_U, r'$U$ ($\frac{m}{s}$)', 0.01, 200, valinit=1,valfmt='%1.1f')
sDAB= Slider(ax_DAB, r'$D_{AB}$ ($\frac{m^2}{s}$)', 10**-11, 10**-4, valinit=10**-8,valfmt='%1.1E')
sdp = Slider(ax_dp,r'$d_P (m)$',0.0001, 0.1, valinit=10**-3,valfmt='%1.0E')
skr = Slider(ax_kr,r'$k_{r}$ ($\frac{m}{s}$)', 0.00001, 50, valinit= 0.5,valfmt='%1.2f')
srho = Slider(ax_rho,r'${\rho}$ ($\frac{kg}{m^3}$)', 0.1, 1800, valinit=1000,valfmt='%1.0f')
smu = Slider(ax_mu,r'$\mu$ ($\frac{kg}{m.s}$)', 0.00001, 10, valinit= 10**-3,valfmt='%1.1E')
sCa0 = Slider(ax_Ca0, r'$C_{A0}$ ($\frac{mol}{m^3}$)', 0.001, 10, valinit=1,valfmt='%1.1f')
sphi = Slider(ax_phi, r'$\phi$', 0.01, 1, valinit=0.4,valfmt='%1.1f')
sy= Slider(ax_y, r'y', 0.01, 5, valinit=1,valfmt='%1.1f')
sAc= Slider(ax_Ac, r'$A_{C}$ ($m^2$)', 0.01, 0.5, valinit=0.05,valfmt='%1.2f')
srhoc= Slider(ax_rhoc, r'$\rho_{C}$ ($\frac{kg}{m^3}$)', 500, 30000, valinit=3000,valfmt='%1.0f')

def update_plot2(val):
    U = sU.val
    DAB =sDAB.val
    dp = sdp.val
    kr =skr.val
    rho = srho.val
    mu=smu.val
    Ca0 = sCa0.val
    phi= sphi.val
    y= sy.val
    Ac=sAc.val
    rhoc=srhoc.val
    sol = odeint(ODEfun, y0, Wspan, (U,DAB,dp,kr,rho,mu,Ca0,phi,y,Ac,rhoc))
    X =sol[:, 0]
    
    Ca = Ca0*(1-X) 
    nu=mu/rho
    Sc = nu/DAB 
    Re = dp*U/nu
    Reprime=Re/((1-phi)*y)
    Shprime = (Reprime**(1/2))*(Sc**(1/3)) 
    kc = Shprime*DAB*(1-phi)*y/(dp*phi) 
    k = kc*kr/ (kc+kr) 
    ra = -k*Ca 
    WA=-ra
    p1.set_ydata(X)
    p2.set_ydata(WA)
    p3.set_ydata(k)

    fig.canvas.draw_idle()


sU.on_changed(update_plot2)
sDAB.on_changed(update_plot2)
sdp.on_changed(update_plot2)
skr.on_changed(update_plot2)
srho.on_changed(update_plot2)
smu.on_changed(update_plot2)
sCa0.on_changed(update_plot2)
sphi.on_changed(update_plot2)
sy.on_changed(update_plot2)
sAc.on_changed(update_plot2)
srhoc.on_changed(update_plot2)

resetax = plt.axes([0.37, 0.86, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sU.reset()
    sDAB.reset()
    sdp.reset()
    skr.reset()
    srho.reset()
    smu.reset()
    sCa0.reset()
    sphi.reset()
    sy.reset()
    sAc.reset()
    srhoc.reset()
button.on_clicked(reset)
    
