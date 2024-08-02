def insertion_sort(arr):
    for end in range(1, len(arr)):
        for cur in range(end, 0, -1):
            if arr[cur] < arr[cur - 1]:
                arr[cur], arr[cur - 1] = arr[cur - 1], arr[cur]
    return arr

print(insertion_sort([8,2,4,9,3,6]))