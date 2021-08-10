# vislization lib's
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


bank_df = pd.read_csv("Datasets/bank/bank.csv",delimiter=";")
# https://archive.ics.uci.edu/ml/datasets/Bank+Marketing


# bank_df.head()
bank_df.y.unique()
bank_df["y"] = bank_df["y"].replace("yes",1)
bank_df["y"] = bank_df["y"].replace("no",0)
bank_df


## small intor data
print("List of the columns : ",list(bank_df.columns))
print("Length of the columsn  : ",len(list(bank_df.columns)))
print("shape of the dataset :",bank_df.shape)


# bank_df["y"].value_counts()


# bank_df.info()


## numberical values
num_val = list(bank_df.describe().columns)
print("Numerical values : ",num_val)
cat_val = [ name  for name in list(bank_df.columns) if name not in num_val]
print("Category values :  ",cat_val)


bank_df.pivot_table(index =bank_df["y"])


bank_df["age"].value_counts().sort_index()



bank_df.describe()


## underdstand the data to visliuzation
# age 
plt.hist(bank_df["age"],bins = len(list(bank_df["age"].unique())))
plt.xlabel("age ")
plt.ylabel("Count")
plt.show()


## underdstand the data to visliuzation
# balance
plt.hist(bank_df["balance"],bins = 10)
plt.xlabel("balance ")
plt.ylabel("Count")
plt.show()


for name in num_val:
    plt.hist(bank_df[name],bins = len(list(bank_df[name].unique())))
    plt.xlabel(name)
    plt.ylabel("Count")
    plt.show()


# bank_df["y"] =bank_df["y"].replace("yes",0) # 1 for yes
# bank_df["y"] =bank_df["y"].replace("no",1)  # 0 for no



plt.hist(list(bank_df["age"])  )


list(bank_df["age"])



