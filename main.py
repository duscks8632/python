array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = pivot + 1
    right = end
    while (left < right):
        while (left < end and left < pivot):
            left += 1
        while (right > start and start > pivot):
            right -= 1
        if (left > right):
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right)
    quick_sort(arr, right, len(arr) - 1)

quick_sort(array, 0, len(array))

print(array)

# 재귀함수 쓸 때 인덱스 값이 좀 어려운 거 같다.