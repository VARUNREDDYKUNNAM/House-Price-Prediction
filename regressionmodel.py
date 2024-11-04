# -*- coding: utf-8 -*-
"""Regressionmodel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UaJmVow5tBZRKlIYfgruUzsr4hTabn8J
"""

import pandas as pd
data = pd.read_csv('/content/NY-House-Dataset.csv')
print(data.head())
numeric_cols = data.select_dtypes(include=['int64', 'float64'])
data[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())
categorical_cols = data.select_dtypes(include=['object'])
data[categorical_cols.columns] = categorical_cols.fillna('Unknown')

y = data['PRICE']
X = data.drop('PRICE', axis=1)
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
X_encoded = pd.DataFrame(encoder.fit_transform(X.select_dtypes(include=['object'])).toarray())
X_encoded.columns = encoder.get_feature_names_out()
X = pd.concat([X.select_dtypes(exclude=['object']), X_encoded], axis=1)

median_price = data['PRICE'].median()
data['Category'] = (data['PRICE'] >= median_price).astype(int)

X = data.drop(['PRICE', 'Category'], axis=1)
y = data['Category']

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('/content/NY-House-Dataset.csv')

X = data.drop('PRICE', axis=1)
y = data['PRICE']

categorical_cols = X.select_dtypes(include=['object']).columns
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_data = encoder.fit_transform(X[categorical_cols])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))

X = X.drop(categorical_cols, axis=1)
X = pd.concat([X, encoded_df], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")