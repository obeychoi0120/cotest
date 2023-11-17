import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    
    # 1. truck당 적재용량을 초과하지 않으면서 가장 무거운 짐을 들게 하기
    result = 0
    
    for i in range(m):
        truck = trucks[i]
        can_lift = True
        for j in range(n):
            load = containers[j]
            if can_lift and load != 0 and load <= truck:
                result += load
                containers[j] = 0
                can_lift = False

    
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
