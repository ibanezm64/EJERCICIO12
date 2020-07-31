"""reto Semanal # 12 J2LOGO
Autor : Miguel Ibañez Pozo

funcion ordena_positivos (list)
    Parametro  :  lista de numeros a ordenar
    Retorna    : lista ordenada de numeros poisitivos manteniendo la posision de los numeros negativos
    
    ejecute : python Ejercicio12.py
"""
def ordena_positivos(list_num):
    list_result = []
    list_neg_index = []
    index = 0
    for num in list_num :
        if num < 0 :
            list_neg_index.append(index) 
        else :
            list_result.append(num)
        index += 1   
    list_result.sort()
    for ind in list_neg_index:
        list_result.insert(index, list_num[ind])
    return list_result
    
    
 
if __name__ == '__main__':
    print(ordena_positivos([6, 3, -2, 5, -8, 2, -2]))
    print(ordena_positivos([6, 5, 4, -1, 3, 2, -1, 1]))
    print(ordena_positivos([-5, -5, -5, -5, 7, -5]))
    print(ordena_positivos([]))