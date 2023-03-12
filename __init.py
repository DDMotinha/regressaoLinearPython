import pandas as pd
import numpy as np

class operacoes:
      

    def soma(k1,k2):
        return (k1+k2)

    def multiplica(k1,k2):
        return (k1*k2)

    def divide(k1,k2):
        return (k1/k2)

    def subtrai(k1,k2):
        return (k1-k2)
    
    def quadrado(k1):
        return (k1*k1)

    def raiz(k1):
        return (k1**(0.5))

    def regressaoYResult(matriz, x1, colunaResultado):
        matriz = pd.DataFrame(matriz)

        colunas = matriz.columns.values.tolist()
        colunas.remove(colunaResultado)

        listaY = matriz[colunaResultado].values.tolist()
        listaX = matriz[colunas[0]].values.tolist()

        yquadr = []

        x1quadr = []
        x1Vezesx2 = []

        xmenosxmedio = []
        ymenosymedio = []
        
        xmenosxmedioquadrado = []
        ymenosymedioquadrado = []

        somay = sum(listaY)
        somax1 = sum(listaX)

        nX = len(listaX)
        nY = len(listaY)
        
        xmedio = operacoes.divide(somax1,nX)
        ymedio = operacoes.divide(somay,nY)

        somadoprodutodasdiferencasdasmedias = 0.0

        for i in listaY:
            yquadr.append(operacoes.quadrado(i))
            ymenosymedio.append(operacoes.subtrai(i,ymedio))
        
        for i in ymenosymedio:
            ymenosymedioquadrado.append(operacoes.quadrado(i))

        for i in listaX:
            x1quadr.append(operacoes.quadrado(i))
            xmenosxmedio.append(operacoes.subtrai(i, xmedio))
            
        for i in xmenosxmedio:
            xmenosxmedioquadrado.append(operacoes.quadrado(i))
            
        for i in range(nY):
            x1Vezesx2.append(operacoes.multiplica(listaY[i],listaX[i]))

        for i in range(nY):
            somadoprodutodasdiferencasdasmedias += operacoes.multiplica(xmenosxmedioquadrado[i], ymenosymedioquadrado[i])
                    
        somax1quadrado = sum(x1quadr)
        somayquadrado = sum(yquadr)
        somamultiplica = sum(x1Vezesx2)

        somaxmenosxmedioquadrado = sum(xmenosxmedioquadrado)
        somaymenosymedioquadrado = sum(ymenosymedioquadrado)

        coeficienteA = (operacoes.multiplica(nY, somamultiplica) - (operacoes.multiplica(somax1, somay)))/((operacoes.multiplica(nX, somax1quadrado))-operacoes.quadrado(somax1))
        coeficienteB = operacoes.subtrai(ymedio, operacoes.multiplica(coeficienteA, xmedio))
        
        yParelho = operacoes.soma(operacoes.multiplica(coeficienteA, x1),coeficienteB)
        
        numerador_correlacao = (nY * somamultiplica - somax1*somay)
        denominador_correlacao = ((nY * somax1quadrado - somax1**2) * (nY*somayquadrado - somay ** 2))**0.5

        correlacao = operacoes.divide(numerador_correlacao, denominador_correlacao)

        return {
            "resultante":yParelho,
            "coeficiente_angular": coeficienteA,
            "altura": coeficienteB,
            "correlacao": correlacao
        }


        
                
