from graphgen import generate_connected_graph
from smastar import SMAStar
import time
# Sinh đồ thị
V = 6
min_weight, max_weight = 1, 10
graph = generate_connected_graph(V, min_weight, max_weight)

print("Danh sách cạnh của đồ thị:")
for edge in graph:
    print(edge)

# Tìm đường đi với SMA*
start = 0
goal = V - 1
memory_limit = 10

sma_star = SMAStar(graph, start, goal, memory_limit)
start_time = time.time()  # Thời gian bắt đầu
result = sma_star.search()
end_time = time.time()  # Thời gian kết thúc
execution_time = end_time - start_time # Tính thời gian thực thi

if result is not None:
    print(f"Chi phí ngắn nhất từ {start} đến {goal}: {result}")
else:
    print(f"Không tìm thấy đường đi từ {start} đến {goal}.")

print(f"Thời gian thực thi: {execution_time:.6f} giây")




