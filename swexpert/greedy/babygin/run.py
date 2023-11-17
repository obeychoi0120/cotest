import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def check_run(count):
    for i in range(8):
        if count[i] != 0 and count[i+1] != 0 and count[i+2] != 0:
                return True
    return False
            
def check_triple(count):
    for i in range(10):
        if count[i] >= 3:
            return True 
    return False

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    cards = list(map(int, input().split()))
    count_1 = [0] * 10
    count_2 = [0] * 10

    result = 0

    for i in range(12):
        # card_idx = cards[i]-1 if cards[i] != 0 else 9
        card_idx = cards[i]
        # player 1
        if i % 2 == 0:
            count_1[card_idx] += 1
            if check_run(count_1) or check_triple(count_1):
                result = 1
                break

        # player 2
        else:
            count_2[card_idx] += 1
            if check_run(count_2) or check_triple(count_2):
                result = 2
                break

    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////