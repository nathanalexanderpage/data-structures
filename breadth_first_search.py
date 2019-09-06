graph = {}

class Point:
    def __init__(self, name):
        self.name = name
        self.traversed = False
        self.pointers = []
        graph[self.name] = self

# point sets to choose from
points_1 = ['A', 'B', 'C', 'D', 'E']
points_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

# edge sets to choose from
edges_1 = ['AB', 'AC', 'AD', 'BA', 'BD', 'CA', 'CD', 'DE']
edges_2 = ['AB', 'AE', 'AF', 'BA', 'BC', 'BF', 'CB', 'CD', 'CG', 'DC', 'DH', 'EA', 'EF', 'EI', 'EJ', 'FA', 'FE', 'FB', 'FG', 'FJ', 'FK', 'GF', 'GH', 'GC', 'GK', 'HG', 'HD', 'HL', 'IE', 'IJ', 'IM', 'JI', 'JE', 'JK', 'JF', 'JN', 'KJ', 'KG', 'KL', 'KO', 'KP', 'LK', 'LH', 'LP', 'MI', 'MN', 'NM', 'NI', 'NO', 'ON', 'OK', 'OP', 'PO', 'PK', 'PL']

# configure edges and points variables
configuration = {
    'points': points_1,
    'edges': edges_1
}

def add_edge(points_str):
    print(type(points_str))
    points_str[:1]

def make_graph(points, edges):
    for point in points:
        new_point = Point(point.name)

class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, item):
        self.values.append(item)
    def dequeue(self):
        return self.values.pop(0)

def queue_children(node):
    for pointer in graph[node]['pointers']:
        q.enqueue(pointer)

# start with:
# Queue q containing ref to head node 'A'
q = Queue()
start = 'A'
# empty 'queued nodes' array with letter refs (so as to not queue twice)
queued = []
# empty 'dealt_with nodes' array with letter refs ()
dealt_with = []

while (q):
    current_node = q.dequeue()
    q.enqueue(graph[current_node]['data'])
    
