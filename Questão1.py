#Questão 1
 

def troca(a,b):
    
    a=a+b
    b=a-b
    a=a-b
    print("Valor de a: ", a)
    print("Valor de b: ", b)
    
    return a,b

print(troca(1,2)) #Para teste
