arr = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # while문에 ()를 하는 게 안전한듯?
    while(left <= right):
        # 왼쪽 인덱스가 마지막 인덱스보다 작아야 한다.
        # 같아도 된다. 왼쪽 인덱스는 끝까지 가도 된다.
        while(left <= end and arr[left] > arr[pivot]):
            left += 1
        # right가 start 보단 커야한다.
        while(right > start and arr[right] < arr[pivot]):
        # 얜 점점 작아져야 한다.
            right -= 1
        if(left > right):
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 후 왼쪽(right가 중간 인덱스 값임)
    # pivot의 값이 중간으로 갔을 뿐 인덱스는 그대로이기 때문
    quick_sort(arr,start, right-1)
    quick_sort(arr,right + 1, end)

quick_sort(arr,0, len(arr) - 1)

print(arr)




