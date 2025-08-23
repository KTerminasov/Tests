# n, k = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

# moods = [-100*n] * (n)

# for i in range(n):
#     for j in range(1, 3):
#         if i - j >= 0:
#             moods[i] = max(moods[i], moods[i - j] + a[i])
#         elif i - j == -1:
#             moods[i] = max(moods[i], a[i])
#     for j in range(max(0, i - k)):
#         moods[i] = max(moods[i], moods[j])

# print(moods[-1])

import sys
data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:2+n]))

NEG_INF = -10**15
dp = [[NEG_INF] * (k+1) for _ in range(n+1)]
max_dp = [NEG_INF] * (k+1)

dp[0][0] = 0
max_dp[0] = 0
for j in range(1, k+1):
    max_dp[j] = NEG_INF

for i in range(1, n+1):
    new_dp_row = [NEG_INF] * (k+1)
    for j in range(0, k+1):
        best = NEG_INF
        # Step from i-1
        if i-1 >= 0 and dp[i-1][j] != NEG_INF:
            candidate = dp[i-1][j] + a[i-1]
            if candidate > best:
                best = candidate
            # Jump from i-2
            if i-2 >= 0 and dp[i-2][j] != NEG_INF:
                candidate = dp[i-2][j] + a[i-1]
                if candidate > best:
                    best = candidate
            # Skip from any previous step
            if j >= 1 and max_dp[j-1] != NEG_INF:
                candidate = max_dp[j-1] + a[i-1]
                if candidate > best:
                    best = candidate
            if best != NEG_INF:
                new_dp_row[j] = best
        dp[i] = new_dp_row
        for j in range(k+1):
            if dp[i][j] > max_dp[j]:
                max_dp[j] = dp[i][j]

    ans = max(dp[n])
    print(ans)
