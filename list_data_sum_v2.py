
import matplotlib.pyplot as plt

a1 = list(range(0,5))
a2 = list(range(10,16))
num = 15
sum_numi = []
sum_numj = []
min_list = []
for i in a1:
	for j in a2:
		if i+j == num:
			sum_numi.append(i)
			sum_numj.append(j)
data = zip(sum_numi,sum_numj)
data = set(data)
print(f"First dataset  = {a1}")
print(f"Second dataset = {a2}")

print(data)

plt.plot(sum_numi,sum_numj,markerfacecolor = 'r',marker = 'o')
plt.xlabel("Dataset 1")
plt.ylabel("Dataset 2")
plt.title("Data sum pair")
plt.show()

