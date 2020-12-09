"""
각 행에서 가장 작은수들을 다른 행과 비교해서 가장 큰 수를 출력
"""
row, column = map(int, input().split())

result = 0
for _ in range(row):
  temp_list = list(map(int,input().split()))
  if result < min(temp_list):
    result = min(temp_list)
print(result)

# max 를 이용해서 비교해도 됨
