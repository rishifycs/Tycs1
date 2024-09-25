#dfs
adj_list={
    'A':['C','D','B'],
    'C':['A','K'],
    'D':['A','K','L'],
    'K':['C','D','L'],
    'L':['K','D','J'],
    'J':['M'],
    'B':['A'],
    'M':['J']
    }
visited={}
level={}
parent={}
dfs_traversal=[]
stack=[]
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
source=input("Enter the exact source node to start:")
visited[source]=True
level[source]=True
stack.append(source)
while stack:
    u=stack.pop()
    dfs_traversal.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            stack.append(v)
print("DFS Traversal:",dfs_traversal)
target = input("Enter the exact destination node to reach:")
path=[]
if visited[target]:
    node=target
    while node is not None:
        path.append(node)
        node=parent[node]
    path.reverse()
print("Minimum path from source to destination:",'->'.join(path))


