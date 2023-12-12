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
vl = 1.35          # Liver Flow Rate (l/min)
vt = 0.95         # Tissue Flow Rate (l)
Vc = 11.56     # Volume of Central Compartment (l)
Vt = 25.8     # Volume of Muscle (l)
Vg = 2.4         # Volume of GI track (l)
Vl = 1.1         # Volume of Liver (l)
VmAL = 2.2     
Vrev = 32.6      
KmAL = .4     
Krev =  1        
VmaxAc = 2.74    
KmAc =  .0012
Vs1 = 0.15 # Volume of Stomach Contents @ t=0
Cso = 6300 #Stomach concentration in mM @ t=0
a1 =  1.22   #Stomach Absorption Parameter 1
a2 =  .05    # Stomach Absorption Parameter 2
def ODEfun(Yfuncvec, t, vl, vt, Vc, Vt, Vg,
           Vl, VmAL, Vrev, KmAL, Krev, 
           VmaxAc, KmAc, Cso, a1, a2): 
    Vs= Yfuncvec[0]
    Cc= Yfuncvec[1]
    Cca= Yfuncvec[2]
    Ct=Yfuncvec[3]
    Cta=Yfuncvec[4]
    CL1=Yfuncvec[5]
    CL2=Yfuncvec[6]
    CL3=Yfuncvec[7]
    CL4=Yfuncvec[8]
    CL5=Yfuncvec[9]
    CL6=Yfuncvec[10]
    CL7=Yfuncvec[11]
    CL8=Yfuncvec[12]
    CL9=Yfuncvec[13]
    CL10=Yfuncvec[14]
    CLa1=Yfuncvec[15]
    CLa2=Yfuncvec[16]
    CLa3=Yfuncvec[17]
    CLa4=Yfuncvec[18]
    CLa5=Yfuncvec[19]
    CLa6=Yfuncvec[20]
    CLa7=Yfuncvec[21]
    CLa8=Yfuncvec[22]
    CLa9=Yfuncvec[23]
    CLa10=Yfuncvec[24]
    Cg=Yfuncvec[25]
    Cga=Yfuncvec[26]
    #Explicit Equation Inline
    dVl = Vl/10         # Liver Volume subdivided
    Ds =  Vs1*Cso    #Initial Dose in the Stomach
    ks =   a2/(1+a1*(Ds/1000)**2)         
    # Differential equations
    dVsdt = -ks*Vs #Absorption from stomach
    dCcdt = (-vl*(Cc-CL10)-vt*(Cc-Ct))/Vc         #Alcohol Balance on Central Compartment
    dCcadt =(-vl*(Cca-CLa10)-vt*(Cca-Cta))/Vc         #Aldehyde Balance on Central Compartment
    dCtdt = (vt*(Cc-Ct))/Vt         #Alcohol Balance on Tissues
    dCtadt =(vt*(Cca-Cta))/Vt         #Aldehyde Balance on Tissues
    dCL1dt =(vl*((1/3)*Cc+(2/3)*Cg-CL1)+(-VmAL*CL1+Vrev*CLa1)/(KmAL+CL1+Krev*CLa1)*dVl)/dVl         #Alcohol Balance on Liver Compartment 1
    dCL2dt =(vl*(CL1-CL2)+(-VmAL*CL2+Vrev*CLa2)/(KmAL+CL2+Krev*CLa2)*dVl)/dVl         #Alcohol Balance on Liver Compartment 2
    dCL3dt =(vl*(CL2-CL3)+(-VmAL*CL3+Vrev*CLa3)/(KmAL+CL3+Krev*CLa3)*dVl)/dVl         #Alcohol Balance on Liver Compartment 3
    dCL4dt =(vl*(CL3-CL4)+(-VmAL*CL4+Vrev*CLa4)/(KmAL+CL4+Krev*CLa4)*dVl)/dVl         #Alcohol Balance on Liver Compartment 4
    dCL5dt =(vl*(CL4-CL5)+(-VmAL*CL5+Vrev*CLa5)/(KmAL+CL5+Krev*CLa5)*dVl)/dVl         #Alcohol Balance on Liver Compartment 5
    dCL6dt =(vl*(CL5-CL6)+(-VmAL*CL6+Vrev*CLa6)/(KmAL+CL6+Krev*CLa6)*dVl)/dVl         #Alcohol Balance on Liver Compartment 6
    dCL7dt =(vl*(CL6-CL7)+(-VmAL*CL7+Vrev*CLa7)/(KmAL+CL7+Krev*CLa7)*dVl)/dVl         #Alcohol Balance on Liver Compartment 7
    dCL8dt =(vl*(CL7-CL8)+(-VmAL*CL8+Vrev*CLa8)/(KmAL+CL8+Krev*CLa8)*dVl)/dVl         #Alcohol Balance on Liver Compartment 8
    dCL9dt =(vl*(CL8-CL9)+(-VmAL*CL9+Vrev*CLa9)/(KmAL+CL9+Krev*CLa9)*dVl)/dVl         #Alcohol Balance on Liver Compartment 9
    dCL10dt =(vl*(CL9-CL10)+(-VmAL*CL10+Vrev*CLa10)/(KmAL+CL10+Krev*CLa10)*dVl)/dVl         #Alcohol Balance on Liver Compartment 10
    dCLa1dt =(vl*((1/3)*Cca+(2/3)*Cga-CLa1)-(-VmAL*CL1+Vrev*CLa1)/(KmAL+CL1+Krev*CLa1)*dVl-(CLa1*VmaxAc/(KmAc+CLa1))*dVl)/dVl #Aldehyde Balance on Liver Compartment 1
    dCLa2dt =(vl*(CLa1-CLa2)-(-VmAL*CL2+Vrev*CLa2)/(KmAL+CL2+Krev*CLa2)*dVl-(CLa2*VmaxAc/(KmAc+CLa2))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 2
    dCLa3dt =(vl*(CLa2-CLa3)-(-VmAL*CL3+Vrev*CLa3)/(KmAL+CL3+Krev*CLa3)*dVl-(CLa3*VmaxAc/(KmAc+CLa3))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 3
    dCLa4dt =(vl*(CLa3-CLa4)-(-VmAL*CL4+Vrev*CLa4)/(KmAL+CL4+Krev*CLa4)*dVl-(CLa4*VmaxAc/(KmAc+CLa4))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 4
    dCLa5dt =(vl*(CLa4-CLa5)-(-VmAL*CL5+Vrev*CLa5)/(KmAL+CL5+Krev*CLa5)*dVl-(CLa5*VmaxAc/(KmAc+CLa5))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 5
    dCLa6dt =(vl*(CLa5-CLa6)-(-VmAL*CL6+Vrev*CLa6)/(KmAL+CL6+Krev*CLa6)*dVl-(CLa6*VmaxAc/(KmAc+CLa6))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 6
    dCLa7dt =(vl*(CLa6-CLa7)-(-VmAL*CL7+Vrev*CLa7)/(KmAL+CL7+Krev*CLa7)*dVl-(CLa7*VmaxAc/(KmAc+CLa7))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 8
    dCLa8dt =(vl*(CLa7-CLa8)-(-VmAL*CL8+Vrev*CLa8)/(KmAL+CL8+Krev*CLa8)*dVl-(CLa8*VmaxAc/(KmAc+CLa8))*dVl)/dVl      #Aldehyde Balance on Liver Compartment 8
    dCLa9dt =(vl*(CLa8-CLa9)-(-VmAL*CL9+Vrev*CLa9)/(KmAL+CL9+Krev*CLa9)*dVl-(CLa9*VmaxAc/(KmAc+CLa9))*dVl)/dVl         #Aldehyde Balance on Liver Compartment 9
    dCLa10dt =(vl*(CLa9-CLa10)-(-VmAL*CL10+Vrev*CLa10)/(KmAL+CL10+Krev*CLa10)*dVl-(CLa10*VmaxAc/(KmAc+CLa10))*dVl)/dVl  #Aldehyde Balance on Liver Compartment 10
    dCgdt =   ((2/3)*vl*(Cc-Cg)+ks*Cso*Vs)/Vg    #Alcohol Balance on GI Track
    dCgadt =  ((2/3)*vl*(Cca-Cga))/Vg         # Aldehyde Balance on GI Track 
    
    return np.array([dVsdt,dCcdt,dCcadt,dCtdt,dCtadt,dCL1dt,dCL2dt,dCL3dt,dCL4dt,dCL5dt,dCL6dt,dCL7dt,dCL8dt,dCL9dt,dCL10dt,dCLa1dt,dCLa2dt,dCLa3dt,dCLa4dt,dCLa5dt,dCLa6dt,dCLa7dt,dCLa8dt,dCLa9dt,dCLa10dt,dCgdt,dCgadt])

    

tspan = np.linspace(0, 400, 1000) # Range for the independent variable
y0 = np.array([0.15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) # Initial values for the dependent variables

#%%
fig, (ax1, ax2)= plt.subplots(2,1)
fig.suptitle("""PRS : Pharmacokinetics Alcohol Metabolism""", x = 0.25, y=0.98, fontweight='bold')
plt.subplots_adjust(left  = 0.4)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
sol = odeint(ODEfun, y0, tspan, (vl, vt, Vc, Vt, Vg,
                                 Vl, VmAL, Vrev, KmAL, Krev, 
                                 VmaxAc, KmAc, Cso, a1, a2))

p1 = ax1.plot(tspan, sol[:, 1])[0]
ax1.legend(["Alcohol"], loc='best')
ax1.set_xlabel('time(min)', fontsize='medium')
ax1.set_ylabel('Alcohol (mM)', fontsize='medium')
ax1.set_ylim(0,20)
ax1.set_xlim(0,400)
ax1.grid()

p2 = ax2.plot(tspan, sol[:, 2])[0]
ax2.legend(["Aldehyde"], loc='best')
ax2.set_xlabel('time(min)', fontsize='medium')
ax2.set_ylabel('Aldehyde (mM)', fontsize='medium')
ax2.set_ylim(0,0.01)
ax2.set_xlim(0,400)
ax2.grid()

#%%
axcolor = 'black'
ax_vl = plt.axes([0.1, 0.8, 0.2, 0.02], facecolor=axcolor)
ax_vt = plt.axes([0.1, 0.75, 0.2, 0.02], facecolor=axcolor)
ax_Vc = plt.axes([0.1, 0.7, 0.2, 0.02], facecolor=axcolor)
ax_Vt = plt.axes([0.1, 0.65, 0.2, 0.02], facecolor=axcolor)
ax_Vg = plt.axes([0.1, 0.6, 0.2, 0.02], facecolor=axcolor)
ax_Vl = plt.axes([0.1, 0.55, 0.2, 0.02], facecolor=axcolor)
ax_VmAL = plt.axes([0.1, 0.5, 0.2, 0.02], facecolor=axcolor)
ax_Vrev = plt.axes([0.1, 0.45, 0.2, 0.02], facecolor=axcolor)
ax_KmAL = plt.axes([0.1, 0.4, 0.2, 0.02], facecolor=axcolor)
ax_krev = plt.axes([0.1, 0.35, 0.2, 0.02], facecolor=axcolor)
ax_VmaxAc = plt.axes([0.1, 0.3, 0.2, 0.02], facecolor=axcolor)
ax_KmAc = plt.axes([0.1, 0.25, 0.2, 0.02], facecolor=axcolor)
ax_Cso = plt.axes([0.1, 0.2, 0.2, 0.02], facecolor=axcolor)
ax_a1 = plt.axes([0.1, 0.15, 0.2, 0.02], facecolor=axcolor)
ax_a2 = plt.axes([0.1, 0.1, 0.2, 0.02], facecolor=axcolor)


svl = Slider(ax_vl, r'$v_L (\frac{l}{min})$', 0.05,5, valinit=1.35)
svt = Slider(ax_vt, r'$v_T (\frac{l}{min})$', 0.05,7, valinit=0.95)
sVc= Slider(ax_Vc, r'$V_C (litres)$', 1,20, valinit=11.56)
sVt = Slider(ax_Vt, r'$V_T (litres)$', 5,35, valinit=25.8)
sVg = Slider(ax_Vg, r'$V_G (litres)$', 1,10, valinit=2.4)
sVl = Slider(ax_Vl, r'$V_L (litres)$', 0.2,4, valinit= 1.1)
sVmAL = Slider(ax_VmAL, r'$V_{mAL} (\frac{mmol}{min.kg})$', 0.2,8, valinit=2.2)
sVrev = Slider(ax_Vrev, r'$V_{rev} (\frac{mmol}{min.kg})$', 20,1000, valinit=32.6)
sKmAL = Slider(ax_KmAL, r'$K_{mAL} (mM) $', 0.05,1, valinit=0.4)
skrev = Slider(ax_krev, r'$k_{rev}  (mM) $', 0.01,200, valinit=1)
sVmaxAc = Slider(ax_VmaxAc, r'$V_{maxAc} (\frac{mmol}{min.kg}) $', 0.05,6, valinit=2.74)
sKmAc = Slider(ax_KmAc, r'$K_{mAc} (mM) $', 0.0005, 0.004, valinit=0.0012)
sCso = Slider(ax_Cso, r'$C_{s0} (mM) $', 700, 8500, valinit=6300,valfmt='%1.0f')
sa1 = Slider(ax_a1, r'$a_1 (mol^{-2})$', 0.2,5, valinit=1.22)
sa2 = Slider(ax_a2, r'$a_2 (min^{-1}) $', 0.005, 1, valinit=0.05)


def update_plot2(val):
    vl = svl.val
    vt =svt.val
    Vc =sVc.val
    Vt = sVt.val
    Vg =sVg.val
    Vl = sVl.val
    VmAL = sVmAL.val
    Vrev = sVrev.val
    KmAL = sKmAL.val
    Krev = skrev.val
    VmaxAc = sVmaxAc.val
    KmAc = sKmAc.val
    Cso = sCso.val
    a1 = sa1.val   
    a2 = sa2.val   
	
    sol = odeint(ODEfun, y0, tspan, (vl, vt, Vc, Vt, Vg,
                                     Vl, VmAL, Vrev, KmAL, Krev, 
                                     VmaxAc, KmAc, Cso, a1, a2))
    p1.set_ydata(sol[:, 1])
    p2.set_ydata(sol[:, 2])

    fig.canvas.draw_idle()


svl.on_changed(update_plot2)
svt.on_changed(update_plot2)
sVc.on_changed(update_plot2)
sVt.on_changed(update_plot2)
sVg.on_changed(update_plot2)
sVl.on_changed(update_plot2)
sVmAL.on_changed(update_plot2)
sVrev.on_changed(update_plot2)
sKmAL.on_changed(update_plot2)
skrev.on_changed(update_plot2)
sVmaxAc.on_changed(update_plot2)
sKmAc.on_changed(update_plot2)
sCso.on_changed(update_plot2)
sa1.on_changed(update_plot2)
sa2.on_changed(update_plot2)

#

resetax = plt.axes([0.15, 0.85, 0.09, 0.05])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    svl.reset()
    svt.reset()
    sVc.reset()
    sVt.reset()
    sVg.reset()
    sVl.reset()
    sVmAL.reset()
    sVrev.reset()
    sKmAL.reset()
    skrev.reset()
    sVmaxAc.reset()
    sKmAc.reset()
    sCso.reset()
    sa1.reset() 
    sa2.reset()    
	
button.on_clicked(reset)
    
