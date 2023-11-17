from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]

arr = []

def do_something():
    pass

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if in_range(nx, ny) and arr[nx][ny] == 0 and not visited[nx][ny]:
                do_something()
                visited[nx][ny] = 1
                q.append((nx, ny))


