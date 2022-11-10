# блочная сортировка
def bucket_sort(input_list):
    max_value = max(input_list)
    size = max_value / len(input_list)
    buckets_list = []
    for i in range(len(input_list)):
        buckets_list.append([])

    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            var = bucket[i]
            j = i - 1
            while (j >= 0) and (var < bucket[j]):
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var

    for i in range(len(input_list)):
        insertion_sort(buckets_list[i])

    final_output = []
    for i in range(len(input_list)):
        final_output = final_output + buckets_list[i]

    return final_output


# пирамидальная сортировка
def heap_sort(nums):
    n = len(nums)

    def heapify(nums, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            heapify(nums, heap_size, largest)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
