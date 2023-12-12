import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
def funca(X, k, KEA, KE):
    RATE = k*X[:,0]*X[:,2]/(1+KEA*X[:,1]+KE*X[:,0])
    return RATE

def funcb(X, k, KE):
    RATE = k*X[:,0]*X[:,2]/(1+KE*X[:,0])
    return RATE

def funcc(X, k, KE):
    RATE = k*X[:,0]*X[:,2]/((1+KE*X[:,0])**2)
    return RATE

def funcd(X, k, a, b):
    RATE = k*(X[:,0]**a)*(X[:,2])**b
    return RATE

Pe = np.array([1,1,1,3,5,0.5,0.5,0.5,0.5])
Pea = np.array([1,1,1,1,1,1,0.5,3,5])
Ph = np.array([1,3,5,3,3,3,5,3,1])
x_data = np.array([Pe, Pea, Ph])
x_data = x_data.T
y_data = np.array([1.04,3.13,5.21,3.82,4.19,2.391,3.867,2.199,0.75])

#%%
#Part a
yo = np.array([3,3,3]) #Initial Guess
popta, pcova = curve_fit(funca, x_data, y_data, p0=yo)

#%%
#Part b
yo = np.array([3,3]) #Initial Guess
poptb, pcovb = curve_fit(funcb, x_data, y_data, p0=yo)

#%%
#Part b
yo = np.array([3,3]) #Initial Guess
poptc, pcovc = curve_fit(funcc, x_data, y_data, p0=yo)

#%%
#Part d
yo = np.array([3,3,3]) #Initial Guess
poptd, pcovd = curve_fit(funcd, x_data, y_data, p0=yo)
#%%
fig, ax = plt.subplots()
fig.suptitle("""Example 10-3 Hydrogenation of Ethylene to Ethane""", fontweight='bold', x = 0.2, y=0.98)


ax.axis([0,100,0,100])
ax.axis('off')
ax.text(50, 70,'Model (a)'
         '\n'
         r'$-r_{E}^\prime = \dfrac{kP_EP_H}{1 + K_{EA}P_{EA} + K_EP_E}$'
                  '\n \n'
         'Optimal Parameter are:' '\n' r'$k = $%f' '\n' r'$K_{EA} = $%f' '\n' r'$K_E = $%f'%(tuple(popta))

        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10))

ax.text(75, 72,'Model (b)'
         '\n'
         r'$-r_{E}^\prime = \dfrac{kP_EP_H}{1 + K_EP_E}$'
                  '\n \n'
         'Optimal Parameter are:' '\n' r'$k = $%f' '\n' r'$K_E = $%f'%(tuple(poptb))

        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10))

ax.text(50, 25,'Model (c)'
         '\n'
         r'$-r_{E}^\prime = \dfrac{kP_EP_H}{1 + (K_EP_E)^2}$'
                  '\n \n'
         'Optimal Parameter are:' '\n' r'$k = $%f' '\n' r'$K_E = $%f'%(tuple(poptc))

        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10))

ax.text(75, 25,'Model (d)'
         '\n'
         r'$-r_{E}^\prime = kP_E^aP_H^b$'
                  '\n \n'
         'Optimal Parameter are:' '\n' r'$k = $%f' '\n' r'$a = $%f' '\n' r'$b = $%f'%(tuple(poptd))

        , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=10))


clust_data = np.hstack((x_data, y_data.reshape(9,1)))
clust_data = np.round(clust_data, 2)
collabel=(r'P$_E (atm)$', r'P$_{EA} (atm)$',r'P$_{H} (atm)$', 'RATE (mol/kg-cat.s)')
plt.axis('off')
p1 = plt.table(cellText=clust_data,colLabels=collabel,
               cellLoc='left', colLoc='left',bbox=[-0.08, 0.3, 0.5, 0.6])
p1.auto_set_font_size(False)
p1.set_fontsize(12)












