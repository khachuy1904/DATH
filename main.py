from smastar import sma_star
from graphgen import generate_named_graph
import time
# Định nghĩa graph và heuristic
graph = {
    'S': [('A', 4), ('B', 5), ('C', 6)],
    'A': [('G', 5)],
    'B': [('G', 3)],
    'C': [('G', 1)],
    'G': []
}
heuristic = {
    'S': 3,
    'A': 1,
    'B': 1,
    'C': 1,
    'G': 0
}

# Ví dụ sử dụng:
node_names = ['S', 'A', 'B', 'C', 'G','H', 'O']
g = generate_named_graph(node_names, min_weight=1, max_weight=10)
print(g)

start = 'S'
goal = 'G'
memory_limit = 3


# Chạy thuật toán SMA* và tính thời gian
start_time = time.time()  # Lấy thời gian bắt đầu
result = sma_star(start, goal, g, heuristic, memory_limit)
end_time = time.time()  # Lấy thời gian kết thúc

# Tính thời gian thực thi
execution_time = end_time - start_time

# In kết quả và thời gian
print("Kết quả:", result)
print(f"Thời gian thực thi: {execution_time:.6f} giây")

