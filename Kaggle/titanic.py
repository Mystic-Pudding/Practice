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