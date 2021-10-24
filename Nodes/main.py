#!/usr/bin/env python3

"""
Michal Špano
Nodes in Python
24/10/2021
"""


# Import libs
import graphviz as gv


# TODO: Create 'Node' class
class Node:
    def __init__(self):
        pass


def main(out_path: str = 'out/node'):
    # TODO: Provide input from .txt document
    # Compute nodes in a dict
    struct: dict = {"A": {'node': ['B', 'C'], 'dist': [10, 12], 'time': [4, 5]},
                    "B": {'node': ['C', 'E'], 'dist': [4, 8], 'time': [4, 10]},
                    "C": {'node': ['D', 'E'], 'dist': [10, 2], 'time': [20, 5]},
                    "D": {'node': ['E'], 'dist': [10], 'time': [5]},
                    "E": {'node': [], 'dist': [], 'time': []}  # {End node}
                    }

    # Create a graphviz object
    dot = gv.Digraph(format='png')
    for node in struct:
        current_edge: list = [f"{node}{n}" for n in struct[node]['node'] if len(struct[node]['node']) > 0]
        dot.edges(current_edge)
    
    # print(f'Schema:\n{dot.source}')  # {Optional}
    dot.render(out_path, view=True)  # {Render node map as png}

    # TODO: Fix search algorithm
    """A -> E, by a) distance, b) time
    a) distance [x]
    """

    # List to store individual weights
    temp = []
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
                sort_dist: list = sorted(current_node['dist'])

                # Assign weight of node's property with corresponding indexes
                dist_weight: int = sort_dist.index(current_node['dist'][i])

                # Populate weights' list
                weights.append([f"{node}{node_point}", i, dist_weight])
            temp.append(weights)

        # If a point is pointing to a single node
        elif len(current_node['node']) == 1:

            # Default data assertion
            temp.append([[f"{node}{current_node['node'][0]}", 0, 0]])

    i: int = 0

    # Store continuous chain of node-to-node moves
    path: list = []

    # Current node HEAD
    HEAD: str = temp[0][0][0][0]

    # Process until HEADer doesn't point to the end of the sequence
    while HEAD != 'E':

        # Decision making: weights
        moves: list = []
        for move in temp[i]:
            moves.append(sum(move[1:]))

        # Decide which weight is the lowest
        min_weight: int = min(moves)

        # Assign its index value
        min_weight_index = moves.index(min_weight)

        # Handle the same weights (i.e. if computed weights are the same) -> Bool
        exact_list: bool = all(el == moves[0] for el in moves)

        # Assign the most convenient pointer from node-to-node
        pointer = temp[i][min_weight_index] if not exact_list else temp[i][-1]

        # Update current HEAD
        HEAD = pointer[0][1]

        # Write current pointer value
        path.append(pointer)

        # Increment counter
        i += 1

    # Compute total distance
    # TODO: Make universal for distance and time

    def format_move(idx: int, start: str, end: str) -> None:
        print(f"{idx}: {start} -> {end}")

    total_dist: int = 0
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
                    current_node: dict = struct[current_point]

                    # Assign node to which the current node is pointing to
                    node_head: str = node[0][1]

                    # Receive index of pointing node
                    node_head_index: int = current_node['node'].index(node_head)

                    # Increment counter
                    total_dist += current_node['dist'][node_head_index]

                    format_move(move_count, current_point, node_head)
                    move_count += 1

    print(f'Total distance travelled: {total_dist!r}')


if __name__ == '__main__':
    main()
