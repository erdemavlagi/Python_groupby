import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()
df.count()
df.sum
df.shape
df.info()
df.index
df.columns

df["age"].mean()
df["age"].value_counts(10)
df.columns
df["class"].value_counts()

# Cinsiyete göre Group_BY işlemi yapmak yaş ortalamasını aldık

df.groupby("sex")["age"].mean()

# Yaş grubunun ve binilen yerin kırılımları

df.groupby(["sex","embark_town"]).agg({"age": ["mean"],"survived": "mean"})

# Gemiye Binen kadın erkeklerin hayatta kalma ortalamaları
df.groupby(["sex"]).agg({"age": ["mean"],"survived": "mean"})


df.groupby(["sex","class","embark_town"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex" :"count"})

