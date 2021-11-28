import pandas as pd

# in this project, I want to analyse the locations of starbucks stores and see what patterns
# exist for where Starbucks locates their stores. To achieve this, I will use a directory of Starbucks stores
# N.B. (for simplicity, I edited the headers in the CSV to replace any space in a name with '.'
# as well as country GDP data and population data
# import starbucks directory data
strbck_direct = pd.read_csv('starb_directory.csv', sep=',')
print('All data loaded')
# top level breakdown of strbck_direct data
print(strbck_direct.info())
print(strbck_direct.head())
# clean starbucks directory data
strbckstr_direct = pd.read_csv('starb_directory.csv', sep=',', index_col='Store.Name')
print(strbckstr_direct.head())

