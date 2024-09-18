import numpy as np
import matplotlib.pyplot as plt

class AnimadorGradiente:
    def __init__(self, funcion, x_inicial, y_inicial, limite_grafica=200, ajuste=0.0001):
        self.funcion = funcion
        self.x = x_inicial
        self.y = y_inicial
        self.z = funcion(x_inicial, y_inicial)
        self.ajuste = ajuste
        self.limite_grafica = limite_grafica
        self.limites_positivos = self.limite_grafica
        self.limites_negativos = -self.limites_positivos
        self.fig, self.ax = self._configurar_grafica()

    def _configurar_grafica(self):
        pasos = 40
        eje_x = np.linspace(self.limites_negativos, self.limites_positivos, pasos)
        eje_y = np.linspace(self.limites_negativos, self.limites_positivos, pasos)
        X, Y = np.meshgrid(eje_x, eje_y)
        Z = self.funcion(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha=0.7)
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.set_zlabel("Eje Z")
        ax.set_xlim([self.limites_negativos, self.limites_positivos])
        ax.set_ylim([self.limites_negativos, self.limites_positivos])
        z_min, z_max = np.min(Z), np.max(Z)
        ax.set_zlim(z_min - 0.1 * abs(z_min), z_max + 0.1 * abs(z_max))
        return fig, ax

    def derivada_parcial_x(self, x, y, h=1e-5):
        return (self.funcion(x + h, y) - self.funcion(x - h, y)) / (2 * h)

    def derivada_parcial_y(self, x, y, h=1e-5):
        return (self.funcion(x, y + h) - self.funcion(x, y - h)) / (2 * h)

    def gradiente(self, x, y):
        parcial_x = self.derivada_parcial_x(x, y)
        parcial_y = self.derivada_parcial_y(x, y)
        return parcial_x, parcial_y

    def graficar_punto(self):
        scatter = self.ax.scatter(self.x, self.y, self.z, c="black", marker="o")
        plt.draw()
        plt.pause(0.000001)
        return scatter

    def borrar_punto(self, scatter):
        scatter.remove()

    def animar(self):
        print("│        X        │        Y        │        Z        │      GradX      │      GradY      │ DesplazamientoX │ DesplazamientoY │      Ajuste     │")
        print("├─────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────┤")
        try:
            while True:
                if not plt.fignum_exists(self.fig.number):
                    break
                scatter = self.graficar_punto()
                grad_x, grad_y = self.gradiente(self.x, self.y)
                self.x -= grad_x * self.ajuste
                self.y -= grad_y * self.ajuste
                self.z = self.funcion(self.x, self.y)
                print("│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│ {:<16.5f}│".format(
                    self.x, self.y, self.z, grad_x, grad_y, grad_x * self.ajuste, grad_y * self.ajuste, self.ajuste))
                self.borrar_punto(scatter)

                # Revisa si el punto se ha salido de la grafica
                if self.x < self.limites_negativos or self.x > self.limites_positivos or self.y < self.limites_negativos or self.y > self.limites_positivos:
                    print("El punto ha salido de los limites en ({:.2f}, {:.2f}, {:.2f}) Terminando la animacion".format(self.x, self.y, self.z))
                    plt.pause(5)
                    break
                
                # Revisar si debe aumentarse el ajuste
                if np.abs(grad_x * self.ajuste) <= 1 and np.abs(grad_y * self.ajuste) <= 1 and self.ajuste <= 0.01:   # Aumenta el valor del ajuste para que no tarde tanto en encontrar valles o crestas
                    self.ajuste *= 10

                # Revisar se debe disminurse el ajuste
                if np.abs(grad_x * self.ajuste) > 5 or np.abs(grad_y * self.ajuste) > 5:
                    self.ajuste /= 10

                # Revisa si ha llegado a una cresta o valle
                if np.abs(grad_x * self.ajuste) < 1e-5 and np.abs(grad_y * self.ajuste) < 1e-5:
                    print("Valle o cresta encontrada cerca de ({:.5f}, {:.5f}, {:.5f}) Terminando la animacion".format(self.x, self.y, self.z))
                    plt.pause(5)
                    break
        except KeyboardInterrupt:
            print("Animacion interrumpida.")
        finally:
            plt.close(self.fig)