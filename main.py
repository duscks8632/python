# 동전 갯수가 가장 적은 경우의 수
n = 1260
count = 0
# 항상 큰 단위가 작은 단위의 배수이므로 그리디로 최적의 해를 구할 수 있음
# 예시로 500은 100,50,10의 배수, 100은 50,10의 배수, 50은 10의 배수
kind_of_coin = [500, 100, 50, 10]

for coin in kind_of_coin:
    count += n // coin
    n %= coin

print(count)
