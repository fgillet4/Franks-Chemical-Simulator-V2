#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 13})
from matplotlib.widgets import Slider, Button

#%%
# Explicit equations
mu1max = .9      
mu2max = .6      
K1 =     .1      
K2 =     .5      
alpha1 = .0001      
alpha2 = .0001      
beta1 =  .05      
beta2 =  .05      
Ycs1 =   .4      
Ycs2 =   .4 
Cs10 = 4   
Cs20 = 20  
D = .6 
def ODEfun(Yfuncvec, t, mu1max, mu2max, K1, 
           K2, alpha1, alpha2, beta1, beta2,
           Ycs1, Ycs2): 
    Cc = Yfuncvec[0]
    Cs1 =Yfuncvec[1]
    Cs2 =Yfuncvec[2]
    e1 = Yfuncvec[3]
    e2 = Yfuncvec[4]
    #Explicit Equations  Inline
    e1max = alpha1/( mu1max+ beta1)      
    e2max = alpha2/( mu2max+ beta2) 
    E1 =  e1/e1max      
    E2 =  e2/e2max      
    mu1 = mu1max*E1*Cs1/(K1+Cs1)      
    mu2 = mu2max*E2*Cs2/(K2+Cs2)      
    u1 =  mu1/(mu1+mu2)      
    u2 =  mu2/(mu1+mu2)      
    mumax = np.where(mu1 > mu2, mu1, mu2)
    v1 =  mu1/ mumax      
    v2 =  mu2/mumax   
    alphastar = .01*alpha1   

    # Differential equations
    dCcdt =(mu1*v1+mu2*v2)*Cc - D*Cc  
    dCs1dt =  -mu1*v1*Cc/Ycs1 + D*(Cs10-Cs1)  
    dCs2dt =  -mu2*v2*Cc/Ycs2 + D* (Cs20 - Cs2)  
    de1dt = alpha1*Cs1/(K1+Cs1)*u1 - beta1*e1 - (mu1*v1+mu2*v2)*e1 + alphastar  
    de2dt = alpha2*Cs2/(K2+Cs2)*u2 - beta2*e2 - (mu1*v1+mu2*v2)*e2 + alphastar   
        
    return np.array([dCcdt, dCs1dt, dCs2dt, de1dt, de2dt])

tspan = np.linspace(0, 10, 1000) # Range for the independent variable
y0 = np.array([0.1, 4, 20, 8.3e-5, 1e-6]) # Initial values for the dependent variables

