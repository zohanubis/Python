class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def push_front(head, x):
    new_node = Node(x, head)
    return new_node

def push_back(head, x):
    if not head:
        return Node(x)
    current = head
    while current.next:
        current = current.next
    current.next = Node(x)
    return head

def insert_at(head, x, pos):
    if pos == 0:
        return push_front(head, x)
    current = head
    for i in range(pos - 1):
        if not current:
            raise IndexError('Index out of range')
        current = current.next
    current.next = Node(x, current.next)
    return head

def remove_front(head):
    if not head:
        return None
    return head.next

def remove_back(head):
    if not head:
        return None
    if not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

def remove_at(head, pos):
    if not head:
        return None
    if pos == 0:
        return remove_front(head)
    current = head
    for i in range(pos - 1):
        if not current.next:
            raise IndexError('Index out of range')
        current = current.next
    if not current.next:
        raise IndexError('Index out of range')
    current.next = current.next.next
    return head

def search(head, x):
    current = head
    while current:
        if current.data == x:
            return True
        current = current.next
    return False

def count(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def display(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()
