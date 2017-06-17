# 縦 H ブロック、横 W ブロックの板チョコがあります。 すぬけ君は、この板チョコをちょうど 3 つのピースに分割しようとしています。 ただし、各ピースはブロックの境目に沿った長方形でなければなりません。
# すぬけ君は、3 つのピースの面積 (ブロック数) をできるだけ均等にしようとしています。 具体的には、3 つのピースの面積の最大値を Smax、最小値を Smin としたとき、Smax−Smin を最小化しようとしています。 Smax−Smin の最小値を求めてください。

x, y = map(int, raw_input().split())

if x % 3 == 0 or y % 3 == 0:
	print 0
else:
	m = 10000000
	for i in range(1, x):
		j = y / 2
		s1 = y * i
		s2 = (x - i) * j
		s3 = (x - i) * (y - j)
		l = [s1, s2, s3]
		l.sort()
		if l[-1] - l[0] < m:
			m = l[-1] - l[0]
	x, y = y, x
	for i in range(1, x):
		j = y / 2
		s1 = y * i
		s2 = (x - i) * j
		s3 = (x - i) * (y - j)
		l = [s1, s2, s3]
		l.sort()
		if l[-1] - l[0] < m:
			m = l[-1] - l[0]
	if m > x:
		m = x
	if m > y:
		m = y
	print m