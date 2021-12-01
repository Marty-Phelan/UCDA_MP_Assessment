import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from importing_and_cleaning_data import strbck_mapping

# I won't need all of the data in mapping for geopandas so I will remove some of the columns to tidy the dataframe up.
strbck_mapping_reduced = strbck_mapping.drop(columns=['Store.Number', 'Ownership Type', 'Phone.Number', 'Timezone'])
strbck_mapping_IE = strbck_mapping_reduced[(strbck_mapping_reduced['Country'] == 'IE')]
strbck_mapping_US = strbck_mapping_reduced[[(strbck_mapping_reduced['Country'] == 'US')]

print(strbck_mapping_IE.head)

strbck_mapping_IE['geometry'] = strbck_mapping_IE.apply(lambda ((x.Longtude, x.Latitude)), axis = 1)



map_of_Ireland = gpd.read_file('IRL_adm/IRL_adm1.shp')