def Describe_City(city = 'Moscow', country = 'Russia'):
    """
    Being captain obvious

    Parameters
    ----------
    city : string, optional
        City, duh. The default is 'Moscow'.
    country : string, optional
        Country, no shit. The default is 'Russia'.

    Returns
    -------
    None.

    """
    print(city +' is in '+country)

Describe_City(country = 'UK', city = 'Sheffield')
Describe_City('Touluse', 'France')
Describe_City(country = 'Idaho')