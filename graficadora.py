import numpy as np
import matplotlib.pyplot as plt

def derivada_parcial_x(f, x, y, h = 1e-5):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def derivada_parcial_y(f, x, y, h = 1e-5):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

def gradiente(f, x, y):
    parcial_x = derivada_parcial_x(f, x, y)
    parcial_y = derivada_parcial_y(f, x, y)
    return parcial_x, parcial_y

def graficar_punto(ax, x, y, z):
    scatter = ax.scatter(x, y, z, c = "black", marker = "o")
    plt.draw()
    plt.pause(0.000001)
    return scatter 

def borrar_punto(scatter):
    scatter.remove()
    return
    
def animar_punto(par_funcion, par_x, par_y, limite_grafica = 200):
    # Punto inicial y función
    x, y = par_x, par_y
    f = par_funcion
    z = f(x, y)
    ajuste = 0.0001
    print("│       X       │       Y       │       Z       │     GradX     │     GradY     │DesplazamientoX│DesplazamientoY│     Ajuste    │")
    print("├───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼───────────────┤")
    
    # Configuración de la gráfica
    limites_positivos = limite_grafica
    limites_negativos = -limites_positivos
    pasos = 40
    eje_x = np.linspace(limites_negativos, limites_positivos, pasos)
    eje_y = np.linspace(limites_negativos, limites_positivos, pasos)
    X, Y = np.meshgrid(eje_x, eje_y)
    Z = f(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap = "coolwarm", alpha=0.7)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_xlim([limites_negativos, limites_positivos])
    ax.set_ylim([limites_negativos, limites_positivos])
    z_min, z_max = np.min(Z), np.max(Z)
    ax.set_zlim(z_min - 0.1 * abs(z_min), z_max + 0.1 * abs(z_max))

    # Loop de la animacion
    try:
        while True:
            # Salir si la ventana ha sido cerrada
            if not plt.fignum_exists(fig.number):
                break
            
            scatter = graficar_punto(ax, x, y, z)
            grad_x, grad_y = gradiente(f, x, y)
            
            # Ajuste para evitar saltos grandes
            x -= grad_x * ajuste
            y -= grad_y * ajuste
            z = f(x, y)
            
            print("│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│ {:<14.5f}│".format(x, y, z, grad_x, grad_y, grad_x * ajuste, grad_y * ajuste, ajuste))
            borrar_punto(scatter)
            
            # Revisa si el punto se ha salido de la grafica
            if x < limites_negativos or x > limites_positivos or y < limites_negativos or y > limites_positivos:
                print("El punto ha salido de los limites en ({:.2f}, {:.2f}, {:.2f}) Terminando la animacion".format(x, y, z))
                plt.pause(5)
                break
            
            # Revisar si debe aumentarse el ajuste
            if np.abs(grad_x * ajuste) <= 1 and np.abs(grad_y * ajuste) <= 1 and ajuste <= 0.01:   # Aumenta el valor del ajuste para que no tarde tanto en encontrar valles o crestas
                ajuste *= 10
                
            # Revisar se debe disminurse el ajuste
            if np.abs(grad_x * ajuste) > 10 or np.abs(grad_y * ajuste) > 10:
                ajuste /= 10
            
            # Revisa si ha llegado a una cresta o valle
            if np.abs(grad_x * ajuste) < 1e-5 and np.abs(grad_y * ajuste) < 1e-5:
                print("Valle o cresta encontrada cerca de ({:.5f}, {:.5f}, {:.5f}) Terminando la animacion".format(x, y, z))
                plt.pause(5)
                break
            
    except KeyboardInterrupt:
        print("Animacion interrumpida.")
    finally:
        plt.close(fig)