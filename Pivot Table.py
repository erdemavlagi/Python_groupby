import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
# Kod çıktısı ekranda tam görüntülenmesini istiyorsak
#pd.set_option('display.width',500)

#####################################################
#Pivot tablo oluşturmak

# pivot table birinci argümanı values argümanıdır kesişimde neyi görmek istiyorsak ilk onu yazarız ,
#ikinci girilecek argüman satırdaki görmek istediğimiz değişkendir.
#üçüncü değilken ise sutunda hangi değişkeni görmek istediğimizdir.

#bu durumda ağaıdaki kod bize satırlarda cinsiyet bilgisi sutunlarda ise lokasyon bilgisi verir.


df.pivot_table("survived","sex","embarked")

df.pivot_table("survived","sex",["embarked","class"])

# cut fonsiyonu ve qcut fonsiyonu elimizdeki sayısal fonksiyonları katagorik şekilde çevirmeye kullanılan
#en yaygın fonksiyondur.

df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])

df.pivot_table("survived","sex","new_age")



