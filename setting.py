import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

#Verinin kırılımını gerçekleştirdik cinsitetine göre yaş ve hayatta kalanların ortalamalarını alıyoruz.

df.groupby("sex").agg({"age" : ["mean" ,"sum", ],
                       "survived": "mean"})

#Katagorik değişkenlere göre de kırılım yapabiliriz.

df.groupby(["sex","embark_town","class"]).agg({"age" : ["mean" ],
                       "survived": "mean"})
