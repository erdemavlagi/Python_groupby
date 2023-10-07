import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

#Apply satır yada sütunlarda otomatik olarak fonsiyon çalıştırmayı sağlar.
#lambda bir fonk tanımlama şeklidir.Kullan at şeklindedir.

df["age2"]= df["age"] *2
df["age3"]= df["age"] *5

# elimizdeki yaş değişkenlerini 10 a bölmek istersek

#apply ve lampda kullanmadan yaparsak

#Döngü yazarak aşağıdaki işlemler yapılır.

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col] /10).head())

for col in df.columns:
    if "age" in col:
       df[col] = (df[col] / 10)

df.head()

# apply ve lambda kullanarak ise :

df[["age","age2","age3"]].apply(lambda x : x / 10 ).head()

#daha programatik daha getirirsek

df.loc[:, df.columns.str.contains("age")].apply(lambda x : x /10  ).head()

#işlemi dahada detaylı halde yazmak istersek ;,
# ortalamasına çıkartıp standart sapmasına almak istersek

df.loc[:, df.columns.str.contains("age")].apply(lambda x : (x-x.mean()) / x.std()).head()

#istersek fomksiyon yazıpda sol tarafı yazabiliriz.
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# kaydetmek istersek

df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

#veya

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.head()