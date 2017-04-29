# N 個の品物が与えられます。
# i 番目の品物の価値は vi(1≦i≦N) です。
# これらの品物から、A 個以上、B 個以下を選ばなければなりません。
# この制約下において、選んだ品物の価値の平均の最大値を求めてください。
# また、選んだ品物の平均が最大となるような品物の選び方が何通りあるかを求めてください。

def combb(a, b):
	s1, s2 = 1, 1
	for i in range(a - b + 1, a + 1):
		s1 *= i
	for i in range(1, b + 1):
		s2 *= i
	return s1 / s2


n, a, b = map(int, raw_input().split())
l = map(int, raw_input().split())

l.sort(reverse = True)
s = 0

for i in range(a):
	s += l[i]

s = float(s) / a
print s

q = l[i]
c, d = 0, 0

for i in range(n):
	if (i < a) and (l[i] == q):
		c += 1
	if (i >= a) and (l[i] == q):
		d += 1

e = c + d

if q < s:
	print combb(e, c)
else:
	ss = 0
	for i in range(a, b + 1):
		ss += combb(e, i)
	print ss