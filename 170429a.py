# 文字列 A, B, C が与えられます。これがしりとりになっているか判定してください。
# つまり、
# A の最後の文字と B の最初の文字が同じ
# B の最後の文字と C の最初の文字が同じ
# この 2 つが正しいか判定してください。
# 両方とも正しいならば YES、そうでないならば NO を出力してください。

a = raw_input()

l = a.split(' ')

if l[0][-1] == l[1][0] and l[1][-1] == l[2][0]:
	print "YES"
else:
	print "NO"