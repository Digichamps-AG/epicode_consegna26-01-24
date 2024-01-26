import pandas as pd 
import numpy as np
from matplotlib import pyplot as pp

dataset = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/election.csv")
#print(dataset)


coderre = np.sum(dataset["Coderre"])
bergeron = np.sum(dataset["Bergeron"]) 
joly = np.sum(dataset["Joly"])

voti = [coderre, bergeron, joly]
candidati = ["Coderre","Bergeron","Joly"]


#print(coderre)
#print(bergeron)
#print(joly)

voti_distretti = dataset.groupby('district')['total'].sum()
nomi_distretti = [i for i in dataset["district"]]
#print(distretti)

pp.bar(candidati, voti)
pp.show()

pp.bar(nomi_distretti, voti_distretti)
pp.show()


primi_4_distretti = dataset.head(4)

coderre_voti = primi_4_distretti[["district", "Coderre"]]
bergeron_voti = primi_4_distretti[["district", "Bergeron"]]
joly_voti = primi_4_distretti[["district", "Joly"]]


pp.subplot(1, 3, 1)
pp.bar(coderre_voti["district"], coderre_voti["Coderre"])
pp.title("Voti Coderre")


pp.subplot(1, 3, 2)
pp.bar(bergeron_voti["district"], bergeron_voti["Bergeron"])
pp.title("Voti Bergeron")


pp.subplot(1, 3, 3)
pp.bar(joly_voti["district"], joly_voti["Joly"])
pp.title("Voti Joly")


pp.tight_layout()
pp.show()

#pp.savefig("Grafico", dpi=600)