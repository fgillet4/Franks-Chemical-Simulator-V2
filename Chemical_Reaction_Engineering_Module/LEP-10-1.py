import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

KT=1.038
KB=1.39
PT0=1
#%%
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
fig.suptitle("""Example 10-1 : Non-linear Regression Analysis to Determine the Model Parameters""", fontweight='bold', x = 0.35, y=0.96)
plt.subplots_adjust(left = 0.23, wspace = 0.3, hspace = 0.5)
X = np.linspace(0, 1, 1000)

c1 = (KT*(1-X))/(KB*X)
p1 = ax1.plot(X, c1)[0]
ax1.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax1.set_ylabel(r'$\dfrac{C_{T.S}}{C_{B.S}}$', fontsize='medium', fontweight='bold')
ax1.set_ylim(0,30)
ax1.set_xlim(0,1)
ax1.grid(alpha = 0.2)
ax1.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax1.set_title('Ratio of Toluene to Benzene occupied site', fontsize = 14)
ax1.text(0.5, 15,r'$\dfrac{C_{T.S}}{C_{B.S}} = \dfrac{K_T(1-X)}{K_BX}$'
         ,   fontsize=12, fontweight='bold')


c2 = 1/(KB*PT0*X)
p2 = ax2.plot(X, c2)[0]
ax2.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax2.set_ylabel(r'$\dfrac{C_{V}}{C_{B.S}}$', fontsize='medium', fontweight='bold')
ax2.set_ylim(0,30)
ax2.set_xlim(0,1)
ax2.grid(alpha=0.2)
ax2.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax2.set_title('Ratio of Vacant to Benzene occupied site', fontsize = 14)
ax2.text(0.5, 15,r'$\dfrac{C_{V}}{C_{B.S}} = \dfrac{1}{K_BP_{T0}X}$'
         ,   fontsize=12, fontweight='bold')


c3 = KT*PT0*(1-X)
p3 = ax3.plot(X, c3)[0]
ax3.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax3.set_ylabel(r'$\dfrac{C_{T.S}}{C_{V}}$', fontsize='medium', fontweight='bold')
ax3.set_ylim(0,10)
ax3.set_xlim(0,1)
ax3.grid(alpha=0.2)
ax3.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax3.set_title('Ratio of Toluene to Vacant occupied site', fontsize = 14)
ax3.text(0.25, 5,r'$\dfrac{C_{T.S}}{C_{V}} = K_TP_{T0}(1-X)$'
         ,   fontsize=12, fontweight='bold')


c4 = (KT*PT0*(1-X))/(1+KT*PT0*(1-X)+KB*PT0*X)
p4 = ax4.plot(X, c4)[0]
ax4.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax4.set_ylabel(r'$\dfrac{C_{T.S}}{C_{T}}$', fontsize='medium', fontweight='bold')
ax4.set_ylim(0,1)
ax4.set_xlim(0,1)
ax4.grid(alpha=0.2)
ax4.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax4.set_title('Fraction of Toluene occupied sites', fontsize = 14)
ax4.text(0.2, 0.8,r'$\dfrac{C_{T.S}}{C_{T}} = \dfrac{K_TP_{T0}(1-X)}{1+K_TP_{T0}(1-X)+K_BP_{T0}X}$'
         ,   fontsize=12, fontweight='bold')


c5= 1/(1+KT*PT0*(1-X)+KB*PT0*X)
p5 = ax5.plot(X, c5)[0]
ax5.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax5.set_ylabel(r'$\dfrac{C_{V}}{C_{T}}$', fontsize='medium', fontweight='bold')
ax5.set_ylim(0,1)
ax5.set_xlim(0,1)
ax5.grid(alpha=0.2)
ax5.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax5.set_title('Fraction of Vacant sites', fontsize = 14)
ax5.text(0.2, 0.8,r'$\dfrac{C_{V}}{C_{T}} = \dfrac{1}{1+K_TP_{T0}(1-X)+K_BP_{T0}X}$'
         , fontsize=12, fontweight='bold')


c6 = (KB*PT0*X)/(1+KT*PT0*(1-X)+KB*PT0*X)
p6  = ax6.plot(X, c6)[0]
ax6.set_xlabel(r'$Conversion, X$', fontsize='medium', fontweight='bold')
ax6.set_ylabel(r'$\dfrac{C_{B.S}}{C_{T}}$', fontsize='medium', fontweight='bold')
ax6.set_ylim(0,1)
ax6.set_xlim(0,1)
ax6.grid(alpha=0.2)
ax6.ticklabel_format(style='sci',scilimits=(3,4),axis='x')
ax6.set_title('Fraction of Benzene occupied sites', fontsize = 14)
ax6.text(0.05, 0.8,r'$\dfrac{C_{B.S}}{C_{T}} = \dfrac{K_BP_{T0} X}{1+K_TP_{T0}(1-X)+K_BP_{T0}X}$'
         , fontsize=12, fontweight='bold')


#%%
axcolor = 'black'
ax_KT = plt.axes([0.06, 0.50, 0.1, 0.015], facecolor=axcolor)
ax_KB = plt.axes([0.06, 0.46, 0.1, 0.015], facecolor=axcolor)
ax_PT0 = plt.axes([0.06, 0.42, 0.1, 0.015], facecolor=axcolor)


sKT= Slider(ax_KT, r'$K_T (atm^{-1})$', 0.1, 10, valinit=1.038)
sKB = Slider(ax_KB, r'$K_B (atm^{-1})$', 0.1, 10, valinit=1.39)
sPT0 = Slider(ax_PT0, r'$P_{T0} (atm)$', 1, 5, valinit= 1)


def update_plot2(val):
    KT =sKT.val
    KB = sKB.val
    PT0 = sPT0.val
    c6 = (KB*PT0*X)/(1+KT*PT0*(1-X)+KB*PT0*X)
    c5= 1/(1+KT*PT0*(1-X)+KB*PT0*X)
    c4 = (KT*PT0*(1-X))/(1+KT*PT0*(1-X)+KB*PT0*X)
    c3 = KT*PT0*(1-X)
    c2 = 1/(KB*PT0*X)
    c1 = (KT*(1-X))/(KB*X)
    p1.set_ydata(c1)
    p2.set_ydata(c2)
    p3.set_ydata(c3)
    p4.set_ydata(c4)
    p5.set_ydata(c5)
    p6.set_ydata(c6)    
    fig.canvas.draw_idle()


sKT.on_changed(update_plot2)
sKB.on_changed(update_plot2)
sPT0.on_changed(update_plot2)


resetax = plt.axes([0.06, 0.55, 0.09, 0.03])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sKT.reset()
    sKB.reset()
    sPT0.reset()	
button.on_clicked(reset)
    










