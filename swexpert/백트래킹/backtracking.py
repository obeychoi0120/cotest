from collections import deque

def do_something(comb):
    pass

M = 3
some_list = [1, 2, 3, 4]

# k는 depth
def dfs(comb, k):
    if len(comb) == M:  # 종료 조건 1: M개를 모두 선택했을 때
        do_something(comb)
        return
    
    if k == len(some_list): # 종료 조건 2: 리스트의 마지막까지 탐색했을 때
        return 
    
    # 현재 depth의 값 포함하여 재귀 호출
    comb.append(some_list[k])
    dfs(comb, k+1)

    # 현재 depth의 값 미포함하여 재귀 호출
    comb.pop()
    dfs(comb, k+1)

dfs([], 0)
    