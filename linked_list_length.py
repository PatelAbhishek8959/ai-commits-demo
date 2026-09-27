class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def linked_list_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
