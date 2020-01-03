import pandas as pd

#analysing the lego colors datasets
lego_colors = pd.read_csv('csv/lego_colors.csv')
print(lego_colors.info(), 'analysing the coloumn names and its dtypes using info() method\n')
print(lego_colors.head(5), 'printing the first 5 rows of the data sets\n')

#Checking for the unique color
unique_colors = lego_colors.name.unique()
print(unique_colors, 'displaying all the unique colors\n')
print(len(unique_colors), 'displaying the count of the unique colors\n')

#checking for th transparent vs non-transparent
trans_nontrans = lego_colors.groupby('is_trans').count()
print(trans_nontrans, 'displaying the total count of transparent coors and non-transparent colors\n')

#analysing the lego-sets datasets
lego_sets = pd.read_csv('csv/lego_sets.csv')
print(lego_sets.info(), 'analysing the coloumn names and its dtypes using info() method\n')
print(lego_sets.head(5), 'printing the first 5 rows of the data sets\n')