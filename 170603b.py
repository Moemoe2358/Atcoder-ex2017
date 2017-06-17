# 英小文字からなる文字列 S が与えられます。S に含まれる文字がすべて異なるか判定してください。

a = raw_input()
d = []
ok = True

for i in a:
	if i in d:
		ok = False
		break
	else:
		d.append(i)

if ok:
	print "yes"
else:
	print "no"