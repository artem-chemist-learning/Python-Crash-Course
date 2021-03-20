"""
Formating names
"""

def print_formatted(first = '', last = ''):
    """
    Returns a title formatted full name

    Parameters
    ----------
    first : string, optional
        First name. The default is ''.
    last : string, optional
        Last name. The default is ''.

    Returns
    -------
    full : string
        Title formated full name.

    """
    full = first.title()+' '+last.title()
    return full

def print_initials(first = '', last = ''):
    """
    Returnsthe name in the Initial.Last format

    Parameters
    ----------
    first : string, optional
        First name. The default is ''.
    last : string, optional
        Last name. The default is ''.

    Returns
    -------
    full : string
        Formated full name.

    """
    full = first.title()[0]+'. '+last.title()
    return full
