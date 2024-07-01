h = int(input())
count = 0

# h는 시간 j는 분, k는 초로 3이 한번이라도 있으면 count + 1이다.
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)

