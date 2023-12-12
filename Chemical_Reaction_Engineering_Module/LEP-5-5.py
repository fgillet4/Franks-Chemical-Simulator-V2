#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
k = 12 
Cao = 0.1
vo=7.15
alpha = 0.037 
yao = 1 
def ODEfun(Yfuncvec, V, k, Cao, vo ,alpha, yao): 
    X = Yfuncvec[0]
    p= Yfuncvec[1] 
    Fa0 = Cao*vo
    Ca = Cao*(1-X)*p
    ra = -k*Ca**2 
    #Differential equations
    dXdW = -ra/Fa0 
    dpdW = -alpha/2/p 
    return np.array([dXdW, dpdW]) 

W = np.linspace(0, 27, 100) # Range for the Volume of the reactor. 
y0 = np.array([0, 1]) # Initial values for the dependent variables Ca and Cb

 
#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""Example 5-5 Effect of Pressure Drop on Conversion""", fontweight='bold', x = 0.2)
plt.subplots_adjust(left  = 0.3)

sol = odeint(ODEfun, y0, W, (k, Cao, vo ,alpha, yao))
X = sol[:, 0]
p= sol[:, 1] 
Fa0 = Cao*vo
Ca = Cao*(1-X)*p
Cb = Cao*X*p/2
Cc = Cb
ra = -k*Ca**2 

p1, p2, p3 = ax2.plot(W, Ca, W, Cb, W, Cc)
ax2.legend(['$C_A$', '$C_B$', '$C_C$'], loc="upper right")
ax2.set_xlabel('Catalyst Weight (Kg)', fontsize='medium')
ax2.set_ylabel('Concentration ($kmol/m^3$)', fontsize='medium')
ax2.set_ylim(0, 0.5)
ax2.set_xlim(0, 27)
ax2.grid()


p4, p5= ax3.plot(W, odeint(ODEfun, y0, W, (k, Cao, vo ,alpha, yao)))
ax3.legend(['X', 'p'], loc="upper right")
ax3.set_xlabel('Catalyst Weight (kg)', fontsize='medium')
ax3.set_ylabel('Conversion, pressure drop', fontsize='medium')
ax3.set_ylim(0, 1.1)
ax3.set_xlim(0, 27)
ax3.grid()


p6 = ax4.plot(W, -ra)[0]
ax4.legend(['$-r_A\prime$'], loc="upper right")
ax4.set_xlabel('Catalyst Weight (kg)', fontsize='medium')
ax4.set_ylabel('Reaction Rate (kmol/h.kg.cat)', fontsize='medium')
ax4.set_ylim(0, 0.5)
ax4.set_xlim(0, 27)
ax4.grid()

ax1.axis('off')
ax1.text(-0.9, -0.7,'Differential Equations'
         '\n\n'
        r'$\dfrac{dX}{dW} = \dfrac{-r_A^\prime}{F_{A0}}$'
                  '\n \n' 
        r'$\dfrac{dp}{dW} = -\dfrac{\alpha}{2.p}$'
                  '\n \n'
         'Explicit Equations'
                  '\n\n'
         r'$C_A = C_{A0}(1-X)p$'
         '\n\n'         
         r'$C_B = \dfrac{C_{A0} \thinspace X p}{2}$'
         '\n\n'
         r'$C_C = C_B$'
         '\n\n'
         r'$r_A^\prime = -kC_A^2$'
         '\n\n'
         r'$F_{A0} = C_{A0}v_0$'

         , ha='left', wrap = True, fontsize=14,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')


#%%
axcolor = 'black'
ax_k = plt.axes([0.32, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Cao = plt.axes([0.32, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_vo = plt.axes([0.32, 0.6, 0.2, 0.02], facecolor=axcolor)
ax_alpha = plt.axes([0.32, 0.55, 0.2, 0.02], facecolor=axcolor)

sk = Slider(ax_k, r'$k \thinspace(\frac{m^6}{kmol.kg_{cat}.h})$', 1, 100, valinit=12, valfmt="%1.1f")
sCao = Slider(ax_Cao, r'$C_{A0} (\frac{kmol}{m^3}$)', 0.0001, 1, valinit=0.1, valfmt="%1.2f") 
svo = Slider(ax_vo, r'$v_0 (\frac{m^3}{h})$', 1, 100, valinit=7.15, valfmt="%1.2f")
salpha = Slider(ax_alpha, r'$\alpha (kg^{-1})$', 0.0001, 0.037, valinit=0.037, valfmt="%1.3f")


def update_plot(val):
    k = sk.val
    Cao = sCao.val
    vo = svo.val
    alpha = salpha.val
    sol = odeint(ODEfun, y0, W, (k, Cao, vo ,alpha, yao))
    X = sol[:, 0]
    p= sol[:, 1] 
    Ca = Cao*(1-X)*p
    Cb = Cao*X*p/2
    Cc = Cb
    ra = -k*Ca**2 
    p1.set_ydata(Ca)
    p2.set_ydata(Cb)
    p3.set_ydata(Cc)
    p4.set_ydata(X)
    p5.set_ydata(p)
    p6.set_ydata(-ra)
    
    fig.canvas.draw_idle()

sk.on_changed(update_plot)
sCao.on_changed(update_plot)
svo.on_changed(update_plot)
salpha.on_changed(update_plot)

resetax = plt.axes([0.38, 0.75, 0.09, 0.05])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    sk.reset()
    sCao.reset()
    svo.reset()
    salpha.reset()
button.on_clicked(reset)


plt.show()
