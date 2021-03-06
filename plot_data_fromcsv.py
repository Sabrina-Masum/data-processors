# -*- coding: utf-8 -*-
"""plotdatafromcsv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zRm_aHJxRs4ZtVc_mTn0Jj47C9Mzq5In
"""

import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/winequality-red.csv')
#df = pd.read_csv(file, names=['col'], skiprows=skip)
print(df)

a = df['fixed acidity'].values 
b = df['volatile acidity'].values 
c = df['citric acid'].values 
d = df['residual sugar'].values 
f = df['chlorides'].values 
g = df['free sulfur dioxide'].values 
h = df['total sulfur dioxide'].values 
i = df['density'].values 
j = df['pH'].values 
k = df['sulphates'].values 
l = df['alcohol'].values 
m = df['quality'].values 

 

print([a],[b],[c],[d],[f],[g],[h],[i],[j],[k],[l],[m])

"""Check for null in each col:"""

df['fixed acidity'].isnull().values.any().sum()
df['volatile acidity'].isnull().values.any().sum()
df['residual sugar'].isnull().values.any().sum()
df['chlorides'].isnull().values.any().sum() 
df['free sulfur dioxide'].isnull().values.any().sum()
df['total sulfur dioxide'].isnull().values.any().sum() 
df['density'].isnull().values.any().sum() 
df['pH'].isnull().values.any().sum()
df['sulphates'].isnull().values.any().sum()
df['alcohol'].isnull().values.any().sum() 
df['quality'].isnull().values.any().sum()

"""Check for null in the whole dataframe/*csv*"""

df.isnull().values.any().sum()

#fig, ax = plt.subplots(4, 3, sharex='col', sharey='row')

fig = plt.figure(figsize =(15, 16))

fig.add_subplot(3,4,1).set_title('fixed acidity')
plt.plot(df['fixed acidity'])
fig.add_subplot(3,4,2).set_title('volatile acidity')
plt.plot(df['volatile acidity'])
fig.add_subplot(3,4,3).set_title('fixed acidity')
plt.plot(df['fixed acidity'])
fig.add_subplot(3,4,4).set_title('residual sugar')
plt.plot(df['residual sugar'])
fig.add_subplot(3,4,5).set_title('chlorides')
plt.plot(df['chlorides'])
fig.add_subplot(3,4,6).set_title('free sulfur dioxide')
plt.plot(df['free sulfur dioxide'])
fig.add_subplot(3,4,7).set_title('total sulfur dioxide')
plt.plot(df['total sulfur dioxide'])
fig.add_subplot(3,4,8).set_title('density')
plt.plot(df['density'])
fig.add_subplot(3,4,9).set_title('pH')
plt.plot(df['pH'])
fig.add_subplot(3,4,10).set_title('sulphates')
plt.plot(df['sulphates'])
fig.add_subplot(3,4,11).set_title('alcohol')
plt.plot(df['alcohol'])
fig.add_subplot(3,4,12).set_title('quality')
plt.plot(df['quality'])


plt.show()