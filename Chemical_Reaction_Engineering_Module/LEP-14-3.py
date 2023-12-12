import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

rhoc=2.226*10**6;
DAB=10**-4;
dp0=100;
phic=1;
CAinf= np.linspace(1,20, 100)
rhocm = rhoc/12;
Ks = 8*DAB*CAinf/(rhocm*phic)*10**9;
tc = dp0**2/Ks;
fig, ((ax1, ax2)) = plt.subplots(2, 1)
fig.suptitle("""LEP-14-3: Combustion time for a single particle""", fontweight='bold', x = 0.22, y= 0.98)
plt.subplots_adjust(left  = 0.5)
fig.subplots_adjust(wspace=0.3,hspace=0.5)

p1 = ax1.plot(CAinf,tc)[0]
ax1.grid()
ax1.set_ylim(0, 1000)
ax1.set_xlim(0, 20)
ax1.set_xlabel(r'$C_{A \infty} (mol/m^3)$', fontsize="medium")
ax1.set_ylabel(r'$t_c \thinspace (ms)$', fontsize='medium')

p2 = ax2.plot(CAinf,Ks)[0]
ax2.grid()
ax2.set_ylim(0, 100)
ax2.set_xlim(0, 20)
ax2.set_xlabel(r'$C_{A \infty} (mol/m^3)$', fontsize="medium")
ax2.set_ylabel(r'$K_S \thinspace (\mu m^2/ms)$', fontsize='medium')
ax2.text(-18, 90,
         'Equations'
                  '\n\n'
          r'$K_{S} = \dfrac{8*D_{AB}*C_{A\infty}}{\rho_c*\phi_c}$'
                 '\n\n'                 
          r'$t_c = \dfrac{d_{p0}^2}{K_S}$'
                 '\n\n'
  
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
    
      
axcolor = 'black'
ax_rhoc = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_DAB = plt.axes([0.1, 0.76, 0.2, 0.02], facecolor=axcolor)
ax_dp0 = plt.axes([0.1, 0.72, 0.2, 0.02], facecolor=axcolor)
ax_phic = plt.axes([0.1, 0.68, 0.2, 0.02], facecolor=axcolor)

srhoc = Slider(ax_rhoc, r'$\rho_c (g/m^3)$', 1e4, 1e8, valinit=2.226e6,valfmt='%1.2E')
sDAB = Slider(ax_DAB, r'$D_{AB} (m^2/s)$',1e-6, 1e-2, valinit=1e-4,valfmt='%1.2E')
sdp0 = Slider(ax_dp0, r'$d_{p0} (\mu m)$',10, 500, valinit=100,valfmt='%1.0f')
sphic = Slider(ax_phic, r'$\phi_c$',0.0, 1, valinit=1,valfmt='%1.2f')

def update_plot(val):
    rhoc = srhoc.val
    DAB = sDAB.val
    dp0=sdp0.val
    phic=sphic.val
    rhocm = rhoc/12;
    Ks = 8*DAB*CAinf/(rhocm*phic)*10**9;
    tc = dp0**2/Ks;
    p1.set_ydata(tc)
    p2.set_ydata(Ks)
    fig.canvas.draw_idle()

srhoc.on_changed(update_plot)
sDAB.on_changed(update_plot)
sdp0.on_changed(update_plot)
sphic.on_changed(update_plot)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    srhoc.reset()
    sDAB.reset()
    sdp0.reset()
    sphic.reset()
        
button.on_clicked(reset)    


