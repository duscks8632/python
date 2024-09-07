def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left_idx = start + 1
    right_idx = end
    while left_idx < right_idx:
        while arr[pivot] < arr[left_idx] and left_idx < end:
            left_idx += 1
        while arr[pivot] > arr[right_idx] and right_idx > start:
            right_idx -= 1

        arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

    arr[right_idx], arr[pivot] = arr[right_idx], arr[pivot]

    quick_sort(arr,start, pivot)
    quick_sort(arr,pivot+1,end)

arr1 = [5,7,9,0,3,1,6,2,4,8]
print(quick_sort(arr1, 0, len(arr1)))



