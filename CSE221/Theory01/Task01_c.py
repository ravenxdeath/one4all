arr = [1, 1, 2, 2, 2, 4, 4, 4, 22, 32, 33, 44, 46, 64, 65]

def binSearcher(arr, target):
    low = 0
    high = len(arr) - 1
    first_index = -1
    count = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            if first_index == -1:
                first_index = mid
            count += 1

            # Continue searching in both halves for duplicates
            left = mid - 1
            right = mid + 1

            while left >= low and arr[left] == target:
                count += 1
                first_index = left
                left -= 1

            while right <= high and arr[right] == target:
                count += 1
                right += 1

            return (first_index, count)

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

result = binSearcher(arr, 4)
print(result)
