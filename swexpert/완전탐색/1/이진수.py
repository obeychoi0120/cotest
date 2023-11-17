
import sys
sys.stdin = open("sample_input.txt", "r")

convert_map = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

def convert(s):
    ans = ''
    result = [0,0,0,0]
    if s in ['A', 'B', 'C', 'D', 'E', 'F']:
        s = convert_map[s]
    else:
        s = int(s)

    if s >= 8:
        result[0]=1
        s -= 8
        if s>=4:
            result[1]=1
            s-=4
            if s>=2:
                result[2]=1
                s-=2
                result[3]=s
    elif s>=4:
        result[1]=1
        s-=4
        if s>=2:
            result[2]=1
            s-=2
            result[3]=s

    elif s>=2:
        result[2]=1
        s-=2
        result[3]=s

    else:
        result[3]=s
    
    for r in result:
        ans = ans + str(r)
    return ans

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    result = ''
    N, string = input().split(' ')
    string = list(string)
    for s in string:
        ans = convert(s)
        result = result + ans
    print(result)
    # ///////////////////////////////////////////////////////////////////////////////////