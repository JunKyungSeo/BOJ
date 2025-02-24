import sys
#from queue import PriorityQueue
# from collections import deque
# sys.stdin.readline().strip()

N = int(sys.stdin.readline().strip())

# using two pointer
a = 1
b = 2
sum = a + b
result = 0
while(a <= b):
    if sum < N:
        b += 1
        sum += b
    elif sum > N:
        sum -= a
        a += 1
    else:
        result += 1
        sum -= a
        a += 1
if N == 1:
    result = 1
print(result)