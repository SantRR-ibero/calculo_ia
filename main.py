from graficadora import AnimadorGradiente

def monkey_saddle(x, y):
    return x**3 - 3*x*y**2

def paraboloide(x, y):
    return x**2 + y**2

def paraboloide_invertida(x, y):
    return - (x**2 + y**2)

if __name__ == "__main__":
    """
    AnimadorGradiente(funcion, x_inicial, y_inicial, limite_grafica, pasos, ajuste)
        f:      funcion
        x:      punto inicial en x
        y:      punto inicial en y
        lim:    limite de la grafica, 200 por default
        pasos:  cantidad de cuadriculas en la grafica, 40 por default
        ajuste: ajuste del salto del punto, 0.0001 por default
    """
    anim_silla_del_mono = AnimadorGradiente(monkey_saddle, 200, -1)
    anim_silla_del_mono.animar()
    
    anim_paraboloide = AnimadorGradiente(paraboloide, 140, 160)
    anim_paraboloide.animar()
    
    anim_paraboloide_invertida = AnimadorGradiente(paraboloide_invertida, 0.1, -0.1)
    anim_paraboloide_invertida.animar()