import pandas as pd
import matplotlib.pyplot as plt

# read the csv using pandas and store it in the dataframe
police_data = pd.read_csv('./csv/police.csv')

print('################## Begining of Cleaning ###################')
# analyse the data by means of printing the head and shape of the dataframe
print(police_data.head())
print(police_data.shape, 'Shape of the dataframe\n')

# checking the total null values present in the columns
print(police_data.isnull().sum(), 'Sum of total null values present in the data frame, column wise\n')

# it appears that county_name has nothing but null values. so we can remove the county_name and state, which is same for all the observation
police_data.drop(['county_name', 'state'], axis='columns', inplace=True)
print(police_data.head(), 'county_name and state columns been removed\n')
print(police_data.shape, 'Shape of the dataframe after removing the county_name and state columns\n')

#it appears that driver_gender is very crucial, without that data the whole observation is not meant to be usefull
police_data.dropna(subset=['driver_gender'], inplace=True)
print(police_data.isnull().sum()['driver_gender'], 'Checking the total number of null values in he driver_gender which sould be 0\n')

# lets check for data types, dtypes, of the columns existing in the dataframe
print(police_data.dtypes, 'Columnwise data types\n')
print(police_data.is_arrested.head(), 'Checking the data of is_arrested')
#it appears that is_arrested can be boolean, instead it is in object datatype
police_data['is_arrested'] = police_data.is_arrested.astype('bool')
print(police_data.is_arrested.dtype, 'Checking the data type of is_arrested')

#assigning the datatime index to the dataframe.
#dataframe has stop_time and stop_date which is in object dtype
#We have to combine them and set those as index in date time format
combined_columns = police_data.stop_date.str.cat(police_data.stop_time, sep=' ')
police_data['date_time'] = pd.to_datetime(combined_columns)
police_data.set_index('date_time', inplace=True)
print(police_data.index, 'Checking whether the index is datetime, it has to be\n')

print('################### End of Cleaning ###################\n')

print('################### Begining of Analysing ##############\n')

#check for viloation data from the data frame
print(police_data.violation.value_counts(), 'Checking for the unique values in the violation\n')
print(police_data.violation.value_counts(normalize=True), 'Normalizing the unique values\n')

#analysing the violation based on gender
male = police_data[police_data.driver_gender == 'M']
female =  police_data[police_data.driver_gender == 'F']
print(male.violation.value_counts(normalize=True), 'Normalizing the unique values of violation for male \n')
print(female.violation.value_counts(normalize=True), 'Normalizing the unique values of violation for female\n')

#analysing the dataframe for speeding and gender
male_and_speeding = police_data[(police_data.driver_gender == 'M') & (police_data.violation == 'Speeding')]
female_and_speeding = police_data[(police_data.driver_gender == 'F') & (police_data.violation == 'Speeding')]
print(male_and_speeding.stop_outcome.value_counts(normalize=True), 'Normalized values of stop outcomes based on gender and speeding, male\n')
print(female_and_speeding.stop_outcome.value_counts(normalize=True), 'Normalized values of stop outcomes based on gender and speeding, female\n')

#analyse the search_conducted, whuch is of bool dtype, for male and female seperately or using groupby
print(police_data.search_conducted.value_counts(normalize=True), 'Get the Normalized value of the search_conducted column\n')
print(police_data[police_data.driver_gender == 'F'].search_conducted.mean(), 'Mean of the search_conducted for female\n')
print(police_data[police_data.driver_gender == 'M'].search_conducted.mean(), 'Mean of the search_conducted for male\n')
print(police_data.groupby('driver_gender').search_conducted.mean(), 'Mean of the search_conducted for all the genders using groupby\n')
print(police_data.groupby(['driver_gender', 'violation']).search_conducted.mean(), 'Mean of the search_conducted for all the genders and the violations using groupby\n')

#now lets examine the search_type columns
#the nan counts of the search_type.value_counts(dropna=False) will be equal to the search_conducted "False" count
print(police_data.search_type.value_counts(dropna=False), 'Unique values count of search type, also includes the counts of the missing values or na values\n')
print(police_data.search_conducted.value_counts(), 'Unique Values count of search conducted\n')

# lets cxalculate the arrest rate in terms of hour
arrest_rate_hourly = police_data.groupby(police_data.index.hour).is_arrested.mean()
print(arrest_rate_hourly, 'Arrest rate in terms of hours\n')

# let plot the arrest rate, line plot default
arrest_rate_hourly.plot()
plt.xlabel('Hour')
plt.ylabel('Arrest rate')
plt.title('Arrest rate in terms of hourly basis')
plt.show()

#checking the drug related stop in terms of years
#getting the search_conducted in terms of resampling annualy and aggregating it with mean function
annual_drug_rate = police_data.drugs_related_stop.resample('A').mean()
annual_drug_rate.plot()
plt.show()
annual_search_conducted = police_data.search_conducted.resample('A').mean()
annual_search_comparisions = pd.concat([annual_drug_rate, annual_search_conducted], axis=1)
annual_search_comparisions.plot(subplots=True)
plt.show()