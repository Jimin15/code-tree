n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

m = 0
for i in range(n):
    for j in range(n):
        c = 0
        if i+2<=n-1 and j+2<=n-1:
            for k in range(i, i+3):
                for l in range(j,j+3):
                    if grid[k][l] == 1:
                        c+=1
            if c>m:
                m = c
print(m)
                
# Please write your code here.
