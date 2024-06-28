people_count = int(input())
scared_numbers = list(map(int, input().split()))
# 리스트를 정렬
scared_numbers.sort()

result = 0 # 총 모험가 그룹 수
count = 0 # 현 그룹에 있는 모험가 수

for i in scared_numbers:
    count += 1 # 현 그룹에 모험가가 추가된다.
    if count >= i: # 현 그룹 모험가수가 현재 공포도보다 크다면 그룹은 완성된 그룹이므로 총 그룹수 + 1를 하고 현 그룹의 모험가수는 0으로 만든다.
        result += 1
        count = 0

print(result)




