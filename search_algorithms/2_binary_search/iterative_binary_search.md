# 말로 요약

# 손으로 해보기

정렬된 리스트에서 9가 몇번째에 있는지 찾기
[1, 3, 5, 6, 9, 13, 22, 24]

[step1]
left = 0
right = 7
mid = (0+7) // 2 = 3
arr[mid] = 6

6<9
9는 오른쪽 반쪽에 있겠군
left = mid+1 로 조정

[step2]
left = 4
right = 7
mid = (4+7) // 2 = 5
arr[5] = 13
13>9
9는 왼쪽 반쪽에 있겠군
right = mid-1 로 조정

[step3]
left = 4
right = 4
mid = (4+4) // 2 = 4
arr[4] = 9

찾았다! 9의 위치는 4