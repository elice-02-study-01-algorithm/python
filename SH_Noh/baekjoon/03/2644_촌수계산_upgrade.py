import sys

input = sys.stdin.readline

# Get input.
n = int(input())
s, e = map(int, input().split())
m = int(input())

# Get edge.
edge = [[] for _ in range(n+1)]
for i in range(m):
	a, b = map(int, input().split())
	edge[a].append(b)
	edge[b].append(a)

# Make array for distance and visit.
visit = [0 for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]

#BFS
q = [s]
visit[s] = 1
dist[s] = 0
for here in q:
	for there in edge[here]:
            # print(here)
            if not visit[there]:
                visit[there] = 1
                q.append(there)
                print(there)
                dist[there] = dist[here] + 1

#print answer
print(dist[e])