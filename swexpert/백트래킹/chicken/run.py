import sys
sys.stdin = open("sample_input.txt", "r")

n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

homes = []
chickens = []
selected_chickens = []
best_min_dist = 9999

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))


# 집마다의 치킨거리
def single_chicken_dist(x, y):  
    min_dist = 9999
    for x2, y2 in selected_chickens:
        dist = abs(x2-x) + abs(y2-y)
        if dist < min_dist:
            min_dist = dist 
    return min_dist

def calc_chicken_dist():
    ans = 0
    for home in homes:
        x, y = home 
        ans += single_chicken_dist(x, y)
    return ans 


def dfs(idx, cnt):
    global best_min_dist
    if idx == len(chickens):
        if cnt == m:
            best_min_dist = min(best_min_dist, calc_chicken_dist())
        return
    
    selected_chickens.append(chickens[idx])
    dfs(idx+1, cnt+1)
    selected_chickens.pop()
    dfs(idx+1, cnt)

dfs(0, 0)
print(best_min_dist)