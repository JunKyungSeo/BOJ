import itertools as it

def dist(a):
    return (a[0]**2 + a[1]**2)**0.5

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

T = int(input())
for testcase in range(T):
    N = int(input())
    P = [tuple(map(int, input().split())) for i in range(N)]
    P_p = list(it.combinations(P, int(N/2)))
    result = list()
    allsum = (sum([i[0] for i in P]), sum([i[1] for i in P]))
    for case in P_p:
        result.append(dist(sub(allsum, (2 * sum([i[0] for i in case]), 2 * sum([i[1] for i in case])))))
    print(min(result))
