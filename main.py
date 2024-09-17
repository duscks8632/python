def quick_sort(arr):
    # 배열이 1보다 작으면 현재 배열 리턴하면서 끝내기
    if len(arr) <= 1:
        return arr
    # 피벗값은 맨 앞 값, tail를 피벗을 제외한 값
    pivot = arr[0]
    tail = arr[1:]
    # 리스트 컴프리헨션을 통해 tail에 속해있는 애들 중 피벗값보다 작으면 left_side 크면 right_side이다.
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    # 그렇게 선별한 배열들을 재귀함수를 호출하고 피벗값은 그들 중간에 위치시키게 배열을 조정한다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

arr1 = [3, 6 ,7, 1, 3, 4, 4, 4, 8]
print(quick_sort(arr1))
