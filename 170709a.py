def ncr(n, r):
	s = 1
	for i in range(n - r + 1, n + 1):
		s = s * i / (i - (n - r))
	return s

a, b = map(int, raw_input().split())
l = map(int, raw_input().split())

c1 = len([i for i in l if i % 2 == 1])
c2 = len([i for i in l if i % 2 == 0])
s1 = 0
s2 = 0

for i in range(c1 + 1):
	if i % 2 == 0:
		s2 += ncr(c1, i)
	else:
		s1 += ncr(c1, i)

s3 = 2 ** c2

if b == 1:
	print s1 * s3
else:
	print s2 * s3