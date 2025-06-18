# Runge Kutta 4
import numpy as np
import matplotlib.pyplot as plt

def f(x) :
    return 28*x+1

def RK4(dt,t0,x0,t_end):
    x = [x0]
    t = [t0]

    while t[-1]<= t_end :
        i = x[-1]

        k1 = f(i)*dt
        k2 = f(i+0.5*k1)*dt
        k3 = f(i+0.5*k2)*dt
        k4 = f(i + k3)*dt

        a = i + (1/6)*(k1+2*k2+2*k3+k4)

        x.append(a)
        t.append(t[-1]+dt)
    return t,x
    
t,x = RK4(0.1,0,0,10) # RK4(dt,t0,x0,t_end), return = t,x

plt.plot(t,x)
plt.show()




