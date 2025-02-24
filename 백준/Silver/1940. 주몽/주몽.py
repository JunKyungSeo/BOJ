import sys
# sys.stdin.readline().strip()

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

ingre = list(map(int, sys.stdin.readline().strip().split()))
ingre.sort()
result = 0

idx1 = 0
idx2 = N-1

while(idx1 < idx2):
    sum = ingre[idx1] + ingre[idx2]
    if sum > M:
        idx2 -= 1
    elif sum < M:
        idx1 += 1
    else:
        result += 1
        idx1 += 1
        idx2 -= 1

print(result)