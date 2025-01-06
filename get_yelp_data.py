from yelpapi import YelpAPI
import time, datetime
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='hidden.env')
api_key = os.getenv('YELP_API_KEY')
yelp_api = YelpAPI(api_key)

business_id = 'capital-one-café-los-angeles-10'

# Business query function is specific to a certain business
def get_business_query(api_key, business_id):
    yelp_api = YelpAPI(api_key)
    response = yelp_api.business_query(id=business_id)
    return response

# Search query function is more general and can be used for any search
def get_search_query(api_key,term,location):
    yelp_api = YelpAPI(api_key)
    response = yelp_api.search_query(term=term, location=location,limit=1)
    return response

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
    hours_str = ""
    if 'hours' in response:
        for hours in response['hours']:
            for open_info in hours['open']:
                if open_info['day'] == today:
                    day = day_map[open_info['day']]
                    start = calculate_hour(open_info['start'])
                    end = calculate_hour(open_info['end'])
                    hours_str += f"{day}: {start} - {end}\n"
    else:
        hours_str = "No hours found for this business"
    return hours_str
response = get_business_query(api_key, business_id)


display_today_hours(response)