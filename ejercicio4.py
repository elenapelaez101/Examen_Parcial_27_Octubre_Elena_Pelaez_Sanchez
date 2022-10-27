class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno se ha creado con éxito")

    def __str__(self):
        formato = "Nombre: {}, Nota: {}".format(self.nombre,self.nota)

    def calificacion(self):
        respuesta=None
        if self.nota > 5:
            respuesta= "El alumno {} ha aprobado".format(self.nombre)
        else:
            respuesta= "El alumno {} ha suspendido".format(self.nombre)
        return respuesta
alumno1 = Alumno("Marta",3)
alumno2 = Alumno("Juan",6)

print(alumno1.calificacion())
print(alumno2.calificacion())