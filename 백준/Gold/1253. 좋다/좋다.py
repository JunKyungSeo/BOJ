import sys
# sys.stdin.readline().strip()

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
num.sort()
result = 0

for i in range(N):
    idx1 = 0
    idx2 = N-1
    while idx1 < idx2:
        if idx1 == i:
            idx1 += 1
            continue
        if idx2 == i:
            idx2 -= 1
            continue
        if num[idx1] + num[idx2] < num[i]:
            idx1 += 1
        elif num[idx1] + num[idx2] > num[i]:
            idx2 -= 1
        else:
            result += 1
            break
print(result)