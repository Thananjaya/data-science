import pandas as pd
import matplotlib.pyplot as plt

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

#checking for the number of themes sold per year
num_theme = lego_sets[['year', 'theme_id']].groupby('year').count()
print(num_theme.head(), 'theme id vs grouped year\n')
plt.plot(num_theme)
plt.xlabel('years -->')
plt.ylabel('Theme id -->')
plt.show()

#checking for the average lego parts per year
parts_by_year = lego_sets[['year', 'num_parts']].groupby('year', as_index=False).mean().round(2)
print(parts_by_year.head(6), 'parts by year vs grouped year')
plt.plot(parts_by_year, color='r')
plt.xlabel('Year')
plt.ylabel('Average Number of Parts')
plt.title('Average Lego Parts by Year')
plt.show()
