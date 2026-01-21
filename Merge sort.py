def merge_sort(arr):
    # Base case: array of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # maintains stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------- Main Program ---------------- #

user_input = input("Enter numbers to sort (space-separated): ").strip()

if not user_input:
    print("Empty input. Exiting.")
    exit()

arr = list(map(int, user_input.split()))
sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)
