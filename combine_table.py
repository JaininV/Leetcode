import pandas as pd

tab1 = pd.DataFrame({'personId': [1, 2], 'lastName': ['Wang', 'Alice'], 'firstName': ['Allen', 'Bob']})
tab2 = pd.DataFrame({'addressId': [1, 2], 'personId': [2,3], 'city': ['New York City', 'Bob'], 'state': ['New York', 'California']}) 

print(tab1)
print(tab2)

#combine two tables
final_table = tab1.merge(tab2, how='left', on='personId')
print(final_table[['firstName', 'lastName', 'city', 'state']])