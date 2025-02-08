K, N = map(int, input().split())
lanlen = [int(input()) for i in range(K)]
lanlen.sort()
start = 1
end = sum(lanlen) // N + 1
mid = int((start + end) / 2)
while (start < mid):
    mid = int((start + end) / 2)
    if (sum([i // mid for i in lanlen]) >= N):
        start = mid
    else:
        end = mid
    mid = int((start + end) / 2)
print(mid)