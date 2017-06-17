# あなたが散歩していると、突然 N 体の魔物が出現しました。それぞれの魔物は 体力 という値を持ち、i 体目の魔物の出現時の体力は hi です。体力が 0 以下となった魔物は直ちに消滅します。
# 幸い、あなたは熟練の魔法使いであり、爆発を引き起こして魔物を攻撃できます。一回の爆発では、以下のように魔物の体力を減らすことができます。
# 生存している魔物を一体選び、その魔物を中心に爆発を引き起こす。爆発の中心となる魔物の体力は A 減り、その他の魔物の体力はそれぞれ B 減る。ここで、A と B はあらかじめ定まった値であり、A>B である。
# すべての魔物を消し去るためには、最小で何回の爆発を引き起こす必要があるでしょうか？

import numpy as np

n, a, b = map(int, raw_input().split())
l = []

for i in range(n):
	l.append(input())
ll = np.array(l)
ll.sort()
ll = ll[::-1]

def solve(hp, count):
	q = hp - b * count
	p = (q - 1) / (a - b) + 1
	p = p[p > 0]
	if p.sum() <= count:
		return True
	else:
		return False

l = 0
r = ll[0] / b + 1
while r - l > 1:
	m = (l + r) / 2
	if solve(ll, m):
		r = m
	else:
		l = m

print r