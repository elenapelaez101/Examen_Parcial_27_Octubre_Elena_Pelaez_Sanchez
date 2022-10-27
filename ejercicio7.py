class Nodo(object):
    info,sig = None, None

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

    def __str__(self):
        return "valor {}, termino {}".format(self.valor, self.termino)


class Polinommio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1


    def agregar_termino(polinomio, termino,valor):
        