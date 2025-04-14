import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib # to save the model

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
name = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df=pd.read_csv(url, names=name)

print(df)

x=df.iloc[:,0:8]
y=df.iloc[:,8]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=101)

model=LogisticRegression()
model.fit(x_train,y_train)
print('[INFO] - Training completed')

#Accuracy
result=model.score(x_test,y_test)
print(f"[INFO] - accurcay - {result}")

#to Save the model

#joblib.dump(model,'dib_79.pkl')

#prediction
pred_op=model.predict(x_test)