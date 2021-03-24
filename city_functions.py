def city(city='', country='', populaton = 0):
    return_string = ''
    if (city !=''):
        return_string+=city
    if (country!=''):
        return_string= return_string+ ', '+country
    if(populaton >0):
        return_string = return_string + ', population of '+ str(populaton)
    return return_string


    