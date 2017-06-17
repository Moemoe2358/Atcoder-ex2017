# 縦 H ピクセル、横 W ピクセルの画像があります。 各ピクセルは英小文字で表されます。 上から i 番目、左から j 番目のピクセルは aij です。
# この画像の周囲 1 ピクセルを "#" で囲んだものを出力してください。

x, y = map(int, raw_input().split())

print "#" * (y + 2)

for i in range(x):
	a = raw_input()
	print "#" + a + "#"

print "#" * (y + 2)