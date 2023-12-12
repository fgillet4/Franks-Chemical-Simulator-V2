#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
t = np.array([0, 0.5, 1, 2, 3, 4])
y = np.array([0, 0.6, 1.4, 5, 8, 10]) 
poly = np.polyfit(t, y, 3)
poly = np.round(poly, 3)
p = np.poly1d(poly)
tspan = np.linspace(0, 4, 100)
Y = p(tspan)
#%%

fig, (ax1,ax2) = plt.subplots(1, 2)
fig.suptitle("""LEP-16-1: Constructing the C(t) and E(t) Curves""", x = 0.25, y=0.98, fontweight='bold')
#plt.subplots_adjust(left  = 0.4)

ax1.scatter(t, y, c='r')
ax1.plot(tspan, Y)
ax1.legend(['Polynomial fit', 'data'], loc='best')
ax1.set_xlabel('t (mins)', fontsize='medium')
ax1.set_ylabel('C(t)', fontsize='medium')
ax1.set_ylim(0,10)
ax1.set_xlim(0,4)
ax1.set_title('Plot of C(t) vs t for ascending portion')
ax1.text(0.5, 8, r'$%1.2ft^3 + %1.2ft^2 + %1.2ft + %1.3f $'%(tuple(poly))
 , ha='left', wrap = True, fontsize=13,
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')
#%%
t1 = np.array([4, 5, 6, 7, 8, 9, 10, 12, 14])
y1 = np.array([10, 8, 6, 4, 3 ,2.2, 1.6, 0.6, 0]) 
poly1 = np.polyfit(t1, y1, 6)
#poly1 = np.round(poly1, 3)
p1 = np.poly1d(poly1)
tspan1 = np.linspace(4, 14, 100)
Y1 = p1(tspan1)

ax2.scatter(t1, y1, c='r')
ax2.plot(tspan1, Y1)
ax2.legend(['Polynomial fit', 'data'], loc='best')
ax2.set_xlabel('t (mins)', fontsize='medium')
ax2.set_ylabel('C(t)', fontsize='medium')
ax2.set_ylim(0,10)
ax2.set_xlim(4,14)
ax2.set_title('Plot of C(t) vs t for descending portion')
ax2.text(6, 8, r'$%1.5ft^6 + %1.3ft^5 + %1.2ft^4 + %1.2ft^3 + %1.2ft^2 + %1.2ft + %1.2f$'%(tuple(poly1))
         , ha='left', wrap = True, fontsize=10,
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0), fontweight='bold')


