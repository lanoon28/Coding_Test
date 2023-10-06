#가장 적은 동전 수 구하기
def changeMoney(x):
    coin_list = [500, 100, 50, 10]
    count = 0
    for coin in coin_list:
        count += x // coin
        x %= coin
    return count

print(changeMoney(1260))

#시간 복잡도 O(k)