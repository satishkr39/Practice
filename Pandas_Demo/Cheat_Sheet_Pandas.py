import pandas  as pd

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
print(groceries)

# shape, size, values, index, ndim
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)

# check whether an index label exists in Series
# check whether an index label exists in Series
x = 'bananas' in groceries
print(x)

print('Do we need milk and bread:\n', groceries[['milk', 'bread']])

# Delete Elements
# doesn't change the original Series being modified
groceries.drop('apples')
# delete items from Series in place by setting keyword inplace to True
groceries.drop('apples', inplace = True)

# understanding axes
df.sum()
# sums “down” the 0 axis (rows)
df.sum(axis=0)
# equivalent (since axis=0 is the default)
df.sum(axis=1)
# sums “across” the 1 axis (columns)

# change the maximum number of rows and columns printed (‘None’ means unlimited)
pd.set_option(‘max_rows’, None)
# default is 60 rows

pd.set_option(‘max_columns’, None)
# default is 20 columns

# create a DataFrame that only has a subset of the data/columns
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

# create a DataFrame that only has selected keys
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# combine both of the above - selected keys for selected columns
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# Access Elements
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])

# Delete Element

# .pop() method only allows us to delete columns, while the .drop()
# method can be used to delete both rows and columns by use of the axis keyword

# remove the new watches column
store_items.pop('new watches')

# remove the watches and shoes columns
store_items = store_items.drop(['watches', 'shoes'], axis = 1)

# remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

# Rename the row and column labels
# change the column label
store_items = store_items.rename(columns = {'bikes': 'hats'})
# change the row label
store_items = store_items.rename(index = {'store 3': 'last store'})

# change the index to be one of the columns in the DataFrame
store_items = store_items.set_index('pants')

# Dealing with NaN values (missing data)

# create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

print(items2)

# check if we have any NaN values in our dataset  .any() performs an or operation. If any of the values along the
# specified axis is True, this will return True
print(store_items.isnull().any())
# count the number of NaN values in DataFrame
x =  store_items.isnull().sum().sum()
print(x)
# count the number of non-NaN values in DataFrame
x = store_items.count()
print(x)

# remove rows or columns from our DataFrame that contain any NaN values

# drop any rows with NaN values
store_items.dropna(axis = 0)
print(store_items)
# drop any columns with NaN values
store_items.dropna(axis = 1)
print(store_items)

# replace all NaN values with 0
store_items.fillna(0)

# forward filling: replace NaN values with previous values in the df, this is known as . When replacing NaN values with forward filling,
# we can use previous values taken from columns or rows. replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)

# backward filling: replace the NaN values with the values that go after them in the DataFrame
# replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)

df.head()
df.tail()
df.describe()
# prints max value in each column
df.max()

# display the memory usage of a DataFrame
# total usage
df.info()
# usage by column
df.memory_usage()

# Groupby
data.groupby(['Year'])
data.groupby(['Year'])['Salary']

# display the average salary per year
data.groupby(['Year'])['Salary'].mean()

# display the total salary each employee received in all the years they worked for the company
data.groupby(['Name'])['Salary'].sum()

# group the data by Year and by Department
data.groupby(['Year', 'Department'])['Salary'].sum()

# various file formats that can be read in out wrote out
'''
Format Type     Data Description      Reader           Writer
text                  CSV            read_csv          to_csv
text                 JSON            read_json         to_json
text                 HTML            read_html         to_html
text             Local clipboard  read_clipboard     to_clipboard
binary             MS Excel          read_excel        to_excel
binary            HDF5 Format        read_hdf           to_hdf
binary           Feather Format     read_feather      to_feather
binary              Msgpack         read_msgpack      to_msgpack
binary               Stata           read_stata        to_stata
binary                SAS             read_sas 
binary        Python Pickle Format   read_pickle       to_pickle
SQL                   SQL             read_sql          to_sql
SQL             Google Big Query      read_gbq          to_gbq
'''


# sorting
df.column_z.order()
# sort a column
df.sort_values(‘column_z’)
# sort a DataFrame by a single column
df.sort_values(‘column_z’, ascending=False)
# use descending order instead

# Sort dataframe by multiple columns
df = df.sort([‘col1’,’col2',’col3'],ascending=[1,1,0])


# rename one or more columns
df.rename(columns={‘original_column_1’:’column_x’, ‘original_column_2’:’column_y’}, inplace=True)

# replace all column names (in place)
new_cols = [‘column_x’, ‘column_y’, ‘column_z’]
df.columns = new_cols

# removing columns
df.drop(‘column_x’, axis=1)
# axis=0 for rows, 1 for columns — does not drop in place
df.drop([‘column_x’, ‘column_y’], axis=1, inplace=True)

# Lower-case all DataFrame column names
df.columns = map(str.lower, df.columns)

# Even more fancy DataFrame column re-naming
# lower-case all DataFrame column names (for example)
df.rename(columns=lambda x: x.split('.')[-1], inplace=True)

# detecting duplicate rows
df.duplicated()

# True if a row is identical to a previous row
df.duplicated().sum()

# count of duplicates
df[df.duplicated()]

# only show duplicates
df.drop_duplicates()

# drop duplicate rows
df.column_z.duplicated()

# check a single column for duplicates
df.duplicated([‘column_x’, ‘column_y’, ‘column_z’]).sum()
# specify columns for finding duplicates

# Loop through rows in a DataFrame
for index, row in df.iterrows():
 print index, row[‘column_x’]

# Much faster way to loop through DataFrame rows if you can work with tuples
for row in df.itertuples():
 print(row)