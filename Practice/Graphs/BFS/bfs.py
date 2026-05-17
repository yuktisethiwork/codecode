# Practice: BFS
# Language: python3
# Date: 17/05/2026


from collections import deque

edges=[(1,2), (2,3), (3,4), (3,5), (2,5)]
alist={}
for i, j in edges:
    if i not in alist:
        alist[i] = []
    if j not in alist:
        alist[j] = []
    alist[i].append(j)
    

def bfs(s,alist):
    level={}
    parent={}
    for i in alist.keys():
        parent[i]=None
        level[i]=-1
    q=deque()
    level[s]=0
    parent[s]=0
    q.append(s)
    while q:
        j=q.popleft()
        for k in alist[j]:
            if level[k]==-1:
                q.append(k)
                parent[k]=j
                level[k]=level[j]+1
                
    return level,parent
level,parent = bfs(1,alist)
print(level,parent)