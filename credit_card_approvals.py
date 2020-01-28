import numpy as np
import pandas as pd

#reading the datasets from the csv file using pandas dataframe
df = pd.read_csv('./csv/cc_approvals.data', header=None)

# checking the dtypes and other aspects in the dataframe
print('\ndisplaying the first 20 records\n', df.head(20))
print(df.info(), 'checking the dtypes of the dataframe\n')
print('\ndisplaying the summary statistics of all the numerical rows\n', df.describe())
