

# A simple function to flatten nested lists, no matter how deep they are nested




def flatten(array):

    result = []                                                 # final result list to out

    for item in array:

        if type(item) != list:                                  # if it is not a list, an int or a string
            result.append(item)                                 # we just append it to the result list
        else:                                                   # if it is a list
            result += item                                      # we extend the result list by it

    if any(isinstance(item, list) for item in result):          # then we check if there any list remain
        return flatten(result)                                  # if so, the function called recursively on the result list
    else:                                                       # if no lists found
        return result                                           # the result list just returned



if __name__ == "__main__":

    ...

    # chaotically_nested_int_list = [1, 2, 3, 4, [5, 6, 7, [8, 9, 10]], 888, [1919, -77], 1985, [404]]
    # chaotically_nested_mixed_list = [1, 2, 3, ["x", 4, "y", 5, "z", 6, ["hello world", 7]], "spam"]
    #
    # x = flatten(chaotically_nested_int_list)
    # print(x)
    #
    # y = flatten(chaotically_nested_mixed_list)
    # print(y)
