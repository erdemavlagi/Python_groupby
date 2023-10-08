import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df["embarked"].value_counts()

# binlerce katagorik değişken olduğunda bunları programatik şekilde analiz etmemiz gerekir

df["embarked"].value_counts()
# Cinsiyet bilgisi içinde kaç adet değişken bilgisi ve isimleri nelerdir?
df["sex"].unique()
#toplamda kaç eşsiz değer var erişmek için
df["sex"].nunique()

df["class"].value_counts()
df["class"].unique()
df["class"].nunique()

############## yukardaki verileri tek tek böyle bulabiliriz ancak bunlar çoklu olduğunda ########################
#######################################################################################

#öyle bir şey yapalım ki katagorik değişkenlerde olasılık bütün değişkenleri şeçsin arada kaçan sinsi veriler olacaktır
# öncelikle tip bilgisyle yakalayalım


#Yakaladığı veri yaparılarını kontrol et , kontrol ettiğin veri yapıları (bool ,object , cateray) içeriyorsa bunları seç
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

# str(df[col].dtypes) bu yaptığımız kısım aslında df["sex].dtypes in ["object"] olarak yazmaktır.
#biz tip bilgisini strye çevirip bu var mı diye baktırıyoruz.

#aralarında sinsirella olan katagorik değişkenleride olabilir bunlar için
#numerik görünümlü katagorik değişkenler için
#Aşağıdaki koşul int ve float değerlerini taşıyor ve 10 dan küçük ise bu sinsirelları yakala

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

# karninaletisi yüksek değişkenler önrneğim bir katagorik değişkenlerde isimler bunlara örnek verilebilir isimler uniquedir
#ölçülemeyecek kadar açıklanamayacak kadar yüksek fazla sınıfı vardır anlamındadır.
#bşr katagorik sınıfın 50 sınıfı olması yüksek ihtimalle bir bilgi taşımadığı anlamına gelir

#şimdi öyle birşey yapmamız lazım ki katagorik veri olan ama katagorik olmayan değişkenleri yakalayabilmeyiliz
#eğer int ve float olup çok fazla eşsiz sayısal değere sahipse bu sayısal değişkendir

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["object", "category"] ]
# ihtimale karşı denetledik yokmuş

cat_cols = cat_cols + num_but_cat # sinserellar ve katagorikler aynı yerdedir

# Eğer cat_but_car den de birşeyler gelmiş olsaydı süzme işlemi yapmalıydık
#katagorik değişkenlerin içerisinden katagorik görünümlüleri çıkarmamız gerekecekti

cat_cols = [col for col in cat_cols if col not in cat_but_car] # işlemini yaparak süzerdik

# şeçimi yaptık
# şimdi fonksiyon yazıcaz bu fonsksiyon kendisine gelenlerin value countunu alsın
# ve yüzdelik oransal bilgisini versin

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)



def cat_summary(dataframe , col_name):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################################################")

cat_summary(df,"sex")

#Bütün değişkenlerde uygulayalım
for col in cat_cols:
    cat_summary(df,col)

############################################################################

# Grafik özelliğinide eklemek istersek

def cat_summary(dataframe , col_name, plot=False):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################################################")

    if plot:
        sns.countplot(x = dataframe[col_name], data =dataframe)
        plt.show(block=True)

cat_summary(df,"sex",plot=True)

# bütün katagorik değişkenleri grafik halinde getirir
for col in cat_cols:
    cat_summary(df,col,plot=True)

