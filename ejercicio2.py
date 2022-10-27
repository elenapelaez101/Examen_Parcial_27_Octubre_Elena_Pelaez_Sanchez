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

def mergesort(listad):
    if len(lis)<=1:
        return listad
    else:
        med =len(listad)//2
        izq= []
        for i in range(0,med):
            izq.append(listad[i])
        der = []
        for i in range(med,len(listad)):
            der.append(lis[i])
        izq = mergesort(izq)
        der = mergesort(der)
        if(izq[med-1]<=der[0]):
            izq +=der
            return izq
        resultado = merge(izq,der)
        return resultado

def devolver_indice(indice):
    for i in resultado:
        if i == indice:
            return indice
        else:return -1

valor =145

if valor in lista:

    print(lista)
else:
    print("-1")



