# すけぬ君は、N 階建てのビルを建てました。ビルにはエレベーターが 1 基あり、すべての階に止まります。
# すけぬ君は、各階に上下の方向ボタンを設置しましたが、うっかりしていたため、どの階にも上向きか下向きの片方のボタンしかありません。 そのため、どの階からも上か下のどちらかにしか進むことができません。 Si が U のとき i 階には上向きのボタンしかなく、上にしか進めないことを、D のとき下向きのボタンしかなく、 下にしか進めないことを表します。
# ある階から目的の階へと移動したい住民は、仕方がないので必要があれば他の階を経由して目的の階へと向かうことにしました。 全ての階の順序対 (i,j) についての、i 階から j 階へ行くときのエレベーターに乗る回数の最小値の合計を求めてください。

a = raw_input()

l = len(a)

s = l * (l - 1)
for i in range(l):
	if a[i] == "U":
		s += i
	else:
		s += l - i - 1

print s