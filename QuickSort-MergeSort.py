import random
import time
import sys
import psutil
import os
sys.setrecursionlimit(10**6)

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure the time taken by a sorting algorithm
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return round(end_time - start_time, 5)

# Performance Testing
def performance_test():
    sizes = [1000, 5000, 10000, 20000]  # Different sizes for the test
    for size in sizes:
        arr_sorted = list(range(size))
        arr_reverse_sorted = list(range(size, 0, -1))
        arr_random = random.sample(range(size), size)

        print(f"\nPerformance on arrays of size {size}:")

        # Quick Sort
        print("\nQuick Sort on sorted data:", measure_time(quick_sort, arr_sorted[:]))
        print("Quick Sort on reverse sorted data:", measure_time(quick_sort, arr_reverse_sorted[:]))
        print("Quick Sort on random data:", measure_time(quick_sort, arr_random[:]))

        # Merge Sort
        print("\nMerge Sort on sorted data:", measure_time(merge_sort, arr_sorted[:]))
        print("Merge Sort on reverse sorted data:", measure_time(merge_sort, arr_reverse_sorted[:]))
        print("Merge Sort on random data:", measure_time(merge_sort, arr_random[:]))

# Call the performance test function
performance_test()

# Function to measure memory usage
def measure_memory(sort_function, arr):
    process = psutil.Process(os.getpid())
    before_memory = process.memory_info().rss  # Memory usage in bytes before sorting

    sort_function(arr)
    after_memory = process.memory_info().rss  # Memory usage in bytes after sorting
    return (after_memory - before_memory) / 1024  # Convert to KB

# Memory Usage Testing
def memory_test():
    size = 10000
    arr_random = random.sample(range(size), size)

    print(f"\nMemory usage for array of size {size}:")

    # Quick Sort
    print("Quick Sort memory usage (KB):", measure_memory(quick_sort, arr_random[:]))

    # Merge Sort
    print("Merge Sort memory usage (KB):", measure_memory(merge_sort, arr_random[:]))

# Call the memory test function
memory_test()

# Function to measure memory usage
# def measure_memory(sort_function, arr):
#     process = psutil.Process(os.getpid())
#     before_memory = process.memory_info().rss  # Memory usage in bytes before sorting
#     sort_function(arr)
#     after_memory = process.memory_info().rss  # Memory usage in bytes after sorting
#     return (after_memory - before_memory) / 1024  # Convert to KB

# Memory Usage Testing with sorted array
def memory_test_sorted_array():
    size = 10000  # Set size for testing
    arr_sorted = list(range(size))  # Create a sorted array

    print(f"Memory usage for sorted array of size {size}:")

    # Quick Sort memory test
    quick_sort_memory = measure_memory(quick_sort, arr_sorted[:])
    print(f"Quick Sort memory usage (KB): {quick_sort_memory:.3f}")

    # Merge Sort memory test
    merge_sort_memory = measure_memory(merge_sort, arr_sorted[:])
    print(f"Merge Sort memory usage (KB): {merge_sort_memory:.3f}")

# Call the memory test function
memory_test_sorted_array()
