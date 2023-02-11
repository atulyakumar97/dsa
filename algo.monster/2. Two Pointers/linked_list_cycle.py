class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def next_node(nodes: Node) -> Node:
    if nodes.next:
        return nodes.next
    else:
        return nodes


def has_cycle(nodes: Node) -> bool:
    slow = next_node(nodes)
    fast = next_node(next_node(nodes))

    while slow != fast and fast.next is not None:
        # exit condition = intersection or end
        slow = next_node(slow)
        fast = next_node(next_node(fast))

    if fast.next is None:
        # end reached -> no cycle
        return False
    else:
        # slow == fast -> interesection occured
        return True


if __name__ == '__main__':
    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i, entry in enumerate(raw_input):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = has_cycle(nodes)
    print('true' if res else 'false')
