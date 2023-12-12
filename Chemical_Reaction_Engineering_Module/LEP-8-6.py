#Libraries
import numpy as np
from scipy.optimize import fsolve
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
k1a = 10
k2c = 15
Cao = 2
Cbo = 2
V = 2500
v = 100
def MNLEfun(x, k1a, k2c, V, v, Cao, Cbo):
    Ca = x[0]
    Cb = x[1]
    Cc = x[2]
    Cd = x[3]

    r2c = 0 - (k2c * Ca ** 2 * Cc ** 3)
    r1a = 0 - (k1a * Ca * Cb ** 2)
    r1b = 2 * r1a
    r2a = 2 / 3 * r2c
    r1c = 0 - r1a
    r2d = -1 / 3 * r2c
    rb = r1b
    ra = r1a + r2a
    rc = r1c + r2c
    rd = r2d

    # Nonlinear equations
    f1 = v * Cao - (v * Ca) + ra * V
    f2 = v * Cbo - (v * Cb) + rb * V
    f3 = 0 - (v * Cc) + rc * V
    f4 = 0 - (v * Cd) + rd * V
    
    return np.array([f1, f2, f3, f4])

#%%   
xguess = np.array([0.5, 0.5, 0.5, 0.5])
sol=fsolve(MNLEfun, xguess, args=( k1a, k2c, V, v, Cao, Cbo))
Ca = sol[0]
Cb = sol[1]
Cc = sol[2]
Cd = sol[3]
Scd = np.nan_to_num(Cc/Cd)

clust_data = np.array([[Ca, Cb, Cc, Cd, Scd]])
clust_data = np.round(clust_data, 3)
collabel=(r'C$_A$', r'C$_B$',r'C$_C$', r'C$_D$', r'S$_{cd}$',)
resetax = plt.axes([0.22, 0.52, 0.2, 0.06])
plt.axis('off')
p1 = plt.table(cellText=clust_data,colLabels=collabel,loc='center')
p1.auto_set_font_size(False)
p1.set_fontsize(13)

axcolor = 'black'
ax_k1a = plt.axes([0.15, 0.8, 0.3, 0.015], facecolor=axcolor)
ax_k2c = plt.axes([0.15, 0.76, 0.3, 0.015], facecolor=axcolor)
ax_V = plt.axes([0.15, 0.72, 0.3, 0.015], facecolor=axcolor)
ax_v = plt.axes([0.15, 0.68, 0.3, 0.015], facecolor=axcolor)
ax_Cao = plt.axes([0.15, 0.64, 0.3, 0.015], facecolor=axcolor)
ax_Cbo = plt.axes([0.15, 0.6, 0.3, 0.015], facecolor=axcolor)
#
sk1a = Slider(ax_k1a, r'$k_{1A}(\frac{dm^6}{mol^2.min})$', 1, 30, valinit=10,valfmt='%1.1f')
sk2c= Slider(ax_k2c, r'k$_{2C}(\frac{dm^{12}}{mol^4.min})$', 1, 30, valinit=15,valfmt='%1.1f')
sV = Slider(ax_V, r'$V (dm^3)$', 500, 4000, valinit=2500,valfmt='%1.0f')
sv = Slider(ax_v, r'$v_0(\frac{dm^3}{min})$', 10, 500, valinit=100,valfmt='%1.0f')
sCao = Slider(ax_Cao,r'C$_{A0} (\frac{mol}{dm^3})$', 1, 10, valinit= 2,valfmt='%1.1f')
sCbo = Slider(ax_Cbo, r'C$_{B0} (\frac{mol}{dm^3})$', 1, 10, valinit=2,valfmt='%1.1f')

plt.text(-1.83, -5,
         'Default/Original Values ->'
                      '\n'       
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='Red', pad=13), fontweight='bold')

plt.text(-1.03, 20,
         'Updated Values ->'
         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='Red', pad=13), fontweight='bold')


plt.text(14.83, -25,
                  
         'Equations'
         '\n\n'            
          r'$f(C_A)= v_0*C_{A0}-v_0*C_A+r_A*V$'
         '\n\n'     
         r'$f(C_B)= v_0*C_{B0}-v_0*C_B+r_B*V$'
         '\n\n' 
         r'$f(C_C)= -v_0*C_C+r_C*V$'
         '\n\n'
         r'$f(C_D)= -v_0*C_D+r_D*V$'
         '\n\n'
          r'$r_{1A} = -k_{1A}C_AC_B^2$'
                '\n\n'
        r'$r_{1B} = 2r_{1A}$'
                '\n\n'
        r'$r_B = r_{1B}$'
                '\n\n'
        r'$r_{2C} = -k_{2C}C_A^2C_C^3$'
                '\n\n'
        r'$r_{2A} = (2/3)r_{2C}$'
                '\n'
        r'$r_{2D} = -(1/3)r_{2C}$'
                '\n'
        r'$r_{1C} = -r_{1A}$'
                '\n'
        r'$r_D = r_{2D}$'
                '\n'
        r'$r_A = r_{1A}+ r_{2A}$'
                '\n\n'
        r'$r_C = r_{1C} + r_{2C}$'
                '\n\n'
        r'$S_{C/D}=C_C/C_D$'
              '\n'       
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=13), fontweight='bold')

def update_plot2(val):
    k1a = sk1a.val
    k2c =sk2c.val
    V = sV.val
    v =sv.val
    Cao = sCao.val
    Cbo = sCbo.val
    sol=fsolve(MNLEfun, xguess, args=( k1a, k2c, V, v, Cao, Cbo))
    Ca = sol[0]
    Cb = sol[1]
    Cc = sol[2]
    Cd = sol[3]
    Scd = np.nan_to_num(Cc/Cd)
    clust_data = np.array([[Ca, Cb, Cc, Cd, Scd]])
    clust_data = np.round(clust_data, 3)
    collabel=(r'C$_A$', r'C$_B$',r'C$_C$', r'C$_D$', r'S$_{cd}$')
    p1 = plt.table(cellText=clust_data,colLabels=collabel,loc='bottom')
    p1.auto_set_font_size(True)
    #p1.set_fontsize(13)
   # p1.set_text_props(clust_data) 
#    plt.canvas.draw_idle()

sk1a.on_changed(update_plot2)
sk2c.on_changed(update_plot2)
sV.on_changed(update_plot2)
sv.on_changed(update_plot2)
sCao.on_changed(update_plot2)
sCbo.on_changed(update_plot2)

resetax = plt.axes([0.22, 0.92, 0.2, 0.06])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1a.reset()
    sk2c.reset()
    sV.reset()
    sv.reset()
    sCao.reset()
    sCbo.reset()
button.on_clicked(reset)

    