import sys
sys.stdin = open("sample_input.txt", "r")

# k: 방문 횟수, curr_idx: 현재 위치
def dfs(k, curr_idx, curr_sum):
    global min_sum
    
    if curr_sum >= min_sum:
        return
    
    if k == n-1:
        min_sum = min(min_sum, curr_sum+arr[curr_idx][0])
        return
    
    # (1, 2, 3....n-1)의 도착지점 비교
    for next_idx in range(1, n):
        if  visited[next_idx]==0 and arr[curr_idx][next_idx] != 0:
            visited[next_idx] = 1
            dfs(k+1, next_idx, curr_sum+arr[curr_idx][next_idx])
            visited[next_idx] = 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [0 for _ in range(n)] 
    min_sum = 9999
    
    dfs(0, 0, 0)
    print(f'#{test_case} {min_sum}')
    # ///////////////////////////////////////////////////////////////////////////////////
