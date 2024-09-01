def binary_search(array, x, low, high):
    if high >= low:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, x, low, mid - 1)
        else:
            return binary_search(array, x, mid + 1, high)
    else:
        return -1

array = [3, 4, 5, 6, 7, 8, 97]
x = 8
result = binary_search(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index:", result)
else:
    print("Not found")
