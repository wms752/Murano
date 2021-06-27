#Bibliotecas necessárias importadas abaixo

import time
import numpy as np
import matplotlib.pyplot as plt

#Infelizmente não tive tempo hábil para conseguir processar a ordenação com N=10**9 (minha máquina não foi capaz de fazer) e, portanto, não fiz os gráficos
#mas, pelo o que entendi escrevendo o código e estudando os métodos, o mais simples é o bubble sort, que pode ser feito com poucas linhas.
#Entretanto, também é o mais ineficiente dos 3 por precisar percorrer a lista inteira várias vezes. O quick sort foi o mais eficiente pelos testes que eu fiz,
#ordenando N=10**5 em menos de 2 segundos (no geral) e N=10**7 em por volta de 3 minutos. O Merge sort foi pouco mais ineficiente que o quick mas ainda sim muito
#mais eficiente que o Bubble, alcançando por volta de 3 segundos e 5 minutos para N=10**5 e N=10**7 respectivamente.

#No fim de cada algortimo há uma função print comentada, para ser utilizada como teste do algoritmo, podendo retornar o tempo de processamento ou a lista ordenada

'-------------Merge Sort------------'


def merge(esquerda, direita):

    if not len(esquerda):
        
        return esquerda

    if not len(direita):
        
        return direita

    resultado = []
    esqcont = 0
    direcont = 0
    tamanho = len(esquerda) + len(direita)

    while (len(resultado) < tamanho):
        
        if esquerda[esqcont] < direita[direcont]:
            
            resultado.append(esquerda[esqcont])
            esqcont += 1
            
        else:
            
            resultado.append(direita[direcont])
            direcont += 1


        if esqcont == len(esquerda) or direcont == len(direita):
            
            resultado.extend(esquerda[esqcont:] or direita[direcont:])
            
            break
        
    return resultado


def mergeSort(lista):

    if len(lista) < 2:
        
        return lista

    meio = len(lista)//2
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])
    merged = merge(esquerda, direita)

    return merged

def calculomerge(N):#Retorna o tempo de calculo para uma lista de tamanho N e a lista
    
    array = np.random.randint(0,N+1,N)
    t=time.time()
    lista = mergeSort(array)
    tt=time.time()
    
    return {"t":tt-t,"lista":lista} 
    


#print(calculomerge(10**5)["t"]) #Utilizar "lista" para ver a ordenação ou "t" para ver o tempo de execução

    

'-----------------Quick Sort----------------'




def particao(lista,primeiro,ultimo):

   pivo = lista[primeiro]
   esqcont = primeiro+1
   direcont = ultimo

   while True:

       while esqcont <= direcont and lista[esqcont] <= pivo:
           
           esqcont += 1

       while lista[direcont] >= pivo and direcont >= esqcont:
           
           direcont += -1

       if direcont < esqcont:
           
           break
        
       else:
           
           temp = lista[esqcont]
           lista[esqcont] = lista[direcont]
           lista[direcont] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direcont]
   lista[direcont] = temp

   return direcont


def auxrec(lista,primeiro,ultimo):
    
    if primeiro<ultimo:
        
       ponto = particao(lista,primeiro,ultimo)
       auxrec(lista,primeiro,ponto-1)
       auxrec(lista,ponto+1,ultimo)


def quickSort(alist):
    
    auxrec(alist,0,len(alist)-1)


def calculoquick(N):#Retorna o tempo de calculo para uma lista de tamanho N e a lista
    
    lista = np.random.randint(1,N+1,N)
    t=time.time()
    quickSort(lista)
    tt=time.time()
    
    return {"t":tt-t,"lista":lista}


#print(calculoquick(10**5)["t"]) #Utilizar "lista" para ver a ordenação ou "t" para ver o tempo de execução





'-----------------Bubble Sort--------------'



def bubbleSort(lista):#Ordena uma lista dada
    
    for numero in range(len(lista)-1,0,-1):
        
        for i in range(numero):
            
            if lista[i]>lista[i+1]:
                
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

def calculobuble(N):#Retorna o tempo de calculo para uma lista de tamanho N
    
    lista = np.random.randint(1,N+1,(N))
    t=time.time()
    bubbleSort(lista)
    tt=time.time()
    
    return {"t":tt-t,"lista":lista}


#print(calculobuble(10**5)["t"]) #Utilizar "lista" para ver a ordenação ou "t" para ver o tempo de execução
