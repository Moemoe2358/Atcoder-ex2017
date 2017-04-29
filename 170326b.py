# xy 平面があり、その上に N 人の学生がいて、M 個のチェックポイントがあります。
# i 番目の学生がいる座標は (ai,bi)(1≦i≦N) であり、番号 j のチェックポイントの座標は (cj,dj)(1≦j≦M) です。 
# これから合図があり、各学生はマンハッタン距離で一番近いチェックポイントに集合しなければなりません。 
# 2つの地点 (x1,y1) と (x2,y2) 間のマンハッタン距離は |x1−x2|+|y1−y2| で表されます。
# ここで、|x| は x の絶対値を表します。
# ただし、一番近いチェックポイントが複数ある場合には、番号が最も小さいチェックポイントに移動することとします。
# 合図の後に、各学生がどのチェックポイントに移動するかを求めてください。

n, m = map(int, raw_input().split())
lx, ly, lxx, lyy = [], [], [], []
for i in range(n):
	x, y = map(int, raw_input().split())
	lx.append(x)
	ly.append(y)

for i in range(m):
	x, y = map(int, raw_input().split())
	lxx.append(x)
	lyy.append(y)

for i in range(n):
	mi = 10000000000
	note = 0
	for j in range(m):
		if abs(lx[i] - lxx[j]) + abs(ly[i] - lyy[j]) < mi:
			mi = abs(lx[i] - lxx[j]) + abs(ly[i] - lyy[j])
			note = j + 1
	print note