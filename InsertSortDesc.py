"""
INSERTION-SORT procedure to sort into monotonically decreasing order.
"""


# fuction that sorts in the decreasing order
def insertion_sort_decreasing(arr):
   
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted (key)
        j = i - 1
        
        # Move elements that are smaller than key, to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at the correct position
        arr[j + 1] = key



##### Test ###
if __name__ == "__main__":
    arrayA = [31, 41, 59, 26, 41, 58]
    print("Original array:", arrayA)
    insertion_sort_decreasing(arrayA)
    print("Sorted array in decreasing order:", arrayA)
