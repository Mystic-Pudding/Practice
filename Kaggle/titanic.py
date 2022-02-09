from cProfile import label
import pandas as pd 
import numpy as np 
train_df = pd.read_csv("../input/titanic/train.csv")
test_df = pd.read_csv("../input/titanic/test.csv")
submission = pd.read_csv("../input/titanic/gender_submission.csv")
test_df.head()
import random
np.random.seed(1234)
random.seed(1234)
print(train_df.shape)
print(test_df.shape)
train_df.dtypes
train_df.describe()
train_df["Sex"].value_counts()

train_df["Embarked"].value_counts()

train_df["Cabin"].value_counts()

train_df.isnull().sum()

import matplotlib.pyplot as plt 
import seaborn as sns
plt.style.use('ggplot')
embarked_df = train_df[['Embarked','Survived','PassengerId']].dropna().groupby(['Embarked','Survived']).count().unstack()
embarked_df
embarked_df.plot.bar(stacked=True)
embarked_df["survied_rate"] = embarked_df.iloc[:,0] / (embarked_df.iloc[:,0] + embarked_df.iloc[:,1])
embarked_df

sex_df = train_df[['Sex','Survived','PassengerId']].dropna().groupby(["Sex","Survived"]).count().unstack()
sex_df.plot.bar(stacked=True)

ticket_df = train_df[['Pclass',"Survived",'PassengerId']].dropna().groupby(['Pclass','Survived']).count().unstack()
ticket_df.plot.bar(stacked=True)

plt.hist(x=[train_df.Age[train_df.Survived==0], train_df.Age[train_df.Survived==1]],
bins=8,histtype='barstacked',label=['Death',"Survived"])
plt.legend()

train_df_corr=pd.get_dummies(train_df,columns=['Sex'], drop_first=True)
train_df_corr = pd.get_dummies(train_df_corr, columns=["Embarked"])
train_df_corr.head()

train_corr = train_df_corr.corr()
train_corr

plt.figure(figsize=(9,9))
sns.heatmap(train_corr,vmax=1,vmin=-1,center=0,annot=True)

all_df=pd.concat([train_df,test_df],sort=False).reset_index(drop=True)
all_df
all_df.isnull().sum()

Fare_mean = all_df[["Pclass","Fare"]].groupby("Pclass").mean().reset_index()
Fare_mean.columns = ["Pclass","Fare_mean"]
Fare_mean
all_df = pd.merge(all_df,Fare_mean, on="Pclass",how="left")
all_df.loc[(all_df["Fare"].isnull(),"Fare")] = all_df["Fare_mean"]
all_df = all_df.drop("Fare_mean", axis=1)

all_df["Name"].head()