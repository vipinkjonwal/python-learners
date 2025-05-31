from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, head, value):
        new_node = Node(value)
        temp = head

        if head is None:
            head = new_node
            return

        temp = head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
        return head

    def display(self, head):
        current = head
        while (current):
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
        
if __name__ == '__main__':
    obj = LinkedList()
    head = Node(1)
    
    for i in range(2,9):
        obj.push(head, i)

    obj.display(head)
    head = obj.reverse(head)
    obj.display(head)
    

