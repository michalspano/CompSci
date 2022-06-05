#!/usr/bin/env python3

"""
Michal Špano
Nodes in Python
24/10/2021
"""


# Import libs
import graphviz as gv
from sys import argv

# Global structure of nodes
struct: dict = {}

# Error backslash
ERROR = '\033[91m'


# Node class
class Node:
    def __init__(self, currentNode=None):
        self.currentNode = currentNode

    # Assign current node to memory
    def __assign__(self) -> dict:
        return {'node': (self.currentNode[1].split()),
                'dist': [int(d) for d in self.currentNode[2].split()],
                'time': [int(t) for t in self.currentNode[3].split()]}

    # Static method to display node graph
    @staticmethod
    def __graph__(out: str) -> None:
        # Create a graphviz object
        dot = gv.Digraph(format='png')
        for node in struct:
            current_edge: list = [f"{node}{n}" for n in struct[node]['node'] if len(struct[node]['node']) > 0]
            dot.edges(current_edge)

        print(f'Schema:\n{dot.source}')  # {Optional}
        dot.render(out, view=True)  # {Render node map as png}


def main(out_path: str = 'out/node'):
    # Compute nodes in a dict with an error assertion
    assert load_data(), f'{ERROR}Input file or Input file data type error!'
    Node().__graph__(out_path)

    # TODO: A -> E, by a) distance, b) time

    # Assert proper amount of command line arguments
    assert len(argv) == 2, f"{ERROR}`Usage: {argv[0]} d/t [distance or time computed]`."

    # Parse desired option
    option: str = 'dist' if argv[1].lower() in ['distance', 'dist', 'd'] else 'time'

    # List to store individual weights
    temp: list = []
    for node in struct:

        # Detect the current point and access its properties
        current_node: dict = struct[node]

        # Detect multiple element point node
        if len(current_node['node']) > 1:

            """Decision-making based upon individual 'weights' of each moves
            NODE -> weight1 [index of sorted pointers], weight2 [dist/time sorted]
            """

            weights: list = []

            # Iterate over all pointers from the current point
            for i in range(len(current_node['node'])):

                # Str of the node (point) pointing to
                node_point: str = current_node['node'][i]

                # Sort assigned distances
                sort_dist: list = sorted(current_node[option])

                # Assign weight of node's property with corresponding indexes
                dist_weight: int = sort_dist.index(current_node[option][i])

                # Populate weights' list
                weights.append([f"{node}{node_point}",
                                len(current_node['node']) - (i + 1),
                                dist_weight])
            temp.append(weights)

        # If a point is pointing to a single node
        elif len(current_node['node']) == 1:

            # Default data assertion
            temp.append([[f"{node}{current_node['node'][0]}", 0, 0]])

    j: int = 0
    # Store continuous chain of node-to-node moves
    path: list = []

    # Current node HEAD
    HEAD: str = temp[0][0][0][0]

    # Process until HEADer doesn't point to the end of the sequence
    while HEAD != 'E':

        # Decision making: weights
        moves: list = []
        for move in temp[j]:
            moves.append(sum(move[1:]))

        # Decide which weight is the lowest
        min_weight: int = min(moves)

        # Assign its index value
        min_weight_index = moves.index(min_weight)

        # Handle the same weights (i.e. if computed weights are the same) -> Bool
        exact_list: bool = all(el == moves[0] for el in moves)

        # Assign the most convenient pointer from node-to-node
        pointer = temp[j][min_weight_index] if not exact_list else temp[j][-1]

        # Update current HEAD
        HEAD = pointer[0][1]

        # Write current pointer value
        path.append(pointer)

        # Increment counter
        j += 1

    # Format each node pointer to the console
    def format_move(idx: int, start: str, end: str) -> None:
        print(f"{idx}: {start} -> {end}")

    # Compute total distance/time
    total_sum: int = 0
    move_count: int = 1
    for move in temp:
        for node in move:
            for pointer in path:

                """
                Iterate over all possible matches of assigned moves
                Detect matching edges (a.k.a. pointers to nodes)
                """

                if node[0] == pointer[0]:

                    # Current point
                    current_point: str = node[0][0]

                    # Assign current point and its properties stored in a dict
                    current_node_dict: dict = struct[current_point]

                    # Assign node to which the current node is pointing to
                    node_head: str = node[0][1]

                    # Receive index of pointing node
                    node_head_index: int = current_node_dict['node'].index(node_head)

                    # Increment counter
                    total_sum += current_node_dict[option][node_head_index]
                    format_move(move_count, current_point, node_head)
                    move_count += 1

    # Show final output value
    print(f"Total {option} travelled: {total_sum!r}")


# Function to load each node to a struct
def load_data(input_src: str = 'src/input.txt') -> bool:
    global struct  # {Global reference}

    # Read text file
    try:
        with open(input_src) as f:
            for row in f:
                current_instance: list = row.strip().split(';')  # {Format current node}
                # Parse to Node class and assign to struct
                struct[current_instance[0]] = Node(current_instance).__assign__()

        # Indicate successful completion
        return True

    # Handle possible errors and return False
    except FileNotFoundError or TypeError:
        return False


# Invoke main function
if __name__ == '__main__':
    main()
