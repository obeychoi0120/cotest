import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

'''
생각

1. 전선은 상하좌우로 놓을수 있음. -> dxs, dys
2. 벽면에 닿지 않는 코어마다, 가장 가까운 면을 찾음
3. 백트래킹
'''

def in_range(x, y):
    return 1<=x<n-1 and 1<=y<n-1

def check_dir(x, y):
    dir_counts = [0, 0, 0, 0]

    for d in range(4):
        nx, ny = x, y
        l = 0
        while in_range(nx, ny):
            nx += dxs[d]
            ny += dys[d]
            l += 1
            if arr[nx][ny] != 0:
                break
        else:
            dir_counts[d] = l

    return dir_counts

def draw_line(x, y, d):

    nx, ny = x, y
    while in_range(nx, ny):
        nx += dxs[d]
        ny += dys[d]
        arr[nx][ny] = 1

def erase_line(x, y, d):
    nx, ny = x, y
    while in_range(nx, ny):
        nx += dxs[d]
        ny += dys[d]
        arr[nx][ny] = 0

# k: 탐색 depth, n: 전원 연결한 코어 수, l: 전선 길이
def dfs(k, core_n, line_len):
    global result

    # 코어 연결된 개수가 더 많으면 바꿔줌
    if core_n > result[0]:
        result[0] = core_n
        result[1] = line_len

    # 연결된 개수가 같을 경우, 전선 길이가 더 작은 놈으로
    elif core_n == result[0]:
        if line_len < result[1]:
            result[1] = line_len

    # 더 연결할 수 없을 경우, 종료
    if k == core_cnt:
        return
    
    x, y = core_pos[k]

    dir_counts = check_dir(x, y)

    for d in range(4):
        if dir_counts[d] == 0:
            continue
        
        draw_line(x, y, d)
        dfs(k+1, core_n+1, line_len+dir_counts[d])
        # draw_line(x, y, d)
        erase_line(x, y, d)
    
    dfs(k+1, core_n, line_len)  # 선을 연결하지 않고 다음으로


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core_cnt = 0
    core_pos = []

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                core_pos.append((i, j))
                core_cnt += 1
    
    result = [0, 0] # 연결한 코어 개수, 연결한 길이

    dfs(0, 0, 0)
    print(f'#{tc} {result[1]}')
    # ///////////////////////////////////////////////////////////////////////////////////