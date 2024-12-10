import heapq
import time
def heuristic(graph, current, goal):
    """
    Hàm heuristic thỏa mãn admissible và consistency.
    - current: đỉnh hiện tại.
    - goal: đỉnh đích.
    """
    # Tìm trọng số nhỏ nhất trong đồ thị
    min_weight = min(weight for _, _, weight in graph)
    
    estimated_steps = abs(goal - current)  # Khoảng cách ước tính dựa trên chỉ số các đỉnh

    # Giá trị heuristic: trọng số nhỏ nhất nhân với số bước dự tính
    return min_weight * estimated_steps

class SMAStar:
    def __init__(self, graph, start, goal, memory_limit):
        self.graph = graph  # Đồ thị: danh sách cạnh [(u, v, weight), ...]
        self.start = start  # Đỉnh bắt đầu
        self.goal = goal  # Đỉnh đích
        self.memory_limit = memory_limit  # Giới hạn bộ nhớ
        self.open_list = []  # Hàng đợi ưu tiên (heapq)
        self.closed_list = {}  # Các trạng thái đã được mở rộng

    def heuristic(self, node):
        # Sử dụng heuristic thỏa mãn consistency và admissible
        return heuristic(self.graph, node, self.goal)

    def expand_node(self, node, g_cost):
        neighbors = []  
        for u, v, weight in self.graph:
            if u == node:
                neighbors.append((v, weight))
            elif v == node:
                neighbors.append((u, weight))
        return neighbors

    def search(self):
        # Đo thời gian tổng thể của hàm search
        search_start_time = time.time()
        # Khởi tạo
        start_node = (self.heuristic(self.start), self.start, 0)  # (f(n), node, g(n))
        heapq.heappush(self.open_list, start_node)

        while self.open_list:
            # Lấy nút có f(n) thấp nhất từ hàng đợi
            f, current, g = heapq.heappop(self.open_list)

            # Nếu đến đích, trả về đường đi
            if current == self.goal:
                search_end_time = time.time()
                print(f"Thời gian tìm kiếm: {search_end_time - search_start_time:.6f} giây")
                return g  # Trả về chi phí tổng

            # Đánh dấu nút là đã mở rộng
            self.closed_list[current] = g

            # Mở rộng nút
            neighbors = self.expand_node(current, g)
            for neighbor, cost in neighbors:
                new_g = g + cost
                f_neighbor = new_g + self.heuristic(neighbor)

                # Nếu nút không có trong closed_list hoặc có chi phí nhỏ hơn
                if neighbor not in self.closed_list or new_g < self.closed_list[neighbor]:
                    self.closed_list[neighbor] = new_g
                    heapq.heappush(self.open_list, (f_neighbor, neighbor, new_g))

                    # Kiểm tra giới hạn bộ nhớ
                    if len(self.open_list) > self.memory_limit:
                        # Loại bỏ nút có f(n) cao nhất
                        self.open_list.pop()

        search_end_time = time.time()
        print(f"Thời gian tìm kiếm: {search_end_time - search_start_time:.6f} giây")

        return None  # Không tìm thấy đường đi
