import sys
sys.stdin = open("./sample_input.txt", "r")
def dfs(curr_idx, sum_):
    global result
    # depth가 N이 되면 return
    if curr_idx == N:
        result = min(result, sum_)
        return 
    # 가지치기
    if result <= sum_:
        return 
    
    # 행별로 겹치면 안됨
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(curr_idx+1, sum_+arr[curr_idx][i])
        visited[i] = 0
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 999999999
    dfs(0, 0)
    
    print('#{} {}'.format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////