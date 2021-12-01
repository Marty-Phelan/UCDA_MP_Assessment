import matplotlib.pyplot as plt
from importing_and_cleaning_data import starbucks_country_analysis
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.columns)

plt.bar(starbucks_country_analysis['Region'], starbucks_country_analysis['No_Starbucks'],
        color=starbucks_country_analysis['Color'])
plt.xlabel("Global Region")
plt.ylabel("Number of Starbucks")
plt.title("Starbucks per global region")

plt.show()