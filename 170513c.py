# 空の配列が 1 つあります。 
# この配列に、整数を配列に挿入する操作を N 回行います。 
# i(1≦i≦N) 回目の操作では、配列に整数 ai を bi 個挿入します。 
# N 回の挿入操作後の配列の中で、K 番目に小さい数を求めてください。 
# 例えば、配列が {1,2,2,3,3,3} の時、4 番目に小さい数は 3 となります。

n, k = map(int, raw_input().split(' '))
d = {}

for i in range(n):
	a, b = map(int, raw_input().split(' '))
	if d.has_key(a):
		d[a] += b
	else:
		d[a] = b

l = d.keys()
l.sort()

s = 0
for i in l:
	s += d[i]
	if s >= k:
		print i
		break


