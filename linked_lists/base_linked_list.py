class linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None


a = linked_list("a")
b = linked_list("b")
c = linked_list("c")
d = linked_list("d")

a.next = b
b.next = c
c.next = d


def print_linked_list(head):
    current = head
    while current != None:
        print(current.value)
        current = current.next


def get_values(head):
    values = []
    current = head
    while current != None:
        values.append(current.value)
        current = current.next

    return values


def get_sum(head):
    sum = ""
    current = head
    while current != None:
        sum += current.value
        current = current.next

    return sum


def reverse_linked_list(head):
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def zip_lists(head1, head2):
    tail = head1
    current1 = head1
    current2 = head2
    count = 0

    while current1 != None and current2 != None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1

    if current1 != None:
        tail.next = current1
    if current2 != None:
        tail.next = current2

    return head1
