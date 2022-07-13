import requests, os, configparser
import pandas as pd
import matplotlib.pyplot as plt


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_dir = CURR_DIR_PATH + "/data/"

# 3 
WEATHER_URL = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json"
# GET /api/category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json

r = requests.get(WEATHER_URL)
json_data = r.json()


weather_data = {
                "temperature": json_data['timeSeries'][3]["parameters"][10]['values'][0],
                "air pressure": json_data['timeSeries'][3]["parameters"][11]['values'][0],
                "precipitation": json_data['timeSeries'][3]["parameters"][3]['values'][0],
                "date": json_data['timeSeries'][3]['validTime']
            }



weather_data = pd.json_strip(weather_data)

df = pd.DataFrame(weather_data)
df.to_json(CURR_DIR_PATH + "/data/" + "smhi_data" + ".json", index=False)
 

           
# manuellt utplockade data: för att göra ett plotdiagram
# 0         21.2        1011.1            0.0  2022-07-13T07:00:00Z
# 0         22.6        1010.7            0.0  2022-07-13T08:00:00Z
# 0         23.9        1010.1            0.0  2022-07-13T09:00:00Z
# 0         24.7        1009.6            0.0  2022-07-13T10:00:00Z
