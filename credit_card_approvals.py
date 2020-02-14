import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, scale
from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.ensemble import VotingClassifier, RandomForestClassifier>
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#reading the datasets from the csv file using pandas dataframe
df = pd.read_csv('./csv/cc_approvals.data', header=None)
df.columns = ['gender', 'age', 'debt', 'married', 'bank_customer', 'education', 'ethnicity', 'years_employed', 'prior_default', 'employed', 'credit_score', 
	'drivers_license', 'citizen', 'zip_code', 'income', 'approved']

# inspecting the dataframe ad checking the dtypes, also other aspects in the dataframe
print('\ndisplaying the first 20 records\n', df.head(20))
print(df.info(), 'checking the dtypes of the dataframe\n')
print('\ndisplaying the summary statistics of all the numerical rows\n', df.describe())

#checking for missing values in the dataframe
print('\nchecking for the missing values\n',df.tail(20))
df = df.replace('?', np.NaN) #replacing the ? symbol with the Nan
print('\nchecking the dataframe after replacing the missing values with NaN\n',df.tail(20))

df.age = df.age.astype(float)
df = df.dropna(axis=0)

#datasets consists of objects which cane be of categorical type. We have to convert those in to integers
#we will be using label encoder to convert the categorical object type in to integer type
#droping zipcode and drivers license which is of no use for deciding the credit approval
df = df.drop(['drivers_license', 'zip_code'], axis=1)
le = LabelEncoder()
for col in df.columns:
	if df[col].dtypes == 'object':
		df[col] = le.fit_transform(df[col])
	elif df[col].dtypes == 'float64':
		df[col] = scale(df[col])

print('\nreplacing the object type in to integer type using label encoder\n', df.head())

# seperating the feature variables and target variable
X = df.drop('approved', axis=1).values
y = df.approved.values

# splitting the datasets in to train data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#using logistic regression, since credit card approval is of classification problem
#fitting the model using train datasets
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

#predicting the results using test datasets
y_predict = logreg.predict(X_test)

#model performance calculation
print("Accuracy of logistic regression classifier: ", logreg.score(X_test, y_test))
print('\nConfusion matrix\n', confusion_matrix(y_test, y_predict))

#hyperparameters tuning
#Define the grid of values for tol and max_iter
tol = [0.01,0.001,0.0001]
max_iter = [100,150,200]

# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
param_grid = {'tol': tol, 'max_iter': max_iter}

# Instantiate GridSearchCV with the required parameters
grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)
cv_results = grid_model.fit(X_train, y_train)

best_params, best_score = cv_results.best_params_, cv_results.best_score_
print("The best params are", best_params)
print("The best scores are", best_score)
