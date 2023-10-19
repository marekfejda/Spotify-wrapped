CURRENT_YEAR = 2023

import json

file_prefix = "data\AccountData\MyData\\"
file_names = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json", "StreamingHistory4.json"]

total_ms_played_2023 = 0

for file_name in file_names:
    with open(file_prefix+file_name, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    for entry in json_data:
        end_time = entry.get("endTime")
        year = int(end_time.split('-')[0])
        
        if year == CURRENT_YEAR:
            ms_played = entry.get("msPlayed")
            total_ms_played_2023 += ms_played

# Print the total msPlayed in hours, minutes, and seconds
print("Total msPlayed in 2023 from all files:", total_ms_played_2023)