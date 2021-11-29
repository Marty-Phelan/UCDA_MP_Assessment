import pandas as pd
import numpy as np
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
print(RoE)
print(type(RoE))
# Now, I can create my subsets of strbck_direct
#USA
strbck_US = strbck_direct[strbck_direct['Country'] == 'US']
print(strbck_US.info)
#UK
strbck_UK = strbck_direct[strbck_direct['Country'] == 'GB']
print(strbck_UK)
#IE
strbck_IE = strbck_direct[strbck_direct['Country'] == 'IE']
print(strbck_IE)
strbck_RoE = strbck_direct[strbck_direct['Country'].isin(RoE)]
print(strbck_RoE)