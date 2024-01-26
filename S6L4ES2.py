import pandas as pd 

from matplotlib import pyplot as pp

dataset = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv")
#print(dataset)

colonna = dataset["AAPL"]
print(colonna)

pp.plot(colonna,
        "red",
        ls = "--",
        marker = "o",
        linewidth = 2.0,
        markerfacecolor = "black"
        )
pp.xlabel("Data")
pp.ylabel("Valore")
pp.title("Azioni Apple")

pp.show()