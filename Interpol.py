


'----------------- Interpolação Polinomial -------------------'
def interpol(xzes,fx,ponto):#fixo p grau 3 (por causa da matriz a)
    n=3+1   #colocar grau do polinômio aqui + 1

    a = [[1,xzes[0],xzes[0]**2,xzes[0]**3,fx[0]],
         [1,xzes[1],xzes[1]**2,xzes[1]**3,fx[1]],
         [1,xzes[2],xzes[2]**2,xzes[2]**3,fx[2]],
         [1,xzes[3],xzes[3]**2,xzes[3]**3,fx[3]]]

    x=[]
    
    for i in range(n):
        
        x.append(0)

    for i in range(n):
        
        if a[i][i] == 0.0:
            
            print("Divisão por zero!")
            
            break
            
        for j in range(i+1, n):
            
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]
  
    sol=(x[0]+x[1]*ponto + x[2]*ponto**2+x[3]*ponto**3)
    
    pol="P(x)= "+str(x[3])+"x³ + "+str(x[2])+"x² + "+str(x[1])+"x + "+str(x[0])
    
    #print ("Polinômio interpolador: "+pol)
    
    return pol,"P("+str(ponto)+")=" + str(sol)

    
'---------------------------Lagrange-----------------------------'

def Lagrange(xzes,fx,x):#3 pontos
    
    L0=((x-xzes[1])*(x-xzes[2]))/((xzes[0]-xzes[1])*(xzes[0]-xzes[2]))
    
    L1=((x-xzes[0])*(x-xzes[2]))/((xzes[1]-xzes[0])*(xzes[1]-xzes[2]))
    
    L2=((x-xzes[0])*(x-xzes[1]))/((xzes[2]-xzes[0])*(xzes[2]-xzes[1]))
    
    P=fx[0]*L0 + fx[1]*L1 + fx[2]*L2
    
    Po=str(L0)+'x³'+' + '+str(L1)+'x²'+' + '+str(L2)+'x'
    
    #return ('P(x)=' + Po)
    return ('P(x)=' + Po, 'P('+str(x)+')='+ str(P))

'--------------------------- Entrada de dados ---------------------------'


