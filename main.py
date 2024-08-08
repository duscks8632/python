arr1 = [5,7,9,0,3,1,6,2,4,8]
# 파라미터를 arr로만 함
def quick_sort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]
    # 여기를 어떻게 표현해야 하지?
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

print(quick_sort(arr1))