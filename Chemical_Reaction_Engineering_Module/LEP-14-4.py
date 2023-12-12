#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})

from matplotlib.widgets import Slider, Button

Di = 0.0025
L = 0.005
v = 4.94*10**-5
U = 150
DAB = 0.69*10**-4
phi = 0.4

LB = np.linspace(0, 0.2, 1000)

dp = (1.5*(Di**2)*L)**(1/3)
ac1 = 6*(1 - phi)/dp
Re1 = dp*U/v
gamma = ((2*(Di/2)*L)+(2*(Di/2)**2))/(dp**2)
Reprime1 = Re1/((1-phi)*gamma)
DAB1 = DAB*(450/298)**1.75
Sc = v/DAB1
Shprime1 = (Reprime1**(1/2))*(Sc**(1/3))
kc1 = (DAB1*(1-phi)*gamma*Shprime1)/(dp*phi)

X = 1 - np.exp(-1*(kc1*ac1/U)*LB)


A = np.pi*Di*L + 2*np.pi*(Di**2/4)
dp2 = np.sqrt(A/np.pi)
ac2 = 6*(1 - phi)/dp2
Re2 = dp2*U/v
JD1 = ((0.765/ (Re2**0.82)) + (0.365/ (Re2**0.386)))/phi
Shprime2 = Re2*(Sc**(1/3))*JD1
kc2 = DAB1*Shprime2/dp2

X1 = 1 - np.exp(-1*(kc2*ac2/U)*LB)

