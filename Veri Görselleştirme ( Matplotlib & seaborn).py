
# katagorik bir değişken varsa : sutün grafiği ile görselleştirirz.
#bunuda seaborn içindeki counplot veya matplotlib içerisndeki bar ile gerçekleştiririz.


#Sayısal değişken ise : iki istatiksilsel grafik vardır bunlar : hist ve boxplot


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
#kind sutün bilgisi verilir
df["sex"].value_counts().plot(kind="bar")

#grafiği ekrana yazdırmak istersek
plt.show()