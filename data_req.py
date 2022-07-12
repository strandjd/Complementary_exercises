from pendulum import date
import requests, os, configparser
import pandas as pd


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_dir = CURR_DIR_PATH + "/data/"
target_dir = data_dir + "/rawfiles/"
# 1 
config = configparser.ConfigParser()
config.read(CURR_DIR_PATH + "/config.ini")

# 2 
API_KEY = config.get("DEV", "API_KEY")

# 3 
WEATHER_URL = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json"
# GET /api/category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json

r = requests.get(WEATHER_URL)

# 4
print("url:", r.url) # Should ressemble link from above, else check params dictionary
print("http code:", r.status_code) # Should be 200, else check key

# 5 
if r.status_code == 200: # If connection is successful (200: http ok)
    json_data = r.json() # Get result in json
#print(json_data['timeSeries'][0])

#####################################################################
# smhidictlist = {"approvedTime":"2022-07-12T20:04:50Z","referenceTime":"2022-07-12T20:00:00Z","geometry":{"type":"Point","coordinates":[[15.990068,57.997072]]},"timeSeries":[{"validTime":"2022-07-12T21:00:00Z","parameters":[{"name":"spp","levelType":"hl","level":0,"unit":"percent","values":[-9]}]}]}
# print(smhidictlist['timeSeries'][0]["parameters"][0]['name'])
# timeSeries --> dict, list--> validtime k&v, parameter: --> dict, lista, dicts
#####################################################################

# 6 
weather_data = {
                "temperature": json_data['timeSeries'][0]["parameters"][10]['values'][0],
                "air pressure": json_data['timeSeries'][0]["parameters"][11]['values'][0],
                "precipitation": json_data['timeSeries'][0]["parameters"][3]['values'][0],
                "date": json_data['timeSeries'][0]['validTime']
            }

# date = validTime                                  -   json_data['timeSeries'][0]['validTime']
# temperature = parameter = t, unit = C             -   json_data['timeSeries'][0]["parameters"][10]['values'][0]
# air pressure = parameter = msl, unit = hPa        -   json_data['timeSeries'][0]["parameters"][11]['values'][0] 
# precipitation = parameter = pmean, unit = mm/h    -   json_data['timeSeries'][0]["parameters"][3]['values'][0]


weather_data = pd.json_normalize(weather_data)
print("this is a print statement with more stuff\n",weather_data)







df = pd.DataFrame(weather_data)
df.to_csv(CURR_DIR_PATH + "/data/" + "smhi_data" + ".csv", index=False)
            


# print("this is a print statement with more stuff\n",)