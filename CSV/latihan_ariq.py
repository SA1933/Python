# -*- coding: utf-8 -*-
"""latihan ariq.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DBOI8xDdpFEvf0pecSU3xXP9_6HLx8_F
"""

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

import sys


sys.path.append('D:\\kuliah\\folder kuliah_AriqRasyaEkaMaulana\\ProKom_Ariq\\Data Mining and Big Data')
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

# settings to display all columns
pd.set_option("display.max_columns", None)

dataset =pd.read_csv('D:\\kuliah\\folder kuliah_AriqRasyaEkaMaulana\\ProKom_Ariq\\Data Mining and Big Data\\agaricus-lepiota.data', sep=',', header=None)

dataset.head()

dataset.columns = ['Class','a1','a2','a3','a4','a5',
                   'a6','a7','a8','a9','a10','a11',
                   'a12','a13','a14','a15','a16','a17',
                   'a18','a19','a20','a21','a22']

dataset.tail()

dataset.info()

dataset.replace("?", np.nan, inplace= True)

dataset.loc[:,list(dataset.loc[:,dataset.isnull().any()].columns)].isnull().sum()/(len(dataset))*100

dataset = dataset.drop_duplicates()

dataset.info()

dataset = dataset.loc[:,dataset.apply(pd.Series.nunique) != 1]

dataset.info()

sns.set(font_scale=1.4)
for col in dataset.columns:
  dataset[col].value_counts().plot(kind='bar', figsize=(23, 6), rot=0)
  plt.xlabel(col, labelpad=14)
  plt.ylabel("Jumlah", labelpad=14)
  plt.title(col, y=1.02);
  plt.show()

plt.subplots(figsize = (25,5))
for col in dataset.columns:
  sns.countplot(x=dataset[col],order=dataset[col].value_counts().index,hue=dataset['Class'])
  plt.show()

categorical_col = []
for column in dataset.columns:
    if dataset[column].dtype == object and len(dataset[column].unique()) <= 50:
        categorical_col.append(column)
        print(f"{column} : {dataset[column].unique()}")
        print("====================================")

Class = {'p':1, 'e':0}
a1    = {'x':1, 'b':2, 's':3, 'f':4, 'k':5, 'c':6}
a2    = {'s':1, 'y':2, 'f':3, 'g':4}
a3    = {'n':1, 'y':2, 'w':3, 'g':4, 'e':5, 'p':6, 'b':7, 'u':8, 'c':9, 'r':10}
a4    = {'t':1, 'f':2,}
a5    = {'p':1, 'a':2, 'l':3, 'n':4, 'f':5, 'c':6, 'y':7, 's':8, 'm':9}
a6    = {'f':1, 'a':2,}
a7    = {'c':1, 'w':2,}
a8    = {'n':1, 'b':2,}
a9    = {'k':1, 'n':2, 'g':3, 'p':4, 'w':5, 'h':6, 'u':7, 'e':8, 'b':9, 'r':10, 'y':11, 'o':12}
a10   = {'e':1,'t':2}
a11   = {'e':1, 'c':2, 'b':3, 'r':4,}
a12   = {'s':1, 'f':2, 'k':3, 'y':4,}
a13   = {'s':1, 'f':2, 'y':3, 'k':4,}
a14   = {'w':1, 'g':2, 'p':3, 'n':4, 'b':5, 'e':6, 'o':7, 'c':8, 'y':9,}
a15   = {'w':1, 'p':2, 'g':3, 'b':4, 'n':5, 'e':6, 'y':7, 'o':8, 'c':9,}
a17   = {'w':1, 'n':2, 'o':3, 'y':4,}
a18   = {'o':1, 't':2, 'n':3,}
a19   = {'p':1, 'e':2, 'l':3, 'f':4, 'n':5,}
a20   = {'k':1, 'n':2, 'u':3, 'h':4, 'w':5, 'r':6, 'o':7, 'y':8, 'b':9}
a21   = {'s':1, 'n':2, 'a':3, 'v':4, 'y':5, 'c':6,}
a22   = {'u':1, 'g':2, 'm':3, 'd':4, 'p':5, 'w':6, 'l':7}

