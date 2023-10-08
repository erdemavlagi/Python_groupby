import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df.head()  # genel bakış verir tabloyu gösterir
df.tail() # sondan 5 veriyi gösteriri
df.shape # kaç satır kaç sutun olduğunu gösteririr
df.columns # sutunları gösterir
df.info #kaç değişken tipi var
df.index #index bilgisini verir kaç satırdan başlar kaça kadar kaçar kaçar
df.describe().T  # Sayısal değişkenleri betimleme
df.isnull().values.any() #Eksik değer var mı yok mu sorusu
df.isnull().sum() # veri setindeki eksik değer sayısını veren fonsiyonları gösterir

# bir fonksiyon tanımlıcaz elimize genel bir veri geldiğinde bize genel resmi bize vermesi için bu çok önemli
# işimizi rahat görmemize sebep olacaktır.

def check_df(dataframe , head= 5 ):
    print("################## Shape( satır , Sutun ) sayısını verir ####################")
    print(dataframe.shape)
    print("###################### Types ################################################")
    print(dataframe.dtypes)
    print("####################### Head (Baştan ilk beş bilgi) ###########################")
    print(dataframe.head(head))
    print("####################### Tail (Sondan beş bilgi) ###############################")
    print(dataframe.tail(head))
    print("####################### NA (Eksik bilgiler ve frekans bilgileri  ##############")
    print(dataframe.isnull().sum())
    print("################ Quantiles (Sayısal Değişkenlerin Dağılım bilgisi) ############")
    print(dataframe.describe([0,0.05,0.50,0.95,0.99,1]).T)
    print("########################### Columns #############################################")
    print(dataframe.columns)
    print("##############################  index ##########################################")
    print(dataframe.index)

di = sns.load_dataset("tips")

check_df(df)
check_df(di)
