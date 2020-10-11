#implementation of selection sort
#Algorithm using Python List
def selection_sort(data):
	n=len(data)
	for i in range(n-1):
		smallindex=i
		for j in range(i+1,n):
			if data[j]<data[smallindex]:
				smallindex=j
		if smallindex!=i:
			temp=data[i]
			data[i]=data[smallindex]
			data[smallindex]=temp
		
#calling selection sort
mark=[88,100,23,45,11,71,83,8]
print("Data Before Sort")
print(mark)
selection_sort(mark)
print("Data After Sort")
print(mark)