map_size = int(input())
move = input().split()

x,y = 1, 1

mx = [0, 0, 1, -1]
my = [-1, 1, 0, 0]
m = ['D', 'U', 'R', 'L']

for mo in move:
    for k in range(len(m)):
        if mo == m[k]:
            x += mx[k]
            y += my[k]
    
    if x>map_size or y>map_size or x<1 or y<1:
        continue
    