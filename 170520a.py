# すぬけ君は、1 から 12 までの整数を下図のようにグループ分けしました。 整数 x, y (1≤x<y≤12) が与えられるので、x, y が同一のグループに属しているか判定してください。

x, y = map(int, raw_input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]

if x in a and y in a or x in b and y in b:
	print "Yes"
else:
	print "No"