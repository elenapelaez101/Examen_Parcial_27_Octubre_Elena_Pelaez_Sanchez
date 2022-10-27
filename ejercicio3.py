"""PREGUNTA 3

Creación (0,5 puntos)
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación (0,5 Puntos)
Crea algunos alumnos
Prueba a ejecutar el método calificación de cada objeto que has creado
"""

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno se ha creado con éxito")

    def __str__(self):
        return "Nombre {}, nota{}".format(self.nombre, self.nota)

    def clasificacion(self):
        if self.nota > 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")