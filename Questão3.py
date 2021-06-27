#Questão 3
#Fiz esse código baseado na solução da equação M=c(i+j)^n + c2(i+j)^n-1 + .... ; e considerando c1=c2=c3=...=cn=c e n=meses-1


def investimento(idade_atual, idade_retirada, quantia_desejada, taxa_de_juros):
    
    meses=int((idade_retirada-idade_atual)*12)
    denominador=0
    
    for i in range(0,meses):
        
        j=(1+taxa_de_juros)**(i)
        denominador+=j                      
        
    deposito=quantia_desejada/denominador

    return "O indivíduo precisará depositar mensalmente a quantia de %s reais" %(round(deposito,2))                #Arredondado com duas casas decimais

#print(investimento(18,50,3000000,0.005)) #Para teste
    
