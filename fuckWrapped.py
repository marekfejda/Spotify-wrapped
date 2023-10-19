#-----------SETTINGS----------------
CURRENT_YEAR = 2023
MINIMAL_PODCAST_LENGHT_IN_MINUTES = 5
file_prefix = "data\AccountData\MyData\\"
file_names = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json", "StreamingHistory4.json"]
#-----------------------------------

import json
import datetime

def daysElapsedFromFirstDayOfYear():
    current_date = datetime.date.today()
    first_day_of_year = datetime.date(current_date.year, 1, 1)
    return (current_date - first_day_of_year).days+1

music_ms_played = 0
podcasts_ms_played = 0

for file_name in file_names:
    with open(file_prefix+file_name, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    for entry in json_data:
        end_time = entry.get("endTime")
        year = int(end_time.split('-')[0])
        
        if year == CURRENT_YEAR:
            ms_played = entry.get("msPlayed")
            if MINIMAL_PODCAST_LENGHT_IN_MINUTES*60*1000 < ms_played:
                podcasts_ms_played += ms_played
            else:
                music_ms_played += ms_played


music_minutes = music_ms_played // 1000 // 60
podcasts_minutes = podcasts_ms_played // 1000 // 60
total_minutes = music_minutes + podcasts_minutes

average = total_minutes // daysElapsedFromFirstDayOfYear()

print(f"Total [minutes]: {total_minutes} -> {total_minutes // 60} hours and {total_minutes % 60} minutes")
print(f"Daily average [minutes]:", average)
print(f"Music [minutes]: ", music_minutes)
print(f"Podcasts [minutes]: ", podcasts_minutes)
