import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= sns.load_dataset("tips")
df.head()

# Amacımız tips veri setindeki verileri görselleştirmek

# iki tip veri yapımız var biri katagorik (text,str) formatı  diğeri sayısal

df["sex"].value_counts()
sns.countplot(x= df["sex"] , data= df)
plt.show()

#sayısal verileri görselleştirme için ise :

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()