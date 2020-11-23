# 2562 최댓값

"""

문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

예제 입력 1 
3
29
38
12
57
74
40
85
61
예제 출력 1 
85
8
"""
# 2562 최댓값

#1 매번 확인
maxNum = 1
maxOrder = 1

for i in range(1,10):
    n = int(input())
    if n > maxNum:
        maxNum = n
        maxOrder = i
print(maxNum)
print(maxOrder)

#2 list 로 모은다음에 sorted 로 정렬

li = []
for i in range(1,10):
    li.append((int(input()), i))
sorted_li = sorted(li, key=lambda number: number[0])
print(sorted_li[-1][0])
print(sorted_li[-1][1])


# 다른 사람 풀이
# 최댓값을 구한 다음, 해당 값의 인덱스를 구함
l = [int(input()) for i in range(9)]
print(max(l), l.index(max(l))+1)