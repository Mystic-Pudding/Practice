from lightgbm import train
import pandas as pd 
import numpy as np 
train_df = pd.read_csv("./data/titanic/train.csv")
test_df = pd.read_csv("./data/titanic/test.csv")
submission = pd.read_csv("./data/titanic/gender_submission.csv")
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
name_df = all_df["Name"].str.split("[,.]",2,expand=True)
name_df['family_name'] = name_df[0]
name_df['honorific'] = name_df[1]
name_df['name'] = name_df[2]
name_df
name_df["family_name"] = name_df["family_name"].str.strip()
name_df["honorific"] = name_df["honorific"].str.strip()
name_df["name"] = name_df["name"].str.strip()

name_df["honorific"].value_counts()

all_df = pd.concat([all_df,name_df],axis=1)
plt.figure(figsize=(18,5))
sns.boxplot(x="honorific",y="Age",data=all_df)

all_df[["Age","honorific"]].groupby("honorific").mean()

train_df = pd.concat([train_df,name_df[0:len(train_df)].reset_index(drop=True)],axis=1)
test_df = pd.concat([test_df,name_df[0:len(train_df)].reset_index(drop=True)],axis=1)
honorific_df = train_df[["honorific","Survived","PassengerId"]].dropna().groupby(["honorific","Survived"]).count().unstack()
honorific_df.plot.bar(stacked=True)

honorific_age_mean = all_df[["honorific","Age"]].groupby("honorific").mean().reset_index()
honorific_age_mean.columns = ["honorific","honorific_Age"]
all_df = pd.merge(all_df, honorific_age_mean, on="honorific", how="left")
all_df.loc[(all_df["Age"].isnull()), "Age"] = all_df["honorific_Age"]
all_df = all_df.drop(["honorific_Age"],axis=1)
all_df["family_num"] = all_df["Parch"] + all_df["SibSp"]
all_df["family_num"].value_counts()

all_df.loc[all_df["family_num"] ==0, "alone"] = 1
all_df["alone"].fillna(0, inplace=True)
all_df = all_df.drop(["PassengerId","Name","family_name","name","Ticket","Cabin"],axis=1)

categories = all_df.columns[all_df.dtypes == "object"]
print(categories)
all_df.loc[~((all_df["honorific"] =="Mr") |
    (all_df["honorific"] =="Miss") |
    (all_df["honorific"] =="Mrs") |
    (all_df["honorific"] =="Master")), "honorific"] = "other"
all_df.honorific.value_counts()

from sklearn.preprocessing import LabelEncoder

all_df["Embarked"].fillna("missing", inplace=True)
le = LabelEncoder()
le = le.fit(all_df["Sex"])
all_df["Sex"] = le.transform(all_df["Sex"])
for cat in categories:
    le = LabelEncoder()
    print(cat)
    if all_df[cat].dtypes == "object":    
        le = le.fit(all_df[cat])
        all_df[cat] = le.transform(all_df[cat])
train_X = all_df[~all_df["Survived"].isnull()].drop("Survived",axis=1).reset_index(drop=True)
train_Y = train_df["Survived"]
test_X = all_df[all_df["Survived"].isnull()].drop("Survived",axis=1).reset_index(drop=True)

import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

X_train, X_valid, y_train, y_valid = train_test_split(train_X, train_Y, test_size=0.2)

categories = ["Embarked", "Pclass", "Sex","honorific","alone"]
lgb_train = lgb.Dataset(X_train, y_train, categorical_feature=categories)
lgb_eval = lgb.Dataset(X_valid, y_valid,  categorical_feature=categories, reference=lgb_train)

lgbm_params = {
    "objective":"binary",        
    "random_seed":1234,
}

model_lgb = lgb.train(lgbm_params, 
                      lgb_train, 
                      valid_sets=lgb_eval, 
                      num_boost_round=100,
                      early_stopping_rounds=5,
                      verbose_eval=10)

model_lgb.feature_importance()

importance = pd.DataFrame(model_lgb.feature_importance(), index=X_train.columns, columns=["importance"]).sort_values(by="importance",ascending =True)
importance.plot.barh()

y_pred = model_lgb.predict(X_valid, num_iteration=model_lgb.best_iteration)

from sklearn.metrics import accuracy_score

accuracy_score(y_valid, np.round(y_pred))

lgbm_params = {
    "objective":"binary",
    "max_bin":331,
    "num_leaves": 20,
    "min_data_in_leaf": 57,
    "andom_seed":1234,
}

model_lgb = lgb.train(lgbm_params, lgb_train, 
                      valid_sets=lgb_eval, 
                      num_boost_round=100,
                      early_stopping_rounds=20,
                      verbose_eval=10)

y_pred = model_lgb.predict(X_valid, num_iteration=model_lgb.best_iteration)
accuracy_score(y_valid, np.round(y_pred))

folds = 3

kf = KFold(n_splits=folds)

models = []

for train_index, val_index in kf.split(train_X):
    X_train = train_X.iloc[train_index]
    X_valid = train_X.iloc[val_index]
    y_train = train_Y.iloc[train_index]
    y_valid = train_Y.iloc[val_index]
        
    lgb_train = lgb.Dataset(X_train, y_train, categorical_feature=categories)
    lgb_eval = lgb.Dataset(X_valid, y_valid, categorical_feature=categories, reference=lgb_train)    
    
    model_lgb = lgb.train(lgbm_params, 
                          lgb_train, 
                          valid_sets=lgb_eval, 
                          num_boost_round=100,
                          early_stopping_rounds=20,
                          verbose_eval=10,
                         )
    
    
    y_pred = model_lgb.predict(X_valid, num_iteration=model_lgb.best_iteration)
    print(accuracy_score(y_valid, np.round(y_pred)))
    
    models.append(model_lgb)

preds = []

for model in models:
    pred = model.predict(test_X)
    preds.append(pred)
preds_array = np.array(preds)
preds_mean = np.mean(preds_array, axis=0)
preds_int = (preds_mean > 0.5).astype(int)

submission["Survived"] = preds_int
submission

submission.to_csv("./titanic_submit01.csv",index=False)
