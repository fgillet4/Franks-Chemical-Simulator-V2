#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})

from matplotlib.widgets import Slider, Button

lam = np.linspace(-1, 1, 100)
Pe=1
Da=1
Pe1=5
q=(1+4*Da/Pe)**0.5
A=(1+q)*np.exp(q*Pe*(1-lam)/2)
B=(1-q)*np.exp(-q*Pe*(1-lam)/2)
A0=(1+q)*np.exp(q*Pe*(1-0)/2)
B0=(1-q)*np.exp(-q*Pe*(1-0)/2)
C=(1+q)**2*np.exp(q*Pe/2)
D=(1-q)**2*np.exp(-q*Pe/2)
Sai=(2*np.exp(Pe*lam/2)*(A-B))/(C-D)
Sai0=(2*np.exp(Pe*0/2)*(A0-B0))/(C-D)
Sai1=1-(1-Sai0)*np.exp((lam*Pe1))
Sa = []
for i in range(len(lam)):
    if (lam[i] >= 0):  
        Sa.append(Sai[i])
    else:
        Sa.append(Sai1[i])
#%%
fig, ax1 = plt.subplots()
plt.subplots_adjust(left=0.5, bottom = 0.3)
fig.suptitle("""LEP-18-open: Dimensionless Concentration profile""", fontweight='bold', x = 0.2, y=0.97)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

p1 = ax1.plot(lam, Sa)[0]
ax1.set_xlabel(r'$Dimensionless \thinspace distance, \lambda=z/L$', fontsize='medium')
ax1.set_ylabel(r'$Dimensionless \thinspace concentration, \psi=C_A/C_{A0}$', fontsize='medium')
ax1.set_ylim(0, 1)
ax1.set_xlim(-1, 1)
ax1.grid()

ax1.text(-3, -0.2,'Equations'
         '\n\n'
        
         r'$q = \sqrt{1+ \dfrac{4Da_{1}}{Pe_{r}}}$'
                  '\n\n'
         r'$A = (1+q)* exp\left(q*Pe_{r}(1-\lambda)/2 \right)$'
         '\n\n'
         r'$B = (1-q)* exp\left(-q*Pe_{r}(1-\lambda)/2 \right)$'
                  '\n\n'
         r'$A0 = (1+q)* exp\left(q*Pe_{r}(1-0)/2 \right)$'
         '\n\n'
         r'$B0 = (1-q)* exp\left(-q*Pe_{r}(1-0)/2 \right)$'
                  '\n\n'
         r'$C = (1+q)^2* exp\left(q*Pe_{r}/2 \right)$'
         '\n\n'
         r'$D = (1-q)^2* exp\left(-q*Pe_{r}/2 \right)$'
         '\n\n'
         r'$\psi = (2* exp\left(Pe_{r}*\lambda/2 \right)*(A-B))/(C-D)$'
         '\n\n'
         r'$\psi0 = (2* exp\left(Pe_{r}*0/2 \right)*(A0-B0))/(C-D)$'
         '\n\n'
         r'$\psi1 = (1-(1-\psi0)) exp\left(\lambda*Pe_{r1} \right)$'
        , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


axcolor = 'black'
ax_Pe = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_Pe1 = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Da = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)

sPe = Slider(ax_Pe, r'$P_e$', 0.01,20, valinit=1, valfmt='%1.2f')
sPe1 = Slider(ax_Pe1, r'$P_{e1}$', 0.1,20, valinit=5,  valfmt='%1.2f')
sDa = Slider(ax_Da, r'$D_a$', 0, 100, valinit=1,  valfmt='%1.1f')

def update_plot(val):
    Pe = sPe.val
    Pe1 = sPe1.val
    Da = sDa.val    
    q=(1+4*Da/Pe)**0.5
    A=(1+q)*np.exp(q*Pe*(1-lam)/2)
    B=(1-q)*np.exp(-q*Pe*(1-lam)/2)
    A0=(1+q)*np.exp(q*Pe*(1-0)/2)
    B0=(1-q)*np.exp(-q*Pe*(1-0)/2)
    C=(1+q)**2*np.exp(q*Pe/2)
    D=(1-q)**2*np.exp(-q*Pe/2)
    Sai=(2*np.exp(Pe*lam/2)*(A-B))/(C-D)
    Sai0=(2*np.exp(Pe*0/2)*(A0-B0))/(C-D)
    Sai1=1-(1-Sai0)*np.exp((lam*Pe1))
    Sa = []
    for i in range(len(lam)):
       if (lam[i] >= 0):  
        Sa.append(Sai[i])
       else:
        Sa.append(Sai1[i])
    p1.set_ydata(Sa)
    fig.canvas.draw_idle()

sPe.on_changed(update_plot)
sPe1.on_changed(update_plot)
sDa.on_changed(update_plot)

resetax = plt.axes([0.15, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sPe.reset()
    sPe1.reset()
    sDa.reset()

button.on_clicked(reset)