data = input()
# 초기 누적값을 result로
result = int(data[0])

# 왼쪽부터 차례로 하나씩 연산실행 ( 더하기 먼저 안함 )
for i in range(1, len(data)):
    # 각자리 숫자는 num으로 세팅
    num = int(data[i])
    # 둘 중 하나라도 0이거나 1 이면 더하기
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)

