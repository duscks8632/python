arr1 = [5,7,9,0,3,1,6,2,4,8]
# 파라미터를 arr로만 함
def quick_sort(arr):
    # 재귀하다가 원소가 하나면 그대로 반환
    if len(arr) < 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    # 피벗보다 작은 경우 왼쪽
    left_arr = [x for x in tail if x <= pivot]
    # 피벗보다 큰 경우 오른쪽
    right_arr = [x for x in tail if x > pivot]
    # 각 조건에 맞는 것들을 재귀시키고 가운데에 pivot 넣기(리스트로 처리해서)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

print(quick_sort(arr1))