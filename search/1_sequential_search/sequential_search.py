def sequential_search(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            print(f"found! {i}")
            return i
        print(f"{i}:{arr[i]}")
    return -1

arr = [4, 2, 9, 1, 7]

print(sequential_search(arr, 1))
print(sequential_search(arr, 5))