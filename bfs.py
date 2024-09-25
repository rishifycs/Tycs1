#BFS Algorithm
from queue import Queue
adj_list={
    "M":["N","Q","R"],
    "N":["M","O","Q"],
    "O":["N","P"],
    "P":["O","Q"],
    "Q":["M","N","P"],
    "R":["M"]
    }
visited={}
level={}
parent={}
bfs_traversal=[]
queue=Queue()
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
print("Before Traversal")
print("visited:",visited)
print("level:",level)
print("parent:",parent)
source="M"
visited[source]=True
level[source]=0
queue.put(source)
while not queue.empty():
    u=queue.get()
    bfs_traversal.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print("After Traversal")
print("BFS Traversal:",bfs_traversal)
print("Minimum Distance")
print("Level N:",level["N"])
print("Level O:",level["O"])
print("Parent M:",parent["M"])
print("Parent P:",parent["P"])
node="O"
path=[]
while node is not None:
    path.append(node)
    node=parent[node]
path.reverse()
print("Shortest Path is:",path)


