# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total' : 'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', (np.where(data['Total_Summer'] == data['Total_Winter'], 'Both',  'Winter')))

better_event = data["Better_Event"].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
#Code starts here
##Creating a new dataframe comprising only the country names and medal totals
top_countries = data[["Country_Name", "Total_Summer", "Total_Winter", "Total_Medals"]]

##Dropping the last row
top_countries.drop(len(top_countries) - 1, inplace = True)

##Creating a Top-10 function
def top_ten(dataframe, series):
    country_list = list(dataframe.nlargest(10, series)["Country_Name"])
    return country_list

##Checking the 10-largest medla winners by total medal counts, and saving the same
top_10_summer = top_ten(top_countries, "Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")

##Checking for common elements and saving it as a list
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin( top_10)]

summer_df.plot.bar(x='Country_Name', y='Total_Summer')
winter_df.plot.bar(x='Country_Name', y='Total_Summer')
top_df.plot.bar(x='Country_Name', y='Total_Summer')


# --------------
##Creating new "Golden Ratio" columns in the subsetted dataframes, and identifyying the max value and country
summer_df["Golden_Ratio"] = summer_df[["Gold_Summer", "Total_Summer"]].apply(lambda x: x[0]/x[1], axis = 1)
summer_max_ratio = summer_df["Golden_Ratio"].max()
summer_country_gold = summer_df[summer_df["Golden_Ratio"] == summer_max_ratio]["Country_Name"].values[0]

winter_df["Golden_Ratio"] = winter_df[["Gold_Winter", "Total_Winter"]].apply(lambda x: x[0]/x[1], axis = 1)
winter_max_ratio = winter_df["Golden_Ratio"].max()
winter_country_gold = winter_df[winter_df["Golden_Ratio"] == winter_max_ratio]["Country_Name"].values[0]

top_df["Golden_Ratio"] = top_df[["Gold_Total", "Total_Medals"]].apply(lambda x: x[0]/x[1], axis = 1)
top_max_ratio = top_df["Golden_Ratio"].max()
top_country_gold = top_df[top_df["Golden_Ratio"] == top_max_ratio]["Country_Name"].values[0]




# --------------
##Dropping the last row from the datframe "data"
data_1 = data.drop(len(data) - 1, inplace = False)

##Adding the points column
data_1["Total_Points"] = (3*data_1["Gold_Total"]) + (2*data_1["Silver_Total"]) + (1*data_1["Bronze_Total"])

##Identifying the max of points and the associated country
most_points = data_1["Total_Points"].max()
best_country = data_1[data_1["Total_Points"] == most_points]["Country_Name"].values[0]


# --------------
#Code starts here
best = data[(data['Country_Name']==best_country) == True]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel = 'United States'
plt.ylabel = 'Medals Tally'
plt.xticks(rotation=45)
plt.show


