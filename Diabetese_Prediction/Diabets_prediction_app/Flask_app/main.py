#To install flask - type 'pip install flask' in the terminal

from flask import Flask, render_template, request
import joblib

#load the model
model=joblib.load('dib_79.pkl')

#intialize the app
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/alumni')
def alumni():
    return render_template('alumni.html')

@app.route('/blog')
def Blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

# To save & display the input data
@app.route('/predict', methods=['POST'])
def predict():
    data=[float(values) for values in request.form.values()]
    result=model.predict([data])
    if result[0]==1:
        return'person is diabetic'
    return 'person is not diabetic'

#Run the app
app.run(debug=True, host="0.0.0.0", port=8080)