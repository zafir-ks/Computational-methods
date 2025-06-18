import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

sigma = 10
rho = 24
beta = 8/3



def X(x,y,z,t):
    return sigma*(y-x)

def Y(x,y,z,t):
    return x*(rho-z)-y

def Z(x,y,z,t):
    return x*y-beta*z 

dt = 0.01

x0 = 1
y0 = 1
z0 = 1
t0 = 0
t_end = 40

x = [x0]
y = [y0]
z = [z0]
t = [t0]

while t[-1] <= t_end :
    xn = x[-1]
    yn = y[-1]
    zn = z[-1]
    tn = t[-1]

    kx1 = X(xn,yn,zn,tn)*dt
    ky1 = Y(xn,yn,zn,tn)*dt
    kz1 = Z(xn,yn,zn,tn)*dt

    kx2 = X((xn+0.5*kx1),(yn+0.5*ky1),(zn+0.5*kz1),tn)*dt
    ky2 = Y((xn+0.5*kx1),(yn+0.5*ky1),(zn+0.5*kz1),tn)*dt
    kz2 = Z((xn+0.5*kx1),(yn+0.5*ky1),(zn+0.5*kz1),tn)*dt

    kx3 = X((xn+0.5*kx2),(yn+0.5*ky2),(zn+0.5*kz2),tn)*dt
    ky3 = Y((xn+0.5*kx2),(yn+0.5*ky2),(zn+0.5*kz2),tn)*dt
    kz3 = Z((xn+0.5*kx2),(yn+0.5*ky2),(zn+0.5*kz2),tn)*dt

    kx4 = X((xn+kx3),(yn+ky3),(zn+kz3),tn)*dt
    ky4 = Y((xn+kx3),(yn+ky3),(zn+kz3),tn)*dt
    kz4 = Z((xn+kx3),(yn+ky3),(zn+kz3),tn)*dt

    x_next = xn + (1/6)*(kx1+2*(kx2+kx3)+kx4)

    y_next = yn + (1/6)*(ky1+2*(ky2+ky3)+ky4)

    z_next = zn + (1/6)*(kz1+2*(kz2+kz3)+kz4)

    x.append(x_next)
    y.append(y_next)
    z.append(z_next)

    t.append(t[-1]+dt)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], lw=2)

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-40, 40)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=1, blit=True)

ax.set_xlabel('X axis ')
ax.set_ylabel('Y axis ')
ax.set_zlabel('Z axis ')
ax.set_title('Lorentz system')

plt.show()


