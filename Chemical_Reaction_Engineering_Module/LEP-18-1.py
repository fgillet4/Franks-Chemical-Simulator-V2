#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})

from matplotlib.widgets import Slider, Button

#%%
k=0.25
tau=5.15
Pe=7.5
lambd = np.linspace(0,1,500)
Da1 = k*tau;
q = (1 + 4*Da1/Pe)**0.5;
num = (np.exp(Pe*lambd/2)*2*((1 + q)*np.exp(Pe*q/2*(1 - lambd)) - (1 - q)*np.exp(Pe*q/2*(lambd - 1))));
den1 = (1 + q)**2*np.exp(Pe*q/2);
den2 = (1 - q)**2*np.exp(-Pe*q/2);
Conc = num/(den1 - den2);
ConcPFR = np.exp(-Da1*lambd);
X = 1 - Conc;
XPFR = 1 - np.exp(-Da1*lambd);

#%%
fig, (ax1, ax2) = plt.subplots(2,1)
plt.subplots_adjust(left=0.6)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""Example 18-1 Concentration and Conversion Profiles for Dispersion and Reaction in a Tubular Reactor""", fontweight='bold', x = 0.35, y=0.97)

p1,p2 = ax1.plot(lambd,Conc,lambd, ConcPFR)
ax1.grid()
ax1.set_xlabel(r'$Dimensionless \thinspace distance, \lambda=z/L$', fontsize='medium', )
ax1.set_ylabel(r'$Dimensionless \thinspace Concentration, \psi=\dfrac{C_A}{C_{A0}}$', fontsize='medium', )
ax1.set_ylim(0, 1)
ax1.set_xlim(0, 1)
ax1.legend([r'$ Reactor \thinspace with \thinspace dispersion$',r'$X_{PFR}$'], loc='upper right')

p3,p4 = ax2.plot(lambd,X,lambd, XPFR)
ax2.grid()
ax2.set_xlabel(r'$Dimensionless \thinspace distance, \lambda=z/L$', fontsize='medium', )
ax2.set_ylabel('Conversion, X', fontsize='medium', )
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 1)
ax2.legend([r'$ Reactor \thinspace with \thinspace dispersion$',r'$X_{PFR}$'], loc='lower right')

ax1.text(-1.2, -1.2,'Equations'
         '\n\n'
         r'For reaction with dispersion'
         '\n\n'
         r'$\psi =  2*exp\left(Pe_{r}\lambda/2 \right)*\dfrac{(1+q)*a-(1-q)*exp(-Pe_r*q(1-\lambda)/2)}{(1+q)^2exp\left(Pe_{r}q/2 \right) - (1-q)^2exp\left(-Pe_{r}q/2 \right)}$'
         '\n\n'
         r'$a=exp\left(Pe_{r}*q(1-\lambda)/2 \right)$'
         '\n\n'
         r'$Da_{1} = \tau k$'
                  '\n\n'
         r'$q = \sqrt{1+ \dfrac{4Da_{1}}{Pe_{r}}}$'
                  '\n\n'
         r'$X=1-\psi$'
         '\n\n'
         r'For reaction with PFR'
         '\n\n'
           r'$\psi=exp(-Da_1\lambda)$'
          '\n\n'
         r'$X_{PFR} = 1 -\psi$'
         
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
axcolor = 'black'
ax_k = plt.axes([0.33, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_tau = plt.axes([0.33, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_Pe = plt.axes([0.33, 0.65, 0.15, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k \thinspace (min^{-1})$', 0.02, 1, valinit= 0.25,valfmt='%1.2f')
stau= Slider(ax_tau, r'$\tau \thinspace (min)$', 1, 100, valinit=5.15,valfmt='%1.2f')
sPe = Slider(ax_Pe, r'$P_{er}$', 0.5, 50, valinit=7.5, valfmt='%1.1f')

#%%
def update_plot(val):
    k = sk.val
    tau = stau.val
    Pe = sPe.val
    Da1 = k*tau;
    q = (1 + 4*Da1/Pe)**0.5;
    num = (np.exp(Pe*lambd/2)*2*((1 + q)*np.exp(Pe*q/2*(1 - lambd)) - (1 - q)*np.exp(Pe*q/2*(lambd - 1))));
    den1 = (1 + q)**2*np.exp(Pe*q/2);
    den2 = (1 - q)**2*np.exp(-Pe*q/2);
    Conc = num/(den1 - den2);
    ConcPFR = np.exp(-Da1*lambd);
    X = 1 - Conc;
    XPFR = 1 - np.exp(-Da1*lambd);
    p1.set_ydata(Conc)
    p2.set_ydata(ConcPFR)
    p3.set_ydata(X)
    p4.set_ydata(XPFR)
    fig.canvas.draw_idle()

sk.on_changed(update_plot)
stau.on_changed(update_plot)
sPe.on_changed(update_plot)

resetax = plt.axes([0.36, 0.8, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk.reset()
    stau.reset()
    sPe.reset()

button.on_clicked(reset)

