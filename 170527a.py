# すぬけ君は、整数を N 個持っています。このうち最小のものは A、最大のものは B です。すぬけ君が持っている整数の総和としてありうる値は何通りあるでしょうか。

n, a, b = map(int, raw_input().split())

if b - a > 1 and n == 1:
	print 0
elif b < a:
	print 0
else:
	print b * (n - 1) + a - (a * (n - 1) + b) + 1