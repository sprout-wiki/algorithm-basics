# Greedy (탐욕 알고리즘)
- 각 단계에서 현재 상태에서의 최선 선택을 고르는 류의 알고리즘
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
- 큰 문제의 최적해가 작은 문제들의 최적회를 합친 것인 류의 알고리즘들
### 중복 부분 문제(Overlapping Subproblems)
- 동일한 부분문제가 여러반 발생하는 경우, 연산하지 않고 메모리에 저장된 값을 갖다 쓰면 효율적임.

Bottom-up DP 와 Top-down DP 가 존재함.
- Bottom-up DP : tabulation (작은 해부터 계산해서 테이블을 채워나감. 나중에 이 테이블을 참고하여 다른 문제 해결)
- Top-down DP : recursion + memoization (결과 자체를 저장(캐시))

대표적인 예시 : Knapsack, 피보나치, 최장 공통 부분 수열(LCS), 최장 증가 부분 수열(LIS)

# Backtracking (백트래킹)
Brute Force 를 하되, 규칙 등으로 인해 불가능한 수는 제거(prune)하고 세는 류의 알고리즘들
- 기본적으로 완전탐색(Brute Force)이다

# 메타휴리스틱 (Metaheuristic)
- 해를 "개선"하며 반복 탐색하는 류의 알고리즘들 (진화, 확률 등)
- 알고리즘이 이전 해를 기억하며, 이를 토대로 더 나은 해를 찾음

정확한 해 대신 ’좋은 해(근사해)’를 찾기 위한 일반적인 탐색 전략.
특정 문제에 종속되지 않고, 광범위한 최적화 문제에 사용할 수 있는 고수준 알고리즘 프레임워크
**“국소최적에 빠지지 않고, 전역최적을 잘 찾아보자”**는 전략
 NP-hard → 완전탐색은 불가능한 경우에 쓸 수 있는 도구

- 유전 알고리즘 (GA)
- 시뮬레이티드 어닐링 (SA)
- 개미 군집 최적화 (ACO)
- 입자군집 최적화 (PSO)
- Tabu Search

