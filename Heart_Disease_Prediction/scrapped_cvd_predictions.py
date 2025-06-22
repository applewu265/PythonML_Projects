import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("heart.csv") # 303 rows
# columns: ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
# 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# exploratory data analysis
# one hot encode cp, ca, thal
encoder = OneHotEncoder(sparse_output = False)
bin_cols = encoder.fit_transform(data[["cp", "ca", "thal"]])
bin_col_names = encoder.get_feature_names_out(["cp", "ca", "thal"]) # get column names created by OneHotEncoder
bin_col_df = pd.DataFrame(bin_cols, columns = bin_col_names, index = data.index)
data.drop(columns = ["cp", "ca", "thal"], in_place = True)
data = pd.concat([data, bin_col_df], axis = 1)
# normalize age, trestbps, chol, thalach, oldpeak
scaler = StandardScaler()
norm_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]
data[norm_cols] = scaler.fit_transform(data[norm_cols])

# split data
y = data["target"]
X = data.drop(columns = "target", axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# train various models and compare performance
# KNN
# SVM
# Decision Tree
# Random Forest