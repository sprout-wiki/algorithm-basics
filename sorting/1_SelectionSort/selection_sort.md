# 선택정렬(Selection Sort)

- 숫자들을 크기 순서대로 나열

### 제자리 알고리즘(In-place Algorithm)

메모리를 추가로 쓰기 보다는, swap 을 해서 기존 arr 자리를 낭비하지 않도록 하는게 리빙포인트.

- 원본 데이터가 변경됨.
- Bubble Sort, Selection Sort, Insertion Sort

input

[5,3,8,2]

i=0

[5,3,8,2] 에서 최소를 구해서 arr[0] 으로 이동

[2,3,8,5]

i=1

[3,8,5] 에서 최소를 구해서 arr[1] 으로 이동

[2,3,8,5]

i=2

[8,5] 에서 최소를 구해서 arr[2] 으로 이동

[2,3,5,8]

i=3

논리적으로, 할 필요 없음.

- 마지막놈이 어차피 최대일테니까…

# 설계

- 첫번째 수를 기억
- 전체를 한번 훑으면서 첫번째 수와 비교하면서 최솟값 찾기
    - 최솟값을 1번과 교환
- 반복

# 의사코드

```c
void SelectionSort(int A[], int n)
{
	int i,j, MinIndex;
	for(i=0; i<n-1; i++){
		MinIndex = i;
		for(j=MinIndex+1; j<n; j++)
			if(A[MinIndex] > A[j])
				MinIndex = j;
			if(MinIndex != i)
				Swap(&A[i], &A[MinIndex]);
	}
```

# 성능

- 평균 : O(n^2) : for문 두개임.
- 최악 : O(n^2) : 정렬하나도 안된 경우에, for문 두개를 돈다.
- 제자리 정렬 : 입력 크기 n 에 상관없이 항상 똑같은 크기의 추가 메모리(tmp)가 필요. 즉, O(1) 메모리를 사용함
- 불안정 정렬 : 작은배열의 최솟값을 찾아서 무조건 swap 하기 때문.

# 튜토리얼

i=0

[5,3,8,2] 에서 최소를 구해서 arr[0] 으로 이동

[2,3,8,5]

```python
def selection_sort_1(arr):
	n = len(arr)
	for j in range(0,n):
		if(arr[j]<arr[0]):
			arr[0] = arr[j]
			arr[j] = arr[0]
```

근데 이러면 arr[i] 가 덮어써지니까,

```python
def selection_sort_2(arr):
	n = len(arr)
	for j in range(0,n):
		if(arr[j]<arr[i]):
			tmp = arr[0]
			arr[0] = arr[j]
			arr[j] = tmp
```

이걸 하나씩 줄여가면서 해야하니까,

```python
def selection_sort_3(arr):
	n = len(arr)
	for i in range(0,n):
		for j in range(i+1,n):
			if(arr[j]<arr[i]):
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp
		print(f'{i}:{arr}')
```

swap 을 여러번 하면 성능이 떨어지니까(3줄이나 실행해야된다), swap 은 마지막에 확실히 최소일때 한번만 수행하도록 바꾸면,

```python
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
```

완료