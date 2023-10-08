import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# yaş değişkeninin analiz etmek istersek

df[["age","fare"]].describe().T
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["object", "category"] ]
cat_cols = cat_cols + num_but_cat # sinserellar ve katagorikler aynı yerdedir

# yukarıdaki döngğnğn çıktısı ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare'] bu değişkenler gelmetedir.
#ancak bu değişkenler arasında katagorik değişken görünümlüler vardır mesela survşved , pclass gibi
#bunları aralarından analiz etmek için :

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]


num_cols = [col for col in num_cols if col not in cat_cols ]

# cat_cols u bulamadı cat colsu getirelim diğer tarafta tanımlamıştık
