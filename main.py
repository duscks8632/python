# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0
while True:
    # 우선 n를 나눌 수 있는 현재 가장 큰 k를 찾는 과정
    target = (n // k) * k
    # 그 다음 n를 k의 가장 큰 배수가 되도록 가공하는 과정
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    # 나눌 거기 때문에 연산횟수를 늘려준다.(result는 연산횟수)
    result += 1
    n //= k
# n이 1이 되기 전까지 일일이 빼야하기 때문에(나누는 과정은 끝남) n - 1 번 만큼 카운트를 시켜준다.
result += (n - 1)
print(result)
