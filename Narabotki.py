#Нужно найти данные
#написать алгоритм, который определяет 4 ближайшие точки
# (к нашему пользователю)
import pandas as pd 
import matplotlib.pyplot as pl
df=pd.read_csv(r"D:\Programming\Datasets\data_for_application")
print(df.head(5))