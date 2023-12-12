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
#    F= Yfuncvec[0]
#    tm= Yfuncvec[1]
    # Explicit equations
    C1= 0.0038746 + 0.2739782*t + 1.574621*t**2 - 0.2550041*t**3
    C2= -33.43818 + 37.18972*t - 11.58838*t**2 + 1.695303*t**3 - 0.1298667*t**4 + 0.005028*t**5 - 7.743*10**-5*t**6
    C = np.where(t<=4, C1, C2)
    E=C/51
    dFdt=E

    # Differential equations
    return dFdt

tspan = np.linspace(3, 6, 100)
y0 = 0

#%%
fig, ax = plt.subplots()
fig.suptitle("""LEP-16-2: Mean Residence Time and Variance Calculations (Part d)""", x = 0.3, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
plt.plot(tspan, odeint(ODEfun, y0, tspan))

plt.legend([r"F"], loc='best')
ax.set_xlabel('Time (mins)', fontsize='medium')
ax.set_ylabel('F', fontsize='medium')
plt.ylim(0,0.5)
plt.xlim(3,6)
plt.grid()

ax.text(1.2, 0.15,'Differential Equations'
         '\n\n'
         r'$\dfrac{dF}{dt} = E$'
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
