N = int(input())

resultlist = list()

for i in range(N):
    n = int(input())
    for i in range(len(resultlist), n+1):
        resultlist.append([0, 0])
        # print(f"i : {i}, len : {len(resultlist)}")
        if i == 0:
            resultlist[i] = [1, 0]
        elif i == 1:
            resultlist[i] = [0, 1]
        else:
            resultlist[i] = [resultlist[i-1][0] + resultlist[i-2][0], resultlist[i-1][1] + resultlist[i-2][1]]
    print(resultlist[n][0], resultlist[n][1])
    # print(resultlist)