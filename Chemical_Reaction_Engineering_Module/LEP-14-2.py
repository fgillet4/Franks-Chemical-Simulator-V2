#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})

from matplotlib.widgets import Slider, Button

U = 0.1
v = 0.5*10**-6
DAB = 10**-10
CAb = 1000
CAs = 0
dp = np.linspace(0.000000001, 0.1, 1000)
Sc = v/DAB
Re = dp*U/v
Sh = 2 + 0.6*Re**0.5*Sc**(1/3)
kc = (DAB/dp)*Sh
WAr = kc*(CAb-CAs)
mA = 3.14*(dp**2)*WAr;
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.43)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""LEP-14-2: Rapid Liquid phase Reaction on the Surface of a Catalyst""", fontweight='bold', x = 0.3, y=0.97)

p1 = ax1.plot(dp, WAr)[0]
ax1.grid()
ax1.set_xlabel('Pellet diameter, dp(m)', fontsize='medium')
ax1.set_ylabel(r'$W_{Ar}(mol/m^2.s)$', fontsize='medium')
ax1.set_ylim(0.001, 0.01)
ax1.set_xlim(1e-5, 1e-1)

p2 = ax2.plot(dp, mA)[0]
ax2.grid()
ax2.set_xlabel('Pellet diameter, dp(m)', fontsize='medium')
ax2.set_ylabel(r'$m_{A}(mol/s)$', fontsize='medium')
ax2.set_ylim(0, 1e-4)
ax2.set_xlim(1e-5,1e-1)
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

p3 = ax3.plot(dp, kc)[0]
ax3.grid()
ax3.set_xlabel('Pellet diameter, dp(m)', fontsize='medium')
ax3.set_ylabel(r'$k_{c}(m/s)$', fontsize='medium')
ax3.set_ylim(0, 1e-4)
ax3.set_xlim(1e-5,1e-1)
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='y')

ax4.axis('off')

ax1.text(-0.18, -0.011,
                  
         'Equations'
                  '\n\n'            
          r'$W_{AR} = k_c (C_{Ab}-C_{As})$'
                 '\n\n'
         r'$Sh=\dfrac{k_c*d_p}{D_{AB}}= 2+0.6 Re^{1/2} Sc^{1/3}$'
                 '\n\n'
         r'$Re=\dfrac{d_P U}{\nu}$'
                 '\n\n'        
         r'$Sc=\dfrac{\nu}{D_{AB}}$'
         '\n\n'
         r'$k_c=\dfrac{D_{AB}}{d_p} Sh$'
         '\n\n'
         r'$mA=\pi*(dp^2)*W_{AR}$'
         '\n\n'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
ax1.text(-0.1,-0.011,'Instructions'
         '\n \n'
'$C_{As}$ should be always less than $C_{Ab}$',  ha='left', wrap = True, fontsize=12,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0 ))

axcolor = 'black'
ax_U = plt.axes([0.07, 0.80, 0.2, 0.02], facecolor=axcolor)
ax_v = plt.axes([0.07, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_DAB = plt.axes([0.07, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_CAb = plt.axes([0.07, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_CAs = plt.axes([0.07, 0.60, 0.2, 0.02], facecolor=axcolor)


sU = Slider(ax_U, r'$U (\frac{m}{s})$', 0.05, 0.8, valinit= 0.1, valfmt='%1.2f')
sv = Slider(ax_v, r'$\nu (\frac{m^2}{s})$', 10**-8, 0.01, valinit=0.5*10**-6,  valfmt='%1.0E')
sDAB = Slider(ax_DAB, r'$D_{AB} (\frac{m^2}{s})$', 10**-11, 10**-9, valinit=10**-10,  valfmt='%1.0E')
sCAb = Slider(ax_CAb, r'$C_{Ab} (\frac{mol}{m^3})$', 100, 5000, valinit=1000, valfmt='%1.0f')
sCAs = Slider(ax_CAs, r'$C_{As} (\frac{mol}{m^3})$', 0, 900, valinit=0, valfmt='%1.0f')


def update_plot(val):
    U = sU.val
    v = sv.val
    DAB = sDAB.val
    CAb = sCAb.val    
    CAs = sCAs.val    
    Sc = v/DAB
    Re = dp*U/v
    Sh = 2 + 0.6*Re**0.5*Sc**(1/3)
    kc = (DAB/dp)*Sh
    WAr = kc*(CAb-CAs)
    mA = 3.14*(dp**2)*WAr
    p1.set_ydata(WAr)
    p2.set_ydata(mA)
    p3.set_ydata(kc)
    fig.canvas.draw_idle()

sU.on_changed(update_plot)
sv.on_changed(update_plot)
sDAB.on_changed(update_plot)
sCAb.on_changed(update_plot)
sCAs.on_changed(update_plot)

resetax = plt.axes([0.13, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sU.reset()
    sv.reset()
    sDAB.reset()
    sCAb.reset()
    sCAs.reset()

button.on_clicked(reset)

