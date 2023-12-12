#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 1.5})

from matplotlib.widgets import Slider, Button

#%%
tau = np.linspace(0, 20, 1000)
Pe=7.5
k = .25
n = 4.35
def func1(tau, Pe,k, n):
    Da1 = tau*k
    q = np.sqrt(1+ 4*Da1/Pe)
    Xdis = 1- (4*q*np.exp(Pe/2))/((1+q)**2*np.exp(Pe*q/2) - (1-q)**2*np.exp(-Pe*q/2) )
    Xpfr = 1 - np.exp(-tau*k)
    Xtan = 1 - 1/(1 + tau*k/n)**n
    Xcstr = (tau*k)/(1+tau*k)
    Cdis=1-Xdis
    Cpfr=1-Xpfr
    Ctan=1-Xtan
    Ccstr=1-Xcstr
    return np.array([Xdis, Xpfr, Xtan, Xcstr,Cdis,Cpfr,Ctan,Ccstr])

#%%
fig, (ax1, ax2) = plt.subplots(2,1)
plt.subplots_adjust(left=0.6)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""Example 18-2 Conversion Using Dispersion,PFR,CSTR and Tank-in-series Models""", fontweight='bold', x = 0.28, y=0.97)
sol1 = func1(tau, Pe, k, n)
Xdis, Xpfr, Xtan, Xcstr, Cdis, Cpfr, Ctan, Ccstr = sol1

p1, p2, p3, p4 = ax1.plot(tau, Xdis, tau, Xpfr, tau, Xtan, tau, Xcstr)
ax1.grid()
ax1.set_xlabel(r'Space Time, $\tau (min)$', fontsize='medium', )
ax1.set_ylabel('Conversion, X', fontsize='medium', )
ax1.set_ylim(0, 1)
ax1.set_xlim(0, 20)
ax1.legend([r'$X_{dispersion}$',r'$X_{PFR}$',r'$X_{Tank \hspace{0.2} in  \hspace{0.2}series}$',r'$X_{CSTR}$'], loc='lower right')


p5, p6, p7, p8 = ax2.plot(tau, Cdis, tau, Cpfr, tau, Ctan, tau, Ccstr)
ax2.grid()
ax2.set_xlabel(r'Space Time, $\tau (min)$', fontsize='medium', )
ax2.set_ylabel('Concentration', fontsize='medium', )
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 20)
ax2.legend([r'$C_{dispersion}$',r'$C_{PFR}$',r'$C_{Tank \hspace{0.2} in  \hspace{0.2}series}$',r'$C_{CSTR}$'], loc='upper right')
ax1.text(-38, -0.5,'Equations'
         '\n\n'
         r'$Da_{1} = \tau k$'
         '\n\n'
         r'$q = \sqrt{1+ \dfrac{4Da_{1}}{Pe_{r}}}$'
                  '\n\n'
         r'$X_{dispersion} = 1 - \dfrac{4qexp\left(Pe_{r}/2 \right)}{(1+q)^2exp\left(Pe_{r}q/2 \right) - (1-q)^2exp\left(-Pe_{r}q/2 \right)}$'
         '\n\n'
         r'$X_{PFR} = 1 - exp(-\tau k)$'
                  '\n\n'
         r'$X_{Tanks \hspace{0.5} In \hspace{0.5} Series} = 1 - \dfrac{1}{(1+ \dfrac{\tau k}{n})^n}$'
         '\n\n'
         r'$X_{Single \hspace{0.5} CSTR} = \dfrac{\tau k}{1 + \tau k}$'
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
axcolor = 'black'
ax_Pe = plt.axes([0.33, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.33, 0.7, 0.15, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.33, 0.65, 0.15, 0.02], facecolor=axcolor)

sPe = Slider(ax_Pe, r'$Pe$', 0.1, 100, valinit=7.5, valfmt='%1.1f')
sk = Slider(ax_k, r'$k (min^{-1})$', 0.02, 1, valinit=.25,valfmt='%1.2f')
sn = Slider(ax_n, r'$n$', 0.5, 10, valinit=4.35,valfmt='%1.1f')


def update_plot(val):
    Pe = sPe.val
    k = sk.val 
    n = sn.val
    sol1 = func1(tau,Pe, k, n)
    Xdis, Xpfr, Xtan, Xcstr,Cdis, Cpfr, Ctan, Ccstr = sol1  

    p1.set_ydata(Xdis)
    p2.set_ydata(Xpfr)
    p3.set_ydata(Xtan)
    p4.set_ydata(Xcstr)
    p5.set_ydata(Cdis)
    p6.set_ydata(Cpfr)
    p7.set_ydata(Ctan)
    p8.set_ydata(Ccstr)
    fig.canvas.draw_idle()

sPe.on_changed(update_plot)
sk.on_changed(update_plot)
sn.on_changed(update_plot)


resetax = plt.axes([0.36, 0.8, 0.09, 0.03])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sPe.reset()
    sk.reset()
    sn.reset()


button.on_clicked(reset)

