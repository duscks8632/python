def binary_search(arr, tar, start, end):
    # start 인덱스가 end 인덱스를 넘기면 끝남
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == tar:
        return mid
    elif tar < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(arr, tar, start, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소없음")
else:
    print(result + 1)
