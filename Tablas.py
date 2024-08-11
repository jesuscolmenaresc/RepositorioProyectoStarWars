import pandas as pd 

df= pd.read_csv('starships.csv')
Variables= ['Clasificacion de imperimpulsor', 'MGLT', 'Velocidad Maxima en atmósfera', 'costo en créditos']

Media= df[Variables].mean()
Moda= df[Variables].median()
Max= df[Variables].max()
Min= df[Variables].min()

