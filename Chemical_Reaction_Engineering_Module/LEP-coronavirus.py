import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

k1=6e-7
k2=10.58e-9
k3=14.5645
k4=2.0e-3
So= 1386400000
Io=770
def ODEfun(Yfuncvec,t,k1,k2,k3,k4):
    S= Yfuncvec[0]
    I= Yfuncvec[1]
    R= Yfuncvec[2]
    D= Yfuncvec[3]
      #Explicit Equation Inline
    # Differential equations
    dSdt =  -k1*S-k2*I*S;
    dIdt = k1*S+k2*I*S-k3*I-k4*I;
    dRdt=k3*I;
    dDdt=k4*I;
    return np.array([dSdt,dIdt,dRdt,dDdt])

tspan = np.linspace(0,76, 500) # Range for the independent variable
y0 = np.array([So,Io,0,0]) # Initial values for the dependent variables

x_data = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76])
y_data_I = np.array([554,771,1208,1870,2613,4349,5739,7417,9308,11289,13748,16369,19383,22942,26302,28985,31774,33738,35982,37626,38791,51591,55748,56873,57416,57934,58016,57805,56301,54921,53284,52093,49824,47765,45600,43258,39919,37414,35129,32616,30004,27423,25353,23784,22179,20533,19016,17721,16136,14831,13524,12088,10733,9893,8967,8056,7263,6569,6013,5353,5120,4735,4287,3947,3460,3128,2691,2691,2161,2004,1863,1727,1558,1376,1229,1242,1190])
y_data_D = np.array([17,25,41,56,80,106,132,170,213,259,304,361,425,490,563,636,722,811,908,1016,1113,1259,1380,1523,1665,1770,1868,2004,2118,2236,2345,2442,2592,2663,2715,2744,2788,2835,2870,2912,2943,2981,3012,3042,3070,3097,3119,3136,3158,3169,3176,3189,3199,3213,3226,3237,3245,3248,3255,3261,3270,3277,3281,3287,3292,3295,3300,3300,3305,3312,3318,3322,3326,3329,3331,3331,3333])
y_data_H=np.array([1386399429,1386399204,1386398751,1386398074,1386397307,1386395545,1386394129,1386392413,1386390479,1386388452,1386385948,1386383270,1386380192,1386376568,1386373135,1386370379,1386367504,1386365451,1386363110,1386361358,1386360096,1386347150,1386342872,1386341604,1386340919,1386340296,1386340116,1386340191,1386341581,1386342843,1386344371,1386345465,1386347584,1386349572,1386351685,1386353998,1386357293,1386359751,1386362001,1386364472,1386367053,1386369596,1386371635,1386373174,1386374751,1386376370,1386377865,1386379143,1386380706,1386382000,1386383300,1386384723,1386386068,1386386894,1386387807,1386388707,1386389492,1386390183,1386390732,1386391386,1386391610,1386391988,1386392432,1386392766,1386393248,1386393577,1386394009,1386394009,1386394534,1386394684,1386394819,1386394951,1386395116,1386395295,1386395440,1386395427,1386395477])
#%%
#Plot the data
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("""LEP-P-13-11: COVID-19 Analysis""", fontweight='bold', x = 0.18, y=0.98)
plt.subplots_adjust(left=0.3)
fig.subplots_adjust(wspace=0.4,hspace=0.4)
sol =  odeint(ODEfun, y0, tspan, (k1,k2,k3,k4))
S = sol[:, 0]
I = sol[:, 1]
R = sol[:, 2]
D = sol[:, 3]
H=S+R
ax1.axis('off')
ax2.scatter(x_data, y_data_I, label='data',marker='o',color='red',facecolors='none')
p1= ax2.plot(tspan, I)[0]
ax2.grid()
ax2.set_ylim(0, 100000)
ax2.set_xlim(0, 80)
ax2.set_xlabel(r'$Time \thinspace (days)$', fontsize='medium')
ax2.set_ylabel(r'No of People', fontsize='medium')
ax2.legend(['Model fit','Data'], loc='upper right')
ax2.set_title('Infected cases of China (Active)', fontweight='bold', fontsize='medium')

