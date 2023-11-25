arr = ([1, 2, 4, 2, 4, 65, 1, 22, 33, 32, 44, 64, 46]) 
#############[1, 1, 2, 2, 4, 4, 22, 32, 33, 44, 46, 64, 65] # mid =22

def binSearcher(arr, val):  #val = 33 
    low = 0 
    high = len(arr)-1
    
    while low <= high: 
        mid = (low + high) // 2
        
        if arr[mid] == val:
            return mid
        elif val > arr[mid]: # low becomes the new elem of mid cause we discard the left side
            low = mid + 1
        else:
            high = mid -1 # high becomes the previous elem of mid cause we discard the right side
        
    return False # -(low + 1) # search val not found --> return the negative index


result = binSearcher(sorted(arr), 69)
print(result)