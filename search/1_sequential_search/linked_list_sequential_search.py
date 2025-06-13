class Node:
    def __init__(self,key):
        self.key = key
        self.link = None # 다음 노드를 가리키는 포인터

# 노드 생성
node1 = Node(7)
node2 = Node(10)
node3 = Node(8)
node4 = Node(2)
node5 = Node(9)

# 연결
node1.link = node2
node2.link = node3
node3.link = node4
node4.link = node5
# node1 → node2 → node3 → None

def seq_search(head, search_key):
    # head : Node reference, 시작 노드
    t = head
    while((t is not None) and (t.key!=search_key)):
        t = t.link
        # 다음 노드 탐색
    if t:
        print(f"found! {t}")
    else:
        print("not found")
    return t

seq_search(node1, 2) # node1 의 reference 를 넘김