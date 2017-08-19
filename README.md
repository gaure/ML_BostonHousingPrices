ML Predicting Boston Housing Prices
Created as part of the Udacity Machine Learning Engineer Nanodegree.
The project uses Python version 2.6


In this project, you will evaluate the performance and predictive power of a model that has been trained and tested on data collected from homes in suburbs of Boston, Massachusetts.

The goals of this project is to illustrate how to use basic techincs to prepare a dataset so it can be feed to a prediction model, how to analyze the dataset statistics properties, how to measure the performance of model and finally the fundamental concepts behind prediction models such as Linear Regression and Decision Trees.

The dataset for this project originates from the UCI Machine Learning Repository. The Boston housing data was collected in 1978 and each of the 506 entries represent aggregated data about 14 features for homes from various suburbs in Boston, Massachusetts. For the purposes of this project, the following preprocessing steps have been made to the dataset:

#    16 data points have an 'MEDV' value of 50.0. These data points likely contain missing or censored values and have been removed.
#    1 data point has an 'RM' value of 8.78. This data point can be considered an outlier and has been removed.
#    The features 'RM', 'LSTAT', 'PTRATIO', and 'MEDV' are essential. The remaining non-relevant features have been excluded.
#    The feature 'MEDV' has been multiplicatively scaled to account for 35 years of market inflation.

The above listed dataset characteristics by themself, imply  some important concepts related to the preparation of the data used to train a prediction model. 