ax3.scatter(x_data, y_data_D, label='data',marker='o',color='red',facecolors='none')
p2= ax3.plot(tspan, D)[0]
ax3.grid()
ax3.set_ylim(0, 6000)
ax3.set_xlim(0, 80)
ax3.set_xlabel(r'$Time  \thinspace(days)$', fontsize='medium')
ax3.set_ylabel(r'No of People', fontsize='medium')
ax3.legend(['Model fit','Data'], loc='upper left')
ax3.set_title('Death cases of China',fontweight='bold', fontsize='medium')

ax4.scatter(x_data, y_data_H, label='data',marker='o',color='red',facecolors='none')
p3= ax4.plot(tspan, H)[0]
ax4.grid()
ax4.set_ylim(1.38630*1000000000, 1.38645*1000000000)
ax4.set_xlim(0, 80)
ax4.set_xlabel(r'$Time \thinspace (days)$', fontsize='medium')
ax4.set_ylabel(r'No of People', fontsize='medium')
ax4.legend(['Model fit','Data'], loc='lower right')
ax4.set_title('Healthy cases of China',fontweight='bold', fontsize='medium')

ax3.text(-75, 7000,'Differential Equations'
         '\n\n'
         r'$\dfrac{dS}{dt} = -k_1*S-k2*S*I$'
         '\n'
         r'$\dfrac{dI}{dt} = k_1*S+k_2*I*S-k_3*I-k_4*I $'
         '\n'
         r'$\dfrac{dR}{dt} = k_3*I$'
                  '\n' 
         r'$\dfrac{dD}{dt} = k_4*I$'
                  '\n\n'         
                  
         'Explicit Equations'
                  '\n\n'
        r'$H=S+R$'
                 '\n'
      , ha='left', wrap = True, fontsize=13,
        bbox=dict(facecolor='none', edgecolor='black', pad=11.0), fontweight='bold')

axcolor = 'black'
ax_k1 = plt.axes([0.35, 0.82, 0.15, 0.015], facecolor=axcolor)
ax_k2 = plt.axes([0.35, 0.78, 0.15, 0.015], facecolor=axcolor)
ax_k3 = plt.axes([0.35, 0.74, 0.15, 0.015], facecolor=axcolor)
ax_k4 = plt.axes([0.35, 0.70, 0.15, 0.015], facecolor=axcolor)
ax_So = plt.axes([0.35, 0.66, 0.15, 0.015], facecolor=axcolor)
ax_Io = plt.axes([0.35, 0.62, 0.15, 0.015], facecolor=axcolor)

sk1n = Slider(ax_k1, r'$k_1 *10^{-7}$',0,20, valinit=6,valfmt='%1.1f')
sk2n = Slider(ax_k2,r'$k_2*10^{-9}$',10, 12, valinit=10.58,valfmt='%1.2f')
sk3 = Slider(ax_k3,r'$k_3$', 7, 20, valinit= 14.5645,valfmt='%1.4f')
sk4n = Slider(ax_k4,r'$k_4*10^{-3}$ ', 0, 25, valinit= 2,valfmt='%1.1f')
sSon = Slider(ax_So,r'$S (0)*10^{9}$ ', 1, 1.5, valinit= 1.3864,valfmt='%1.4f')
sIo = Slider(ax_Io,r'$I (0)$ ', 0, 25000, valinit= 770,valfmt='%1.0f')

def update_plot2(val):
    k1=sk1n.val*10**-7
    k2=sk2n.val*10**-9
    k3 =sk3.val
    k4=sk4n.val*10**-3
    So=sSon.val*10**9
    Io =sIo.val
    y0 = np.array([So,Io,0,0])
    sol = odeint(ODEfun, y0, tspan, (k1,k2,k3,k4))
    S = sol[:, 0]
    I = sol[:, 1]
    R = sol[:, 2]
    D = sol[:, 3]
    H=S+R  
    p1.set_ydata(I)
    p2.set_ydata(D)
    p3.set_ydata(H)
    fig.canvas.draw_idle()

sk1n.on_changed(update_plot2)
sk2n.on_changed(update_plot2)
sk3.on_changed(update_plot2)
sk4n.on_changed(update_plot2)
sSon.on_changed(update_plot2)
sIo.on_changed(update_plot2)

resetax = plt.axes([0.37, 0.88, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sk1n.reset()
    sk2n.reset()
    sk3.reset()
    sk4n.reset()
    sSon.reset()
    sIo.reset()
button.on_clicked(reset)