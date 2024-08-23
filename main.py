def insert_sort(arr):
    # 삽입할 놈을 선택
    for i in range(len(arr)):
        min_index = i
        #중괄호 안에서 젤 작은 놈 찾기
        for j in range(i+1, len(arr)):
            #중괄호 안에서 젤 작은 놈이 나오면 업데이트
            if arr[j] < arr[min_index]:
                min_index = j
        # 이러면 min_index는 젤 작은 값을 가진 인덱스가 된다. 그때 순서 바꾸기
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr1 = [7,5,9,0,3,1,6,2,4,8]

print(insert_sort(arr1))