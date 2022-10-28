# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел, отсортированных по
# возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(*args):

    n = ''
    for i in args:
        if len(i) == 1:
             n = n + str(min(i)) + ','
        else:
            n = n + str(min(i)) + '-' + str(max(i)) + ','
    print('"' + n[:len(n) - 1] + '"')

get_ranges([1, 2, 3, 4], [7, 8], [10])
get_ranges([4], [7], [10])
get_ranges([2, 3], [8, 9])