CURRENT_YEAR = 2023

import json

file_prefix = "data\AccountData\MyData\\"
file_names = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json", "StreamingHistory4.json"]

total_ms_played = 0

for file_name in file_names:
    with open(file_prefix+file_name, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    for entry in json_data:
        end_time = entry.get("endTime")
        year = int(end_time.split('-')[0])
        
        if year == CURRENT_YEAR:
            ms_played = entry.get("msPlayed")
            total_ms_played += ms_played


total_seconds = total_ms_played // 1000
total_minutes = total_seconds // 60
remaining_minutes = total_minutes % 60
total_hours = total_minutes // 60

print(f"Time spend listening to spotify [min]: {total_minutes} -> {total_hours} hours and {remaining_minutes} minutes")
