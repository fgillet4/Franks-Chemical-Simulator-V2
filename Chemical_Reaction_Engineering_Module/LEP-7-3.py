import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

A=8
beta=0.5
Ea = 100
alpha = np.linspace(0, 4, 100)
r1m = 4.9*10**(-4)
r2m = 1.1*10**(-4)
r3m = 2.4*10**(-3)
r4m = 2.2*10**(-2)
r5m = 1.18*10**(-1)
r6m = 1.82*10**(-2)
k1 = A*np.exp(-Ea/(8.314*700))
k2 = A*np.exp(-Ea/(8.314*750))
k3 = A*np.exp(-Ea/(8.314*800))
k4 = A*np.exp(-Ea/(8.314*850))
k5 = A*np.exp(-Ea/(8.314*900))
k6 = A*np.exp(-Ea/(8.314*950))
r1c = k1*(0.2**alpha)*(0.05**beta)
r2c = k2*(0.02**alpha)*(0.03**beta)
r3c = k3*(0.05**alpha)*(0.04**beta)
r4c = k4*(0.08**alpha)*(0.06**beta)
r5c = k5*(0.1**alpha)*(0.2**beta)
r6c = k6*(0.06**alpha)*(0.03**beta)
ssquare = (r1m - r1c)**2 + (r2m - r2c)**2 + (r3m - r3c)**2 + (r4m -r4c)**2 + (r5m-r5c)**2 + (r6m-r6c)**2
fig, ax1 = plt.subplots()
fig.suptitle("""LEP-7-3: To find optimum parameter values to minimize $s^{2}$""", fontweight='bold', x = 0.22, y= 0.98)
plt.subplots_adjust(left  = 0.4)
p1 = ax1.plot(alpha,ssquare)[0]
ax1.grid()
ax1.set_ylim(0, 0.05)
ax1.set_xlim(0, 4)
ax1.set_xlabel(r'$\alpha$', fontsize="large")
ax1.set_ylabel(r'$s^2}$', fontsize='large')

ax1.text(-2.0, 0.02,
         'Equations'
                  '\n\n'
          r'$r_{ic} = k_i*\left(C_{Ai}^{\alpha}*C_{Bi}^{\beta}\right)$'
                 '\n\n'                 
          r'$k_i = A*exp \left(\dfrac{-E}{RT_i}\right)$'
                 '\n\n'
          r'$s^{2} = \sum\left(r_{1m}-r_{1c}\right)^{2}$'
                 '\n\n'  
         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
    
      
axcolor = 'black'
ax_A = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_beta = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)

sA = Slider(ax_A, r'$A$', 1.5, 10, valinit=8,valfmt='%1.2f')
sbeta = Slider(ax_beta, r'$\beta$',0.1, 1, valinit=0.5,valfmt='%1.2f')

def update_plot(val):
    A = sA.val
    beta = sbeta.val
    k1 = A*np.exp(-Ea/(8.314*700))
    k2 = A*np.exp(-Ea/(8.314*750))
    k3 = A*np.exp(-Ea/(8.314*800))
    k4 = A*np.exp(-Ea/(8.314*850))
    k5 = A*np.exp(-Ea/(8.314*900))
    k6 = A*np.exp(-Ea/(8.314*950))
    r1c = k1*(0.2**alpha)*(0.05**beta)
    r2c = k2*(0.02**alpha)*(0.03**beta)
    r3c = k3*(0.05**alpha)*(0.04**beta)
    r4c = k4*(0.08**alpha)*(0.06**beta)
    r5c = k5*(0.1**alpha)*(0.2**beta)
    r6c = k6*(0.06**alpha)*(0.03**beta)
    ssquare = (r1m - r1c)**2 + (r2m - r2c)**2 + (r3m - r3c)**2 + (r4m -r4c)**2 + (r5m-r5c)**2 + (r6m-r6c)**2
    p1.set_ydata(ssquare)
    fig.canvas.draw_idle()

sA.on_changed(update_plot)
sbeta.on_changed(update_plot)

resetax = plt.axes([0.17, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sA.reset()
    sbeta.reset()
        
button.on_clicked(reset)    


