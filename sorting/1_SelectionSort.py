def selection_sort_1(arr):
	n = len(arr)
	for j in range(0,n):
		if(arr[j]<arr[0]):
			arr[0] = arr[j]
			arr[j] = arr[0]
			
def selection_sort_2(arr):
	n = len(arr)
	for j in range(0,n):
		if(arr[j]<arr[0]):
			tmp = arr[0]
			arr[0] = arr[j]
			arr[j] = tmp
			
def selection_sort_3(arr):
	n = len(arr)
	for i in range(0,n):
		for j in range(i+1,n):
			if(arr[j]<arr[i]):
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp
		print(f'{i}:{arr}')
		
def selection_sort_4(arr):
	n = len(arr)
	for i in range(0,n):
		min_idx = i
		for j in range(i+1,n):
			if(arr[j]<arr[min_idx]):
				min_idx=j
		tmp = arr[i]
		arr[i] = arr[min_idx]
		arr[min_idx] = tmp
		print(f'{i}:{arr}')
		

unsorted_arr = [5, 8, 4, 2]

print(f"unsorted_arr: {unsorted_arr}")

selection_sort_4(unsorted_arr)

print(f"sorted_arr: {unsorted_arr}")


