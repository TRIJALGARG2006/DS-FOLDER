def binary_search(arr, key, low, high):
    if low > high:
        return -1 # Base case: not found
    
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(sorted_arr, target, 0, len(sorted_arr) - 1)
print(f"Element {target} found at index: {result}")