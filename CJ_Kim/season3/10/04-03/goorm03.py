# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
island, bridge, max_bridge = map(int, input().split())
island_info = [[] for _ in range(island+1)]
for _ in range(bridge):
	a, b = map(int, input().split())
	island_info[a].append(b)
	island_info[b].append(a)

def BFS(map_info, start, end):
	visited = [start]
	queue = [start]
	while queue:
		cur_node = queue.pop(0)
		if end in map_info[cur_node]:
			visited.append(end)
			return visited
		for next_node in map_info[cur_node]:
			if next_node not in visited and end in map_info[next_node]:
				visited.append(next_node)
				visited.append(end)
				return visited
		for next_node in map_info[cur_node]:
			if next_node not in visited:
				visited.append(next_node)
				queue.append(next_node)
	return visited

visited = BFS(island_info, 1, island)

if island in visited:
	min_bridge = visited.index(island)
	if min_bridge<=max_bridge:
		print("YES")
	else:
		print("NO")
else:
	print("NO")

# 정답률 약 60%


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import heapq
island, bridge, max_bridge = map(int, input().split())
island_info = [[] for _ in range(island+1)]
for _ in range(bridge):
	a, b = map(int, input().split())
	island_info[a].append(b)
	island_info[b].append(a)

dist = [float('inf') for _ in range(island+1)]

def shortest(map_info, start):
	queue = []
	heapq.heappush(queue, (0, start))
	dist[start] = 0
	
	while queue:
		distance, current = heapq.heappop(queue)
		if dist[current] < distance: continue
		
		for i in map_info[current]:
			cost = dist[current] + 1
			if cost < dist[i]:
				dist[i] = cost
				heapq.heappush(queue, (cost, i))
	
shortest(island_info, 1)

if dist[island] <= max_bridge:
	print("YES")
else:
	print("NO")