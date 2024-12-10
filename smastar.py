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
        self.forgotten = [float('inf')]
        self.children = self.expand_node(graph, heuristic)

    def __lt__(self, other):
        if self.fn == other.fn:
            return self.depth > other.depth
        return self.fn < other.fn
    
    # def expand_node(self, graph, heuristic):
    #     children = []
    #     for neighbor, cost in graph[self.state]:
    #         gn = self.gn + cost
    #         hn = heuristic[neighbor]
    #         children.append(Node(neighbor, self, gn, hn, self.depth + 1, graph, heuristic))
    #     return children

    def expand_node(self, graph, heuristic):
        children = []
        current_state_path = self.Get_path()  # Lấy danh sách các đỉnh trên đường đi hiện tại
        for neighbor, cost in graph[self.state]:
            if neighbor in current_state_path:  # Ngăn đệ quy quay lại chu trình
                continue
            gn = self.gn + cost
            hn = heuristic.get(neighbor, float('inf'))  # Giá trị mặc định cho heuristic
            children.append(Node(neighbor, self, gn, hn, self.depth + 1, graph, heuristic))
        return children

    def Get_path(self):
        """
        Trả về danh sách các đỉnh trên đường đi từ gốc đến đỉnh hiện tại.
        """
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return set(path)

    def resetNode(self):
        self.fn = self.gn + self.hn
        self.expand_all = False
        self.visited = []
        self.forgotten = [float('inf')]


def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def update_fn(node, queue):
    node.expand_all = True
    temp_node = node
    while temp_node and temp_node.expand_all:
        child_fn = []
        for child in temp_node.children: 
            if child in queue:
                child_fn.append(child.fn)

        if child_fn:  # Kiểm tra nếu child_fn không rỗng
            min_child_fn = min(child_fn)
        else:
            min_child_fn = float('inf')  # Gán giá trị lớn vô cùng nếu không có con

        min_forgotten = min(temp_node.forgotten) if temp_node.forgotten else float('inf')

        if min_forgotten < min_child_fn:
            temp_node.fn = min_forgotten
            temp_node.forgotten.remove(min_forgotten)
        else:
            temp_node.fn = min_child_fn
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
            continue

        if (not successor.state == goal) and (successor.depth + 1 == memory_limit):
            successor.fn = float('inf')
        else:
            successor.fn = max(node.fn, successor.fn)

        if len(queue) >= memory_limit:
            removal_candidates = [temp_node for temp_node in queue if temp_node is not node]
            badNode = max(removal_candidates, key=lambda temp_node: (temp_node.fn, temp_node.depth))
            queue.remove(badNode)
            badNode.resetNode
            badNode.parent.forgotten.append(badNode.fn)

        queue.append(successor)

        if (not node.expand_all) and (len(node.visited) == len(node.children)):
            update_fn(node, queue)


    return None 

# '''if __name__ == "__main__":
#   graph = {
#         'S': [('A', 10), ('B', 8)],
#         'A': [('C', 2), ('G', 10)],
#         'B': [('D', 8), ('G', 16)],
#         'C': [('E', 3), ('G', 9)],
#         'E': [('G', 2)],
#         'D': [('G', 3), ('H', 1)],
#         'H': [('F', 1)],
#         'F': [],
#         'G': []
#     }
#   heuristic = {
#         'S': 12,
#         'A': 5,
#         'B': 5,
#         'C': 5,
#         'D': 2,
#         'E': 2,
#         'F': 1,
#         'H': 1,
#         'G': 0
#   }
#   start = 'S'
#   goal = 'G'
#   memory_limit = 4
#   print(sma_star(start, goal, graph, heuristic, memory_limit))'''

# if __name__ == "__main__":
#   graph = {
#         'S': [('A', 4), ('B', 5), ('C', 6)],
#         'A': [('G', 5)],
#         'B': [('G', 3)],
#         'C': [('G', 1)],
#         'G': []
#     }
#   heuristic = {
#         'S': 3,
#         'A': 1,
#         'B': 1,
#         'C': 1,
#         'G': 0
#   }
#   start = 'S'
#   goal = 'G'
#   memory_limit = 3
#   print(sma_star(start, goal, graph, heuristic, memory_limit))
