import pandas as pd
#I am dealing with three imports of data. The starbucks directory data, starb_directory.csv, the countries_of_the_world.csv
#and a dictionary of ISO codes that I retrieved from github.
from ISO3166 import ISO3166_dict
strbck_direct = pd.read_csv('starb_directory.csv', sep=',')
countries_world_prelim = pd.read_csv("countries_of_the_world.csv")
# I ultimately want to work with two files.
# The first will contain the location data for all Starbucks stores in the US and Ireland in order to map.
strbck_mapping = strbck_direct[(strbck_direct['Country'] == 'US') | (strbck_direct['Country'] == 'IE')]
print(strbck_mapping.head())
print(strbck_mapping.info())
# The second will contain the statistical data such as number of stores per country and GDP that I will use to garner further insights.
store_no_rank = strbck_direct['Country'].value_counts()
print(store_no_rank)
print(type(store_no_rank))
# Now, I want to change this series to a Dataframe where I can then include more comprehensive stats about each country.
country_starbuck_count_df = pd.DataFrame(store_no_rank).reset_index()
country_starbuck_count_df.columns = ['Country_ISO', 'No_Starbucks']
print(country_starbuck_count_df)
#There is a wide-range between the country with the most stores and the country with the least.
print('Median number of Starbucks per country: ', country_starbuck_count_df['No_Starbucks'].median())
print('Mean number of Starbucks per country: ', country_starbuck_count_df['No_Starbucks'].mean())
print('Standard Deviation: ', country_starbuck_count_df['No_Starbucks'].std())
print(country_starbuck_count_df[country_starbuck_count_df.values == 'IE'])
print(country_starbuck_count_df[country_starbuck_count_df['No_Starbucks'].values <= 20])
# There is a very high std dev in the data and a large discrepancy between the median and mean. I am going to remove all countries with a number of stores below 10.
country_starbuck_merge1_df = country_starbuck_count_df[country_starbuck_count_df['No_Starbucks'] > 9]
print(country_starbuck_merge1_df.info())
#The first of my three merge sheets is now ready.
print(countries_world_prelim.columns)
print(countries_world_prelim.info)
# countries_world_prelim contains many columns that will not be used for my analysis. I will remove these first.
countries_world = countries_world_prelim.drop(columns=['Coastline (coast/area ratio)', 'Net migration', 'Infant mortality (per 1000 births)', 'Literacy (%)', 'Phones (per 1000)', 'Arable (%)',
       'Crops (%)', 'Other (%)', 'Climate', 'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service'])
print(type(countries_world))
# I will be merging this list based on Country so I need to examine how Country is listed in the dataframe
print(countries_world['Country'].values)
# There seems to be a space in each string that needs to be stripped away.
countries_world['Country'] = countries_world['Country'].str.rstrip()
# I later discovered a similar problem in 'Region'. For simplicity, I cleaned the data here.
countries_world['Region'] = countries_world['Region'].str.rstrip()
print(countries_world['Country'].values)
#I will also creat a new column that adds an uppercase variation of each country name.
for lab, row in countries_world.iterrows() :
    countries_world.loc[lab, "COUNTRY"] = row["Country"].upper()
print(countries_world['COUNTRY'].values)
# I can now exclude the 'Country' column as it will not be needed.
countries_world_2 = countries_world.drop(columns= 'Country')
print(countries_world_2.columns)
# To ensure the merge works correctly, I will need to check my ISO dict against the COUNTRY strings in countries_world_2.
# First, I will change the ISO dict into a Dataframe.
ISO_df = pd.DataFrame.from_dict(ISO3166_dict, orient='index')
ISO_df.reset_index(level=0, inplace= True)
ISO_df = ISO_df.rename(columns={'index': 'Country_ISO', 0 : 'COUNTRY'})
print(ISO_df)
# With the ISO dataframe created, I can now compare the values. However, comparing the 200+ values in both dataframes
# is not the most productive way to do this so I will merge ISO and starbucks first.
starbucks_country_fullnames = country_starbuck_merge1_df.merge(ISO_df, on = 'Country_ISO', how = 'left')
print(starbucks_country_fullnames.head(-1))
# We can see now that all rows were successfully given a value. We can now compare this data to countries_world_2
for value in list(starbucks_country_fullnames['COUNTRY']) :
       if value not in list(countries_world_2['COUNTRY']) :
              print(value)
       else :
              print('All Good')
#I now know there are five values my starbucks data that do not match in countries_world. I can print this alphabetical list
# and check the data manually.
print(countries_world_2['COUNTRY'].values)
# 'KOREA, SOUTH', 'TAIWAN', 'RUSSIA', 'VIETNAM', 'BAHAMAS, THE'.
# Now that I have the correct terms, I can change the names in my starbucks_country_fullnames list.
starbucks_country_fullnames['COUNTRY'] = starbucks_country_fullnames['COUNTRY'].replace(["KOREA, REPUBLIC OF", "TAIWAN, PROVINCE OF CHINA", "RUSSIAN FEDERATION", "VIET NAM", "BAHAMAS"],
                                                                                        ['KOREA, SOUTH', 'TAIWAN', 'RUSSIA', 'VIETNAM', 'BAHAMAS, THE'])
for value in list(starbucks_country_fullnames['COUNTRY']) :
       if value not in list(countries_world_2['COUNTRY']) :
               print(value)
       else :
              print('All Good')
# I have verified that my two dataframes have been correctly matched. I can now complete my last merge.
starbucks_country_analysis = starbucks_country_fullnames.merge(countries_world_2, on = 'COUNTRY', how = 'left')
# I want to create some new columns: Area (sq. km), Pop. Density (per sq. km), GDP (€ per capita)
starbucks_country_analysis["Area_sqkm"] = starbucks_country_analysis['Area (sq. mi.)'] * 2.58999
starbucks_country_analysis['Pop_dens_sqkm'] = starbucks_country_analysis['Pop. Density (per sq. mi.)'] * 2.58999
starbucks_country_analysis['GDP_€_percapita'] = starbucks_country_analysis['GDP ($ per capita)'] * 1.13
# I also want to tidy the regions to make colour categorisation more manageable
orig_regions= starbucks_country_analysis["Region"].values
print(set(orig_regions))
starbucks_country_analysis['Region'] = starbucks_country_analysis['Region'].replace(["ASIA (EX. NEAR EAST)", 'C.W. OF IND. STATES'],'ASIA')
starbucks_country_analysis['Region'] = starbucks_country_analysis['Region'].replace(['LATIN AMER. & CARIB'],'SOUTH AMERICA')
starbucks_country_analysis['Region'] = starbucks_country_analysis['Region'].replace(['WESTERN EUROPE', 'EASTERN EUROPE'],'EUROPE')
Regions = starbucks_country_analysis["Region"].values
print(set(Regions))
for lab, row in starbucks_country_analysis.iterrows() :
    starbucks_country_analysis.loc[lab, "Color"] = row["Region"]
starbucks_country_analysis['Color'] = starbucks_country_analysis['Region'].replace(['NEAR EAST', 'NORTHERN AMERICA', 'ASIA', 'EUROPE', 'NORTHERN AFRICA', 'OCEANIA', 'SOUTH AMERICA'],
                                                                                   ['darkorange', 'blue', 'red', 'green', 'maroon', 'mediumpurple', 'yellow'])
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.info())
# Both Dataframes are now available: strbck_mapping and starbucks_country_analysis.