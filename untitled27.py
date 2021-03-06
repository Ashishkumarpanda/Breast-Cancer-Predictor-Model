#Load all  the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#load dataaset
data=pd.read_csv("datasets_56485_108594_Breast_cancer_data.csv")

#checking data set
data.info()

#checking for null values
data.isnull().sum()

#differentiate between independent and dependent variables
x=data.iloc[:,0:5].values
y=data.iloc[:,5].values

#train and test the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#performing feature scalling
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

#handeling the zero values if any
val=SimpleImputer(missing_values=0,strategy='mean')
x_train=val.fit_transform(x_train)
x_test=val.fit_transform(x_test)

#training model using Logistic Regression
Lr=LogisticRegression(random_state=0)
Lr.fit(x_train,y_train)

#prediction
Lr.predict(x_test)

#print the accuracy
print("accuracy of model=",metrics.accuracy_score(y_test,Lr.predict(x_test)))

print("Enter floating values as we are using mean")
x1=float(input("Enter mean radius"))
x2=float(input("Enter mean texture"))
x3=float(input("Enter mean perimeter"))
x4=float(input("Enter mean area"))
x5=float(input("Enter mean smoothness"))
c=Lr.predict([[x1,x2,x3,x4,x5]])
if c==[0]:
  print("lump not found")
else:
  print("lump found")

import matplotlib.pyplot as plt
plt.hist(c,histtype='bar')
