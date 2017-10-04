# 2.1
# Remove Dups
# Write code to remove duplicates from an unsorted linked list


def remove_dups(ll):
    if ll.head is None:
        return

    node = ll.head
    seen = {node.val}
    while node.next:
        if node.next.val in seen:
            node.next = node.next.next
        else:
            seen.add(node.next.val)
            node = node.next

    return ll


def remove_dups2(ll):
    if ll.head is None:
        return

    current = ll.head
    while current.next:
        runner = current
        while runner.next:
            if current.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll