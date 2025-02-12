
import random as rd





def sorter(seq):

    """Sorting function

    Parameters:
        seq (list): a list to sort

    Returns:
        list: a sorted list

    Examples:
        >> sorter([9, 6, 2, 0, 4, 7, 8, 5, 3, 1])
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >> sorter([8, 0, 5, 4, 7, 6, 9, 1, 2, 3, 1055, 811])
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 811, 1055]

    """

    ...




x = [i for i in range(10)]
rd.shuffle(x)
print(x)


rs = sorter(x)
print(rs)
