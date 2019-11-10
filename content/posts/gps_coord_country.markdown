title: Batch assign a country to longitude / latitude coordinates
slug: longitude-latitude-to-country
lang: en
category: python
date: 2019-11-07
modified: 2019-11-07
<br />
A useful script to batch convert a bunch of coordinates to a country (API call for each coordinate pair is sometimes too slow).

There was a bunch of data in an Excel file having coordinates but no country information.

``` python
import pandas as pd
df = pd.ExcelFile("data.xlsx").parse("Sheet1")

```

<img src="static/2019-11-coordinates-country/data.png" alt="drawing" style="margin-top:20px; width:300px;"/>

Thanks to <a href="https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city">linqu's post on Stackoverflow</a> it's easy to do a batch conversion:

``` python
import requests

from shapely.geometry import mapping, shape
from shapely.prepared import prep
from shapely.geometry import Point

data = requests.get("https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson").json()

countries = {}
for feature in data["features"]:
    geom = feature["geometry"]
    country = feature["properties"]["ADMIN"]
    countries[country] = prep(shape(geom))

def get_country(lon, lat):
    point = Point(lon, lat)
    for country, geom in countries.items():
        if geom.contains(point):
            return country

    return "unknown"
```

Add the country column and dump to disk:

``` python

df['country'] = df.apply (lambda row: get_country(row['lng'], row['lat']), axis=1)
df.to_csv('data_with_country.csv')
```

Check out the result:

``` python

from matplotlib import pyplot as plt
counts = df.groupby(['country']).agg(len).sort_values(by=['id'], ascending=False)
plt.xticks(rotation=80)
plt.bar(counts.index, counts.id)
plt.show()
```

<img src="static/2019-11-coordinates-country/plot1.png" alt="drawing" style="margin-top:20px; width:800px;"/>


``` python

above5 = counts[counts['id']>5][1:]
f, ax = plt.subplots(figsize=(18,5))
plt.xticks(rotation=80)
plt.bar(above5.index,above5.id)
```

<img src="static/2019-11-coordinates-country/plot2.png" alt="drawing" style="margin-top:20px; width:800px;"/>



That's all!

~                                                        
