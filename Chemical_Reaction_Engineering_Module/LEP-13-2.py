#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
Nao=9.0448
Nbo=33
Nco=103.7
UA=35.85
DeltaHrx = -590000
t1=45
t2=55
Ta=298
A=37.60
Ea=11273
def ODEfun(Yfuncvec,t,Nao,Nbo,Nco,UA,DeltaHrx,t1,t2,Ta,A,Ea):
    T= Yfuncvec[0]
    X= Yfuncvec[1]
      #Explicit Equation Inline
    k = A*np.exp(-Ea /(1.987* T)) 
    NCp=Nao*40+Nbo*8.38+Nco*18
    Vaqam=3.9
    VONCB=(Nao*157.55)/1199
    V=Vaqam+VONCB
    if (t > t1 and t < t2): 
        Qr = 0
    else:
        Qr = UA * (T - Ta)
    Theata = Nbo / Nao
    ra = 0 - (k * Nao** 2 * (1 - X) * (Theata - (2 * X)) / (V** 2))
    Qg = ra * V * DeltaHrx
     # Differential equations
    dTdt = np.where(t<t1, 0, (Qg - Qr) / NCp)
    dXdt = (0 - ra) * V / Nao;
    return np.array([dTdt,dXdt])

tspan = np.linspace(0,122, 1000) # Range for the independent variable
y0 = np.array([448,0]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-13-2: Safety in Chemical Plants with Exothermic Runaway Reactions""", fontweight='bold', x = 0.25, y=0.98)
plt.subplots_adjust(left=0.37)
fig.subplots_adjust(wspace=0.3,hspace=0.3)
sol =  odeint(ODEfun, y0, tspan, (Nao,Nbo,Nco,UA,DeltaHrx,t1,t2,Ta,A,Ea))
T = sol[:, 0]
X = sol[:, 1]
k = A *np.exp(-Ea /(1.987* T))
Vaqam=3.9
VONCB=(Nao*157.55)/1199
V=Vaqam+VONCB
Theata = Nbo / Nao;
ra = 0 - (k * Nao**2 * (1 - X) * (Theata - (2 * X)) / (V** 2)) 
Qg = ra * V * DeltaHrx
Qr = []
for i in range(len(tspan)):
    if (tspan[i] > t1 and tspan[i] < t2):  
        Qr.append(0)
    else:
        Qr.append(UA * (T[i] - Ta))
p1= ax3.plot(tspan, X)[0]
ax3.legend([r'$X$'], loc='upper left')
ax3.set_xlabel('time $(min)$', fontsize='medium')
ax3.set_ylabel(r'Conversion', fontsize='medium')
ax3.grid()
ax3.set_ylim(0, 1.05)
ax3.set_xlim(0, 122)

p2 = ax2.plot(tspan, T)[0]
ax2.legend([r'$T$'], loc='upper left')
ax2.set_xlabel('time $(min)$', fontsize='medium')
ax2.set_ylabel(r'Temperature $(K)$', fontsize='medium')
ax2.grid()
ax2.set_ylim(400, 1000)
ax2.set_xlim(0, 122)

p3, p4 = ax4.plot(tspan,Qg,tspan,Qr)
ax4.legend(['$Q_g$', '$Q_r$'], loc='upper left')
ax4.set_xlabel('time $(min)$', fontsize='medium')
ax4.set_ylabel(r'Q $(kcal/min)$', fontsize='medium')
ax4.grid()
ax4.set_ylim(0, 50000)
ax4.set_xlim(0, 120)

ax1.text(-1.5, -1.5,'Note: While we used the expression k=$k_1$*exp(E/R*(1/$T_1$ - 1/$T_2$)) \n         in the textbook, in python we have to use k=A*exp(-E/RT) \n          in order to explore all the variables.',wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='red', pad=10))

ax1.text(-1.42, -0.9,'Differential Equations'
         '\n'
         r'$\dfrac{dT}{dt} = if\hspace{0.5}(t<t_1)\hspace{0.5} then\hspace{0.5} (0)\hspace{0.5} else \hspace{0.5}\dfrac{(Q_g - Q_r)}{N*C_P}$'
         '\n'
         r'$\dfrac{dX}{dt} = -r_A* \hspace{0.5}\dfrac{V}{N_{A0}} $'
         '\n\n'
         'Explicit Equations'
         '\n\n'
         r'$A = 37.60 \thinspace m^{3}/(kmol.min)$'
                '\n\n'
         r'$NC_P=N_{A0}C_{P_A}+N_{B0}C_{P_B}+N_{W}C_{P_W}$'
         '\n\n'
         r'$V_{A}=N_{A0}*(157.55/1199)$'
         '\n\n'
         r'$V_{aqam}=3.9$'
        '\n\n'
         r'$V=V_{A}+V_{aqam} $'
         '\n\n'
          r'$k = A*exp\left(\dfrac{-E}{1.987*T}\right)$'  
         '\n\n'
         r'$\theta_B=N_{B0}/N_{A0}$'
         '\n\n'
         r'$Q_r=if\hspace{0.5} (t> t_1 \hspace{0.5}and\hspace{0.5} t<t_2)\hspace{0.5} then (0)\hspace{0.5} else\hspace{0.5} UA*(T-T_a) $'
         '\n\n'
         r'$Q_g=r_A*V *(-\Delta H_{Rx})$'
         '\n\n'
         r'$r_A=-k*{(C_{A0}}^2 (1-X))*(\theta_B-2X)$'
         '\n'
          , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
ax1.text(-1.38, -1.1,
         'Instructions: $t_1$ should always be less than or equal to $t_2$'
        , ha='left', wrap = True, fontsize=12, 
         bbox=dict(facecolor='none', edgecolor='Red', pad=10.0))


ax1.axis('off')
axcolor = 'black'
ax_Nao = plt.axes([0.37, 0.80, 0.18, 0.015], facecolor=axcolor)
ax_Nbo = plt.axes([0.37, 0.76, 0.18, 0.015], facecolor=axcolor)
ax_Nco = plt.axes([0.37, 0.72, 0.18, 0.015], facecolor=axcolor)
ax_UA = plt.axes([0.37, 0.68, 0.18, 0.015], facecolor=axcolor)
ax_DeltaHrx = plt.axes([0.37, 0.64, 0.18, 0.015], facecolor=axcolor)
ax_t1 = plt.axes([0.37, 0.60, 0.18, 0.015], facecolor=axcolor)
ax_t2 = plt.axes([0.37, 0.56, 0.18, 0.015], facecolor=axcolor)
ax_Ta = plt.axes([0.37, 0.52, 0.18, 0.015], facecolor=axcolor)
ax_Ea = plt.axes([0.37, 0.48, 0.18, 0.015], facecolor=axcolor)

sNao = Slider(ax_Nao, r'$N_{A0}$($kmol$)', 2, 20, valinit=9.0448,valfmt='%1.1f')
sNbo= Slider(ax_Nbo, r'$N_{B0}$ ($kmol$)', 10, 80, valinit=33,valfmt='%1.0f')
sNco = Slider(ax_Nco,r'$N_{C0}$($kmol$)',10, 300, valinit=103.7,valfmt='%1.1f')
sUA = Slider(ax_UA,r'$UA$($\frac{kcal}{min. C}$)', 10, 70, valinit= 35.85,valfmt='%1.0f')
sDeltaHrx = Slider(ax_DeltaHrx,r'$\Delta H_{Rx}$($\frac{kcal}{kmol}$)', -900000,-200000, valinit=-5.9e5,valfmt='%1.0f')
st1 = Slider(ax_t1,r'$t_1$ ($min$)', 5, 100, valinit= 45,valfmt='%1.0f')
st2 = Slider(ax_t2,r'$t_2$ ($min$)', 5, 100, valinit= 55,valfmt='%1.0f')
sTa=Slider(ax_Ta,r'$T_a$ ($K$)', 273, 350, valinit= 298,valfmt='%1.0f')
sEa = Slider(ax_Ea, r'$E$($\frac{cal}{mol}$)', 5000, 22000, valinit=11273,valfmt='%1.0f')

def update_plot2(val):
    Nao = sNao.val
    Nbo = sNbo.val
    Nco = sNco.val
    UA =  sUA.val
    DeltaHrx = sDeltaHrx.val
    t1 =st1.val
    t2 =st2.val
    Ta=sTa.val
    Ea=sEa.val
    sol = odeint(ODEfun, y0, tspan, (Nao,Nbo,Nco,UA,DeltaHrx,t1,t2,Ta,A,Ea))
    T = sol[:, 0]
    X = sol[:, 1]
    k = A *np.exp(-Ea /(1.987* T))
    Vaqam=3.9
    VONCB=(Nao*157.55)/1199
    V=Vaqam+VONCB
    Theata = Nbo / Nao;
    ra = 0 - (k * Nao**2 * (1 - X) * (Theata - (2 * X)) / (V** 2)) 
    Qg = ra * V * DeltaHrx
    Qr = []
    for i in range(len(tspan)):
        if (tspan[i] > t1 and tspan[i] < t2):  
            Qr.append(0)
        else:
            Qr.append(UA * (T[i] - Ta))    
    p1.set_ydata(X)
    p2.set_ydata(T)
    p3.set_ydata(Qg)
    p4.set_ydata(Qr)
    fig.canvas.draw_idle()

sNao.on_changed(update_plot2)
sNbo.on_changed(update_plot2)
sNco.on_changed(update_plot2)
sUA.on_changed(update_plot2)
sDeltaHrx.on_changed(update_plot2)
st1.on_changed(update_plot2)
st2.on_changed(update_plot2)
sTa.on_changed(update_plot2)
sEa.on_changed(update_plot2)

resetax = plt.axes([0.41, 0.84, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sNao.reset()
    sNbo.reset()
    sNco.reset()
    sUA.reset()
    sDeltaHrx.reset()
    st1.reset()
    st2.reset()
    sTa.reset()
    sEa.reset()
button.on_clicked(reset)

