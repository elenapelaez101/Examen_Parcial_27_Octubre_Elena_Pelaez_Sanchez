"""PREGUNTA 2

Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
"""

lista= [18,50,210,80,145,333,70,30]


for i in lista:
    if i> 300:
        break
    elif i%10 ==0 and i< 200:
        print(i)

def mergesort(lista):
    tam =len(lista)
    if tam<=1:
        return lista
    else:
        med =tam//2
        izq = lista[:med]
        der = lista[med:]

        mergesort(izq)
        mergesort(der)

        p=0
        q=0
        r=0

        izqtam = len(izq)
        dertam= len(der)

        while p< dertam and q<dertam:
            if der[p] < izq[q]:
                lista[r]=izq[p]
                p+=1

            else:
                lista[r]=der[q]
                q+=1
            r +=1

        while p< izqtam:
            lista[r]= izq[p]
            p+=1
            r+=1

        while q< dertam:
            lista[r]= der[q]
            q+=1
            r+=1



def tuvalor(lista, valor):

    if valor in lista:

        print("Si que está")
    else:
        print("-1")


print(mergesort(lista))
print(tuvalor(lista,145))
