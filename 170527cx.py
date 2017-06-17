# ぬすけ君は、N×M のグリッドを持っています。行には上から順に 1 から N、列には左から順に 1 から M の番号がついています。 グリッドの各マスは白か青かに塗られており、Si,j が 1 のとき i 行 j 列のマスは青マス、0 のとき白マスです。 青く塗られた任意の二つのマス a,b について、a からはじめて、現在いるマスから辺を共有する青いマスに進むことを繰り返して b に至るような経路のうち、同じマスを 2 度以上通らないようなものは、高々 1 通りです。
# ぬすけ君の永遠のライバルである怪盗スヌークは、ぬすけ君に Q 個の質問をしました。i 個目の質問は、4 つの整数 xi,1,yi,1,xi,2,yi,2 からなり、 グリッドの xi,1 行目から xi,2 行目まで、yi,1 列目から yi,2 列目までの範囲の長方形領域を切り出したときに、 その範囲の青マスからなる連結成分がいくつあるかを答える質問です。
# 怪盗スヌークの質問すべてに答えてください。

import numpy as np

def search(xt, yt, a):
	if a[xt, yt] == '1':
		a[xt, yt] = '2'
		search(xt - 1, yt, a)
		search(xt + 1, yt, a)
		search(xt, yt - 1, a)
		search(xt, yt + 1, a)

n, m, q = map(int, raw_input().split())

arr = []

for i in range(n):
	s = raw_input()
	arr.append(list(s))

arr_np = np.array(arr)

for i in range(q):
	y1, x1, y2, x2 = map(int, raw_input().split())
	arr_temp = arr_np[y1 - 1:y2, x1 - 1:x2]

	a = np.array(['0'] * (x2 - x1 + 1))
	arr_temp = np.vstack((a, arr_temp))
	arr_temp = np.vstack((arr_temp, a))

	b = np.array(['0'] * (y2 - y1 + 3))
	arr_temp = np.column_stack([b, arr_temp])
	arr_temp = np.column_stack([arr_temp, b])
	p = np.where(arr_temp == '1')
	s = 0
	while len(p[0]) >= 1:
		search(p[0][0], p[1][0], arr_temp)
		s += 1
		p = np.where(arr_temp == '1')

	print s

