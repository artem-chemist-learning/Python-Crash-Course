import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print (r.status_code)

ids = r.json()

dict_Submissions = {}

for id in ids[:30]:
    item_url = 'http://hacker-news.firebaseio.com/v0/item/'+str(id)+'.json'