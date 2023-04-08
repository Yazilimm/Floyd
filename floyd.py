
def printPath (path,v,u,route):
    if path[v][u] == v:
        return;
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
    
def printSolution(path,n):
    for v in range(n):
        for u in range(n):
            if u!=v and path[v][u] !=-1:
                route=[v]
                printPath(path,v,u,route)
                route.append(u)
                print(f'the shortest path from {v} -> {u} is', route)
                
def floydWarshall(adjMatrix): 
    
    if not adjMatrix:
        return
    
    n= len(adjMatrix)
    
    cost=adjMatrix.copy()
    path =[[None for x in range(n)] for y in range(n)]
    
    #maliyet ve yolu başlat
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u]==0
            elif cost[v][u] != float('inf'):
                path[v][u]=v
            else:
                path[v][u]= -1
                
                
#floyd çalıştır 
    for k in range(n):
        for v in range(n):
            for u in range(n):
                
                if cost[v][u]!=float('inf ') and cost[k][u] !=float('inf') and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u]=cost[v][k]+ cost[k][u]
                    path[v][u]= path[k][u]
                    
            if cost[v][v] < 0:
                print("negative weight cycle found")
                return
            
    printSolution(path,n)
    
if __name__=='__main__':
    
    I=float('inf')


    adjMatrix=[ 
               [0, 4, I , 5 , I, I ,2,I , I],
               [4, 0,I, 9,I, 3, 1 ,5,I],
               [I, I,0, 2,1, 3, I ,I,3],
               [5, 9, 2, 0, I, 2, 1, I,I],
               [I, I,1, I,0, I, I ,1,2],
               [I, 3, 3, 2, I, 0, I, 2,I],
               [2, 1, I, 1, I, I, 0, I,I],
               [I, 5, I, I, 1, 2, I, 0,1],
               [I, I, 3, I, 2, I, I, 1,0],
               ]
floydWarshall(adjMatrix)


                      
                   