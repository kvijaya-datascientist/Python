 #   ---  Joins in Pandas  ---

import pandas as pd
product = pd.DataFrame({
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

#print(customer)

# merge() in pandas perform as inner join

# all the products in the online & who purchased them - INNER JOIN

inner_join_cust_product_data = pd.merge(customer , product , on='Product_ID') # here , we have performed inner join on 'PRODUCT_ID'(common column)
#print(inner_join_cust_product_data)

#But, what if the column names are different in the two dataframes? Then, we have to explicitly mention both the column names.

#‘left_on’ and ‘right_on’ are two arguments through which we can achieve this. ‘left_on’ is the name of the key in the left dataframe and ‘right_on’ in the right dataframe:

inner_join_on_prod_name_purchase_prod = pd.merge(customer,product,left_on='Purchased_Product',right_on='Product_name')
#print(inner_join_on_prod_name_purchase_prod)

# They want to know about all the products sold by the seller to the same city i.e., seller and customer both belong to the same city.
# In this case, we have to perform an inner join on both Product_ID and Seller_City of product and Product_ID and City columns of the customer dataframe.

prod_sold_by_seller_in_same_city=pd.merge(product,customer,how='inner',left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City'])

#print(prod_sold_by_seller_in_same_city)

# ---  FULL JOIN (FULL OUTER JOIN) in Pandas ::returns all those records which either have a match in the left or right dataframe ---

#find all the products that are not sold and all the customers who didn’t purchase anything from us
#We can perform Full join by just passing the how argument as ‘outer’ to the merge() function:
prods_not_sold_and_custs_not_purchase_anything = pd.merge(product,customer,on='Product_ID',how='outer')
#print(prods_not_sold_and_custs_not_purchase_anything)

#Did you notice what happened here? All the non-matching rows of both the dataframes have NaN values for the columns of other dataframes. But wait – we still don’t know which row belongs to which dataframe.
#For this, Pandas provides us with a fantastic solution. We just have to mention the indicator argument as True in the function, and a new column of name _merge will be created in the resulting dataframe:
prod_not_sold_cust_not_purchase = pd.merge(product,customer,on='Product_ID',how='outer',indicator=True)
#print(prod_not_sold_cust_not_purchase)

#   ---  Left Join in Pandas : returns a dataframe containing all the rows of the left dataframe  ---

#wants information about only those customers who bought something from us. You guessed it – we can use the concept of Left Join here.

custs_who_bought_something = pd.merge(product,customer,on='Product_ID',how='left')
#print(custs_who_bought_something)

#  ---  Right Join in Pandas  ---
#Right join, also known as Right Outer Join, is similar to the Left Outer Join. The only difference is that all the rows of the right dataframe are taken as it is and only those of the left dataframe that are common in both.

#customers including the information about the products they bought
custs_info_about_purchased_prods = pd.merge(product,customer,on='Product_ID',how='right')
#print(custs_info_about_purchased_prods)

# ---  Handling Redundancy/Duplicates in Joins  ---
# Duplicate values can be tricky obstacles. They can cause problems while performing joins. These values won’t give an error but will simply create redundancy in our resulting dataframe. I’m sure you can imagine how harmful that can be!

#As you can see, we have duplicate rows in the resulting dataset as well. To solve this, there is a validate argument in the merge() function, which we can set to ‘one_to_one’, ‘one_to_many’, ‘many_to_one’, and ‘many_to_many’.

#This ensures that there exists only a particular mapping across both the dataframes. If the mapping condition is not satisfied, then it throws a MergeError. To solve this, we can delete duplicates before applying join:

#Prods_without_duplicates = pd.merge(product_dup.drop_duplicates(),customer,how='inner',on='Product_ID')

#pd.merge(product_dup,customer,how='inner',on='Product_ID',validate='many_to_many')





