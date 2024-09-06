def insertion_sort(arr):
    # 두번째 원소부터 끝까지로 설정
    for i in range(1, len(arr)):
        # end은 삽입할 원소이다.
        for end in range(i,0,-1):
            #그래서 end와 end보다 하나 작은 원소를 하나씩 비교한다.
            if arr[end] < arr[end - 1]:
                arr[end], arr[end - 1] = arr[end - 1], arr[end]
            #자기보다 작은 데이터를 만나면 멈춤
            else:
                break

    return arr

arr1 = [7,5,9,0,3,1,6,2,4,8]
print(insertion_sort(arr1))

#변수이름을 잘못지어서 반대로 설정함