#%%
fig, (ax1,ax2) = plt.subplots(2,1)
fig.suptitle(""" LEP PRS-9-6 Continuous Cultures""", x = 0.32, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.5)
ax1.text(-11.8 , -28.5,'Differential Equations'
         '\n'
         r'$\dfrac{dC_C}{dt} = (\mu_1 v_1+ \mu_2 v_2)C_C - D C_C $'
                  '\n \n'
         r'$\dfrac{dC_{S1}}{dt} = \dfrac{-\mu_1 v_1 C_C}{Y_{C/S1}} + D(C_{S1,0}-C_{S1}) $'
                  '\n \n'
         r'$\dfrac{dC_{S2}}{dt} = \dfrac{-\mu_2 v_2 C_C}{Y_{C/S2}} + D(C_{S2,0}-C_{S2}) $'
                  '\n \n'                  
         r'$\dfrac{de_1}{dt} = \dfrac{\alpha_1 C_{S1} u_1}{K_1+C_{S1}} - \beta_1e_1 - (\mu_1 v_1+\mu_2 v_2)e_1 + \alpha^*$'
                  '\n \n'    
         r'$\dfrac{de_2}{dt} = \dfrac{\alpha_2 C_{S2} u_2}{K_2+C_{S2}} - \beta_2e_2 - (\mu_2 v_2+\mu_2 v_2)e_2 + \alpha^*$'
                  '\n \n'                       
         'Explicit Equations'
                  '\n'
 
 

        r'$C_{S1,0} = 4   $' '\n'  
        r'$C_{S2,0} = 20  $' '\n' 
        r'$D = 0.6  $' '\n'                 
        r'$\alpha^* = 0.01*\alpha_1$' '\n'             
         r'$e_{1max} =  \dfrac{\alpha_1}{mu_{1max}+ \beta_1}$'
         '\n'      
         r'$e_{2max} =  \dfrac{\alpha_2}{mu_{2max}+ \beta_2}$'
         '\n'          
         r'$E_1 =  \dfrac{e_1}{e_{1max}}$'
         '\n'
         r'$E_2 =  \dfrac{e_2}{e_{2max}}$'
         '\n'         
         r'$\mu_1 =  \dfrac{\mu_{1max}E_1C_{S1}}{K_1+C_{S1}}$'
         '\n'         
         r'$\mu_2 =  \dfrac{\mu_{2max} E_2 C_{S2}}{K_2+C_{S2}}$'
         '\n'          
         r'$u_1 =  \dfrac{\mu_1}{\mu_1 + \mu_2}$'
         '\n'          
         r'$u_2 =  \dfrac{\mu_2}{\mu_1 + \mu_2}$'
         '\n'          
         r'$If (\mu_1 > \mu_2) then (\mu_{max} = \mu_1) else (\mu_{max} = \mu_2)$'    
         '\n'          
         r'$v_1 =  \dfrac{\mu_1}{\mu_{max}}$'
         '\n'          
         r'$v_2 =  \dfrac{\mu_2}{\mu_{max}}$'
         
         , ha='left', wrap = True, fontsize=11,
        bbox=dict(facecolor='none', edgecolor='black', pad=12), fontweight='bold')


sol = odeint(ODEfun, y0, tspan, (mu1max, mu2max, K1, 
                                 K2, alpha1, alpha2, beta1, beta2,
                                 Ycs1, Ycs2))
Cc = sol[:,0]
Cs1= sol[:,1]
Cs2= sol[:,2]
e1 = sol[:,3]
e2 = sol[:,4]

p1, p2, p3 = ax1.plot(tspan, Cc, tspan, Cs1,tspan, Cs2)
ax1.legend(['$C_C(g/L)$','$C_{S1}(g/L)$','$C_{S2}(g/L)$'], loc='best')
ax1.set_xlabel('time (hr)', fontsize='medium')
ax1.set_ylabel('Concentration (M)', fontsize='medium')
ax1.set_ylim(0,20)
ax1.set_xlim(0,10)
ax1.grid()

p4, p5 = ax2.plot(tspan, e1,tspan, e2)
ax2.legend(["$e_1(g_{enzyme}/g_{cell mass})$", "$e_2(g_{enzyme}/g_{cell mass})$"], loc='best')
ax2.set_xlabel('time (hr)', fontsize='medium')
ax2.set_ylabel('Concentration (M)', fontsize='medium')
ax2.set_ylim(0,0.0012)
ax2.set_xlim(0,10)
ax2.grid()


#%%
# Slider
axcolor = 'black'
ax_Ycs1 = plt.axes([0.28, 0.8, 0.12, 0.02], facecolor=axcolor)
ax_alpha1 = plt.axes([0.28, 0.75, 0.12, 0.02], facecolor=axcolor)
ax_beta1 = plt.axes([0.28, 0.7, 0.12, 0.02], facecolor=axcolor)
ax_K1 = plt.axes([0.28, 0.65, 0.12, 0.02], facecolor=axcolor)
ax_mumax1 = plt.axes([0.28, 0.6, 0.12, 0.02], facecolor=axcolor)
ax_Ycs2 = plt.axes([0.28, 0.55, 0.12, 0.02], facecolor=axcolor)
ax_alpha2 = plt.axes([0.28, 0.5, 0.12, 0.02], facecolor=axcolor)
ax_beta2 = plt.axes([0.28, 0.45, 0.12, 0.02], facecolor=axcolor)
ax_K2 = plt.axes([0.28, 0.4, 0.12, 0.02], facecolor=axcolor)
ax_mumax2 = plt.axes([0.28, 0.35, 0.12, 0.02], facecolor=axcolor)

