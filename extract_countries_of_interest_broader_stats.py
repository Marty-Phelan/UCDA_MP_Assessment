import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
strbck_direct = pd.read_csv('starb_directory.csv', sep=',')
# I only want to analyse data for the United State, UK, Ireland and the remainder of the EU27 member states as its own region
# first, I need to see which countries are listed in the directory and how they are represented
countries = strbck_direct['Country'].unique()
print(countries)
print(type(countries))
# the countries are represented with their 2-letter ISO codes. I know that the ISO codes for the United States, Ireland and the UK
# are 'US', 'IE' and 'GB' respectively
# I also need a list of the rest of the EU countries that I will call 'RoE'.
# ISO Codes have been obtained from https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Country_codes
RoE = ['BE', 'BG', 'CZ', 'DK', 'DE', 'EE', 'EL', 'ES', 'FR', 'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'HU', 'MT', 'NL',
       'AT', 'PL', 'PT', 'RO', 'SI', 'SK', 'FI', 'SE']
# Now, I can create my subsets of strbck_direct
#USA
strbck_US = strbck_direct[strbck_direct['Country'] == 'US']
#UK
strbck_UK = strbck_direct[strbck_direct['Country'] == 'GB']
#IE
strbck_IE = strbck_direct[strbck_direct['Country'] == 'IE']
#RoE
strbck_RoE = strbck_direct[strbck_direct['Country'].isin(RoE)]
us_num_strbcks = strbck_US['Brand'].count()
print('US stores: ', us_num_strbcks)
ie_num_strbcks = strbck_IE['Brand'].count()
print('IE stores:', ie_num_strbcks)
uk_num_strbcks = strbck_UK['Brand'].count()
print('UK stores:', uk_num_strbcks)
store_no_rank = strbck_direct['Country'].value_counts()
print(store_no_rank)
print(type(store_no_rank))
# Now, I want to change this series to a Dataframe where I can then include more comprehensive stats about each country.
country_starbuck_analysis_df = pd.DataFrame(store_no_rank).reset_index()
country_starbuck_analysis_df.columns = ['Country_iso', 'No_Starbucks']
print(country_starbuck_analysis_df)
print(type(country_starbuck_analysis_df))
# Now I can start adding extra data to my dataframe.
countries_world_prelim = pd.read_csv("countries_of_the_world.csv")
print(countries_world_prelim.columns)
print(countries_world_prelim.info)
#As we can see, the countries information that I have imported contains 227 countries and also contains many columns of data that
# I do not want to include for analysis. I will remove Coastline, Net migration, Infant mortality, Literacy, Phones, Arable, Crops, Other,
#Climate, Birthrate, Deathrate Agriculture, Industry and Service.
countries_world = countries_world_prelim.drop(columns=['Coastline (coast/area ratio)', 'Net migration', 'Infant mortality (per 1000 births)', 'Literacy (%)', 'Phones (per 1000)', 'Arable (%)',
       'Crops (%)', 'Other (%)', 'Climate', 'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service'])
# I only want to analyse the data for the 73 countries included on my Starbucks list.
# I therefore need to convert my ISO country data into full country names so I can filter this data.
country_iso = pd.ExcelFile('Country_and_ISO.xlsx')
country_iso_convert = country_iso.parse(0)
print(country_iso_convert.head())
#Need to rename my column headings so that they match the names in my country_starbuck_analysis_df
country_iso_convert.columns = ['Country', 'Country_iso']
print(country_iso_convert.head())
#Now, I need to merge all of my data into one dataframe and I can do this using left join to ensure I only get
# the data for the countries in my country_starbuck_analysis_df dataframe
country_starbucks_complete_df = country_starbuck_analysis_df.merge(country_iso_convert, on = 'Country_iso', how = 'left') \
       .merge(countries_world, on = 'Country', how = 'left')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(country_starbucks_complete_df.info)
# I have a large amount of NaN fields in my data that came from countries_world so there is something wrong with
# the secondary merge on the Country column.
broken_countries = countries_world['Country'].unique()
print(broken_countries)
#I can now see that the 'Country' column from countries_world is carrying an additional space at the end of each name.
#I need to remove these and carry out my merge again.
countries_world['Country'] = countries_world['Country'].str.rstrip()
fixed_countries = countries_world['Country'].unique()
print(fixed_countries)
#I can now merge my data again to carry over all values
country_starbucks_full_df = country_starbuck_analysis_df.merge(country_iso_convert, on = 'Country_iso', how = 'left') \
       .merge(countries_world, on = 'Country', how = 'left', validate= 'one_to_one')
print(country_starbucks_full_df)
#Still some columns that contain missing data. I can see that these are at index 4, 7, 17, 35, 53, 60, 63, 65 and 68. The majority of these values have less than
# 10 Starbucks so I will first remove all rows with 10 or less stores.
#First, I need to tidy up 
country_starbucks_reduced_df = country_starbucks_full_df[country_starbucks_full_df['No_Starbucks'] > 10]
print(country_starbucks_reduced_df)
#Now I want to tidy the names of the Countries that have not merged correctly. These are South Korea, Taiwan, Russia and Vietnam.






