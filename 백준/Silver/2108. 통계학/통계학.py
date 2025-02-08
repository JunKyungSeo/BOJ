import sys
N = int(input())
nums = list(map(int, sys.stdin.read().split()))
nums.sort()
def round(num):
    if num >= 0:
        return int(num) if num % 1 < 0.5 else int(num) + 1
    else:
        return int(num) if num % 1 >= 0.5 or num % 1 == 0 else int(num) - 1

print(round(sum(nums) / N))
print(nums[int(N/2)])
counts = dict()
for i in nums:
    if  i in counts.keys():
        counts[i] += 1
    else:
        counts[i] = 1
maxval = max(counts.values())
maxnum = [i[0] for i in counts.items() if i[1] == maxval]
print(maxnum[1] if len(maxnum) > 1 else maxnum[0])
print(nums[-1]-nums[0])