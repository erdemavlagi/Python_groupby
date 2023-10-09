

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

import warnings
warnings.simplefilter(action='ignore')

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset("titanic")

sns.get_dataset_names()

df.head(7)

df["sex"].value_counts()

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df.info()

df["sex"].value_counts()

df.nunique()

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################


df["pclass"].unique()

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df.loc[:, ["pclass", "parch"]].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtype

df["embarked"] = df["embarked"].astype("category")

df["embarked"].dtype

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df.loc[df["embarked"] == "C", :].head(10)

#df.loc[df["embarked"] == "C", :].sample(15, randomstate=1234)

# df.loc[df["embarked"] == "C", :].sample(15)

# df.sample(12, random_state=1234)

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df.loc[df["embarked"] != "S", :].head(10)

# ikinci yol

df.loc[~(df["embarked"] == "S"), :].head(10)

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

# & --> ve icin kullanilir (and) gibi
mask = (df["age"] < 30) & (df["sex"] == "female")

mmale= (df["age"] > 30 )& (df["sex"]=="male")
df.loc[mmale,:].head()
df.loc[mask, :].head(7)

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

# | --> veya icin kullanilir (or) gibi
mask2 = (df["fare"] > 500) | (df["age"] > 70)

df.loc[mask2, :].head(7)

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop("who", axis=1, inplace=True)

"who" in df

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df["deck"].mode()

mode_volume = df["deck"].mode()[0]

df["deck"].fillna(mode_volume, inplace=True)

# check 1
df["deck"].value_counts()

# check 2
df["deck"].isnull().sum()


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

age_med = df["age"].median()

df["age"].fillna(age_med, inplace=True)


df["age"].isnull().sum()

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

(df.groupby(["pclass", "sex"])
 .agg({"survived": ["sum","count", "mean"]}))

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

age_30(37)

df["age_flag"] = (df["age"]
                  .apply(lambda x: age_30(x)))

df.columns


#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df2 = sns.load_dataset("tips")

df2.head(10)

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df2["time"].unique()

(df2.groupby("time")
 .agg({"total_bill": ["sum","min", "max", "mean"]})
 )

## extra guzel satir gorunumu
(df2.groupby("time")
 .agg(total_bill_sum=("total_bill", "sum"),
      total_bill_mean=("total_bill", "mean"))
 )




#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

(df2.groupby(["day", "time"])
 .agg({"total_bill": ["sum","min", "max", "mean"]})
 )

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

mask3 = (df2["time"] == "Lunch") & (df2["sex"] == "Female")

(df2.loc[mask3, :]
 .groupby("day")
 .agg({"total_bill": ["sum", "min", "max", "mean"],
       "tip": ["sum", "min", "max", "mean"]})
 )

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df2.head()

mask4 = (df2["size"] < 3) & (df2["total_bill"] > 10)

df2.loc[mask4, "total_bill"].mean().round(2)

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################


df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]

df2.head()

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

df3_30 = df2.sort_values("total_bill_tip_sum", ascending=False).iloc[:30, :]

# ikinci yol

# df3_30 = df2.sort_values("total_bill_tip_sum", ascending=False).head(30)

df3_30["tip"].count()

df3_30.head(17)
