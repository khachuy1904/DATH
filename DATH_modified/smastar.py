import heapq

class Node: 
    def __init__(self, state, parent, gn, hn, depth, graph, heuristic):
        self.state = state
        self.parent = parent
        self.gn = gn
        self.hn = hn
        self.fn = gn + hn
        self.depth = depth
        self.expand_all = False
        self.visited = []
        self.forgotten = []
        self.children = self.expand_node(graph, heuristic)

    def __lt__(self, other):
        if self.fn == other.fn:
            return self.depth > other.depth
        return self.fn < other.fn
    
    def expand_node(self, graph, heuristic):
        children = []
        for neighbor, cost in graph[self.state]:
            if check_cycle(self, neighbor):
                continue
            gn = self.gn + cost
            hn = heuristic[neighbor]
            children.append(Node(neighbor, self, gn, hn, self.depth + 1, graph, heuristic))
        return children


def check_cycle(node, state):
    temp_node = node
    while temp_node:
        if temp_node.state == state:
            return True
        temp_node = temp_node.parent
    return False
    
def get_path(node):
    path = []
    print('Shortest distance: ', node.gn)
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def update_fn(node, queue, successor):
    node.expand_all = True
    temp_node = node
    while temp_node and temp_node.expand_all:
        child_fn = []
        for child in temp_node.children: 
            if child in queue:
                child_fn.append(child.fn)
        min_child_fn = float('inf')
        if child_fn:
            min_child_fn = min(child_fn)
        child_forgotten = []
        for child in temp_node.forgotten:
            child_forgotten.append(child.fn)
        
        min_forgotten_node = []
        min_child_forgotten = float('inf')
        if child_forgotten:
            min_child_forgotten = min(child_forgotten)
            for child in temp_node.forgotten:
                if child.fn == min_child_forgotten:
                    min_forgotten_node.append(child)
                    
        temp_node.fn = min(min_child_fn, min_child_forgotten)

        if min_child_forgotten < min_child_fn and successor in min_forgotten_node:
            temp_node.forgotten.remove(successor)
        
        temp_node = temp_node.parent

        
def print_queue(queue):
    for node in queue:
        print(node.state, end = " ")
    print()


def sma_star(start, goal, graph, heuristic, memory_limit):
    root = Node(start, None, 0, heuristic[start], 0, graph, heuristic)
    queue = [root]

    while queue:
        heapq.heapify(queue)
        print_queue(queue)
        node = queue[0]

        if node.state == goal:
            return get_path(node)
        
        successor = None 
        #if node.children: 
        #    heapq.heapify(node.children)
        for child in node.children:
            if child not in node.visited:
                successor = child
                node.visited.append(child)
                break
            elif child.fn <= node.fn:
                successor = child
                break
        
        if not successor:
            queue.remove(node)
            node.fn = float('inf')
            continue

        if (not successor.state == goal) and (successor.depth + 1 == memory_limit):
            successor.fn = float('inf')
        else:
            successor.fn = max(node.fn, successor.fn)

        if len(queue) >= memory_limit:
            removal_candidates = [temp_node for temp_node in queue if temp_node is not node]
            badNode = max(removal_candidates, key=lambda temp_node: (temp_node.fn, temp_node.depth))
            queue.remove(badNode)
            badNode.parent.forgotten.append(badNode)

        queue.append(successor)

        if (not node.expand_all) and (len(node.visited) == len(node.children)):
            update_fn(node, queue, successor)


    return None 




