# あなたは N 個の物と、強度 W のバッグを持っています。 i 個目の物は、重さが wi で価値が vi です。
# あなたは、物のうちいくつかを選び、バッグに入れます。 ただし、選んだ物の重さの和は W 以下でなくてはいけません。
# あなたは、バッグに入れた物の価値の総和を最大化したいです。

n, l = map(int, raw_input().split())
dp = [-1 for j in range(110)]

for i in range(n):
	w, v = map(int, raw_input().split())
	for j in reversed(range(ma)):
		if dp[j] != -1:
			dp[min(ma, j + w)] = max(dp[min(ma, j + w)], dp[j] + v)
	dp[w] = v

dp[0] = 0

for i in reversed(range(l + 1)):
	if dp[i] != -1:
		print dp[i]
		break

print dp