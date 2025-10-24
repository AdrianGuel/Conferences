import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# --- Ejemplo de programación lineal ---
# Maximizar Z = 3x + 5y
# Sujeto a: 2x + y <= 18, 6x + 5y <= 60, x, y >= 0

# En linprog se minimiza, así que usamos -Z para maximizar
c = [-3, -5]
A = [[2, 1],
     [6, 5]]
b = [18, 60]
x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
x_opt, y_opt = res.x
z_opt = -res.fun

# --- Graficar restricciones y región factible ---
x = np.linspace(0, 12, 200)
y1 = 18 - 2*x
y2 = (60 - 6*x)/5

plt.figure(figsize=(7,6))
plt.plot(x, y1, label='2x + y ≤ 18')
plt.plot(x, y2, label='6x + 5y ≤ 60')

# Región factible
y_region = np.minimum(y1, y2)
y_region = np.maximum(y_region, 0)
plt.fill_between(x, 0, y_region, color='lightblue', alpha=0.4)

# Punto óptimo
plt.plot(x_opt, y_opt, 'ro', label=f'Óptimo ({x_opt:.2f}, {y_opt:.2f})')
plt.title(f'Programación lineal: Máx Z = 3x + 5y\nValor óptimo Z = {z_opt:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.legend()
plt.grid(True)
plt.show()
