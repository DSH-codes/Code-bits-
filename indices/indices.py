
# A function to find all indices for a given char



def all_index(seq: str | list, char: str):
    """
    Function to return all indices
    of a specified character

    Parameters:
        seq (str, list): a string/list to search
        character occurrences in
        char (str): a character indices of which
        to find

    Returns:
        list: a list of indices

    Raises:
        TypeError: if seq is not a str/list, or
        if seq is a list, but one of the items
        is not a string type

    Examples:
        >>> all_index("hello world", "o")
        [4, 7]
        >>> all_index(["1", "2", "3", "2"], "2")
        [1, 3]
        >>> all_index("axaxa", "a")
        [0, 2, 4]
        >>> all_index("hello world", "x")
        []
    """

    seq = "".join(seq) if type(seq) == list else seq        # convert the sequence into a string, if it is a list
    indices = []                                            # a list to collect indices

    for i in seq:

        if i == char:                                       # if i is the char we search

            indices.append(seq.index(i))                    # add its index to the list
            seq = seq.replace(i, "-", 1)                    # then replace its first occurrence, by a dash, to prevent getting the same index again

    return indices


if __name__ == "__main__":

    s = all_index("hello world", "o")
    print(s)

