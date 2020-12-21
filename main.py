
#Los datos en el arreglo son ordenados de menor a mayor.
def ordenamientoPorInserccion(num):

#Recorre todas las posiciones del arreglo
    for x in range (len(num)):

#No es necesario evaluar con un solo valor
        if x==0:
            pass
        else:

#Comparación e intercambio (en caso de que el numero ubicado en lugar predecesor sea mayor)
            for y in range (x,0,-1):
                if num[y]<num[y-1]:
                    num[y-1],num[y]=num[y],num[y-1]
    ouput="Arreglo modificado: {}".format(num)

    return ouput




if __name__ == '__main__':
    print(ordenamientoPorInserccion([6,5,3,1,8,7,2,4]))


