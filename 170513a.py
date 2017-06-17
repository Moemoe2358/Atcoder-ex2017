# 3 つの整数 A,B,C が与えられます。
# 整数 C が A 以上 かつ B 以下であるかを判定してください。

a, b, c = map(int, raw_input().split(' '))

if c >= a and c <= b:
	print "Yes"
else:
	print "No"