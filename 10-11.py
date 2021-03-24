import json
file = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/number.json'

def ask_for_number(file, user):
    str_num = input('Tell me your fav number: ')
    int_num = int(str_num)
    
    with open(file, 'r', encoding='utf8') as fr:
        user_number = json.load(fr)
    
    user_number[user] = int_num
    
    with open(file, 'w', encoding='utf8') as fw:
        json.dump(user_number,fw)

def fetch_the_number(file, user):
    with open(file, 'r', encoding='utf8') as f:
        user_number = json.load(f)
    return user_number[user]

user = input('What is your name? ')

try:     
    with open(file) as f:
        user_number = json.load(f)
except FileNotFoundError:
    f_new = open(file, 'x', encoding='utf8')
    user_number = {'':''}    
    json.dump(user_number,f_new)
    f_new.close()
    
except ValueError:
    f_new = open(file, 'w', encoding='utf8')
    user_number = {'':''}    
    json.dump(user_number,f_new)
    f_new.close()

    
if user in user_number.keys():
    fav_num = fetch_the_number(file, user)
    print(user+ ', your favorite number is {}'.format(fav_num))
else:
    ask_for_number(file, user)        
