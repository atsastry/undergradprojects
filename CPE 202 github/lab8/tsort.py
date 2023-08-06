from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, key):
        '''Add whatever parameters/attributes are needed'''
        self.key = key
        self.in_deg = 0
        self.adj_verts = []
        self.visited = False


    def add_adj_vertex(self, vertex):
        self.adj_verts.append(vertex)

    def get_in_deg(self):
        return self.in_deg

    def add_in_deg(self):
        self.in_deg += 1

    def subtract_in_deg(self):
        self.in_deg -= 1

    def get_key(self):
        return self.key

    def get_adj_verts(self):
        return self.adj_verts



def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")

    nested_lst = []
    for item in vertices:
        each = item.split(", ")
        nested_lst.append(each)
    newL = []
    for i in range(0, len(nested_lst) - 1, 2):
        newL.append(nested_lst[i] + nested_lst[i + 1])

    adj_lst = {}
    for pair in newL:
        if pair[0] not in adj_lst:
            adj_lst[pair[0]] = Vertex(pair[0])
        if pair[1] not in adj_lst:
            adj_lst[pair[1]] = Vertex(pair[1])
        adj_lst[pair[0]].add_adj_vertex(pair[1])
        adj_lst[pair[1]].add_in_deg()

    stack = Stack(len(vertices))
    for vert in adj_lst:
        if adj_lst[vert].get_in_deg() == 0:
            stack.push(adj_lst[vert])
    if stack.is_empty():
        raise ValueError("input contains a cycle")
    res = []
    while not stack.is_empty():
        vert = stack.pop()
        if vert.visited:
            raise ValueError("input contains a cycle")
        vert.visited = True
        res.append(vert.get_key() + '\n')
        adj_verts = vert.get_adj_verts()
        for item in adj_verts:
            adj_lst[item].subtract_in_deg()
            if adj_lst[item].get_in_deg() == 0:
                stack.push(adj_lst[item])
    if len(res) != len(adj_lst):
        raise ValueError("input contains a cycle")
    return "".join(res)

    # 100% Code coverage NOT required


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()