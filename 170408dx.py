# 2 次元平面上に x 軸と平行な直線が m 本と y 軸と平行な直線が n 本引いてあります。 x 軸と平行な直線のうち下から i 番目は y=yi で表せます。 y 軸と平行な直線のうち左から i 番目は x=xi で表せます。
# この中に存在しているすべての長方形についてその面積を求め、 合計を 109+7 で割ったあまりを出力してください。
# つまり、1≤i<j≤n と 1≤k<l≤m を満たすすべての組 (i,j,k,l) について、 直線 x=xi, x=xj, y=yk, y=yl で囲まれる 長方形の面積を求め、合計を 109+7 で割ったあまりを出力してください。

a, b = map(int, raw_input().split())
p = (a - 1) * (b - 1)

la = map(int, raw_input().split())
lb = map(int, raw_input().split())
s = 0

for i in range(a - 1):
	for j in range(b - 1):
		s += (lb[j + 1] - lb[j]) * (la[i + 1] - la[i]) * p

print s