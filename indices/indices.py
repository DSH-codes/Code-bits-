
# A function to find all indices for a given char



def all_index(seq: str | list, char: str):

    """ Function to return all indices
    of a specified character

    :param seq: A sequence from which the indices are needed
    :type seq: str, list or tuple

    :param char: A char(letter) occupying the indices
    :type char: str

    :return: a list of indices
    :rtype: list

    """

    seq = "".join(seq) if type(seq) == list else seq        # convert the sequence into a string, if it is a list
    indices = []                                            # a list to collect indices
    twin = seq                                              # a copy to perform editing on

    for i in twin:

        if i == char:

            indices.append(seq.index(i))
            seq = seq.replace(i, "-", 1)

    return indices


s = all_index(list("I am writing a code"), "a")

print(s)
