import sys
sys.stdin = open("sample_input.txt", "r")

n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
viruses = []
selected_viruses = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i, j))

def all_infected():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                return False 
    return True 

def in_range(x, y):
    return 0<=x<n and 0<=y<n


def simulate():

    for x, y in selected_viruses:
        infect(x, y)
    
    for i in range(n):
        for j in range(n):
            if 
        

