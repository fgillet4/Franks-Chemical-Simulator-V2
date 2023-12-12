#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button
#%%
vo=2
Cao=0.4
k1=0.0001
k2=0.0015
k3=0.008
Ca = np.linspace(0, 0.5, 100)
def func(Ca,vo,Cao,k1,k2,k3):
    f1 = vo*(Cao-Ca)/(k1+k2*Ca+k3*Ca**2)    
    f2=  k2*Ca/(k1+k3*Ca**2)
    return np.array([f1,f2])

#%%
def ODEfun(Yfuncvec, Wspan, k1,k2,k3): 
    Ca = Yfuncvec[0] 
    Cx = Yfuncvec[1] 
    Cb = Yfuncvec[2] 
    Cy = Yfuncvec[3] 
    # Differential equations
    dCadt = -k1-k2*Ca-k3*Ca**2 
    dCxdt = k1 
    dCbdt = k2*Ca 
    dCydt = k3*Ca**2  
    return np.array([dCadt, dCxdt, dCbdt, dCydt]) 

Wspan = np.linspace(0, 300, 10000) # Range for the independent variable
y0 = np.array([0.112,0.0783, 0.132, 0.0786]) # Initial values for the dependent variables

fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""Example 8-1 Trambouze Reactions""", fontweight='bold', x = 0.2, y= 0.98)
fig.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplots_adjust(left  = 0.4)

sol = func(Ca,vo,Cao,k1,k2,k3)
V = sol[0, :]
SBXY=sol[1, :]

p1 = ax1.plot(Ca,V)[0]
ax1.legend(['$V $'], loc='best')
ax1.set_xlabel(r'$C_A (\frac{mol}{dm^3})$', fontsize='medium')
ax1.set_ylabel('$V (dm^3)$', fontsize='medium')
ax1.set_ylim(0,5000)
ax1.set_xlim(0,0.5)
ax1.grid()
ax1.set_title('Part a')

p2 = ax2.plot(Ca,SBXY)[0]
ax2.legend([r'$S_{\frac{B}{XY}}$'], loc='best', fontsize='large')
ax2.set_xlabel(r'$C_A (\frac{mol}{dm^3})$', fontsize='medium')
ax2.set_ylabel(r'$Selectivity$', fontsize='medium')
ax2.set_ylim(0,2)
ax2.set_xlim(0,0.5)
ax2.grid()
ax2.set_title('Part a')

sol1 = odeint(ODEfun, y0, Wspan, (k1,k2,k3))
Ca1 = sol1[:,0] 
Cx = sol1[:, 1] 
Cb = sol1[:, 2] 
Cy = sol1[:, 3] 
Sbxy=Cb/(Cx+Cy)

p3,p4,p5,p6 = ax3.plot(Wspan,Ca1,Wspan,Cx,Wspan,Cb,Wspan,Cy)
ax3.legend(['$C_A$','$C_X$','$C_B$','$C_Y$'], loc='upper right')
ax3.set_ylim(0,0.6)
ax3.set_xlim(0,300)
ax3.grid()
ax3.set_xlabel('tau (s)', fontsize='medium' )
ax3.set_ylabel(r'$Concentration (\frac{mol}{dm^3})$', fontsize='medium')
ax3.set_title('Part b')

p7 = ax4.plot(Wspan,Sbxy)[0]
ax4.legend([r'$S_{\frac{B}{XY}}$'], loc='upper right', fontsize='large')
ax4.set_ylim(0.7,0.9)
ax4.set_xlim(0,300)
ax4.grid()
ax4.set_xlabel('tau (s)', fontsize='medium' )
ax4.set_ylabel(r'$Selectivity$', fontsize='medium')
ax4.set_title('Part b')

ax1.text(-0.7, -7500.5,
                  
         'Equations'
                  '\n\n'
          'Part a (CSTR):'
          '\n\n'
           r'$v_o = 2$'
         '\n'
          r'$C_{A0} = 0.4$'
         '\n'
          r'$V = \dfrac{v_0*(C_{A0}-C_A)}{k_1+k_2*C_A+k_3*C_A^2}$'
                 '\n\n'  
          r'$S_{B/XY}=\dfrac{k_2*C_A}{k_1+k_3*C_A^2}$'
          '\n\n'
          'Part b (PFR):'
          '\n\n'
         
          r'$\dfrac{dC_A}{d\tau} = -k_1-k_2*C_A-k_3*C_A^2$'
         '\n'
         r'$\dfrac{dC_X}{d\tau} = k_1$'
         '\n'
         r'$\dfrac{dC_B}{d\tau} = k_2*C_A$'
         '\n'
         r'$\dfrac{dC_Y}{d\tau} = k_3*C_A^2$'
         '\n'
          r'$S_{B/XY}=\dfrac{C_B}{C_X+C_Y}$'
          '\n'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')
#%%
axcolor = 'black'
ax_k1 = plt.axes([0.1, 0.82, 0.2, 0.015], facecolor=axcolor)
ax_k2 = plt.axes([0.1, 0.78, 0.2, 0.015], facecolor=axcolor)
ax_k3 = plt.axes([0.1, 0.74, 0.2, 0.015], facecolor=axcolor)

sk1 = Slider(ax_k1, r'$k_1(\frac{mol}{dm^3.s})$', 0.00001, 0.01, valinit=0.0001,valfmt='%1.4f')
sk2 = Slider(ax_k2, r'$k_2 (s^{-1})$', 0.00001, 0.1, valinit=0.0015,valfmt='%1.4f')
sk3 = Slider(ax_k3, r'$k_3(\frac{dm^3}{mol.s})$', 0.00001, 0.01, valinit=0.008,valfmt='%1.3f')

#%%
def update_plot2(val):

    k1 = sk1.val
    k2 = sk2.val    
    k3 =sk3.val
    sol = func(Ca,vo,Cao,k1,k2,k3)
    p1.set_ydata(sol[0,:])
    p2.set_ydata(sol[1,:])
    sol1 = odeint(ODEfun, y0, Wspan, (k1,k2,k3))
    Ca1 = sol1[:,0] 
    Cx = sol1[:, 1] 
    Cb = sol1[:, 2] 
    Cy = sol1[:, 3] 
    Sbxy=Cb/(Cx+Cy)
    p3.set_ydata(Ca1)
    p4.set_ydata(Cx)
    p5.set_ydata(Cb)
    p6.set_ydata(Cy)
    p7.set_ydata(Sbxy)
    fig.canvas.draw_idle()

sk1.on_changed(update_plot2)
sk2.on_changed(update_plot2)
sk3.on_changed(update_plot2)
#
resetax = plt.axes([0.15, 0.88, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1.reset()
    sk2.reset()
    sk3.reset()
        
button.on_clicked(reset)    

