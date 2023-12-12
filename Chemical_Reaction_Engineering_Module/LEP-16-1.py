#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
t1=4
r=1
def ODEfun(Yfuncvec, t, t1, r): 
#    A= Yfuncvec(1)
    # Explicit equations
    C1= 0.0038746 + 0.2739782*t + 1.574621*t**2 - 0.2550041*t**3
    C2= -33.43818 + 37.18972*t - 11.58838*t**2 + 1.695303*t**3 - 0.1298667*t**4 + 0.005028*t**5 - 7.743e-5*t**6
    C = np.where(t<=t1, C1, C2)
    dAdt=C*r
    # Differential equations
    return dAdt

tspan = np.linspace(0, 14, 10000)
y0 = 0

#%%
fig, ax = plt.subplots()
fig.suptitle("""LEP-16-1: Constructing the C(t) and E(t) curves""", x = 0.2, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
sol = odeint(ODEfun, y0, tspan,(t1,r))
A =sol[:, 0]
p1=ax.plot(tspan, A)[0]
plt.legend(["Area"], loc='best')
ax.set_xlabel('Time (min)', fontsize='medium')
ax.set_ylabel('Area', fontsize='medium')
plt.ylim(0,55)
plt.xlim(0,14)
plt.grid()
a=(sol[len(tspan)-1]) 

ax.text(-10.5, 10,'Differential Equations'
         '\n\n'
         r'$\dfrac{dA}{dt} = C$'
                  '\n\n'

         'Explicit Equations'
         '\n\n'
         
         r'$C_1= 0.0039 + 0.274t+ 1.57t^2 - 0.255t^3$'
         '\n\n'
         
         r'$C2= -33.4 + 37.2t- 11.6t^2 + 1.7t^3- 0.13t^4 + 0.005t^5- 7.7.10{^-5}t^6$'    
         '\n\n'
         
         r'$C = If\hspace{0.5} (t<=t1) then\hspace{0.5} (C_1) \hspace{0.5}else\hspace{0.5} (C_2)$'
         '\n\n'
         r'$E = \dfrac{C}{A}$'
         '\n\n'
         'Initial Area Under the Curve = %1.3f'%a
         , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')

axcolor = 'black'
ax_t1 = plt.axes([0.1, 0.75, 0.15, 0.02], facecolor=axcolor)
st1 = Slider(ax_t1, r'$t_1 (min)$', 0, 14, valinit= 4,valfmt='%1.1f')

def update_plot(val):
    t1 = st1.val
    sol1 = odeint(ODEfun, y0, tspan,(t1,r))
    p1.set_ydata(sol1[:,0])
    
st1.on_changed(update_plot)

resetax = plt.axes([0.12, 0.8, 0.09, 0.03])
button = Button(resetax, 'Reset Variables', color='cornflowerblue', hovercolor='0.975')


def reset(event):
    st1.reset()
button.on_clicked(reset)

