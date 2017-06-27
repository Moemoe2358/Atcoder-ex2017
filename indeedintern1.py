n,k,m = map(int,raw_input().split())

pp = k*(m-1)+1

i=1
while i<pp :
	string = raw_input()
	i+=1

while i<=n and i-pp<k :
	string = raw_input()
	print(string)
	i+=1

while i<=n :
	string = raw_input()
	i+=1
