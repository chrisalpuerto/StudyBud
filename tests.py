from yelpapi import YelpAPI
import time, datetime

api_key = 'JwQvJoL9wUVzdYm7zDfkL6LmHI0I0xqpND6fS93EssWtjgnWqLQp3y5_dRtmPBkT7ds6yXwvIqueimKf3j-kgCibv8cwNVOk_Io6TKUv9egrAP1AOEe6QmLpWN96Z3Yx'
yelp_api = YelpAPI(api_key)

business_id = 'capital-one-café-los-angeles-10'
response = yelp_api.business_query(id=business_id)
day_map = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
def calculate_hour(time):
    hour = int(time[:2])
    minute = int(time[2:])
    period = 'AM'
    if hour > 12:
        hour -= 12
        period = 'PM'
    if hour == 0:
        hour = 12
    return f"{hour}:{minute:02d} {period}"

    
today = datetime.datetime.today().weekday()
def display_all_hours(response): 
    if 'hours' in response:
        print(response['hours'])
        for hours in response['hours']:
            for open_info in hours['open']:
                day = day_map[open_info['day']]
                start = open_info['start']
                end = open_info['end']
                print(f"{day} : {start} - {end}")
    else:
        print('No hours found for', business_id)

def display_today_hours(response):
    if 'hours' in response:
        for hours in response['hours']:
            for open_info in hours['open']:
                if open_info['day'] == today:
                    day = day_map[open_info['day']]
                    start = calculate_hour(open_info['start'])
                    end = calculate_hour(open_info['end'])
                    print(f"{day}: {start} - {end}")
    else:
        print("No data found for today")
display_today_hours(response)