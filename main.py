import sort_algorithms as sa
import timeit

sort_algorithm = sa.quick_sort if input("Change sort alg: 1 - Quick sort 2 - Comb sort > ") == "1"\
    else sa.comb_sort

a = [10, 89, 90, 7, 65, 44, 32, 20]
print(timeit.timeit('sort_algorithm(a)', globals=globals(), number=10000))
