import numpy as np
import matplotlib.pyplot as plt

N = 1000   # Number of oscillators
K = 0.1     #coupling constant
dt = 0.01  #timestep
t_end = 100 #final time


mu = 5
sigma = 1

omega = np.random.normal(mu, sigma, N)  # gaussian distributtion

def kuramoto(N,K,dt,t0,t_end):

    theta = np.zeros(N)  # initial condition

    def r_sum(theta): # complex order parameter
        z = np.mean(np.exp(1j * theta))

        return np.abs(z) , np.angle(z)  # np.abs(z) gives the modulus of complex order parameter, ie the value of 'r' and np.angle(z) gives the argument of complex order parameter , ie mean phase (psi)

    def d0_dt(theta, j, psi): # calculating theta_dot using mean field equation
        return omega+ K * j * np.sin(psi - theta)

    t_val = [t0] 
    r_val = []  # For storing the values of order parameter (r) at time 't'

    while t_val[-1] <= t_end :

        r,psi = r_sum(theta)


        k1 = np.array(d0_dt(theta,r,psi)*dt)
        k2 = np.array(d0_dt(theta+ 0.5 * k1,r,psi)*dt)
        k3 = np.array(d0_dt(theta + 0.5 * k2,r,psi)*dt)
        k4 = np.array(d0_dt(theta + k3,r,psi)*dt)

        theta += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            
    # Store order parameter

        r_val.append(r)
        t_val.append(t_val[-1] + dt)

    t_val.pop(-1)

    return r_val,t_val

r,t = kuramoto(N,K,dt,0,t_end)

plt.plot(t,r)
plt.xlabel("time")
plt.ylabel("order parameter ( r )")
plt.grid(True)
plt.show()

