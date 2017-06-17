# N 個の都市があり、M 本の道路があります。
# i(1≦i≦M) 番目の道路は、都市 ai と 都市 bi (1≦ai,bi≦N) を双方向に結んでいます。 
# 同じ 2 つの都市を結ぶ道路は、1 本とは限りません。 
# 各都市から他の都市に向けて、何本の道路が伸びているか求めてください。

n, m = map(int, raw_input().split(' '))
d = {}

for i in range(m):
	a, b = map(int, raw_input().split(' '))
	if d.has_key(a):
		d[a] += 1
	else:
		d[a] = 1
	if d.has_key(b):
		d[b] += 1
	else:
		d[b] = 1

for i in range(1, n + 1):
	if d.has_key(i):
		print d[i]
	else:
		print 0