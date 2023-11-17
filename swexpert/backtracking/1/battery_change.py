import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(idx, cnt):
    global best_cnt
    if cnt >= best_cnt:
        return
    if idx == N:    # 종점에 이르면
        best_cnt = min(best_cnt, cnt)
        return
    
    end_idx = idx + battery[idx-1]
    if end_idx > N:
        end_idx = N
    for i in range(idx+1, end_idx+1):
        dfs(i, cnt+1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lst = list(map(int, input().split()))
    N = lst[0]
    battery = lst[1:]
    best_cnt = 9999
    for i in range(2, battery[0]+2):
        dfs(i, 0)
    print(f'#{test_case} {best_cnt}')
    # ///////////////////////////////////////////////////////////////////////////////////