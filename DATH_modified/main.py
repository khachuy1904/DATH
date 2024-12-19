from smastar import sma_star
from graphgen import generate_named_graph
from solve import dijkstra
import time
import random


'''
graph = {
    'A': [('B', 2), ('C', 4)], 
    'B': [('D', 4)], 
    'C': [('A', 4), ('D', 5)], 
    'D': [('T', 4), ('C', 1), ('A', 5)], 
    'T': [('C', 2), ('A', 5), ('D', 4), ('B', 3)]}
'''


node_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
start = 'A'
goal = 'T'
heuristic = {letter: abs(ord(letter) - ord(goal)) for letter in node_names}
g = generate_named_graph(node_names, min_weight=1, max_weight=10)
print(g)

# heuristic = heuristic_degree(g)

memory_limit = min(len(node_names), 100)


# Chạy thuật toán SMA* và tính thời gian
start_time_sma_star = time.time()  # Lấy thời gian bắt đầu
result = sma_star(start, goal, g, heuristic, memory_limit)
end_time_sma_star = time.time()  # Lấy thời gian kết thúc

# Tính thời gian thực thi
execution_time_sma_star = end_time_sma_star - start_time_sma_star

# In kết quả và thời gian
print("Kết quả:", result)
print(f"Thời gian thực thi: {execution_time_sma_star:.6f} giây")


# Hàm chạy thử nghiệm

# print("Generated Graph:")
# for key, value in graph.items():
#     print(f"{key}: {value}")

# start = 'S'
# goal = 'G'
start_time_dijkstra = time.time() 
shortest_distance, shortest_path = dijkstra(g, start, goal)
end_time_dijkstra = time.time()  
execution_time_dijkstra = end_time_dijkstra - start_time_dijkstra


print("\nDijkstra Result:")
print(f"Shortest distance from {start} to {goal}: {shortest_distance}")
print(f"Shortest path: {shortest_path}")
print(f"Thời gian thực thi: {execution_time_dijkstra:.6f} giây")


