import pandas as pd

Person = pd.DataFrame({'personId': [1, 2], 'lastName': ['Wang', 'Alice'], 'firstName': ['Allen', 'Bob']})
Address = pd.DataFrame({'addressId': [1, 2], 'personId': [2,3], 'city': ['New York City', 'Bob'], 'state': ['New York', 'California']}) 


#combine two tables
combine_two_tables = Person.merge(Address, how='left', on='personId')
print(combine_two_tables[['firstName', 'lastName', 'city', 'state']])