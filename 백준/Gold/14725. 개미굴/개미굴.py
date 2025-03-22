import sys
# sys.stdin.readline().strip()

def mkt(parent, child): # make tree
    if len(child) == 1:
        parent[child[0]] = dict()
        return parent
    if child[0] not in parent.keys():
        parent[child[0]] = dict()
    parent[child[0]] = mkt(parent[child[0]], child[1:])
    return parent

def prt(tree, cnt): # print tree
    pre_cnt = cnt
    if len(tree) == 0:
        return
    key_list = list(tree.keys())
    key_list.sort()
    for key in key_list:
        print("--"*cnt, end="")
        print(key)
        if len(tree[key]) > 0:
            cnt += 1
        prt(tree[key], cnt)
        cnt = pre_cnt

N = int(sys.stdin.readline().strip())
root = dict()
for rpt in range(N):
    sent = sys.stdin.readline().strip().split()[1:]
    root = mkt(root, sent)
# print(root)
prt(root, 0)