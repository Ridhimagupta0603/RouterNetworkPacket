'''
Solution :
Firstly we make an adjancency list with given vertices and edges. Now Starting from the source We iterate to its neighbours and check
if the value assigned to them(if already otherwise -inf) is greater than the minimum of the current assigned maximum capacity to reach at current 
and the capacity of the link joining them . If it is then we leave it as it is , if not then we shift its parent to current value and then reassign 
it new value of capacity.
We also mark the current vertex done so that we don't iterate over it again.
Now we extract the maximum capacity from the heap and check if it is not processed then repeat and if the popped value is the destination we break the loop

'''

class Maxheappriority():
    def __init__(self):
        self._maxheap = []
    def push(self, capind):
        self._maxheap.append(capind)
        self._heapup(self._maxheap, len(self) - 1)
    def pop(self):
        if self.empty():
            raise Warning('Heap is empty')
        else:
            self._switch(self._maxheap, len(self) - 1, 0)
            top = self._maxheap.pop()
            self._heapdown(self._maxheap, 0)
            return top
    def __len__(self):
        return len(self._maxheap)
    def empty(self):
        return len(self._maxheap)==0
    def top(self):
        if self.empty():
            raise Warning('Heap is empty')
        else:
            return(self._maxheap[0])
    def _switch(self,maxheap, i, j):
        maxheap[i], maxheap[j] = maxheap[j], maxheap[i]
    def _heapup(self,maxheap,pos):
        parent = (pos-1) // 2
        if parent < 0:
            return
        if maxheap[pos][0] > maxheap[parent][0]:
            self._switch(maxheap, pos,parent)
            self._heapup(maxheap, parent)
    def _heapdown(self,maxheap,pos):
        child = 2 * pos + 1
        rightchild=2 * pos + 2
        if child >= len(maxheap):
            return
        if rightchild< len(maxheap) and maxheap[child][0] < maxheap[rightchild][0]:
            child =rightchild
        if maxheap[child][0] > maxheap[pos][0]:
            self._switch(maxheap, child, pos)
            self._heapdown(maxheap, child)
class Graph():#O(m)
    def __init__(self,n,links):
        self.vertices=n
        self.adj=[[]for i in range(n)]
        for i in range(len(links)):
            j=links[i][0]
            k=links[i][1]
            cap=links[i][2]
            
            (self.adj[j]).append((k,cap))
            (self.adj[k]).append((j,cap))
            
def findMaxCapacity(n,links,s,t):
    g=Graph(n,links)
    maxmincap=Maxheappriority()
    parent=[-1]*n
    capacityuptil=[0]*n
    done=[False]*n
    for i in range(n):  #O(m)                   
        capacityuptil[i] = float('-inf')                       
        parent[i]= -1                          
    capacityuptil[s]= float('inf')  
    maxmincap.push((float('inf'),s))
    while not maxmincap.empty():#O(m) overallas We can say that O(V)is O(E)
        u=maxmincap.pop()
        cur=u[1]
        curcap=u[0]
        if cur==t:
            break
        if done[cur]==False:
            for v in g.adj[cur]:#O(m) overall
                if done[v[0]]==False:
                    alt=max(capacityuptil[v[0]],min(curcap,v[1]))
                    if alt > capacityuptil[v[0]]:                                
                        capacityuptil[v[0]] = alt 
                        parent[v[0]] = cur
                        maxmincap.push((alt,v[0]))#O(mlogm) overall
            done[cur]=True
       #To print path and capacity we backtrack as follows
    p=t
    path=[t]
    mint=capacityuptil[t]
    while p!=s:#O(m)
        if capacityuptil[p]<mint:
            mint=capacityuptil[p]
        p=parent[p]
        path.append(p)
    path.reverse()
    return (mint,path)
    #Thus Overall O(mlogm)
