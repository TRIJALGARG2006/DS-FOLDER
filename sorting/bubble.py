def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to track if a swap happened in this pass
        swapped = False
        
        # Last i elements are already in place, so we ignore them
        for j in range(0, n - i - 1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        # This gives us the O(n) best-case performance
        if not swapped:
            break

# Example usage:
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)

print("Sorted array:")
print(data)