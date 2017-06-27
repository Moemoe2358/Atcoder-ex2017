n,m = map(int,raw_input().split())

using = [(0,0)]

for i in range(m):
	a,b = map(int,raw_input().split())
	using.append((a,b))

q = input()

for i in range(q):
	c,d =map(int,raw_input().split())
	success = True
	for used in using:
		if c>used[1] or d<used[0] :
			pass
		else:
			success = False
		if not(success): 
			break
	if success :
		print("OK")
		using.append((c,d))
	else:
		print("NG")


