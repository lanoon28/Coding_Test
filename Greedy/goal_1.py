# n을 받아 1이 될 때 까지 k로 나눠 지면 나누고 아니면 -1  
n, k = map(int, input().split())
count = 0
while 1:
    if n == 1:
        break
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# 다른 답
n, k = map(int, input().split())
count = 0

while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1

while n >1:
    n -= 1
    count += 1

print(count)