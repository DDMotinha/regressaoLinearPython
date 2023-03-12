from __init import operacoes
import pandas as pd

matrix = pd.read_csv('dataSet.csv', sep=";")

print(operacoes.regressaoYResult(matrix,0,'y'))