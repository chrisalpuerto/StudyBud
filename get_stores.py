from yelpapi import YelpAPI
import time
from get_yelp_data import *

api_key = 'JwQvJoL9wUVzdYm7zDfkL6LmHI0I0xqpND6fS93EssWtjgnWqLQp3y5_dRtmPBkT7ds6yXwvIqueimKf3j-kgCibv8cwNVOk_Io6TKUv9egrAP1AOEe6QmLpWN96Z3Yx'
yelp_api = YelpAPI(api_key)


def get_cafes(api_key,location,term):
    response = get_search_query(api_key,term,location)
    cafes =[]
    for business in response['businesses']:
        business_id = business['id']
        response_hours = get_business_query(api_key,business_id)
        cafes.append({
            'name': business['name'],
            'rating': business['rating'],
            'address': ' '.join(business['location']['display_address']),
            'review_count': business['review_count'],
            'hours': display_today_hours(response_hours)
        })
    return cafes


location = input(str('Enter your location or ZIP code: '))
cafes = get_cafes(api_key,location,'cafes')

for cafe in cafes:
    print(cafe['name'])
    print(cafe['rating'])
    print(cafe['address'])
    print(cafe['hours'])
    print()

        