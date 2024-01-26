import pandas as pd 

from matplotlib import pyplot as pp

dataset = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv")
print(dataset)

colonna = dataset.iloc[:,0]
print(colonna)

pp.plot(colonna)
pp.show()

prime_righe_MSFT = dataset.iloc[0:5,0]
print(prime_righe_MSFT)

prime_righe_date = dataset.iloc[0:5,5]
print(prime_righe_date)

pp.plot(prime_righe_date, prime_righe_MSFT)
pp.show()

ultime_righe_MSFT = dataset.iloc[-5:,0]
print(prime_righe_MSFT)

ultime_righe_date = dataset.iloc[-5:,5]
print(prime_righe_date)

pp.plot(ultime_righe_date, ultime_righe_MSFT)
pp.show()
