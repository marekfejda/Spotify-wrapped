import json
import datetime

# Settings
CURRENT_YEAR = 2023
MINIMAL_PODCAST_LENGTH_IN_MINUTES = 10
file_prefix = "data/AccountData/MyData/"
file_names = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json", "StreamingHistory3.json", "StreamingHistory4.json"]

# Function to calculate the number of days elapsed from the first day of the year
def daysElapsedFromFirstDayOfYear():
    current_date = datetime.date.today()
    first_day_of_year = datetime.date(current_date.year, 1, 1)
    return (current_date - first_day_of_year).days + 1

# Initialize a dictionary to track minutes played by month
monthly_minutes_played = {
    1: 0,  # January
    2: 0,  # February
    3: 0,  # March
    4: 0,  # April
    5: 0,  # May
    6: 0,  # June
    7: 0,  # July
    8: 0,  # August
    9: 0,  # September
    10: 0,  # October
    11: 0,  # November
    12: 0,  # December
}

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

            # Update the monthly minutes played
            monthly_minutes_played[month] += minutes_played

music_minutes = music_ms_played
podcasts_minutes = podcasts_ms_played
total_minutes = music_minutes + podcasts_minutes

average = total_minutes / daysElapsedFromFirstDayOfYear()

print(f"Total [minutes]: {total_minutes} -> {total_minutes // 60} hours and {total_minutes % 60} minutes")
print(f"Daily average [minutes]: {average}")
print(f"Music [minutes]: {music_minutes}")
print(f"Podcasts [minutes]: {podcasts_minutes}")
print(f"You've played {songs_played} songs and {podcasts_played} podcasts")

# Print monthly minutes played without decimals
for month, minutes in monthly_minutes_played.items():
    print(f"Minutes played in {datetime.date(CURRENT_YEAR, month, 1).strftime('%B')}: {int(minutes)} minutes")
