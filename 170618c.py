def max_t(l):
	m = 0
	index = 0
	for i in range(len(l)):
		if l[i] > m:
			m = l[i]
			index = i
	return index

n = input()
a, b = [], []
sum_a, sum_b = 0, 0

for i in range(n):
	t1, t2 = map(int, raw_input().split())
	sum_a += t1
	sum_b += t2
	a.append(t1)
	b.append(t2)

average = (sum_a + sum_b) / (n * 2)
count = 0

while sum_a != sum_b:
	if sum_a > sum_b:
		index = max_t(a)
		a[index] -= 1
		b[index] += 1
		sum_a -= 1
		sum_b += 1
	else:
		index = max_t(b)
		a[index] += 1
		b[index] -= 1
		sum_b -= 1
		sum_a += 1
	count += 1

for i in range(len(a) - 1):
	offset = a[i] - average
	a[i + 1] += offset
	count += abs(offset)
	a[i] = average


for i in range(len(b) - 1):
	offset = b[i] - average
	b[i + 1] += offset
	count += abs(offset)
	b[i] = average

print count