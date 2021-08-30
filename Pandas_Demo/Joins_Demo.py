import pandas as pd
product=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106,107],
    'Product_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],
    'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],
    'Seller_City':['Delhi','Mumbai','Chennai','Kolkata','Delhi','Chennai','Bengalore']
})
customer=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9],
    'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],
    'age':[20,25,15,10,30,65,35,18,23],
    'Product_ID':[101,0,106,0,103,104,0,0,107],
    'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],
    'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']
})
print(product)
print(customer)
print("============ INNER JOIN USING MERGE ================")
inner_join = pd.merge(left=product, right=customer, on='Product_ID')

# JOINS USING MERGE FUNCTION
inner_join.to_csv('inner_join.csv')
# INNER JOIN ON MULTIPLE COLUMNS
multiple_column_join = pd.merge(product,customer,how='inner',left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City'])
print(multiple_column_join)

# FULL JOIN : Full Join, also known as Full Outer Join, returns all those records which either have a match in the
# left or right dataframe.
full_join = pd.merge(product,customer,on='Product_ID',how='outer')
print(full_join.to_csv('full_join.csv'))

# LEFT JOIN
left_join = pd.merge(left=product, right=customer, how='left', on='Product_ID')
print(left_join.to_csv('left_join.csv'))

# RIGHT JOIN
right_join = pd.merge(left=product, right=customer, how='right', on='Product_ID')
print(right_join.to_csv('right_join.csv'))

# USING JOIN()
print(product.join(customer.set_index('Product_ID'), lsuffix='_prod', rsuffix='cust', on='Product_ID').to_csv('using_join.csv'))

# USING CONCAT
pd.concat([product, customer]).to_csv('concat.csv')  # concat on row basis
pd.concat([product, customer], axis=1).to_csv('concat_column.csv')