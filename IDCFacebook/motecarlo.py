import numpy as np
import matplotlib.pyplot as plt

# Número de puntos aleatorios
N = 10000

# Generar puntos (x, y) en el cuadrado [-1, 1] × [-1, 1]
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

# Distancia al origen
r = np.sqrt(x**2 + y**2)

# Puntos dentro del círculo
inside = r <= 1

# Estimación de π
pi_estimate = 4 * np.sum(inside) / N
print(f"Estimación de π ≈ {pi_estimate:.5f}")

# --- Gráfico ---
plt.figure(figsize=(6,6))
plt.scatter(x[inside], y[inside], color='blue', s=5, label='Dentro del círculo')
plt.scatter(x[~inside], y[~inside], color='red', s=5, label='Fuera del círculo')
circle = plt.Circle((0,0), 1, color='black', fill=False, linewidth=2)
plt.gca().add_artist(circle)
plt.axis('equal')
plt.title(f'Estimación de π con Monte Carlo\nπ ≈ {pi_estimate:.5f}')
plt.legend()
plt.show()
