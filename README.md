ML Predicting Boston Housing Prices
Created as part of the Udacity Machine Learning Engineer Nanodegree.
The project uses Python version 2.6


In this project, you will evaluate the performance and predictive power of a model that has been trained and tested on data collected from homes in suburbs of Boston, Massachusetts.

The goals of this project is to illustrate how to use basic techincs to prepare a dataset so it can be feed to a prediction model, how to analyze the dataset statistics properties, how to measure the performance of model and finally the fundamental concepts behind prediction models such as Linear Regression and Decision Trees.

The dataset for this project originates from the UCI Machine Learning Repository. The Boston housing data was collected in 1978 and each of the 506 entries represent aggregated data about 14 features for homes from various suburbs in Boston, Massachusetts. For the purposes of this project, the following preprocessing steps have been made to the dataset:

###    16 data points have an 'MEDV' value of 50.0. These data points likely contain missing or censored values and have been removed.
###    1 data point has an 'RM' value of 8.78. This data point can be considered an outlier and has been removed.
###    The features 'RM', 'LSTAT', 'PTRATIO', and 'MEDV' are essential. The remaining non-relevant features have been excluded.
###    The feature 'MEDV' has been multiplicatively scaled to account for 35 years of market inflation.

The above listed dataset characteristics by themself, imply  some important concepts related to the preparation of the data used to train a prediction model; These concepts are:

### The eliminations of outliers data points.
### And the adjustment of the labels to account for market inflation.

The above techniques were used to prepare the training data before feeding it to the prediction model; this is a very import step that proceeds any machine learning model creation.

# Data Exploration
During the initial data exploration of this project I concluded the following.

The price of a house is based on the square footage of the land where it seats. More rooms mean more squares feet equivalent to more money. Same way fewer rooms mean fewer sq ft. Directly Proportional Increase of RM will increase the MEDV value. The decrease of RM will reduce the MEDV value.

Lower class workers living in the neighborhood means that they can afford a house in there, which in turns means that the prices are low enough to be affordable with a low income. Inversely Proportional. The increase of LSTAT will decrease the MEDV value. The reduction of LSTAT will increase the MEDV value.

The bigger a teacher class is, the less focus on each student he/she will put and the lesser the student performance could be; this could be seen as a school with poor education. Bad school reputation tends to lower the value of the property close to the school because in a logical world parents are looking for the best possible education for their children. Inversely Proportional. The increase of PTRATIO will decrease the MEDV value. The decline of PTRATIO will increase the MEDV value.
