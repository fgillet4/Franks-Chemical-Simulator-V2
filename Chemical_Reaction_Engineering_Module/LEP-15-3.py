#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

rhoc=2.8*10**6
De=1.82*10**-8
DAB=2*10**-8
Sa=530
k1doubleprime=4.42*10**-10
vo=10**-6
Ac=2.03*10**-3
phi=0.5
vis=1.53*10**-8
R = np.linspace(0,0.005, 1000)
W = np.linspace(0,1000, 1000)
R1=0.003;
k1prime=k1doubleprime*Sa
phi1=R*np.sqrt(k1prime*rhoc/De)
phi11=R1*np.sqrt(k1prime*rhoc/De)
eff=(3/phi1**2) *(phi1*(1/np.tanh(phi1))-1)
eff1=(3/phi11**2) *(phi11*(1/np.tanh(phi11))-1)
CWP=eff*phi1*phi1
U=vo/Ac
dp=2*R
Re=U*dp/((1-phi)*vis)
Sc=vis/DAB
Sh=(Re**0.5)*(Sc**(1/3))

kc=(1-phi)*DAB*Sh/(phi*2*R)
kc1=(1-phi)*DAB*Sh/(phi*2*R1)
ac=6*(1-phi)/dp
ac1=6*(1-phi)/(2*R1)
rhob=rhoc*(1-phi)
effoverall=eff/(1+(eff*k1doubleprime*Sa*rhob)/(kc*ac))
effoverall1=eff1/(1+(eff1*k1doubleprime*Sa*rhob)/(kc1*ac1))
MR=effoverall*k1prime*rhob*R/kc

CAB0 = 2;
CAB = CAB0*np.exp(-effoverall1*k1prime*W/(vo));
X = (CAB0 - CAB)/CAB0;




#%%
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
plt.subplots_adjust(left=0.4, bottom = 0.1)
fig.subplots_adjust(wspace=0.4,hspace=0.4)
fig.suptitle("""LEP-15-3: Reducing Nitrous Oxides in a Plant's Effluent""", fontweight='bold', x = 0.2, y=0.98)

p1 = ax1.plot(R,eff)[0]
ax1.grid()
ax1.set_ylabel('$\eta$', fontsize='medium', fontweight='bold')
ax1.set_xlabel('Pellet Radius, R (m)', fontsize='medium',)
ax1.set_ylim(0, 1)
ax1.set_xlim(0, 0.005)
#
p2 = ax2.plot(R,CWP)[0]
ax2.grid()
ax2.set_ylabel('$WP$', fontsize='medium', fontweight='bold')
ax2.set_xlabel('Pellet Radius, R (m)', fontsize='medium',)
ax2.set_ylim(0, 100)
ax2.set_xlim(0, 0.005)

p3 = ax3.plot(R,effoverall)[0]
ax3.grid()
ax3.set_ylabel('$\Omega$', fontsize='medium', fontweight='bold')
ax3.set_xlabel('Pellet Radius, R (m)', fontsize='medium',)
ax3.set_ylim(0, 1)
ax3.set_xlim(0, 0.005)

p4 = ax4.plot(R,MR)[0]
ax4.grid()
ax4.set_ylabel('$MR$', fontsize='medium', fontweight='bold')
ax4.set_xlabel('Pellet Radius, R (m)', fontsize='medium',)
ax4.set_ylim(0, 3)
ax4.set_xlim(0, 0.005)

p5 = ax5.plot(W,X)[0]
ax5.grid()
ax5.set_ylabel('$Conversion$', fontsize='medium', fontweight='bold')
ax5.set_xlabel('Catalyst Weight,W(gm)', fontsize='medium',)
ax5.set_ylim(0, 1)
ax5.set_xlim(0, 1000)

p6 = ax6.plot(W,CAB)[0]
ax6.grid()
ax6.set_ylabel('$Concentration (mol/dm^3)$', fontsize='medium', fontweight='bold')
ax6.set_xlabel('Catalyst Weight,W(gm)', fontsize='medium',)
ax6.set_ylim(0, 2)
ax6.set_xlim(0, 1000)

