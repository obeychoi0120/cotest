import sys

sys.stdin = open("sample_input.txt", "r")

dxs = [1, 0]
dys = [0, 1]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

def dfs(x, y, s):	# s: 초기값 0
    global ans
    
    if s >= ans:
        return	# 가지치기
    
    if x==n-1 and y==n-1:
        ans = s
        return 
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            dfs(nx, ny, s+arr[nx][ny])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ans = 999999
    
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(test_case, ans)) 
    # ///////////////////////////////////////////////////////////////////////////////////
