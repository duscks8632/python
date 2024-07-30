def merge_sort(arr):
    #원소가 1개 일때 그 자체 리스트를 리턴하고 그걸 추후에 상위 머지소트의 리턴값으로 받는다
    # 예시 merge_sort([3,1])의 경우 low_arr는 merge_sort[3]과 high_arr는 merge_sort[1]로 할당함 각각의 머지소트는 원소가 하나면
    # 각각 3과 1로 리턴하며 low_arr는 3 high_arr는 1이다.
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    # 중간을 기준으로 낮은쪽, 높은쪽 배열로 나눈다
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merge_arr = []
    # 낮은쪽, 높은쪽으로 쪼개진 배열의 원소를 l, h라고 한다.
    l = h = 0
    # 각각의 배열에서 원소를 뽑아 크기를 비교해서 작은 쪽을 머지리스트에 추가하고 추가된 배열의 원소 인덱스도 +1한다.
    # 이 반복은 low_arr의 길이가 원소 크기보다 작을 때까지만 반복한다.
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    # 크기 비교후 남은 값을 머지에 추가한다.
    merge_arr += (low_arr[l:])
    merge_arr += (high_arr[h:])

    return merge_arr

print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))
