from graficadora import animar_punto

def monkey_saddle(x, y):
    return x**3 - 3*x*y**2

def paraboloide(x, y):
    return x**2 + y**2

if __name__ == "__main__":
    """
    animar_punto(f, x, y, lim)
        f:   funcion
        x:   punto inicial en x
        y:   punto inicial en y
        lim: limite de la grafica, 200 por default
    """
    animar_punto(monkey_saddle, 200, -1)
    # animar_punto(paraboloide, 140, 160)