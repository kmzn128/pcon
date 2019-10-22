n = 4
w = (2,1,3,2)
v = (3,2,4,2)
W = 5
dp = [[0 for j in range(W+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(W+1):
        if(j < w[i]):
            dp[i+1][j] = dp[i][j]
        else:
            notin = dp[i][j]
            inn = dp[i][j-w[i]]+v[i]
            dp[i+1][j] = max(notin, inn)

print(dp)
    