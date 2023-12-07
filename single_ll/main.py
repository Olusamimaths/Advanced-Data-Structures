class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = self.head

        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("None")

    def insert_in_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node = Node(data)
        ptr = self.head

        while ptr.next:
            ptr = ptr.next

        ptr.next = new_node

    def insert_after_key(self, data, key):
        new_node = Node(data)
        ptr = self.head

        while ptr and ptr.next and (ptr.data != key):
            ptr = ptr.next

        if ptr and ptr.next is None:
            print(f"Key: {key} not found. Insertion failed")
            return

        if ptr:
            new_node.next = ptr.next
            ptr.next = new_node


def main():
    list = LinkedList()
    list.insert_at_end(2)
    list.insert_at_end(1)
    list.insert_at_end(8)
    list.insert_at_end(4)

    print("Before insertion: ")
    list.print_list()

    list.insert_in_front(0)
    list.insert_at_end(14)
    list.insert_at_end(9)
    list.insert_at_end(11)
    print("After insertion: ")
    list.print_list()

    print(f"Inserting after key {11}: ")
    list.insert_after_key(110, 11)
    list.print_list()

    print(f"Inserting after key {2}: ")
    list.insert_after_key(20, 2)
    list.print_list()

    print(f"Inserting after key {0}: ")
    list.insert_after_key(99, 0)
    list.print_list()


main()
