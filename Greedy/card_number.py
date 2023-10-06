# m개의 요소를 가진 n개의 행에서 최소의 수를 찾아 그 값 중 최대의 값을 구하기 
n, m = map(int, input().split())

answer = 0

for i in range(n):
    num_list = list(map(int, input().split()))
    min_num = min(num_list)
    answer = max(answer,min_num)

print(answer)

# 다른 답
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for k in range(data):
        min_value = min(min_value, k)
    result = max(result, min_value)

print(result)