from prefect import task, flow

@task(log_prints=True)
def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    connections = []
    for line in lines[1:]:
        parent, demand, capacity = map(int, line.split())
        connections.append((parent, demand, capacity))
    return n, connections

#Create graph, demands, and capacities
@flow(log_prints=True)
def max_houses_powered(n, connections):
    graph = [[] for _ in range(n + 1)] 
    demands = [0] * (n + 1)
    capacities = [0] * (n + 1)
    
    #Populate graph, demands, and capacities
    for i, (parent, demand, capacity) in enumerate(connections, start=1):
        graph[parent].append(i)
        demands[i] = demand
        capacities[i] = capacity
    
    #Function to calculate powered houses and total demand
    @task(log_prints=True)
    def house_power_demand(node, visited=set()):
        if node in visited:
            return 0, 0
        visited.add(node)
        
        total_demand = demands[node]
        powered_houses = 0
        
        for child in graph[node]:
            child_powered, child_demand = house_power_demand(child, visited)
            powered_houses += child_powered
            total_demand += child_demand
        
        #Check if the node can power its subtree
        if total_demand <= capacities[node] or node == 0:
            return powered_houses + 1, 0  #Node powers its subtree
        
        return powered_houses, total_demand  #Node cannot power its subtree
    

    powered_houses, _ = house_power_demand(0)
    return powered_houses - 1  #Subtract 1 to exclude the generator

#Input
input = """3
0 3 2
0 100 100
1 1 1"""

#Calculate result
n, connections = parse_input(input)
print(max_houses_powered(n, connections))