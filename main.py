from smastar import sma_star
from graphgen import generate_named_graph
from solve import dijkstra
import time
import random
# Định nghĩa graph và heuristic
graph = {
    'S': [('A', 4), ('B', 5), ('C', 6)],
    'A': [('G', 5)],
    'B': [('G', 3)],
    'C': [('G', 1)],
    'G': []
}
# heuristic = {
#     'A': 3,
#     'B': 1,
#     'C': 1,
#     'D': 1,
#     'E': 0
# }


# Ví dụ sử dụng:
node_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
heuristic = {letter: random.randint(0, 5) for letter in node_names}
g = generate_named_graph(node_names, min_weight=1, max_weight=10)
print(g)

# heuristic = heuristic_degree(g)

start = 'A'
goal = 'T'
memory_limit = min(len(node_names) - 1, 100)


# Chạy thuật toán SMA* và tính thời gian
start_time = time.time()  # Lấy thời gian bắt đầu
result = sma_star(start, goal, g, heuristic, memory_limit)
end_time = time.time()  # Lấy thời gian kết thúc

# Tính thời gian thực thi
execution_time = end_time - start_time

# In kết quả và thời gian
print("Kết quả:", result)
print(f"Thời gian thực thi: {execution_time:.6f} giây")


# Hàm chạy thử nghiệm

# print("Generated Graph:")
# for key, value in graph.items():
#     print(f"{key}: {value}")

# start = 'S'
# goal = 'G'
start_time = time.time() 
shortest_distance, shortest_path = dijkstra(g, start, goal)
end_time = time.time()  
execution_time = end_time - start_time

# In kết quả và thời gian
print("Kết quả:", result)
print(f"Thời gian thực thi: {execution_time:.6f} giây")

print("\nDijkstra Result:")
print(f"Shortest distance from {start} to {goal}: {shortest_distance}")
print(f"Shortest path: {shortest_path}")


