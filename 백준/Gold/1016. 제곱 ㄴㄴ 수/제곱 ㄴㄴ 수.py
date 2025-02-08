minnum, maxnum = map(int, input().split())
result = maxnum - minnum + 1

marked = [False] * result

for i in range(minnum, maxnum + 1):
    if i % 4 == 0:
        marked[i - minnum] = True

for i in range(3, int(maxnum**0.5) + 1, 2):
    square = i**2
    start = (minnum + square - 1) // square * square
    for j in range(start, maxnum + 1, square):
        marked[j - minnum] = True
result -= sum(marked)
print(result)