class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_list(head, k):
        prev = None
        current = head
        count = 0

        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        return prev

    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    length = get_length(head)
    if length < k:
        return head

    num_reversals = length // k
    new_head = None
    prev_tail = None

    for _ in range(num_reversals):
        new_tail = head
        reversed_head = reverse_list(head, k)
        if not new_head:
            new_head = reversed_head
        if prev_tail:
            prev_tail.next = reversed_head
        prev_tail = new_tail
        head = new_tail.next

    prev_tail.next = head
    return new_head

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_string(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return '-'.join(result)

input_values = [1, 2, 3, 4, 5]
k = 2
input_linked_list = create_linked_list(input_values)
reversed_linked_list = reverse_k_group(input_linked_list, k)
output_string = linked_list_to_string(reversed_linked_list)
print("Output:", output_string)
