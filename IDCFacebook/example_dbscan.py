# DBSCAN demo sin librerías externas (excepto numpy/matplotlib).
# Implementamos un DBSCAN simple, generamos datos 2D, corremos clustering y graficamos.

import numpy as np
import matplotlib.pyplot as plt

# ---- Datos sintéticos (3 clusters + ruido) ----
rng = np.random.default_rng(42)

c1 = rng.normal(loc=[0, 0], scale=0.35, size=(180, 2))
c2 = rng.normal(loc=[3.5, 3.2], scale=0.40, size=(160, 2))
theta = rng.uniform(0, 2*np.pi, 220)
r = 1.6 + rng.normal(0, 0.05, 220)
c3 = np.column_stack([2.5 + r*np.cos(theta), -1.5 + r*np.sin(theta)])
noise = rng.uniform(low=-2.5, high=5.5, size=(60, 2))
X = np.vstack([c1, c2, c3, noise])

# ---- DBSCAN básico ----
def dbscan(X, eps=0.28, min_samples=10):
    n = X.shape[0]
    labels = -np.ones(n, dtype=int)   # -1 = ruido por defecto
    visited = np.zeros(n, dtype=bool)
    cluster_id = 0
    dists = np.sqrt(((X[:, None, :] - X[None, :, :])**2).sum(axis=2))  # matriz de distancias

    def neighbors(i):
        return np.where(dists[i] <= eps)[0]

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        neigh = neighbors(i)
        if len(neigh) < min_samples:
            labels[i] = -1
        else:
            labels[i] = cluster_id
            seeds = list(neigh[neigh != i])
            while seeds:
                j = seeds.pop()
                if not visited[j]:
                    visited[j] = True
                    neigh_j = neighbors(j)
                    if len(neigh_j) >= min_samples:
                        for q in neigh_j:
                            if q not in seeds:
                                seeds.append(q)
                if labels[j] < 0:
                    labels[j] = cluster_id
            cluster_id += 1
    return labels, cluster_id

labels, n_clusters = dbscan(X, eps=0.28, min_samples=10)

# ---- Gráfica ----
plt.figure(figsize=(7,6))
for k in range(n_clusters):
    mask = labels == k
    plt.scatter(X[mask, 0], X[mask, 1], s=12, label=f'Cluster {k}')
noise_mask = labels == -1
if np.any(noise_mask):
    plt.scatter(X[noise_mask, 0], X[noise_mask, 1], s=28, marker='x', label='Ruido')
plt.title(f"DBSCAN sobre datos sintéticos\nClusters encontrados: {n_clusters}")
plt.xlabel("x"); plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show()
