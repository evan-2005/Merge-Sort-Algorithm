def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # merge left and right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # maintain stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Input & Output
arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
