from queue import PriorityQueue


graph = {'Oradea':{'Zerind':71,'Sibiu':151},'Zerind':{'Oradea':71,'Arad':75},
          'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},
          'Timisoara':{'Arad':118,'Lugoj':111},
          'Lugoj':{'Timisoara':111,'Mehadia':70},
          'Mehadia':{'Lugoj':70,'Dobreta':70},
          'Dobreta':{'Mehadia':75,'Craiova':120},
          'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},
          'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu Vilcea':80,'Fagaras':99},
          'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},
          'Fagaras':{'Sibiu':99,'Bucharest':221},
          'Pitesti':{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},
          'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
          'Giurgiu':{'Bucharest':90},
          'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
          'Hirsova':{'Urziceni':98,'Eforie':86},
          'Eforie':{'Hirsova':86},
          'Vaslui':{'Urziceni':142,'Iasi':92},
          'Iasi':{'Neamt':87,'Vaslui':92},
          'Neamt':{'Iasi':87}}
heuristic = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242, 'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374}

start = 'Arad'
goal = 'Bucharest'

shortestPaths={}

path =[]
for x in graph.keys():
    shortestPaths[x] = 100000000000

pq = PriorityQueue() 

shortestPaths[start] = 0 

pq.put((0+heuristic[start],start)) 
       


while not pq.empty(): 
    u = pq.get()    
    u = u[1]   
    if u == goal:  
        break
    for v in graph[u].keys():  
        if shortestPaths[v] > shortestPaths[u] + graph[u][v]: 
            shortestPaths[v] = shortestPaths[u] + graph[u][v] 
            pq.put((shortestPaths[v]+heuristic[v],v))
            path.append(v)



    
# print(shortestPaths)
print(path)
print("Arad to Bucharest distance",shortestPaths['Bucharest'])  


