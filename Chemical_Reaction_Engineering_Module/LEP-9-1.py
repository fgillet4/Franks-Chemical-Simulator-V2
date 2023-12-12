#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
k1=0.3
k2=0.5
k3=2
k4=1
CS2=10
M=10
X = np.linspace(0.0001, 10, 100)
def func(X, k1,k2,k3,k4,CS2,M):
    
    f1 = k4*k1*CS2*M/(k2*M+k3*X+k4)    
    f3=  1+ k3*X/(k2*M+k4)
    return np.array([f1,f3])


#%%
k12=0.3
k22=0.5
k42=1
M2=10
CS22 = np.linspace(0.0001, 10, 100)
def func2(CS22, k12,k22,k42,M2):
    f2 = k42*k12*CS22*M2/(k22*M2+k42)    
    return np.array([f2])

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 9-1 The Stern-Volmer Equation""", fontweight='bold', x = 0.2, y= 0.98)
fig.subplots_adjust(hspace=0.3)
plt.subplots_adjust(left  = 0.4)

sol = func(X, k1,k2,k3,k4,CS2,M)
I = sol[0, :]
I_ratio=sol[1, :]

sol2 = func2(CS22, k12,k22,k42,M2)
I2 = sol2[0, :]

p1 = ax3.plot(X,I)[0]
ax3.legend(['$I$'], loc='best')
ax3.set_xlabel('$X (Alcohol)$', fontsize='medium')
ax3.set_ylabel('$Intensity \hspace{0.2} (Alcohol \hspace{0.2} presence)$', fontsize='medium')
ax3.set_ylim(0,30)
ax3.set_xlim(0,10)
ax3.grid()

p3 = ax4.plot(X,I_ratio)[0]
ax4.legend([r'$\frac{I_0}{I}$'], loc='best', fontsize='large')
ax4.set_xlabel('$X (Alcohol)$', fontsize='medium')
ax4.set_ylabel(r'$Intensity \hspace{0.2} ratio$', fontsize='medium')
ax4.set_ylim(0,6)
ax4.set_xlim(0,10)
ax4.grid()

p2 = ax2.plot(CS22,I2)[0]
ax2.legend(['$I$'], loc='best')
ax2.set_xlabel('$CS_2$', fontsize='medium')
ax2.set_ylabel('$Intensity \hspace{0.2} (Alcohol \hspace{0.2} absence)$', fontsize='medium')
ax2.set_ylim(0,4)
ax2.set_xlim(0,10)
ax2.grid()

ax1.axis('off')
ax2.text(-23.83, -0.8,
                  
         'Equations'
                  '\n\n'
          'In the presence of Alcohol'
          '\n\n'
          r'$I = \dfrac{k_4*k_1*CS_2*M}{(k_2*M+k_3*X+k_4)}$'
                 '\n\n'                 
          'In the absence of Alcohol'
          '\n\n'
          r'$I_0 = \dfrac{k_4*k_1*CS_2*M}{(k_2*M+k_4)}$'
                 '\n\n' 
        'Intensity Ratio'
         '\n\n'
         r'$\dfrac{I_0}{I}=1+\dfrac{k_3*X}{k_2 *M +k_4}$'
         '\n\n'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k1 = plt.axes([0.1, 0.38, 0.2, 0.015], facecolor=axcolor)
ax_k2 = plt.axes([0.1, 0.34, 0.2, 0.015], facecolor=axcolor)
ax_k3 = plt.axes([0.1, 0.30, 0.2, 0.015], facecolor=axcolor)
ax_k4 = plt.axes([0.1, 0.26, 0.2, 0.015], facecolor=axcolor)
ax_CS2 = plt.axes([0.1, 0.22, 0.2, 0.015], facecolor=axcolor)
ax_M = plt.axes([0.1, 0.18, 0.2, 0.015], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1$', 0.01, 5, valinit=0.3,valfmt='%1.2f')
sk2 = Slider(ax_k2, r'$k_2$', 0.01, 5, valinit=0.5,valfmt='%1.2f')
sk3 = Slider(ax_k3, r'$k_3$', 0.01, 5, valinit=2,valfmt='%1.2f')
sk4 = Slider(ax_k4, r'$k_4$', 0.01, 10, valinit=1,valfmt='%1.2f')
sCS2 = Slider(ax_CS2, r'$CS_2$', 0.01, 50, valinit=10,valfmt='%1.2f')
sM = Slider(ax_M, r'$M$', 0.01, 50, valinit=10,valfmt='%1.2f')

#%%
axcolor = 'black'
ax_k12 = plt.axes([0.36, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_k22 = plt.axes([0.36, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_k42 = plt.axes([0.36, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_M2 = plt.axes([0.36, 0.6, 0.2, 0.02], facecolor=axcolor)

sk12 = Slider(ax_k12, r'$k_1$', 0.01, 5, valinit=0.3,valfmt='%1.2f')
sk22 = Slider(ax_k22, r'$k_2$', 0.01, 5, valinit=0.5,valfmt='%1.2f')
sk42 = Slider(ax_k42, r'$k_4$', 0.01, 10, valinit=1,valfmt='%1.2f')
sM2 = Slider(ax_M2, r'$M$', 0.01, 50, valinit=10,valfmt='%1.2f')
##
def update_plot2(val):
    k1 = sk1.val
    k2 = sk2.val
    k3 = sk3.val
    k4 = sk4.val    
    CS2 =sCS2.val
    M =sM.val
    sol = func(X, k1,k2,k3,k4,CS2,M)
    p1.set_ydata(sol[0,:])
    p3.set_ydata(sol[1,:])
    k12 = sk12.val
    k22 = sk22.val
    k42 = sk42.val   
    M2 =  sM2.val
    sol2 = func2(CS22, k12,k22,k42,M2)
    p2.set_ydata(sol2)
    fig.canvas.draw_idle()


sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
sk4.on_changed(update_plot2)
sCS2.on_changed(update_plot2)
sM.on_changed(update_plot2)
#

sk12.on_changed(update_plot2)
sk22.on_changed(update_plot2)
sk42.on_changed(update_plot2)
sM2.on_changed(update_plot2)
#

resetax = plt.axes([0.4, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
    sk4.reset()
    sCS2.reset()
    sM.reset()
    
    sk12.reset()
    sk22.reset()
    sk42.reset()
    sM2.reset()
        
button.on_clicked(reset)    

