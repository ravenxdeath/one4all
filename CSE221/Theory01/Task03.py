def find_maximum(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid element is the maximum
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]

        # Search in the descending part
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            high = mid - 1

        # Search in the ascending part
        else:
            low = mid + 1

    return None  # No maximum found

# Example usage
arr = [1, 3, 4, 5, 9, 6, 2, -1]
maximum = find_maximum(arr)
print("Maximum number:", maximum)

# b. The time complexity of the algorithm is O(log N) since we divide the search space in half at each 
# step of the binary search. This is significantly less than O(N) for larger arrays, making it an 
# efficient solution for finding the maximum number in the given wave-like sequence.

# The algorithm uses a modified binary search approach to find the maximum number in the wave-like sequence. 
# In each iteration of the binary search, the search space is halved. This means that the algorithm 
# eliminates half of the remaining elements at each step, leading to a logarithmic time complexity.

# Therefore, the time complexity is O(log N