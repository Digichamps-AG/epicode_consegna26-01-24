import pandas as pd 

from matplotlib import pyplot as pp

dataset = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv")
#print(dataset)

dataset.plot()
pp.legend(loc=4)

pp.show()