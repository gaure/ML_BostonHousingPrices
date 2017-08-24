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

# Metric

To measure the model’s accuracy, I used the R2 or the coefficient of determination, this metric tells us how much the vector features explain our prediction. The highest good value for R2 is 1.0, and the worst can be negative. A model that predicts correctly not matter what features are input will always give an R2 of 0, this is a clear indication of an overfitted model. The Mathematically operation to calculate R2 is as follow: the square difference between the real label value and the predicted value,’ divided by the square variance of the original label’s distribution minus 1. I am dividing the actual error of my prediction between the spread of the values of the fitted data distribution, in an ideal scenario where the prediction is close to the real value the difference between one and the division is close to 1. R2 metric helps to tune the model parameters so the error gets lower, and the R2 gets higher.

# The FrameWork

During this project I also learned about the Python science kit learning; this is a powerful tool used to create supervised and unsupervised machine learning models. The Sklearn as it is known for short also contains functions to optimize the models once they are built and tools that help to prepare the data before fitting it to the model for training purposes.
Sklearn is one of the most important Python machine learning frameworks.

# The Data Shuffle and Split Process

During this project, another fundamental concept I learned was the use of the sklearn "cross validation" function. Usually, the amount of data available to train a model is limited. It is important to measure the model performance using data that the model has not seen before; these two situations create the complication of how much of the data can be used to train the model and how much to test it, based on the premise that the training data set available is not big enough. The use of the cross validation technique helps with this situation. Cross validation not only shuffle the data but also creates two type of folds the training and the test folds; these two folds rotate roles during the process of training/testing, making sure that model overfitting does not occur. 


