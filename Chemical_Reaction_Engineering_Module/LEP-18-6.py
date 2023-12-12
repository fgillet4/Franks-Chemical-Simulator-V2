#%%
#Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
tau = np.linspace(0.1, 100, 1000)
alpha=0.8
beta=0.1
k=0.03
X = (((beta + alpha*tau*k)*(beta + (1 - alpha)*tau*k))-beta**2)/(((1 + beta + alpha*tau*k)*(beta + (1 - alpha)*tau*k))-beta**2);
CA0 = 2;
CA = CA0*(1 - X);
XCSTR = tau*k/(1 + tau*k);
CACSTR = CA0*(1 - XCSTR);

#%%
fig, (ax1, ax2) = plt.subplots(2,1)
plt.subplots_adjust(left=0.6)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""Example 18-6 CSTR with Interchange Model """, fontweight='bold', x = 0.4, y= 0.98)
p1, p2 = ax1.plot(tau, X, tau, XCSTR)
ax1.legend(['$X$', r'$X (Ideal \thinspace CSTR)$'], loc='lower right')
ax1.set_xlabel(r'$\tau\hspace{0.5} (min)$', fontsize='medium', fontweight='bold')
ax1.set_ylabel('Conversion, X', fontsize='medium')
ax1.set_ylim(0,1)
ax1.set_xlim(0,100)
ax1.grid()
p3, p4 = ax2.plot(tau,CA, tau,CACSTR)
ax2.legend(['$C_A$', r'$C_A(Ideal\thinspace CSTR)$'], loc='upper right')
ax2.set_xlabel(r'$\tau\hspace{0.5} (min)$', fontsize='medium', fontweight='bold')
ax2.set_ylabel(r'$Concentration \thinspace (kmol/m^3)$', fontsize='medium')
ax2.set_ylim(0,2)
ax2.set_xlim(0,100)
ax2.grid()

plt.text(-120, 0.60,
                  
         'For CSTR with interchange'
                  '\n\n'
         r'$C_A = \dfrac{C_{A0}}{1+\beta+\alpha*tau*k-(\beta^2/(\beta+ (1-\alpha)*tau*k))}$'
                  '\n\n'            
         r'$X = 1 - \dfrac{C_A}{C_{A0}}$'
                  '\n\n'                  
         'For an Ideal CSTR'
         '\n\n'
        
         r'$C_{A} = C_{A0}*(1-X)$'
                  '\n\n' 
         r'$X = \dfrac{tau*k}{1+tau*k}$'

         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_alpha = plt.axes([0.26, 0.80, 0.15, 0.02], facecolor=axcolor)
ax_beta = plt.axes([0.26, 0.75, 0.15, 0.02], facecolor=axcolor)
ax_k = plt.axes([0.26, 0.70, 0.15, 0.02], facecolor=axcolor)

salpha = Slider(ax_alpha, r'$\alpha$', 0.01, 1, valinit=0.8,valfmt = '%1.2f')
sbeta = Slider(ax_beta, r'$\beta$', 0,1, valinit=0.1,valfmt = '%1.2f')
sk = Slider(ax_k, r'$k \thinspace (min^{-1})$', 0.005,0.1, valinit=0.03, valfmt = '%1.2f')

def update_plot2(val):
    alpha = salpha.val
    beta = sbeta.val
    k =sk.val
    X = (((beta + alpha*tau*k)*(beta + (1 - alpha)*tau*k))-beta**2)/(((1 + beta + alpha*tau*k)*(beta + (1 - alpha)*tau*k))-beta**2);
    CA = CA0*(1 - X);
    XCSTR = tau*k/(1 + tau*k);
    CACSTR = CA0*(1 - XCSTR);
    p1.set_ydata(X)
    p2.set_ydata(XCSTR)
    p3.set_ydata(CA)
    p4.set_ydata(CACSTR)
    fig.canvas.draw_idle()

salpha.on_changed(update_plot2)
sbeta.on_changed(update_plot2)
sk.on_changed(update_plot2)

resetax = plt.axes([0.29, 0.85, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    salpha.reset()
    sbeta.reset()
    sk.reset()
   
button.on_clicked(reset)
    
