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
        print(node.state, end=" ")
    print()


def sma_star(start, goal, graph, heuristic, memory_limit):
    root = Node(start, None, 0, heuristic[start], 0, graph, heuristic)
    queue = [root]
    closed_list = {}
    counter = 0

    while queue and counter < 20 :
        print(f"Iteration: {counter}")
        counter += 1 
        heapq.heapify(queue)
        print_queue(queue)
        node = queue[0]

        if node.state == goal:
            return get_path(node)

        # Move fully expanded nodes to the closed list
        if node.expand_all or not node.children:
            closed_list[node.state] = node
            queue.pop(0)
            continue

        successor = None 
        for child in node.children:
            if child not in node.visited:
                successor = child
                node.visited.append(child)
                # break
            elif child.fn <= node.fn:
                successor = child
                # break

            if not successor:
                queue.remove(node)
                continue

            # Check if successor is in the closed list
            if successor.state in closed_list:
                existing_node = closed_list[successor.state]
                if successor.fn < existing_node.fn:
                    del closed_list[successor.state]
                    queue.append(successor)
            else:
                if (not successor.state == goal) and (successor.depth + 1 == memory_limit):
                    successor.fn = float('inf')
                else:
                    successor.fn = max(node.fn, successor.fn)

                if len(queue) >= memory_limit:
                    removal_candidates = [temp_node for temp_node in queue if temp_node is not node]
                    badNode = max(removal_candidates, key=lambda temp_node: (temp_node.fn, temp_node.depth))
                    queue.remove(badNode)
                    badNode.resetNode()
                    badNode.parent.forgotten.append(badNode.fn)
                queue.append(successor)

        if (not node.expand_all) and (len(node.visited) == len(node.children)):
            update_fn(node, queue)

    return None
