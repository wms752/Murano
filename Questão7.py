#Questão 7
#Bibliotecas necessárias importadas abaixo

import pandas as pd
import matplotlib.pyplot as plt
from math import sin
from math import exp
from Interpol import * #código externo pessoal (enviado juntamente com os arquivos) utilizado no código (explicado quando usado).


'------------------------------------------------Primeiro item--------------------------------------------------'



def mediamovel(caminho,janela):#precisa do caminho até o arquivo que contem as ações ou etf, coloquei abaixo um exemplo
    
    #caminho=('C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\a.us.txt')
    df=pd.read_csv(caminho)
    df.index
    dias=df.values
    media=[]
    esq=0
    
    while True:
        
        p=0
        
        for i in range(janela+esq,esq,-1):
            
            p+=dias[i][4]
            
        media.append(p/janela)
        esq+=1
        
        if esq>=janela:
            
            break
        
    data=[]
    cont=janela
    
    while cont<2*janela:
        
        data.append(dias[cont][0])
        cont+=1
        
    plt.plot(data,media)
    plt.ylabel("Média móvel")
    plt.show()
    
    return {"media":media, "data":data}

def calculopedido():

    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\a.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aa.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aaap.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aaba.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aac.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aal.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aamc.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aame.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aan.us.txt",200)
    mediamovel("C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aaoi.us.txt",200)
    

    

'--------------------------------------------Terceiro item--------------------------------------------------------'



agoogle1="C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\goog.us.txt" #esses caminhos precisam estar definidos corretamente para a leitura dos dados
agoogle2="C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\googl.us.txt"
aapple="C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\aapl.us.txt"
amicrosoft="C:\\Users\\Wesley\\Desktop\\Murano\\archive\\Stocks\\msft.us.txt"

def acoes(caminho):

    df=pd.read_csv(caminho)
    df.index
    dados=df.values
    y=[]
    x=range(0,len(df.values))
    
    for i in df.values:
        
        y.append(i[4])
        
    return {"y":y,"x":x}




############--------Predição para Apple--------############ ok

#Para este gráfico resolvi aproximar pela função exponencial. Utilizando os pontos 2000 e 7800 da função acoes, foi possível encontrar os coeficientes a e b de f(x)=a*exp(b*x)



def funcaoapple(x):#funcao que aproxima as ações
    
    return (0.3233)*exp(x*0.000744827)

def estapple():#gera a lista de dados para plotagem em gráfico
    
    a=range(0,10001)
    b=[]
    for i in range(0,10001):
        b.append(funcaoapple(i))

    return {"x":a,"y":b}


def comparaapple(): #gráfico comparativo entre os valores das ações e dos valores estimados pela minha aproximação
    
    x=estapple()["x"]
    y=estapple()["y"]
    plt.plot(x,y,"-b")

    x=acoes(aapple)["x"]
    y=acoes(aapple)["y"]
    plt.plot(x,y,"-r")

    plt.show()







############--------Predição para Google2--------############ ok



#Neste caso, utilizei uma função pessoal de outro arquivo, que interpola o gráfico pelo polinômio de Lagrange, utilizando 4 pontos.
#Selecionei os pontos 0, 1000, 1500 e 3000 da funcao acoes, que geraram a fórmula polinomial da função funcaogoogle2 (abaixo). Não coloquei
#todos os detalhes para o código não ficar ainda maior, mas podem ser verificados facilmente.


def funcaogoogle2(x): #funcao que aproxima as ações
    
    return (9.544*10**(-8))*x**3 - 0.00036*x**2 + 0.46449*x+50.17


def estgoogle2(): #gera a lista de dados para plotagem em gráfico
    
    a=range(0,3000)
    b=[]
    for i in a:
        
        b.append(funcaogoogle2(i))

    return {"x":a,"y":b}

def comparagoogle2(): #gráfico comparativo entre os valores das ações e dos valores estimados pela minha aproximação
    
    x=estgoogle2()["x"]
    y=estgoogle2()["y"]
    plt.plot(x,y,"-b")

    X=acoes(agoogle2)["x"]
    Y=acoes(agoogle2)["y"]
    plt.plot(X,Y,"-r")

    plt.show()



############--------Predição para Google1--------############


#Nesta utilizei interpolação polinomial do arquivo auxiliar, utilizando os pontos 330, 400, 774 e 900



#print(interpol([acoes(agoogle1)["x"][330],acoes(agoogle1)["x"][400],acoes(agoogle1)["x"][774],acoes(agoogle1)["x"][900]],[acoes(agoogle1)["y"][330],acoes(agoogle1)["y"][400],acoes(agoogle1)["y"][774],acoes(agoogle1)["y"][900]],0),"funcao ai")




def funcaogoogle1(x):#funcao que aproxima as ações

    return 2.9826537163998513e-06*x**3 + -0.005019885958734264*x**2 + 3.1183423035427413*x + 73.4449941307953

def estgoogle1():#gera a lista de dados para plotagem em gráfico
    a=range(300,950)
    b=[]
    for i in a:
        b.append(funcaogoogle1(i))
    return {"x":a,"y":b}

def comparagoogle1():#gráfico comparativo entre os valores das ações e dos valores estimados pela minha aproximação
    x=estgoogle1()["x"]
    y=estgoogle1()["y"]
    plt.plot(x,y,"-b")
    print(x)
    print(y)
    
    X=acoes(agoogle1)["x"]
    Y=acoes(agoogle1)["y"]
    plt.plot(X,Y,"-r")

    plt.show()





############--------Predição para Microsoft--------############ ok

    
    
#Nesta também foi utilizada a interpolacao polinomial de terceiro grau (também contida no arquivo auxiliar) com pontos 4000, 6000, 7000 e 7900.




def funcaomicrosoft(x):#funcao que aproxima as ações
    
    return 4.5145516569200875e-09*x**3 + -7.471021150097482e-05*x**2 + 0.40472568908382156*x + -687.6066783625747

def estmicrosoft():#gera a lista de dados para plotagem em gráfico
    
    a=range(4000,8000)
    b=[]
    for i in range(4000,8000):
        
        b.append(funcaomicrosoft(i))

    return {"x":a,"y":b}


def comparamicrosoft(): #gráfico comparativo entre os valores das ações e dos valores estimados pela minha aproximação
    
    x=estmicrosoft()["x"]
    y=estmicrosoft()["y"]
    plt.plot(x,y,"-b")

    x=acoes(amicrosoft)["x"]
    y=acoes(amicrosoft)["y"]
    plt.plot(x,y,"-r")

    plt.show()





#-------------------------------Comentários--------------------------------------#


##comparaapple()
##comparagoogle2()
##comparagoogle1()
##comparamicrosoft()

#Pelos gráficos, podemos ver que as duas primeiras estimativas (para apple e google2) se comportam bem por todo o conjunto de dados,
#de forma que confere uma aproximação razoávelmente boa do gráfico das ações.
#Já para os outros (google1 e microsoft) os dados se comportam bem apenas no intervalo mais próximo do fim do conjunto de dados(onde
#os valores das ações são mais previsíveis).


'---------------------------------------------Segundo item--------------------------------------------------'

