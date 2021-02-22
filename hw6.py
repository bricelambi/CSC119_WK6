

import pandas as pd

data = pd.read_csv('US_points_hourly_CST.csv') #read the csv file into a pandas object

"""
  Exercise 0:
  data contains several different locations, each record (row)
  has a column named 'lat lon', but we need a list of just the
  unique locations.  Get a list of the unique locations and
  store that list in a variable.
"""

unique_locations = data['lat lon'].unique()

print(unique_locations)

"""
  Exercise 0.1:
  Now that you have a list of the unique locations, look at each
  location and print the average wind speed for that location
"""

for location in unique_locations:
    location_data = data[data['lat lon'] == location]
    avg_wind_speed = location_data['WindSpeed'].mean()
    print(f"location is '{location}' - avg wind speed is {avg_wind_speed:.3f}")

