input_data = input()
result_list = []
value = 0

#알파벳과 숫자가 합쳐진 문자열을 한 번에 받은 후 하나하나 비교
for input in input_data:
    # 현 문자가 알파벳인가 검사
    if input.isalpha() == True:
        result_list += input
    # 숫자면 value에 누적
    else:
        value += int(input)

# 알파벳 리스트들을 순서대로
result_list.sort()
# 맨 처음 input()로 문자열을 받을 때, 숫자가 없어서 value에 추가할게 없지 않다면 알파벳 리스트에 숫자를 추가할 것
if value != 0:
    result_list.append(str(value))

# 공백없이 문자열 출력
print(''.join(result_list))
print('test')