ax1.text(-0.0075, -3.10,
         'Equations'
         '\n\n'
         r'$k_1^\prime = k_1^{\prime\prime}* S_a$'
                  '\n\n'
         r'$\phi_1 = R*\sqrt{\dfrac{k_1^\prime* \rho_c}{D_e}}$'
                  '\n\n'
         r'$\eta = \dfrac{3}{\phi_1^2} \left(\phi_1 coth \thinspace \phi_1-1\right)$'
         '\n\n'
         r'$C_{WP} = \eta*\phi_1^2$'
         '\n\n'
         r'$U = \dfrac{v_0}{A_c}$'
         '\n\n'
         r'$R_e^\prime = \dfrac{U*d_p}{(1-\phi)\nu}$'
         '\n\n'
         r'$S_c = \dfrac{\nu}{D_{AB}}$'
         '\n\n'
         r'$S_h^\prime = (R_e)^{1/2}(S_c)^{1/3}$'
        , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

ax1.text(-0.0045, -3.1,
         'Equations'
         '\n\n'
         r'$k_c = \dfrac{1-\phi}{\phi}*\left(\dfrac{D_{AB}}{d_p}\right)*S_h^\prime$'
         '\n\n'
         r'$a_c = \dfrac{6*(1-\phi)}{d_p}$'
         '\n\n'
         r'$\rho_b = \rho_c*(1-\phi)$'
         '\n\n'
         r'$\Omega = \dfrac{\eta}{1+\eta*k_1^{\prime\prime} *S_a *\rho_b/(k_c*a_c)}$'
         '\n\n'
          r'$MR = \dfrac{\Omega*k_1^\prime*\rho_b*R}{k_c}$'
         '\n\n'
         r'$C_{AB}=C_{AB0}*exp\left(-\Omega*k_1^\prime*W/v_o\right)$'
         '\n\n'
         r'$X=1-\dfrac{C_{AB}}{C_{AB0}}$'
         '\n\n'
                  , ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


axcolor = 'black'

ax_De = plt.axes([0.07, 0.80, 0.2, 0.015], facecolor=axcolor)
ax_vis= plt.axes([0.07, 0.76, 0.2, 0.015], facecolor=axcolor)
ax_Sa= plt.axes([0.07, 0.72, 0.2, 0.015], facecolor=axcolor)
ax_vo= plt.axes([0.07, 0.68, 0.2, 0.015], facecolor=axcolor)
ax_k1doubleprime= plt.axes([0.07, 0.64, 0.2, 0.015], facecolor=axcolor)

sDe = Slider(ax_De, r'$D_e (\frac{m^2}{s})$', 10**-10, 10**-6, valinit=1.82*10**-8,  valfmt='%1.1E')
svis = Slider(ax_vis, r'$\nu (\frac{m^2}{s})$', 0.01*10**-8, 15*10**-8, valinit=1.53*10**-8,  valfmt='%1.2E')
sSa= Slider(ax_Sa, r'$S_{a} (\frac{m^2}{g})$', 0.5, 1000, valinit=530,  valfmt='%1.0f')
svo= Slider(ax_vo, r'$v_{0} (\frac{m^3}{s})$', 10**-8, 10**-4, valinit=10**-6,  valfmt='%1.1E')
sk1doubleprime= Slider(ax_k1doubleprime, r'$k_1^{\prime\prime} (\frac{m^3}{m^2.s})$', 10**-12, 10**-8, valinit=4.42*10**-10,  valfmt='%1.1E')


def update_plot(val):
    De = sDe.val
    vis = svis.val
    Sa = sSa.val
    vo=svo.val 
    k1doubleprime=sk1doubleprime.val
    k1prime=k1doubleprime*Sa
    phi1=R*np.sqrt(k1prime*rhoc/De)
    eff=(3/phi1**2) *(phi1*(1/np.tanh(phi1))-1)
    CWP=eff*phi1*phi1
    p1.set_ydata(eff)
    p2.set_ydata(CWP)
    U=vo/Ac
    dp=2*R
    Re=U*dp/((1-phi)*vis)
    Sc=vis/DAB
    Sh=(Re**0.5)*(Sc**(1/3))
    kc=(1-phi)*DAB*Sh/(phi*dp)
    ac=6*(1-phi)/dp
    rhob=rhoc*(1-phi)
    effoverall=eff/(1+(eff*k1doubleprime*Sa*rhob)/(kc*ac))
    MR=effoverall*k1prime*rhob*R/kc
    p3.set_ydata(effoverall)
    p4.set_ydata(MR)
    phi11=R1*np.sqrt(k1prime*rhoc/De)
    eff1=(3/phi11**2) *(phi11*(1/np.tanh(phi11))-1)
    kc1=(1-phi)*DAB*Sh/(phi*2*R1)
    ac1=6*(1-phi)/(2*R1)
    effoverall1=eff1/(1+(eff1*k1doubleprime*Sa*rhob)/(kc1*ac1))
    CAB = CAB0*np.exp(-effoverall1*k1prime*W/(vo));
    X = (CAB0 - CAB)/CAB0;
    p5.set_ydata(X)
    p6.set_ydata(CAB)
    fig.canvas.draw_idle()

sDe.on_changed(update_plot)
svis.on_changed(update_plot)
sSa.on_changed(update_plot)
svo.on_changed(update_plot)
sk1doubleprime.on_changed(update_plot)

resetax = plt.axes([0.13, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sDe.reset()
    svis.reset()
    sSa.reset()
    svo.reset()
    sk1doubleprime.reset()


button.on_clicked(reset)