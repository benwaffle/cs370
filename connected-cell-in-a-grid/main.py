import sys, operator

rows = int(input())
cols = int(input())

grid = [[0] * cols for _ in range(rows)]
region = [[-1] * cols for _ in range(rows)]

regionChar = {}

for r in range(rows):
    for c, val in enumerate(map(int, input().split())):
        grid[r][c] = val

def search(x, y, t, depth=0):
    if region[x][y] != -1:
        return
    region[x][y] = t
    regionChar[t] = grid[x][y]
    for r in range(-1, 2):
        for c in range(-1, 2):
            if x+r >= 0 and x+r < rows and y+c >= 0 and y+c < cols and not (r == 0 and c == 0):
                if grid[x][y] == grid[r+x][c+y]:
                    search(r+x, c+y, t, depth+1)

t = 0 # fresh
for r in range(rows):
    for c in range(cols):
        search(r, c, t)
        t += 1

count = {}
for row in region:
    for col in row:
        if col in count:
            count[col] += 1
        else:
            count[col] = 1

counts = list(zip(count, count.values()))
counts.sort(key = lambda a: -a[1])
for (region, count) in counts:
    if regionChar[region] != 0:
        print(count)
        break
