import requests
import pandas as pd
from datetime import datetime

# DataFrame for save all pieces of the barrage of one episode
barrage_DataFrame = pd.DataFrame()


# 15
# video_code = "f4100f6zwit"  
# 27
# video_code = "p4100z5khsn"
# 29
video_code = "r41005tibb1"

# amount of request barrage
num = 10000
# step parameter
step = 30000

# loop num times to get barrage
for i in range(num):
    url = f'https://dm.video.qq.com/barrage/segment/{video_code}/t/v1/{i*30000}/{i*30000+step}'
    response = requests.get(url=url).json()
    if ( len(response["barrage_list"])) > 0:
        # the DataFrame to save current barrage
        temp_barrage_DataFrame = pd.json_normalize(response['barrage_list'], errors='ignore')
        barrage_DataFrame = pd.concat([barrage_DataFrame, temp_barrage_DataFrame])
        print(temp_barrage_DataFrame.shape[0], "barrages, total get ", barrage_DataFrame)
    else:
        break

print("totally get ", barrage_DataFrame.shape[0], " barrages")
# check the amount of rows
rows= barrage_DataFrame.shape
print("totally ", rows, " rows")

# choose the columns to sava data
barrage_DataFrame = barrage_DataFrame.loc[:, ['time_offset','create_time','content']]

# transform create_time to the form of hour
barrage_DataFrame["hour"] = barrage_DataFrame["create_time"].apply(lambda x: datetime.fromtimestamp(int(x)).strftime('%H'))

# save DataFrame as a csv file
barrage_DataFrame.to_csv(f"29epi.csv",encoding="utf-8",errors='ignore',index=False)
print("Successfully saved to csv")