import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    dock = []
    selected = []
    for _ in range(n):
        dock.append(list(map(int, input().split())))
    
    dock.sort(key=lambda x: x[-1])
    
    selected.append(dock[0])
    j = 0

    for i in range(1, n):
        # 검사하는 화물의 시작시간이 현재 화물의 끝시간보다 늦다면:
        if dock[i][0] >= dock[j][1]:
            selected.append(dock[i])
            j = i

    print(f'#{test_case} {len(selected)}')
    # ///////////////////////////////////////////////////////////////////////////////////