def make_sandwich(*ingredients):
    """
    

    Parameters
    ----------
    *ingredients : string
        What customer whants on the sandwitch.

    Returns
    -------
    None.

    """
    sandwich = []
    for ingredient in ingredients:
        sandwich.append(ingredient)
    return sandwich

blt = make_sandwich('bacon','lettuce','tomato','jalapenio')
print(blt)