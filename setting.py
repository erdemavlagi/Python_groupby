import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50] ["age"].count()

df.loc[df["age"] > 50 , ["class","age"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male") , ["class","age"]].head()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Southampton"), ["class","age","embark_town"]].head()





df["age"].mean()
df["age"].count()
df["age"].min()
df["age"]


df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})

df.groupby("sex").agg({"survived": "mean"})
