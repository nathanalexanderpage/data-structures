#              A
#        B           C
#     D     E     F     G
#    H I   J K   L M   N O

tree = {
    'A': {
        'data': 'A',
        'pointers': ['B', 'C']
        },
    'B': {
        'data': 'B',
        'pointers': ['D', 'E']
        },
    'C': {
        'data': 'C',
        'pointers': ['F', 'G']
        },
    'D': {
        'data': 'D',
        'pointers': ['H', 'I']
        },
    'E': {
        'data': 'E',
        'pointers': ['J', 'K']
        },
    'F': {
        'data': 'F',
        'pointers': ['L', 'M']
        },
    'G': {
        'data': 'G',
        'pointers': ['N', 'O']
        },
    'H': {
        'data': 'H',
        'pointers': []
        },
    'I': {
        'data': 'I',
        'pointers': []
        },
    'J': {
        'data': 'J',
        'pointers': []
        },
    'K': {
        'data': 'K',
        'pointers': []
        },
    'L': {
        'data': 'L',
        'pointers': []
        },
    'M': {
        'data': 'M',
        'pointers': []
        },
    'N': {
        'data': 'N',
        'pointers': []
        },
    'O': {
        'data': 'O',
        'pointers': []
        },
    }

class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, item):
        self.values.append(item)
    def dequeue(self):
        return self.values.pop(0)

class Point:
    def __init__(self):
        self.data = None

def queue_children(node):
    for pointer in tree[node]['pointers']:
        q.enqueue(pointer)

# start with Queue q containing ref to head node 'A'
q = Queue()
start = 'A'

while (q):
    current_node = q.dequeue()
    q.enqueue(tree[current_node]['data'])
    
