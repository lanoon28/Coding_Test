#n 개의 수를 입력 받아 가장 큰 수로 m번의 합을 구하되 k번의 반복 이상 하지 말 것
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
sum = 0

if len(num_list) != n:
    print('false')

num_list.sort()

max_num = num_list[-1]
max_second_num = num_list[-2]

while 1:
    for i in range(k):
        if m == 0:
            break
        sum += max_num
        m -= 1
    if m == 0:
        break
    sum += max_second_num
    m -= 1
print(sum)

# 다른 답
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

max_num = num_list[-1]
max_second_num = num_list[-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

sum = 0
sum += count * max_num
sum += (m - count) * max_second_num

print(sum)