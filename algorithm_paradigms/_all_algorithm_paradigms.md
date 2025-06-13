# Greedy (탐욕 알고리즘)
- 각 단계에서 현재 상태에서의 최선 선택
- 최적해가 보장되지 않음

대표적인 예시 : 거스름돈 문제(change-making problem), 부분배낭 문제(fractional-knapsack problem), Dijkstra, Kruskal, Prim


# Devide and Conquer(DnC, 분할정복 알고리즘)
- 주어진 입력을 작은 여러개의 입력으로 분할, 각각을 품(정복)
- 푼 것을 합침(병합)
    - 분할 - 정복 - 병합
- Brute Force 의 최적화버전이라고 할 수 있겠다.

대표적인 예시 : Merge Sort, Quick Sort, Binary Search, 거듭제곱

# Dynamic Programming(DP, 동적계획법)
캐싱(caching): 반복되는 동일한 연산들을 저장하고, 두번째부터는 연산하지 않고 저장된 값을 사용하는 것
Dynamic Programming : 중복최적부분구조를 캐싱하여 알고리즘을 최적화하는 기법

# DnC vs DP
- 최적부분구조이면 DnC 사용가능
- 최적부분구조이면서 중복부분구조가 존재하는 경우 DP 사용가능
- 캐시를 저장해야하므로 DP 가 DnC 보다 메모리를 더 사용함 -> 시간복잡도를 낮추고 공간복잡도를 올리는 방법

### 최적부분구조(Optimal Substructure)
- 큰 문제의 최적해가 작은 문제들의 최적회를 합친 것인 경우
### 중복 부분 문제(Overlapping Subproblems)
- 동일한 부분문제가 여러반 발생하는 경우, 연산하지 않고 메모리에 저장된 값을 갖다 쓰면 효율적임.

Bottom-up DP 와 Top-down DP 가 존재함.
- Bottom-up DP : tabulation (작은 해부터 계산해서 테이블을 채워나감. 나중에 이 테이블을 참고하여 다른 문제 해결)
- Top-down DP : recursion + memoization (결과 자체를 저장(캐시))

대표적인 예시 : Knapsack, 피보나치, 최장 공통 부분 수열(LCS), 최장 증가 부분 수열(LIS)

# Backtracking (백트래킹)