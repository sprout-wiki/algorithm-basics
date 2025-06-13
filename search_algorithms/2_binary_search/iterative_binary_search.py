def iterative_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while(left<=right):
        mid = (left+right) // 2

        if(arr[mid] == target):
            return mid
        elif(arr[mid]<target):
            left = mid+1
        else:
            right = mid-1

    return -1

arr = [1, 3, 5, 6, 9, 13, 22, 24] # 정렬되어있어야함

search_key = 22
search_result = iterative_binary_search(arr,search_key)

print(f"{arr} -> {search_key}:{search_result}")