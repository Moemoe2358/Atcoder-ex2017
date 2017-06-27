n = input()
x = []
y = []
count = 0

for i in range(n):
	a, b = map(int, raw_input().split())

	for j in range(len(x)):
		flag = False
		if x[j] == a: 
			flag = True
			print 'a'
		if y[j] == b:
			flag = True
			print 'b'
		if abs(x[j] - a) == abs(y[j] - b):
			flag = True
			print 'c'
		if flag:
			# print abs(x[j] - a), abs(y[j] - b)
			count += 1
			# print a, b, x[j], y[j]
	x.append(a)
	y.append(b)

print count