def checkIfContains(string, segmentArr):
    """returns a boolean response if a single term of a search
     segment arr is found in a string"""
    for segment in segmentArr:
        if segment in string:
            return True
    return False