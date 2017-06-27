n,l = map(int,raw_input().split())

nums = map(int,raw_input().split())

import numpy as np 
nums = np.array(nums)

label = nums[0:l].argmax()
maxnum = nums[label]
print maxnum

for i in range(1,n-l+1):
	j = i+l-1
	if label<i :
		label = nums[i:i+l].argmax()
		maxnum = nums[i+label]
	else :
		if nums[j]>maxnum :
			label = j
			maxnum = nums[j]
	print maxnum


	
