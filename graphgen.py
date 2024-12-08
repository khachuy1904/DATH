import random
from collections import defaultdict

def generate_connected_graph(V, min_weight=1, max_weight=10):
    # Bước 1: Sinh cây khung liên thông
    edges = set()
    nodes = list(range(V))
    random.shuffle(nodes)  # Sắp xếp ngẫu nhiên các đỉnh để tạo cây khung
    for i in range(1, V):
        u = nodes[i]
        v = random.choice(nodes[:i])  # Kết nối với một đỉnh đã có
        weight = random.randint(min_weight, max_weight)
        edges.add((u, v, weight))
    
    # Bước 2: Thêm cạnh ngẫu nhiên (không quá đầy đủ)
    additional_edges = random.randint(V, V * 2)  # Số cạnh bổ sung
    while len(edges) < additional_edges:
        u, v = random.sample(range(V), 2)  # Chọn hai đỉnh khác nhau
        if u > v: u, v = v, u  # Đảm bảo thứ tự
        # Sửa lỗi: Kiểm tra cạnh trùng lặp
        if not any(e[:2] == (u, v) for e in edges):
            weight = random.randint(min_weight, max_weight)
            edges.add((u, v, weight))
    
    # Bước 3: Kiểm tra và sửa consistency
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    def check_and_fix_consistency():
        for u in range(V):
            for v, w_uv in adj_list[u]:
                for w, w_uw in adj_list[u]:
                    for x, w_vw in adj_list[v]:
                        if x == u or w == v: continue
                        if w_uv > w_uw + w_vw:
                            for i, (t, w_t) in enumerate(adj_list[u]):
                                if t == v:
                                    adj_list[u][i] = (v, w_uw + w_vw)
                                    break

    check_and_fix_consistency()
    
    # Bước 4: Trả về danh sách cạnh
    final_edges = []
    for u in adj_list:
        for v, weight in adj_list[u]:
            if u < v:
                final_edges.append((u, v, weight))
    
    return final_edges


