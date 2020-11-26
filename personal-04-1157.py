# 1157 단어 공부
"""
단어 공부 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	75638	28937	23442	38.671%
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A
"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 대문자로 변환
string = input().upper()

count_dict = {}
for i in alphabet:
    count_dict[i] = string.count(i)
aligned_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

if aligned_list[0][1] == aligned_list[1][1]:
    print('?')
else:
    print(aligned_list[0][0])

# 다른 사람 풀이
# 알파벳을 아스키 표기로 바꾸고, 숫자를 세서 해당 위치에 배치시킨 리스트를 만든 다음
# 최대 숫자의 인덱스를 출력함

s,a=input().lower(),[]
for i in range(97,123):
 a.append(s.count(chr(i)))
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())