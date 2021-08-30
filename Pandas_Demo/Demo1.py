import pandas as pd

pd1 = pd.DataFrame({'Yes': [50, 21, 31], 'No': [131, 2, 3], 'Neutral':[1,2,3]})
print(pd1)

pd2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(pd2)

pd3  = pd.DataFrame({'Header1':['h1c1', 'h2c2'], 'Header2':['h2c1', 'h2c2']})
print(pd3)

# making our index variable using Index argument
pd3 = pd.DataFrame({'Header1':['h1c1', 'h2c2'], 'Header2':['h2c1', 'h2c2']}, index=['MyProduct1', 'MyProduct2'])
print("DataFrame with Updated Index \n", pd3)

print("=============== SERIES ===============")
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

s2 = pd.Series([11,22,33,44,55], index=[1,2,3,4,5], name='11 multiples')
print(s2)

print("=============== READING DATA FROM CSV FILES ===============")
automobile_csv = pd.read_csv('automobile.csv', index_col=0)
print("Checking SHape of DataFrame \n", automobile_csv.shape)
print(automobile_csv.head())
print("============= INDEX BASED SELECTION USING ILOC =================")
print("Selecting 1st row \n", automobile_csv.iloc[0])
print("Selecting the 3rd column only \n", automobile_csv.iloc[:,3])
print('to select the 3rd column from just the first, second, and third row \n', automobile_csv.iloc[:3, 3])
print('last five elements of the dataset\n', automobile_csv.iloc[-5:])

print("============= LABEL BASED SELECTION USING LOC =================")
hotel = pd.read_csv('hotel_reviews.csv')
print(hotel.loc[:,'city'])
print('gets all the rows of the mentioned columns only\n', hotel.loc[:, ['city', 'latitude', 'longitude']])
print("CHECKING THE CONDITION \n",hotel.city=='Hanover')
print('Print only those rows where the city is Hanover \n:', hotel.loc[hotel.city == 'Hanover'])
print("Conditional Selection \n", hotel.loc[hotel.city.isin(['Hanover', 'Kansas City'])])
print("=================== SUMMARY FUNCTION ==============")
print("DESCRIBE FUNCTION \n", hotel.describe())
print("MEAN OF Longitude \n", hotel.longitude.mean())
print("UNIQUE FUNCTION \n", hotel.city.unique())
print("UNIQUE VALUE COUNTS: \n", hotel.city.value_counts())
print("Combine City and Country\n", hotel.city+"-"+hotel.country)
print("============ USAGE OF MAP FUNCTION ============")
# the below line of codes check whether tropical or wine is present in the description column or not. if present
# then add else do nothing and at last create series
reviews = pd.read_csv('wine.csv')
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)
print("================= MAKE RATING 3 star, 2 star, 1 star ============")
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)
print("=========== GROUP BY POINTS =========")
print(reviews.groupby('points').points.count())  # group by points and then count the occurence of each points
print("GROUPING BY WINERY and selecting 1st item: \n", reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
print("GROUP USING MORE THAN 1 COLUMN :\n", reviews.groupby(['country', 'province']).count())
print("GENERATE STATS SUMMARY: \n", reviews.groupby(['country']).price.agg([len, min, max]))
# RESET INDEX : Make the multi level index to normal index
country_review = reviews.groupby(['country', 'province']).description.agg([len])
print(country_review.reset_index())
# SORT BY VALUES
print(country_review.reset_index().sort_values(by='len'))
# dtype
print(reviews.dtypes)
# finding sum of null values in price column

missing_price_reviews = reviews[reviews.price.isnull()]
# print(missing_price_reviews)
n_missing_prices = len(missing_price_reviews)
# print(n_missing_prices)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
print(n_missing_prices)
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# Joins
left = df_Name_1.set_index(['title', 'trending_date'])
right = df_Name_2.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')

# renaming columns
renamed = reviews.rename(columns={'region_1':'region', 'region_2':'locale'})