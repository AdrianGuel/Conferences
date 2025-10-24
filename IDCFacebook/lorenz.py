# Lorenz attractor: integrate with RK4 and plot a 3D trajectory using matplotlib (single plot, no custom colors)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 - needed for 3D projection

# Parameters (classic Lorenz)
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Vector field
def f(state):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

# RK4 integrator
def rk4_step(state, dt):
    k1 = f(state)
    k2 = f(state + 0.5 * dt * k1)
    k3 = f(state + 0.5 * dt * k2)
    k4 = f(state + dt * k3)
    return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# Simulation
dt = 0.01
steps = 20000  # 200 seconds total
traj = np.zeros((steps, 3))
state = np.array([1.0, 1.0, 1.0])
for i in range(steps):
    state = rk4_step(state, dt)
    traj[i] = state

# Plot single 3D figure (no specific colors)
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(traj[:,0], traj[:,1], traj[:,2], linewidth=0.6)
ax.set_title("Atractor de Lorenz (σ=10, ρ=28, β=8/3)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
