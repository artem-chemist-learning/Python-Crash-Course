def build_user(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last']=last
    for key, value in user_info.items():
        profile[key]=value
    
    return profile

Art = build_user('Art','Lebedev',Age = 2,Gender = True)
print(Art)
print(type(Art['Age']))