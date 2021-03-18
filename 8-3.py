import string
def make_tshirt (size = 26, design = 'Hello World'):
    """
    Makes a T-Shirt with printed design

    Parameters
    ----------
    size : Int, optional
        T-Shirt size, the default is 26.
    design : string, optional
        What to print on it. The default is 'Hello World'.

    Returns
    -------
    None.

    """
    message = 'You ordered a ' + str(size) +' size t-shirt with "' + design+ '" printed on it'
    print(message)
    
make_tshirt(size = 20, design = 'Fuck off')
make_tshirt(design='Nice one)')


