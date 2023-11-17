import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

'''
1. 오토플레이 -> while문 안에서 동작
2. 크기가 가장 큰 블록 찾기 -> 가능한 블록 그룹의 경우를 모두 구한 후, 내림차순 sorting
    - 블록크기, 무지개크기, 블록 좌표 필요
    - 무지개 블록의 경우 방문체크 해제 
3. 블록 그룹 제거 -> bfs로 카운트 + 점수 더하기
4. 중력
5. 반시계 방향으로 90도 회전
6. 중력

검은색 - -1, 무지개 - 0, 일반 - M이하 자연수

'''
### 입력
n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)] 


def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(x, y, color):
    q = deque()
    q.append((x, y))

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [(x, y)], []

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            # 일반 블록
            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == color:
                visited[nx][ny] = 1
                q.append((nx, ny))
                block_cnt += 1
                blocks.append([nx, ny])

            # 무지개 블록
            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개 블록 방문체크 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return block_cnt, rainbow_cnt, blocks+rainbows

def remove(block_pos):
    for x, y in block_pos:
        arr[x][y] = -2

def gravity():
    # 밑에서부터 체크
    for i in range(n-2, -1, -1):
        for j in range(n):
            # 만약 -1이 아니면 아래로 떨어뜨림
            if arr[i][j] >-1:
                r = i

                while True:
                    # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                    if 0<=r+1<n and arr[r+1][j] == -2:
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break

# 90도 반시계 회전
def rotate90_counterclockwise(arr):
    new_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[n-1-j][i] = arr[i][j]

    return new_arr

# 90도 시계 회전
def rotate90_clockwise(arr):
    new_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[n-1-j][i]
    return new_arr

# # ver.2
# arr = list(zip(*arr))[::-1]
# arr = [list(s) for s in arr]

# 시뮬레이션
score = 0

# 1. 오토플레이 
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    blocks = [] # 가능한 블록 그룹들 넣을 리스트
    
    # 2. 크기가 가장 큰 블록 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_cnt, rainbow_cnt, block_pos = bfs(i, j, arr[i][j])
                # 블록 크기, 무지개블록 크기, 블록 좌표
                if block_cnt >= 2:
                    blocks.append([block_cnt, rainbow_cnt, block_pos])
    
    blocks.sort(reverse=True)

    # 3. 블록제거 + 점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += (blocks[0][0] ** 2)

    # 4. 중력
    gravity()

    # 5. 90도회전
    arr = rotate90_counterclockwise(arr)

    # 6. 중력
    gravity()

print(score)