import joblib

#load model
model=joblib.load('dib_79.pkl')

res=model.predict([[1,1,1,1,1,1,1,1]])

if res[0]==1:
    print('person is dib')
else:
    print('person is non dib')