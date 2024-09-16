

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = pivot + 1
    right = end
    # 왼쪽, 오른쪽 인덱스 값이 같을 때까지 바꾸고 엇갈릴때, while문을 나가야하므로 left <= right 로 바꾸어야 한다.
    while (left <= right):
        # left 인덱스가 끝까지 검사를 해줘야 하기에 left <= end로 고쳐야 함
        # 또한, 인덱스 값을 비교하는 게 아니라 arr값을 비교해야 함
        while (left <= end and arr[left] < arr[pivot]):
            left += 1
        # start가 아니라 right여야 함
        # 또한, 인덱스 값을 비교하는 게 아니라 arr값을 비교해야 함
        while (right > start and arr[right] > arr[pivot]):
            right -= 1
        if (left > right):
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # quick_sort에서 right 값이 겹치면 안됨
    # right + 1나 right -1를 해야함.
    quick_sort(arr, start, right)
    quick_sort(arr, right + 1, end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array)-1 )

print(array)
