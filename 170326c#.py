# 整数 N が与えられます。 
# ここで、2 つの正の整数 A,B に対して、F(A,B) を「10 進表記における、A の桁数と B の桁数のうち大きい方」と定義します。 
# 例えば、F(3,11) の値は、3 は 1 桁、11 は 2 桁であるため、F(3,11)=2 となります。 
# 2 つの正の整数の組 (A,B) が N=A×B を満たすように動くとき、F(A,B) の最小値を求めてください。

import math

a = input()
b = int(math.sqrt(a)) + 1
c = 1
mi = 100

for i in range(1, b):
	if a % i == 0:
		d = a / i
	if max(len(str(i)), len(str(d))) < mi:
		mi = max(len(str(i)), len(str(d)))

print mi