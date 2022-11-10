import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        l = []
        m = []
        r = []
        for elem in array:
            if elem < q:
                l.append(elem)
            elif elem > q:
                r.append(elem)
            else:
                m.append(elem)
        return comb_sort(l) + m + comb_sort(r)


def comb_sort(array):
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(array) - gap):
            j = i + gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True
    return array