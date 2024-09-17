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
    
def animar_punto():
    # Configuración de la gráfica
    limites_negativos = -2000
    limites_positivos = 2000
    pasos = 40
    eje_x = np.linspace(limites_negativos, limites_positivos, pasos)
    eje_y = np.linspace(limites_negativos, limites_positivos, pasos)
    X, Y = np.meshgrid(eje_x, eje_y)
    Z = monkey_saddle(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.7)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")

    ax.set_xlim([limites_negativos, limites_positivos])
    ax.set_ylim([limites_negativos, limites_positivos])
    ax.set_zlim(np.min(Z), np.max(Z))

    x, y = 1, 1
    z = monkey_saddle(x, y)

    # Controlar el estado de la ventana
    try:
        for _ in range(50):
            if not plt.fignum_exists(fig.number):
                break  # Salir si la ventana ha sido cerrada
            scatter = graficar_punto(ax, x, y, z)
            grad_x, grad_y = gradiente(monkey_saddle, x, y)
            x -= grad_x * 0.01  # Ajuste para evitar saltos grandes
            y -= grad_y * 0.01  # Ajuste para evitar saltos grandes
            z = monkey_saddle(x, y)
            borrar_punto(scatter)

    except KeyboardInterrupt:
        print("Animación interrumpida.")
    finally:
        plt.close(fig)

if __name__ == "__main__":
    animar_punto()