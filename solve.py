import heapq

# Hàm đọc đồ thị từ tệp
def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            # Tách từng phần của dòng
            parts = line.strip().split()
            if len(parts) == 3:
                src, dest, weight = parts[0], parts[1], int(parts[2])
                
                # Thêm cạnh vào đồ thị
                if src not in graph:
                    graph[src] = []
                if dest not in graph:
                    graph[dest] = []
                
                # Cạnh hai chiều (vô hướng)
                graph[src].append((dest, weight))
                # graph[dest].append((src, weight))  # Nếu đồ thị là vô hướng
    return graph

# Thuật toán Dijkstra để tìm đường đi ngắn nhất
def dijkstra(graph, start, end):
    queue = [(0, start, [])]  # (tổng trọng số, đỉnh hiện tại, đường đi)
    visited = set()  # Tập hợp các đỉnh đã thăm
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        
        # Nếu đỉnh đã thăm, bỏ qua
        if node in visited:
            continue
        
        # Thêm đỉnh vào đường đi
        path = path + [node]
        
        # Nếu đến đích, trả về đường đi và chi phí
        if node == end:
            return path, cost
        
        # Đánh dấu đỉnh đã thăm
        visited.add(node)
        
        # Thêm các đỉnh kề vào hàng đợi
        for (neighbor, weight) in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    
    return None, float('inf')  # Trả về vô cùng nếu không tìm thấy đường đi

# Đọc đồ thị từ tệp
filename = 'graph.txt'
graph = read_graph_from_file(filename)

# Chọn điểm bắt đầu và kết thúc
start = 'A'
end = 'Z'

# Tìm đường đi ngắn nhất
path, cost = dijkstra(graph, start, end)
if path:
    print("Shortest path:", path)
    print("Total weight:", cost)
else:
    print("No path found between", start, "and", end)
