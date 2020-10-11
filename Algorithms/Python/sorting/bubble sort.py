#Python Implementation of bubble Sort Algorithm
#Using data available in Python List

temperature=[45,10,14,77,-3,22,0]

#ascending Order Sort
def bubble(data):
	n=len(data)
	for i in range(n-1):
		for j in range(i+1,n):
			if data[i]>data[j]:
				temp=data[j]
				data[j]=data[i]
				data[i]=temp
print("Data Before Sort")
print(temperature)
bubble(temperature)
print("Data After Sort")
print(temperature)