import re
import sys


class Node:
    def __init__(
        self,
        id: int,
        rank: int,
        symbol: str,
    ):
        self.id: int = id
        self.rank: int = rank
        self.symbol: str = symbol
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None

    def __repr__(self) -> str:
        return f'Node(symbol={self.symbol}, rank={self.rank})'


def parse_nodes(data: str) -> tuple[Node, Node]:
    id, left_rank, left_symbol, right_rank, right_symbol = re.match(
        pattern=r'ADD id=(\d+) left=\[(\d+),(.+)] right=\[(\d+),(.+)]',
        string=data,
    ).groups()

    return (
        Node(id=int(id), rank=int(left_rank), symbol=left_symbol),
        Node(id=int(id), rank=int(right_rank), symbol=right_symbol),
    )


def append_to_tree(root: Node, node: Node) -> None:
    if node.rank < root.rank:
        if root.left is None:
            root.left = node
        else:
            append_to_tree(root=root.left, node=node)
    else:
        if root.right is None:
            root.right = node
        else:
            append_to_tree(root=root.right, node=node)


def swap_nodes(nodes: tuple[Node, Node], swap_children: int) -> None:
    left_node, right_node = nodes

    tmp_rank, tmp_symbol = left_node.rank, left_node.symbol
    left_node.rank, left_node.symbol = right_node.rank, right_node.symbol
    right_node.rank, right_node.symbol = tmp_rank, tmp_symbol

    if swap_children:
        tmp = left_node.left, left_node.right
        left_node.left, left_node.right = right_node.left, right_node.right
        right_node.left, right_node.right = tmp


def parse_trees(lines: list[str], swap_children: bool) -> Node:
    tree = Node(id=-1, rank=-1, symbol='ROOT')
    tree.left, tree.right = parse_nodes(lines[0])
    nodes = {tree.left.id: (tree.left, tree.right)}

    for line in lines[1:]:
        instruction, *args = line.split(' ')
        match instruction:
            case 'ADD':
                node_left, node_right = parse_nodes(line)
                nodes[node_left.id] = (node_left, node_right)
                append_to_tree(root=tree.left, node=node_left)
                append_to_tree(root=tree.right, node=node_right)
            case 'SWAP':
                swap_nodes(nodes[int(args[0])], swap_children)

    return tree


def group_nodes_by_level(tree: Node) -> dict[int, list[Node]]:
    levels: dict[int, list[Node]] = {}

    def traverse(node: Node, depth: int) -> None:
        if depth not in levels:
            levels[depth] = []

        levels[depth].append(node)

        if node.left:
            traverse(node.left, depth + 1)
        if node.right:
            traverse(node.right, depth + 1)

    traverse(tree, 0)

    return levels


def parse_output_string(tree: Node) -> str:
    def key(x):
        return 1000 * len(x[1]) - x[0]

    nodes = max(group_nodes_by_level(tree.left).items(), key=key)[1]
    nodes += max(group_nodes_by_level(tree.right).items(), key=key)[1]

    return ''.join(node.symbol for node in nodes)


def main():
    input = sys.stdin.readlines()

    tree = parse_trees(input, False)
    print(parse_output_string(tree))
    print(parse_output_string(tree))

    tree = parse_trees(input, True)
    print(parse_output_string(tree))


if __name__ == '__main__':
    main()
