n, q = map(int, raw_input().split())

a = 1
r = 0

while a < n:
	a *= 2
	r += 1
m = r * q + 1

for i in range(r):
	robot_number = 2 **i 
	time_needed = (n - 1) / robot_number + 1
	m = min(time_needed + i * q, m)

print m 