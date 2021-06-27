#Questão 5
import threading
import numpy as np
import time

class Threadsoma(threading.Thread):
    
    def __init__(self,idt):
        
        threading.Thread.__init__(self)
        self.idt=idt

    def somaparc(self,lista,comeco,corte):
        
        som=0
        for i in lista[comeco:corte]:
            som+=i
        return som


def somamultithread(N,K):
    
    lista=np.random.randint(-50,50,N)
    corte=N//K
    Th=[]
    soma=0
    
    for i in range(K):
        a=Threadsoma(i)
        Th.append(a)

    t=time.time()
    
    for j in range(len(Th)):
        soma+=Th[j].somaparc(lista,0+j*corte,corte*(1+j))
    tt=time.time()
    
    return {"s":soma, "t":tt-t}

print(somamultithread(10**7,16))#alterar aqui o numero de itens nas listas e o numero de threads


