# 1316 그룹단어 체커


# 내 풀이
n = int(input())


# 그룹 단어 개수
result = 0

# 현재 연속 되고 있는 알파벳
temp_str = ''

# 확인한 알파벳을 담는 배열
checked_list = []

for i in range(n):
    string = input()
    result += 1
    for alphabet in string:
        if alphabet != temp_str:
            
            # 새로 들어온 알파벳이 확인한 알파벳 배열에 있으면 break
            if alphabet in checked_list:
                result -= 1
                break
            
            # 새로 들어온 알파벳을 비교할 알파벳으로 지정
            temp_str = alphabet

            # 확인한 알파벳 배열에 추가
            checked_list.append(temp_str)

    temp_str = ''
    checked_list = []
print(result)

# 다른 사람 풀이
# sorted 메서드에서 key 를 word.find 로 잡으면, word 에서 찾아지는 character 순서대로 정렬이 됨
# 정렬된 결과물이 list(word)와 같다면 그룹단어라는것

result = 0
for i in range(int(input())):
  word = input()
  result += list(word) == sorted(word. key=word.find)
print(result)

