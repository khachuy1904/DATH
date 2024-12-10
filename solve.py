import heapq

def dijkstra(graph, start, goal):
    # Bước khởi tạo
    pq = []  # Priority Queue (heap)
    heapq.heappush(pq, (0, start))  # (chi phí hiện tại, đỉnh hiện tại)
    distances = {node: float('inf') for node in graph}  # Khởi tạo khoảng cách vô cùng
    distances[start] = 0
    previous = {node: None for node in graph}  # Dùng để lưu đường đi ngắn nhất

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Nếu đạt đến đỉnh goal, dừng tìm kiếm
        if current_node == goal:
            break

        # Duyệt tất cả các cạnh từ đỉnh hiện tại
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Nếu tìm được đường đi ngắn hơn
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Tái tạo đường đi từ previous
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    return distances[goal], path