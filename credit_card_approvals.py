import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, scale
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#reading the datasets from the csv file using pandas dataframe
df = pd.read_csv('./csv/cc_approvals.data', header=None)

# inspecting the dataframe ad checking the dtypes, also other aspects in the dataframe
print('\ndisplaying the first 20 records\n', df.head(20))
print(df.info(), 'checking the dtypes of the dataframe\n')
print('\ndisplaying the summary statistics of all the numerical rows\n', df.describe())

df.columns = ['gender', 'age', 'debt', 'married', 'bank_customer', 'education', 'ethnicity', 'years_employed', 'prior_default', 'employed', 'credit_score', 
	'drivers_license', 'citizen', 'zip_code', 'income', 'approved']

#checking for missing values in the dataframe
print('\nchecking for the missing values\n',df.tail(20))
df = df.replace('?', np.NaN) #replacing the ? symbol with the Nan
print('\nchecking the dataframe after replacing the missing values with NaN\n',df.tail(20))

#replacing the missing values column wise using ffill, which will fill the missing value with the closer value
for col in df.columns:
	if df[col].dtypes == 'object':
		df[col] = df[col].fillna(method='ffill')
print('\nchecking the dataframe after replacing the missing values with the method ffill\n',df.tail(20))

#datasets consists of objects which cane be of categorical type. We have to convert those in to integers
#we will be using label encoder to convert the categorical object type in to integer type
#droping zipcode and drivers license which is of no use for deciding the credit approval
df = df.drop(['drivers_license', 'zip_code'], axis=1)
le = LabelEncoder()
for col in df.columns:
	if df[col].dtypes == 'object':
		df[col] = le.fit_transform(df[col])

print('\nreplacing the object type in to integer type using label encoder\n', df.head())

#seperating the feature variables and target variable
X = df.iloc[:, 0:13]
y = df.iloc[:, 13]

# #if certain values in the features is high, it would have much impact on deciding the credit approval
# # x- mean / variance, we use this formula to bind the values closer
# for col in X.columns:
# 	X[col] = scale(df[col])

#splitting the datasets in to train data and test data
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, y_train.shape)

#using logistic regression, since credit card approval is of classification problem 
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

