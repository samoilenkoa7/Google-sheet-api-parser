import requests


# sending request to get data from website
def check_status(vin):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
    url = 'https://pinpoint-us-api.cox2m.com/v1/association?siteId=lmaa&size=1000&q=' + vin
    # getting response from website with json file
    response = requests.get(url, headers=headers).json()
    if response['total'] != 0:
        return 'At Auction'
    elif response['total'] == 0:
        return 'Waiting Arrival'
