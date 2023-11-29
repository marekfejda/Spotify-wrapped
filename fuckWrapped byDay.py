import json
import datetime

# Settings
CURRENT_YEAR = 2023
MINIMAL_PODCAST_LENGTH_IN_MINUTES = 10
file_prefix = "data/AccountData/MyData/"
file_names = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json", "StreamingHistory4.json"]

# Function to calculate the number of days elapsed from the beginning of the year to the current date
def daysElapsedFromFirstDayOfYear():
    current_date = datetime.date.today()
    first_day_of_the_year = datetime.date(current_date.year, 1, 1)
    delta = current_date - first_day_of_the_year
    return delta.days + 1

# Initialize a dictionary to track minutes played by day
daily_minutes_played = {}

music_ms_played = 0
podcasts_ms_played = 0
songs_played = 0
podcasts_played = 0

for file_name in file_names:
    with open(file_prefix + file_name, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for entry in json_data:
        end_time = entry.get("endTime")
        date_time_obj = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M")
        year = date_time_obj.year
        month = date_time_obj.month
        day = date_time_obj.day

        if year == CURRENT_YEAR:
            ms_played = entry.get("msPlayed")

            # Convert msPlayed to minutes
            minutes_played = ms_played / 60000  # 1 minute = 60,000 milliseconds

            # Determine whether it's music or a podcast
            if minutes_played >= MINIMAL_PODCAST_LENGTH_IN_MINUTES:
                podcasts_ms_played += minutes_played
                podcasts_played += 1
            else:
                music_ms_played += minutes_played
                songs_played += 1

            # Update the daily minutes played
            date = datetime.date(year, month, day)
            if date in daily_minutes_played:
                daily_minutes_played[date] += minutes_played
            else:
                daily_minutes_played[date] = minutes_played

music_minutes = music_ms_played
podcasts_minutes = podcasts_ms_played
total_minutes = music_minutes + podcasts_minutes

print(f"Total [minutes]: {total_minutes} -> {total_minutes // 60} hours and {total_minutes % 60} minutes")
print(f"Music [minutes]: {music_minutes}")
print(f"Podcasts [minutes]: {podcasts_minutes}")
print(f"You've played {songs_played} songs and {podcasts_played} podcasts")

# Print daily minutes played without decimals
for date, minutes in sorted(daily_minutes_played.items()):
    print(f"Minutes played on {date.strftime('%Y-%m-%d')}: {int(minutes)} minutes")
