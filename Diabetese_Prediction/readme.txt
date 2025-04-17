# Diabetes Prediction Model

A simple logistic regression model to predict diabetes based on the Pima Indians Diabetes dataset.

## Overview

This project implements a logistic regression model to predict the onset of diabetes using medical diagnostic measurements. The model is trained on the classic Pima Indians Diabetes dataset.

## Dataset

The dataset is sourced from [UCI Machine Learning Repository](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv) via Jason Brownlee's GitHub.

Features:
1. Pregnancies (`preg`)
2. Plasma glucose concentration (`plas`)
3. Diastolic blood pressure (`pres`)
4. Triceps skinfold thickness (`skin`)
5. 2-Hour serum insulin (`test`)
6. Body mass index (`mass`)
7. Diabetes pedigree function (`pedi`)
8. Age (`age`)
9. Class variable (0 or 1) (`class`)

## Requirements

- Python 3.x
- pandas
- scikit-learn
- joblib (for model saving)

Install requirements:
```bash
pip install pandas scikit-learn joblib
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```

2. Run the script:
```bash
python diabetes_prediction.py
```

## Model Performance

The model achieves approximately 79% accuracy (may vary slightly due to random splitting).

## Saving the Model

The trained model can be saved as a pickle file using:
```python
joblib.dump(model, 'dib_79.pkl')
```

## Making Predictions

To make predictions on new data:
```python
loaded_model = joblib.load('dib_79.pkl')
predictions = loaded_model.predict(new_data)

