#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
def ODEfun(Yfuncvec, t): 
    # Explicit equations
    C1= 0.0038746 + 0.2739782*t + 1.574621*t**2 - 0.2550041*t**3
    C2= -33.43818 + 37.18972*t - 11.58838*t**2 + 1.695303*t**3 - 0.1298667*t**4 + 0.005028*t**5 - 7.743*10**-5*t**6
    C = np.where(t<=4, C1, C2)
    E=C/51
    dFdt=E
    dtmdt=t*E
    # Differential equations
    return np.array([dFdt, dtmdt])

tspan = np.linspace(0, 14, 100)
y0 = np.array([0,0])

#%%
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("""LEP-16-2: Mean Residence Time and Variance Calculations (Part a,b)""", x = 0.24, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.3)

C1= 0.0038746 + 0.2739782*tspan + 1.574621*tspan**2 - 0.2550041*tspan**3
C2= -33.43818 + 37.18972*tspan - 11.58838*tspan**2 + 1.695303*tspan**3 - 0.1298667*tspan**4 + 0.005028*tspan**5 - 7.743*10**-5*tspan**6
C = np.where(tspan<=4, C1, C2)
E=C/51
sol = odeint(ODEfun, y0, tspan)
F = sol[:, 0]
tm = sol[:, 1]
ax1.plot(tspan, tm)
ax1.legend(['$t_m$'], loc='best')
ax1.set_xlabel('t (min)', fontsize='medium')
ax1.set_ylabel('$t_m (min)$', fontsize='medium')
#ax1.set_ylim(0,10)
ax1.set_xlim(0,14)
ax1.set_ylim(0,8)
ax1.grid()
ax1.text(-12.5, 3,'Differential Equations'
         '\n\n'
         r'$\dfrac{dF}{dt} = E$'
                  '\n\n'
         r'$\dfrac{dt_m}{dt} = t.E$'
         '\n\n'

         'Explicit Equations'
         '\n\n'
         r'$C_1= +0.0038746 + 0.2739782t$''\n\t'
         r'$+ 1.574621t^2 - 0.2550041t^3$''\n\n'
         r'$C2= -33.43818 + 37.18972t$''\n\t'
         r'$- 11.58838t^2 + 1.695303t^3$''\n\t'
         r'$- 0.1298667t^4 + 0.005028t^5$''\n\t'
         r'$- 7.743.10{^-5}t^6$'    
         '\n\n'
         r'$C = If\hspace{0.5} (t<=t1)\hspace{0.5} then\hspace{0.5} (C_1) \hspace{0.5}else\hspace{0.5} (C_2)$'
         '\n\n'
         r'$E = \dfrac{C}{51}$'
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


ax2.plot(tspan, F)
ax2.legend(['F'], loc='best')
ax2.set_xlabel('t (min)', fontsize='medium')
ax2.set_ylabel('F(t)', fontsize='medium')
#ax2.set_ylim(0,10)
ax2.set_xlim(0,14)
ax2.set_ylim(0,1)
ax2.grid()

