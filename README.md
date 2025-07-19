### Ongoing and Finished Machine Learning Projects
Author: Apple Wu

**Project 1: Median Housing Price Prediction (Finalized)**
* Objective: predict median house prices from related features (e.g. median income, household, longitude, latitude, etc.)
* Used the California Housing Prices dataset from Statlib (based on 1990 California census)
* Applied custom transformations and preprocessing to data
* Optimized RandomForest model to predict housing prices

**Project 2: Heart Disease Prediction (Finalized)**
* Objective: predict if a patient has heart disease from related features (e.g. age,  cholesterol, cp, etc.)
* Used UCI Heart Dataset from Kaggle (priyanka841/heart-disease-prediction-uci)
* Trained multiple models to predict heart disease, chose RandomForest
* Optimized RandomForestClassifier to achieve 98.35% accuracy, 97. 06% precision, 100.00% recall, and 0.9992 ROC AUC

**Project 3: MNIST Classifier (Finalized)**
* Objective: to train and evaluate various ML models to classify the MNIST dataset
* Trained SVC and RandomForest as binary classifiers and as multiclass classifiers
* Trained KNN as multioutput multiclass classifier to remove added noise from MNIST images
* Achieved 90.05% accuracy, 90.82% precision, and 90.05% recall
* (Primarily for learning purposes)

**Project 4: Hospital Readmission Prediction (Finalizing)**
* Objective: to predict whether a diabetes patient will be readmitted to the hospital within 30 days of discharge
* Using Diabetes 130-US Hospitals for Years 1999-2008 dataset from UCI ML repository
* Trained multiple models for multiclass classification to predict if a patient will be readmitted within 30 days, readmitted after 30+ days, or not readmitted
* Created pipelines to handle missing data, transform numerical features, and apply feature engineering
    * Handled features with over 90% missing values
    * Created custom transformations to 
* Optimized model to achieve 71.79% accuracy, 72.14% precision, 71.79% recall, and 0.8253 ROC AUC
    * Initial metrics (with minimal transformations applied and no hyperparameter optimization): 57.38% accuracy, 53.66% precision, 57.38% recall