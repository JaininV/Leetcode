#Import libraries
import pandas as pd

#Create dataframe
Person = pd.DataFrame({'personId': [1, 2], 'lastName': ['Wang', 'Alice'], 'firstName': ['Allen', 'Bob']})
Address = pd.DataFrame({'addressId': [1, 2], 'personId': [2,3], 'city': ['New York City', 'Bob'], 'state': ['New York', 'California']}) 


#combine two tables
def combine_two_tables(Person, Address):
    result = pd.merge(Person, Address, how='left', on='personId')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result

#call function

print(Person)