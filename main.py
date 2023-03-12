from __init import operacoesDe2valores
import pandas as pd

matrix = pd.read_csv('dataSet.csv', sep=";")

print(operacoesDe2valores.regressaoYResult(matrix,0,'y'))