#%%
fig, (ax3, ax4) = plt.subplots(2,1)
plt.subplots_adjust(left=0.6)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""LEP-14-4: Mass Transfer Effects in Maneuvering a Space Satellite""", fontweight='bold', x = 0.25, y=0.97)

p3 = ax3.plot(LB, X)[0]
ax3.grid()
ax3.set_xlabel('Bed Length, L(m)', fontsize='medium')
ax3.set_ylabel('$Conversion$', fontsize='medium', fontweight='bold')
#ax3.set_ylim(0, 1)
ax3.set_xlim(0, 0.2)
ax3.text(0.08, 0.1, r'$Using \thinspace Thoenes \thinspace Kramers \thinspace correlation$',  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

p4 = ax4.plot(LB, X1)[0]
ax4.grid()
ax4.set_xlabel('Bed Length, L(m)', fontsize='medium')
ax4.set_ylabel('$Conversion$', fontsize='medium', fontweight='bold')
ax4.set_ylim(0, 1)
ax4.set_xlim(0, 0.2)
ax4.text(0.1, 0.1, r'$Using \thinspace Colburn \thinspace J_D \thinspace factor$',  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax4.text(-0.38, 0.5,
         'Using Thoenes-Kramers correlation' 
         '\n\n'
         'Equations'
                  '\n\n'            
          r'$d_p = \left(\dfrac{6V}{\pi}\right)^{1/3}$'
                 '\n\n'
         r'$a_c = 6\left(\frac{1-\phi}{d_p}\right)$'
                 '\n\n'
         r'$Re=\dfrac{d_P U}{\nu}$'
                 '\n\n'   
         r'$\gamma = \dfrac{2 \pi r L_p + 2 \pi r^2}{\pi d_p^2}$'
         '\n\n'
         r'$Re^ \prime=\dfrac{Re}{(1-\phi)\gamma}$'
                 '\n\n'   
         r'$Sc=\dfrac{\nu}{D_{AB}}$'
         '\n\n'
         r'$Sh^\prime=(Re^\prime)^{1/2} Sc^{1/3}$'
         '\n\n'
         r'$k_c=\dfrac{D_{AB} (1-\phi)}{d_p \phi} \gamma (Sh ^\prime)$'
         '\n\n'
         r'$X = 1 - e^{-\left(k_c a_c / U\right)L}$'
         '\n\n'
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

ax4.text(-0.265, 0.515,
         'Using Colburn $J_D$ factor' 
         '\n\n'
         'Equations'        
         '\n\n'            
          r'$A = \pi dL_P +2 \pi \left(\dfrac{d^2}{4}\right)$'
                 '\n\n'
         r'$d_P = \sqrt {\dfrac{A}{\pi}}$'
                 '\n\n'
         r'$Re=\dfrac{d_P U}{\nu}$'
                 '\n\n'   
         r'$a_c = 6\left(\frac{1-\phi}{d_p}\right)$'
                 '\n\n'
         r'$\phi J_D=\dfrac{0.765}{Re^{0.82}}+ \dfrac{0.365}{Re^{0.386}}$'
         '\n\n'
         r'$Sc=\dfrac{\nu}{D_{AB}}$'
         '\n\n'
         r'$Sh=Sc^{1/3} (Re)(J_D) $'
         '\n\n'
         r'$k_c=\dfrac{D_{AB}}{d_p} Sh$'
         '\n\n'
         r'$X = 1 - e^{-\left(k_c a_c / U\right)L}$'
         '\n\n'
         , ha='left', wrap = True, fontsize=10,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


ax1color = 'black'
ax1_Di = plt.axes([0.36, 0.75, 0.15, 0.02], facecolor=ax1color)
ax1_L = plt.axes([0.36, 0.70, 0.15, 0.02], facecolor=ax1color)
ax1_v = plt.axes([0.36, 0.65, 0.15, 0.02], facecolor=ax1color)
ax1_U = plt.axes([0.36, 0.60, 0.15, 0.02], facecolor=ax1color)
ax1_DAB = plt.axes([0.36, 0.55, 0.15, 0.02], facecolor=ax1color)
ax1_phi = plt.axes([0.36, 0.5, 0.15, 0.02], facecolor=ax1color)

s1Di = Slider(ax1_Di, r'$D (m)$', 0.0005, 0.01, valinit=0.0025, valfmt='%1.4f')
s1L = Slider(ax1_L, r'$L (m)$', 0.001, 0.5, valinit=0.005,  valfmt='%1.3f')
s1v = Slider(ax1_v, r'$\nu (\frac{m^2}{s})$', 0.00001, 0.0005, valinit=4.94*10**-5,  valfmt='%1.0E')
s1U = Slider(ax1_U, r'$U (\frac{m}{s})$', 20, 5000, valinit=150, valfmt='%1.0f')
s1DAB = Slider(ax1_DAB, r'$D_{AB} (\frac{m^2}{s})$', 0.000001, 0.003, valinit=0.69*10**-4, valfmt='%1.0E')
s1phi = Slider(ax1_phi, r'$\phi$', 0.1, 1, valinit=0.4, valfmt='%1.1f')


def update_plot(val):
    Di = s1Di.val
    L = s1L.val
    v = s1v.val
    U = s1U.val    
    DAB = s1DAB.val    
    phi = s1phi.val
    
    
    dp = (1.5*(Di**2)*L)**(1/3)
    ac1 = 6*(1 - phi)/dp
    Re1 = dp*U/v
    gamma = (2*Di/2*L+2*(Di/2)**2)/(dp**2)
    Reprime1 = Re1/((1-phi)*gamma)
    DAB1 = DAB*(450/298)**1.75
    Sc = v/DAB1
    Shprime1 = (Reprime1**0.5)*(Sc**(1/3))
    kc1 = (DAB*(1-phi)/(dp*phi))*gamma*Shprime1
    
    X = 1 - np.exp(-1*(kc1*ac1/U)*LB)
    
    
    A = np.pi*Di*L + 2*np.pi*(Di**2/4)
    dp2 = np.sqrt(A/np.pi)
    ac2 = 6*(1 - phi)/dp2
    Re2 = dp2*U/v
    JD1 = ((0.765/ (Re2**0.82)) + (0.365/ (Re2**0.386)))/phi
    Shprime2 = Re2*(Sc**(1/3))*JD1
    
    kc2 = DAB1*Shprime2/dp2
    
    X1 = 1 - np.exp(-1*(kc2*ac2/U)*LB)
    
    p3.set_ydata(X)
    p4.set_ydata(X1)
    fig.canvas.draw_idle()


s1Di.on_changed(update_plot)
s1L.on_changed(update_plot)
s1v.on_changed(update_plot)
s1U.on_changed(update_plot)
s1DAB.on_changed(update_plot)
s1phi.on_changed(update_plot)

resetax = plt.axes([0.39, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):

    s1Di.reset()
    s1L.reset()
    s1v.reset()
    s1U.reset()
    s1DAB.reset()
    s1phi.reset()

button.on_clicked(reset)

