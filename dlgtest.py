# Convert the weather data into parquet format. Set the raw group to appropriate value you see fit for this data.
#importing the required libraries
import os
import pandas as pd 
import pyarrow.parquet as pq


parquetFilename = "output_gen.parquet"


#read weather csv file
df = pd.read_csv("weather_20160201.csv")

#convert csv file to parquet
df.to_parquet(parquetFilename)



#writing csv data into dataframe
df = pd.DataFrame (df, columns = ['ForecastSiteCode','ObservationTime','ObservationDate','WindDirection','WindSpeed',
'WindGust','Visibility','ScreenTemperature','Pressure','SignificantWeatherCode','SiteName','Latitude','Longitude','Region','Country'])

# Finding highest Temperature
highest_temp = df['ScreenTemperature'].max()

#finding associated attributes belongs to the highest temp
output = df.loc[df['ScreenTemperature'] == highest_temp, ['ObservationDate','ScreenTemperature','Region']]

print("-----------------------------------------------------------------------------------------------------------------------")
print("Hottest Date, Temperature, Region : ", output)