sYcs1 = Slider(ax_Ycs1, r'$Y_{c/s1}$', 0.05, 0.8, valinit=0.4, valfmt = "%1.2f")
salpha1 = Slider(ax_alpha1, r'$\alpha_1 (\frac{g_{enzyme1}}{g_{cell mass}.s})$', 5e-6, 0.001, valinit=0.0001, valfmt = "%1.4f")
sbeta1 = Slider(ax_beta1, r'$\beta_1 (hr^{-1})$', 0.01, 0.2, valinit=0.05, valfmt = "%1.2f")
sK1 = Slider(ax_K1, r'$K_1 (\frac{g}{L})$',0.02, 0.3, valinit= 0.1, valfmt = "%1.2f")
smumax1 = Slider(ax_mumax1, r'$\mu_{1max} (hr^{-1})$', 0.2, 1, valinit=0.9, valfmt = "%1.2f")
sYcs2 = Slider(ax_Ycs2, r'$Y_{c/s2}$', 0.05, 0.8, valinit=0.4, valfmt = "%1.2f")
salpha2 = Slider(ax_alpha2, r'$\alpha_2 (\frac{g_{enzyme2}}{g_{cell mass}.s})$', 5e-6, 0.001, valinit=0.0001, valfmt = "%1.4f")
sbeta2 = Slider(ax_beta2, r'$\beta_2 (hr^{-1})$', 0.01, 0.2, valinit=0.05, valfmt = "%1.2f")
sK2 = Slider(ax_K2, r'$K_2 (\frac{g}{L})$',0.02, 0.3, valinit= 0.5, valfmt = "%1.2f")
smumax2 = Slider(ax_mumax2, r'$\mu_{2max} (hr^{-1})$', 0.2, 1, valinit=0.6, valfmt = "%1.2f")

mu1max =  .9  
mu2max =  .6  
K1 =  .1  
K2 =  .5  
alpha1 =  .0001  
alpha2 =.0001   
beta1 =  .05  
beta2 =  .05  
Ycs1 =  .4  
Ycs2 =  .4

def update_plot2(val):
    Ycs1 = sYcs1.val
    alpha1 = salpha1.val
    beta1 =sbeta1.val
    K1 = sK1.val
    mu1max = smumax1.val
    Ycs2 = sYcs2.val
    alpha2 = salpha2.val
    beta2 =sbeta2.val
    K2 = sK2.val
    mu2max = smumax2.val    
    sol = odeint(ODEfun, y0, tspan, (mu1max, mu2max, K1, 
                                     K2, alpha1, alpha2, beta1, beta2,
                                     Ycs1, Ycs2))
    Cc = sol[:,0]
    Cs1= sol[:,1]
    Cs2= sol[:,2]
    e1 = sol[:,3]
    e2 = sol[:,4]
    p1.set_ydata(Cc)
    p2.set_ydata(Cs1)
    p3.set_ydata(Cs2)
    p4.set_ydata(e1)
    p5.set_ydata(e2)    
    fig.canvas.draw_idle()


sYcs1.on_changed(update_plot2)
salpha1.on_changed(update_plot2)
sbeta1.on_changed(update_plot2)
sK1.on_changed(update_plot2)
smumax1.on_changed(update_plot2)
sYcs2.on_changed(update_plot2)
salpha2.on_changed(update_plot2)
sbeta2.on_changed(update_plot2)
sK2.on_changed(update_plot2)
smumax2.on_changed(update_plot2)

resetax = plt.axes([0.29, 0.85, 0.09, 0.04])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sYcs1.reset()
    salpha1.reset()
    sbeta1.reset()
    sK2.reset()
    smumax2.reset()
    sYcs2.reset()
    salpha2.reset()
    sbeta2.reset()
    sK2.reset()
    smumax2.reset()    
button.on_clicked(reset)
    
