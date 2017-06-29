# Import libraries necessary for this project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import visuals as vs # Supplementary code
from sklearn.cross_validation import ShuffleSplit
from sklearn.learning_curve import learning_curve
from sklearn.metrics import make_scorer
from sklearn import tree
from sklearn import grid_search
from sklearn import cross_validation

# Pretty display for notebooks
#%matplotlib inline

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)
    
# Success
print "Boston housing dataset has {} data points with {} variable seach.".format(*data.shape)

# TODO: Minimum price of the data
minimum_price = np.amin(prices)

# TODO: Maximum price of the data
maximum_price = np.amax(prices)

# TODO: Mean price of the data
mean_price = np.mean(prices)

# TODO: Median price of the data
median_price = np.median(prices)

# TODO: Standard deviation of prices of the data
std_price = np.std(prices)

# Show the calculated statistics
print "Statistics for Boston housing dataset:\n"
print "Minimum price: ${:,.2f}".format(minimum_price)
print "Maximum price: ${:,.2f}".format(maximum_price)
print "Mean price: ${:,.2f}".format(mean_price)
print "Median price ${:,.2f}".format(median_price)
print "Standard deviation of prices: ${:,.2f}".format(std_price)

from sklearn.metrics import r2_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between 
    true and predicted values based on the metric chosen. """

    # TODO: Calculate the performance score between
    # 'y_true' and 'y_predict'
    score = r2_score(y_true,y_predict)

    # Return the score
    return score

# TODO: Import 'train_test_split'
from sklearn import cross_validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(features,prices,test_size=0.20,random_state=10)

# Create cross-validation sets from the training data
cv_sets = cross_validation.ShuffleSplit(X_train.shape[0], n_iter = 10,test_size = 0.20, random_state= 0)
#cv_sets = cross_validation.KFold(n=X_train.shape[0],n_folds=10,shuffle=True,random_state=0)

# TODO: Create a decision tree regressor object
regressor = tree.DecisionTreeClassifier(max_depth=6)

# TODO: Transform 'performance_metric' into a scoring function using
# 'make_scorer' 
scoring_fnc = make_scorer(performance_metric)

train_sizes, train_scores, test_scores =learning_curve(regressor,X_train,y_train,cv=cv_sets,scoring=scoring_fnc,train_sizes=np.linspace(.1,1.0,5))


title = 'Max_depth 6'
ylim=(0,1.0)
plt.figure()
plt.title(title)
if ylim is not None:
    plt.ylim(*ylim)
plt.xlabel("Training examples")
plt.ylabel("Score")
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
plt.grid()
plt.plot(train_sizes, train_scores_mean, 'o-', color="r",label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g",label="Cross-validation score")
plt.savefig('learning_curve_max6.png')
