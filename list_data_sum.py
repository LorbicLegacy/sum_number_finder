a1 = list(range(0,5))
a2 = list(range(10,15))
num = 12
sum_numi = []
sum_numj = []
min_list = []
for i in a1:
	for j in a2:
		if i+j == num:
			sum_numi.append(i)
			sum_numj.append(j)
			
