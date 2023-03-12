import pandas as pd
import numpy as np

class operacoesDe2valores:
      

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
        
        xmedio = operacoesDe2valores.divide(somax1,nX)
        ymedio = operacoesDe2valores.divide(somay,nY)

        somadoprodutodasdiferencasdasmedias = 0.0

        for i in listaY:
            yquadr.append(operacoesDe2valores.quadrado(i))
            ymenosymedio.append(operacoesDe2valores.subtrai(i,ymedio))
        
        for i in ymenosymedio:
            ymenosymedioquadrado.append(operacoesDe2valores.quadrado(i))

        for i in listaX:
            x1quadr.append(operacoesDe2valores.quadrado(i))
            xmenosxmedio.append(operacoesDe2valores.subtrai(i, xmedio))
            
        for i in xmenosxmedio:
            xmenosxmedioquadrado.append(operacoesDe2valores.quadrado(i))
            
        for i in range(nY):
            x1Vezesx2.append(operacoesDe2valores.multiplica(listaY[i],listaX[i]))

        for i in range(nY):
            somadoprodutodasdiferencasdasmedias += operacoesDe2valores.multiplica(xmenosxmedioquadrado[i], ymenosymedioquadrado[i])
                    
        somax1quadrado = sum(x1quadr)
        somayquadrado = sum(yquadr)
        somamultiplica = sum(x1Vezesx2)

        somaxmenosxmedioquadrado = sum(xmenosxmedioquadrado)
        somaymenosymedioquadrado = sum(ymenosymedioquadrado)

        coeficienteA = (operacoesDe2valores.multiplica(nY, somamultiplica) - (operacoesDe2valores.multiplica(somax1, somay)))/((operacoesDe2valores.multiplica(nX, somax1quadrado))-operacoesDe2valores.quadrado(somax1))
        coeficienteB = operacoesDe2valores.subtrai(ymedio, operacoesDe2valores.multiplica(coeficienteA, xmedio))
        
        yParelho = operacoesDe2valores.soma(operacoesDe2valores.multiplica(coeficienteA, x1),coeficienteB)
        
        numerador_correlacao = (nY * somamultiplica - somax1*somay)
        denominador_correlacao = ((nY * somax1quadrado - somax1**2) * (nY*somayquadrado - somay ** 2))**0.5

        correlacao = operacoesDe2valores.divide(numerador_correlacao, denominador_correlacao)

        return {
            "resultante":yParelho,
            "coeficiente_angular": coeficienteA,
            "altura": coeficienteB,
            "correlacao": correlacao
        }

                
