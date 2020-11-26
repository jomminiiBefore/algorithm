# 10809 알파벳 찾기
# ['a','b',...'z'] 로 인덱스 확인할 기준 생성
# 기준을 for 문으로 돌면서 인덱스를 확인하고, 해당 숫자로 대체
# .index()를 이용해서 인덱스 확인하면 안되네, 없으면 value error 뱉음
# .find() 를 통해 확인

"""
문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

예제 입력 1 
baekjoon
예제 출력 1 
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)

string = input()

for i in range(len(alphabet)):
    print(string.find(alphabet[i]), end=' ')