import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

response = r.json()
response_items = response['items']

print('Selected data about repositories: ')

for item in response_items:
    print('\nName:', item['name'])
    print('Owner: ', item['owner']['login'])
    print('Stars: ', item['stargazers_count'])
    print('Description: ', item['description'])