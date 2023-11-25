def find_minimum(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        # Check if the mid element is greater than the last element
        if arr[mid] > arr[high]:
            low = mid + 1
        # Check if the mid element is less than the last element
        elif arr[mid] < arr[high]:
            high = mid
        # If they are equal, reduce the search range
        else:
            high -= 1

    return arr[low]


# Example array
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Call the function to find the minimum element
result = find_minimum(arr)
print("Minimum element:", result)

#In this example, the input list arr is [9, 8, 7, 6, 5, 4, 3, 2, 1], which follows a wave-like pattern. The function find_minimum is called with arr as the argument, and the returned minimum element is printed.