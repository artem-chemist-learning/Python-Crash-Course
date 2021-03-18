def city_country(city = '', country= ''):
    formatted = str(city).title() + ", "+str(country).title()
    return formatted
Formatted = city_country('Moscow', 'Russia')

def make_album(artist, title, track_count=None):
    album = {'artist':artist,'title':title}
    if track_count:
        album['track count'] = track_count
    return album

while True:
    album = {}
    print('\nPlease enter new album info. Enter "q" to quit at any time')
    
    usr_artist = input('Artist: ')
    if usr_artist.lower() =='q':
        break
    
    usr_title = input('Title: ')
    if usr_title.lower() =='q':
        break
        
    usr_trck = input('Track count: ')
    if usr_trck.lower() =='q':
        break
    
    album = make_album(usr_artist, usr_title, usr_trck)
        
    for key,value in album.items():
        print(key + ' : '+ value)