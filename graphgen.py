import random
from collections import defaultdict

def generate_named_graph(node_names, min_weight=1, max_weight=10):
    """
    Tạo đồ thị một chiều với định dạng giống như yêu cầu, sử dụng tên cho các đỉnh.
    Bao gồm bước kiểm tra và sửa consistency.
    
    Args:
        node_names (list): Danh sách tên của các đỉnh, ví dụ: ['S', 'A', 'B', 'C', 'G']
        min_weight (int): Trọng số nhỏ nhất cho cạnh.
        max_weight (int): Trọng số lớn nhất cho cạnh.

    Returns:
        dict: Đồ thị dưới dạng dictionary.
    """
    graph = {node: [] for node in node_names}  # Khởi tạo đồ thị rỗng
    n = len(node_names)
    
    # Tạo cây khung liên thông để đảm bảo kết nối
    for i in range(1, n):
        u = node_names[i]
        v = random.choice(node_names[:i])  # Kết nối với một đỉnh đã có trước đó
        weight = random.randint(min_weight, max_weight)
        graph[v].append((u, weight))  # Thêm cạnh từ v đến u

    # Thêm cạnh ngẫu nhiên
    additional_edges = random.randint(n - 1, 2 * n)  # Số cạnh bổ sung
    while additional_edges > 0:
        u, v = random.sample(node_names, 2)  # Chọn hai đỉnh khác nhau
        if not any(neighbor == v for neighbor, _ in graph[u]):  # Kiểm tra cạnh trùng lặp
            weight = random.randint(min_weight, max_weight)
            graph[u].append((v, weight))
            additional_edges -= 1

    # Kiểm tra và sửa consistency
    def check_and_fix_consistency():
        # Tạo danh sách kề từ graph
        adj_list = defaultdict(list)
        for u in graph:
            for v, w in graph[u]:
                adj_list[u].append((v, w))
                adj_list[v].append((u, w))  # Đảm bảo danh sách là hai chiều
        
        for u in adj_list:
            for v, w_uv in adj_list[u]:
                for w, w_uw in adj_list[u]:
                    if v == w: continue  # Bỏ qua nếu là chính nó
                    for x, w_vw in adj_list[v]:
                        if x == u or x == w: continue
                        # Sửa trọng số nếu không thỏa mãn consistency
                        if w_uv > w_uw + w_vw:
                            for i, (t, weight) in enumerate(graph[u]):
                                if t == v:
                                    graph[u][i] = (v, w_uw + w_vw)  # Cập nhật trọng số
                                    break
    
    check_and_fix_consistency()

    return graph


