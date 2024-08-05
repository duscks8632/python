A = [0, 5, 9, 7, 4, 1, 6, 2, 4, 8]

for i in range(len(A)):
    #i가 가장 앞 원소의 인덱스
    min_index = i
    # 맨 앞을 제외한 그 다음 배열에서 가장 작은 값의 인덱스를 구한 다음 위치를 i와 바꾼다.
    for j in range(i+1, len(A)):
        if A[j] < A[min_index]:
            min_index = j
        A[i], A[min_index] = A[min_index], A[i]

print(A)