import numpy as np
import matplotlib.pyplot as plt

def derivada_parcial_x(f, x, y, h=1e-5):
    return (f(x + h, y) - f(x, y)) / h

def derivada_parcial_y(f, x, y, h=1e-5):
    return (f(x, y + h) - f(x, y)) / h

def gradiente(f, x, y):
    parcial_x = derivada_parcial_x(f, x, y)
    parcial_y = derivada_parcial_y(f, x, y)
    return parcial_x, parcial_y

def monkey_saddle(x, y):
    return x**3 - 3*x*y**2

def graficar_punto(ax, x, y, z):
    scatter = ax.scatter(x, y, z, c='black', marker='o')
    plt.draw()
    plt.pause(1)
    return scatter 

def borrar_punto(scatter):
    scatter.remove()
    return
    
# Grafica
limites_negativos = -20
limites_positivos = 20
pasos = 40
eje_x = np.linspace(limites_negativos, limites_positivos, pasos)
eje_y = np.linspace(limites_negativos, limites_positivos, pasos)
X, Y = np.meshgrid(eje_x, eje_y)
Z = monkey_saddle(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
surface = ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha = 0.7)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_xlim([limites_negativos, limites_positivos])
ax.set_ylim([limites_negativos, limites_positivos])
ax.set_zlim(np.min(Z), np.max(Z))

x, y = 1, 1
z = monkey_saddle(x, y)

for _ in range(50):
    scatter = graficar_punto(ax, x, y, z)
    grad_x, grad_y = gradiente(monkey_saddle, x, y)
    x -= grad_x * 0.1
    y -= grad_y * 0.1
    z = monkey_saddle(x, y)
    print(x, y, z)
    borrar_punto(scatter)
    
plt.close(fig)