dataset['Class'] = dataset['Class'].map(Class)
dataset['a1']    = dataset['a1'].map(a1)
dataset['a2']    = dataset['a2'].map(a2)
dataset['a3']    = dataset['a3'].map(a3)
dataset['a4']    = dataset['a4'].map(a4)
dataset['a5']    = dataset['a5'].map(a5)
dataset['a6']    = dataset['a6'].map(a6)
dataset['a7']    = dataset['a7'].map(a7)
dataset['a8']    = dataset['a8'].map(a8)
dataset['a9']    = dataset['a9'].map(a9)
dataset['a10']   = dataset['a10'].map(a10)
dataset['a11']   = dataset['a11'].map(a11)
dataset['a12']   = dataset['a12'].map(a12)
dataset['a13']   = dataset['a13'].map(a13)
dataset['a14']   = dataset['a14'].map(a14)
dataset['a15']   = dataset['a15'].map(a15)
dataset['a17']   = dataset['a17'].map(a17)
dataset['a18']   = dataset['a18'].map(a18)
dataset['a19']   = dataset['a19'].map(a19)
dataset['a20']   = dataset['a20'].map(a20)
dataset['a21']   = dataset['a21'].map(a21)
dataset['a22']   = dataset['a22'].map(a22)

dataset.info()

dataset.head()

dataset.loc[:, dataset.isnull().any()].columns

median_value=dataset['a11'].median()
dataset['a11']=dataset['a11'].fillna(median_value)

dataset.loc[:, dataset.isnull().any()].columns

dataset.info()

dataset['Class'] = dataset['Class'].astype(str).astype(float)
dataset['a11'] = dataset['a11'].astype(float).astype(np.int64)

dataset.info()

correlation = dataset.corr()
plt.subplots(figsize = (25,25))
sns.heatmap(correlation.round(2),
            annot = True,
            vmax = 1,
            square = True,
            cmap = 'RdYlBu_r')
plt.title('Korelasi antar fitur', y=1.05, size=15)
plt.show()

dataset.head()

X = dataset.drop(columns=['Class'])

X

Y = dataset['Class']

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1, random_state=42) #0.1 = 90%

X_train

parameters_dt = {
                "model__max_depth": np.arange(1,10),
                "model__min_samples_leaf": np.arange(1,10),
                "model__min_samples_split": np.arange(2,11),
                "model__criterion": ['gini','entropy'],
                "model__random_state": [42]
}

classifier_dt_pipeline = Pipeline([
                          ('model',DecisionTreeClassifier()),
                          ])

ori_classifier_dt = GridSearchCV(classifier_dt_pipeline, parameters_dt, cv=3, n_jobs=-1)

ori_classifier_dt.fit(X_train,Y_train.ravel())

ori_classifier_dt.best_estimator_

for param_name in sorted(parameters_dt.keys()):
    print('%s: %r' %(param_name,ori_classifier_dt.best_params_[param_name]))

ori_y_pred_dt_train = ori_classifier_dt.predict(X_train)

ori_accuracy_dt_train = accuracy_score(Y_train,ori_y_pred_dt_train)
print('Akurasi pada training set: ', ori_accuracy_dt_train)

ori_precision_dt_train = precision_score(Y_train,ori_y_pred_dt_train, average='micro')
print('Precision pada training set: ', ori_precision_dt_train)

ori_recall_dt_train = recall_score(Y_train,ori_y_pred_dt_train, average='micro')
print('Recall pada training set: ', ori_recall_dt_train)

ori_y_pred_dt_test = ori_classifier_dt.predict(X_test)

ori_accuracy_dt_test = accuracy_score(Y_test,ori_y_pred_dt_test)
print('Akurasi pada test set: ', ori_accuracy_dt_test)

ori_precision_dt_test = precision_score(Y_test,ori_y_pred_dt_test, average='micro')
print('Precision pada test set: ', ori_precision_dt_test)

ori_recall_dt_test = recall_score(Y_test,ori_y_pred_dt_test, average='micro')
print('Recall pada test set: ', ori_recall_dt_test)

sns.heatmap(confusion_matrix(Y_test,ori_y_pred_dt_test),annot=True,cmap='viridis', fmt='.0f')
plt.xlabel('Predicted Values', fontdict={'size':14}, labelpad=10)
plt.ylabel('Actual Values', fontdict={'size':14}, labelpad=10)
plt.title('Confusion Matrix pada bagian testing untuk data asli')
plt.show()

"""## ya begitulah lika liku copy paste"""

