def bubble_sort_1(arr):
	n = len(arr)
	for j in range(0,n-1):
		print("step 0")
		if(arr[j]>arr[j+1]):
			print(f"swap: {arr[j]} {arr[j+1]}")
			tmp = arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = tmp
		print(f"{j}:{arr}")
	for j in range(0,n-2):
		print("step 1")
		if(arr[j]>arr[j+1]):
			print(f"swap: {arr[j]} {arr[j+1]}")
			tmp = arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = tmp
		print(f"{j}:{arr}")
	for j in range(0,n-3):
		print("step 2")
		if(arr[j]>arr[j+1]):
			print(f"swap: {arr[j]} {arr[j+1]}")
			tmp = arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = tmp
		print(f"{j}:{arr}")
		
def bubble_sort_2(arr):
	n = len(arr)
	for i in range(n):
		print(f"step {i}")
		for j in range(n-1-i):
			if(arr[j]>arr[j+1]):
				print(f"swap: {arr[j]} {arr[j+1]}")
				tmp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = tmp
			print(f"{j}:{arr}")


unsorted_arr = [5, 8, 4, 2]

print(f"unsorted_arr: {unsorted_arr}")

bubble_sort_2(unsorted_arr)

print(f"sorted_arr: {unsorted_arr}")


