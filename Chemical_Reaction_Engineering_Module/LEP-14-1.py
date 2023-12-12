import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button


U=0;
Nu=0.5*1e-6
DAB=1e-4
CAinf=8.58
rhoc=2.226*1e6;
Ccloud=200
dH=-93.5
Pi=3.14;
dp = np.linspace(1e-5, 1e-4, 1000)
Re = dp*U/Nu;
Sc = Nu/DAB;
Sh = 2 + 0.6* Re**0.5*Sc**(1/3);
kc = Sh*DAB/dp;
WA = kc*(CAinf);
mA = Pi*(dp**2)*WA;
mp = rhoc*(Pi/6)*(dp)**3;
np = Ccloud/mp;
Qgd = np*mA*(-dH);
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-14-1: Mass Transfer of Oxygen to a Burning Carbon Particle""", fontweight='bold', x = 0.22, y= 0.98)
plt.subplots_adjust(left  = 0.5)
fig.subplots_adjust(wspace=0.3,hspace=0.5)

p1 = ax1.plot(dp,WA)[0]
ax1.grid()
ax1.set_xlabel('Pellet diameter, dp(m)', fontsize='medium')
ax1.set_ylabel(r'$W_{A}\thinspace (mol/m^2.s)$', fontsize='medium')
ax1.set_ylim(0, 200)
ax1.set_xlim(1e-5, 1e-4)
ax1.ticklabel_format(style='sci',scilimits=(3,4),axis='x')

p2 = ax2.plot(dp,mA)[0]
ax2.grid()
ax2.set_ylim(0, 1e-6)
ax2.set_xlim(1e-5, 1e-4)
ax2.set_xlabel('Pellet diameter, dp(m)', fontsize="medium")
ax2.set_ylabel(r'$m_A \thinspace (mol/s)$', fontsize='medium')
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

p3 = ax3.plot(dp,np)[0]
ax3.grid()
ax3.set_ylim(0, 1e10)
ax3.set_xlim(1e-5, 1e-4)
ax3.set_xlabel('Pellet diameter, dp(m)', fontsize="medium")
ax3.set_ylabel(r'$n_p \thinspace (particles/m^3)$', fontsize='medium')
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

p4 = ax4.plot(dp,Qgd)[0]
ax4.grid()
ax4.set_ylim(0, 1e6)
ax4.set_xlim(1e-5, 1e-4)
ax4.set_xlabel('Pellet diameter, dp(m)', fontsize="medium")
ax4.set_ylabel(r'$Q_{gd}\thinspace (kJ/m^3.s)$', fontsize='medium')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='y')


ax1.text(-2e-4, -320,
         'Equations'
                  '\n\n'
         r'$W_{A} = k_c (C_{A\infty})$'
                 '\n'
           r'$Sh=\dfrac{k_c*d_p}{D_{AB}}= 2+0.6 Re^{1/2} Sc^{1/3}$'
                 '\n'
         r'$Re=\dfrac{d_P U}{\nu}$'
                 '\n'        
         r'$Sc=\dfrac{\nu}{D_{AB}}$'
         '\n'
         r'$k_c=\dfrac{D_{AB}}{d_p} Sh$'
         '\n'
         r'$m_A=\pi*(dp^2)*W_{A}$'         
          '\n'
         r'$m_p=\rho_c*\pi*(d_p^3)/6$'  
            '\n'
         r'$n_p=\dfrac{C_{cloud}}{m_p}$'
            '\n'
         r'$Q_{gd}=n_p*m_A*(-\Delta H_{Rx})$'  
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
    
      
axcolor = 'black'
ax_U = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_Nu = plt.axes([0.1, 0.76, 0.2, 0.02], facecolor=axcolor)
ax_DAB = plt.axes([0.1, 0.72, 0.2, 0.02], facecolor=axcolor)
ax_CAinf = plt.axes([0.1, 0.68, 0.2, 0.02], facecolor=axcolor)
ax_rhoc = plt.axes([0.1, 0.64, 0.2, 0.02], facecolor=axcolor)
ax_Ccloud = plt.axes([0.1, 0.60, 0.2, 0.02], facecolor=axcolor)
ax_dH = plt.axes([0.1, 0.56, 0.2, 0.02], facecolor=axcolor)

sU = Slider(ax_U, r'$U(m/s)$', 0, 0.8, valinit=0,valfmt='%1.2f')
sNu = Slider(ax_Nu, r'$\nu (m^2/s)$',1e-9, 1e-3, valinit=1e-6,valfmt='%1.2E')
sDAB = Slider(ax_DAB, r'$DAB (m^2/s)$',1e-6, 0.0005, valinit=1e-4,valfmt='%1.0f')
sCAinf = Slider(ax_CAinf, r'$C_{A \infty} (mol/m^3)$',0, 25, valinit=8.58,valfmt='%1.2f')
srhoc = Slider(ax_rhoc, r'$\rho_c (g/m^3)$',1e5, 1e8, valinit=2.226*1e6,valfmt='%1.2E')
sCcloud = Slider(ax_Ccloud, r'$C_{cloud} (g/m^3)$',10, 2000, valinit=200,valfmt='%1.0f')
sdH = Slider(ax_dH,  r'$\Delta H_{Rx}$ ($\frac{kJ}{mol}$)',-500, -10, valinit=-93.5,valfmt='%1.1f')

def update_plot(val):
    U = sU.val
    Nu = sNu.val
    DAB=sDAB.val
    CAinf=sCAinf.val
    rhoc=srhoc.val
    Ccloud=sCcloud.val
    dH=sdH.val
    Re = dp*U/Nu;
    Sc = Nu/DAB;
    Sh = 2 + 0.6* Re**0.5*Sc**(1/3);
    kc = Sh*DAB/dp;
    WA = kc*(CAinf);
    mA = Pi*(dp**2)*WA;
    mp = rhoc*(Pi/6)*(dp)**3;
    np = Ccloud/mp;
    Qgd = np*mA*(-dH);
    p1.set_ydata(WA)
    p2.set_ydata(mA)
    p3.set_ydata(np)
    p4.set_ydata(Qgd)
    fig.canvas.draw_idle()

sU.on_changed(update_plot)
sNu.on_changed(update_plot)
sDAB.on_changed(update_plot)
sCAinf.on_changed(update_plot)
srhoc.on_changed(update_plot)
sCcloud.on_changed(update_plot)
sdH.on_changed(update_plot)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sU.reset()
    sNu.reset()
    sDAB.reset()
    sCAinf.reset()
    srhoc.reset()
    sCcloud.reset() 
    sdH.reset() 
button.on_clicked(reset)    


