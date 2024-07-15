import timeit
import random
from tabulate import tabulate


def main():
    sizes = [10, 100, 1000, 10000]
    results = []

    for size in sizes:
        random_list = generate_random_list(size)

        sorted_time = test_sorting_function(random_list, sorted)
        sort_method_time = test_sorting_function(random_list, lambda lst: lst.sort())
        merge_sort_time = test_sorting_function(random_list, merge_sort)
        insertion_sort_time = test_sorting_function(random_list, insertion_sort)

        results.append([size, sorted_time, sort_method_time, merge_sort_time, insertion_sort_time])

    print("\nResults:")
    headers = ["List Size", "sorted()", "sort() Method", "merge_sort", "insertion_sort"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

def generate_random_list(n):
    return [random.randint(0, 10000) for _ in range(n)]


def test_sorting_function(random_list, sorting_function):
    temp_list = random_list.copy()
    start_time = timeit.default_timer()
    sorting_function(temp_list)
    end_time = timeit.default_timer()
    time_taken = end_time - start_time
    return f"{time_taken:.8f}"

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst


if __name__ == '__main__':
    main()


