import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.columns

df[df["age"]> 50 ].head()
df[df["age"]> 50 ]["age"].count()

df.loc[df["age"]> 50 , "class"].head()
df.loc[df["age"]> 50 , ("class","age")].head()

df.loc[(df["age"]> 50)
       & (df["sex"]=="male")
       & (df["embark_town"]=="Southampton") ,("class","age","embark_town")].head()

df["embark_town"].value_counts()