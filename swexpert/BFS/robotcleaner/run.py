import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")
# T = int(input())

# 북, 동, 남, 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

### 시뮬레이션

# 시작지 방문 체크

visited[x][y] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d + 4 - 1) % 4
        nx = x + dxs[d]
        ny = y + dys[d]

        if in_range(nx, ny) and arr[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x, y = nx, ny 
                flag = 1
                break
    
    if flag == 0:
        if arr[x-dxs[d]][y-dys[d]] == 1:
            print(cnt)
            break
        else:
            x, y = x-dxs[d], y-dys[d]