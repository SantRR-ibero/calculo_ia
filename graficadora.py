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
    plt.pause(0.000001)
    return scatter 

def borrar_punto(scatter):
    scatter.remove()
    return
    
def animar_punto():
    # Configuración de la gráfica
    limites_positivos = 200
    limites_negativos = -limites_positivos
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

    # Punto inicial y función
    ajuste = 0.0001
    x, y = 200, 0
    z = monkey_saddle(x, y)
    print("|       X       |       Y       |       Z       |     Gradx     |     Grady     |DesplazamientoX|DesplazamientoY")

    # Controlar el estado de la ventana
    try:
        while True:
            if not plt.fignum_exists(fig.number):
                break  # Salir si la ventana ha sido cerrada
            if x < limites_negativos or x > limites_positivos or y < limites_negativos or y > limites_positivos:
                plt.pause(5)  # Salir 5 segundos después de que el punto haya salido del rango de la gráfica
                break
            scatter = graficar_punto(ax, x, y, z)
            grad_x, grad_y = gradiente(monkey_saddle, x, y)
            if ((grad_x * ajuste) <= 0.1 and (grad_y * ajuste) <= 0.1) and ajuste < 0.1:   # Aumenta el valor del ajuste para que no tarde tanto en encontrar valles o crestas
                ajuste *= 10
            if (grad_x * ajuste) <= 1e-4 and (grad_y * ajuste) <= 1e-4:   # Si llega a un valle o a una cresta, salir después de 5 segundos
                print("Valle o cresta encontrada cerca de: ", x, y, z)   # Muestra en qué coordenadas se encontró un valle o cresta
                plt.pause(5)
                break
            x -= grad_x * ajuste  # Ajuste para evitar saltos grandes
            y -= grad_y * ajuste  # Ajuste para evitar saltos grandes
            z = monkey_saddle(x, y)
            print("| {:<14.2f}| {:<14.2f}| {:<14.2f}| {:<14.2f}| {:<14.2f}| {:<14.2f}| {:<14.2f}| {:<14f}|".format(x, y, z, grad_x, grad_y, grad_x * ajuste, grad_y * ajuste, ajuste))
            borrar_punto(scatter)

    except KeyboardInterrupt:
        print("Animación interrumpida.")
    finally:
        plt.close(fig)

if __name__ == "__main__":
    animar_punto()