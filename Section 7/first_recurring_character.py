# find and return first recurring character in an array

def first_recurring_character(arr):
    charHash = {}
    for element in arr:
        if charHash.get(element):
            return element
        else:
            charHash[element] = True
    return None


print(first_recurring_character([1, 2, 5, 1, 2, 3, 5, 1, 2, 4]))
