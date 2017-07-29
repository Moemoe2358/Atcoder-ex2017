# 長さ n の数列 a1,…,an が与えられます。 空の数列 b に対して、以下の操作を n 回行うことを考えます。
# i 回目には
# 数列の i 番目の要素 ai を b の末尾に追加する。
# b を逆向きに並び替える。
# この操作をしてできる数列 b を求めて下さい。

a = input()
s = map(int, raw_input().split())

l1 = []
l2 = []

if a % 2 == 0:
	for i in range(a):
		if i % 2 == 1:
			l2.append(s[i])
		else:
			l1.append(s[i])
else:
	for i in range(a):
		if i % 2 == 0:
			l2.append(s[i])
		else:
			l1.append(s[i])

for i in reversed(l2):
	print i,

for i in l1:
	print i,