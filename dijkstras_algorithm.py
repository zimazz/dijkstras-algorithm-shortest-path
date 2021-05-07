#Graph hash table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

#Weight hash table
infinity = float("inf")
weights = {}
weights["a"] = 6
weights["b"] = 2
weights["fin"] = infinity


#Parents hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#An array to keep track of all the nodes that have been processed
processed = []

#this function takes a dictionary as input and return the node/ key with lowest weight/value
def find_lowest_weight_node(weights):
    lowest_weight = float("inf")
    lowest_weight_node = None
    for node in weights:
        weight = weights[node]
        if weight < lowest_weight and node not in processed:
            lowest_weight_node = weight
            lowest_weight_node = node
    return lowest_weight_node


node = find_lowest_weight_node(weights)                     #get the first lowest-weight node 

while node is not None:                                     #if you've processed all the nodes, this while loop is done.
    weight = weights[node]                                  #get the weight of that node
    neighbors = graph[node]                                 #get all the neighbors of that node
    for n in neighbors.keys():                              #loop over those neighbors
        new_weight = weight + neighbors[n]                  #get the total weight from the starting point
        if weights[n] > new_weight:                         #if the new_weight is less than the original weight of that node
            weights[n] = new_weight                         #update the weight to the new_wight
            parents[n] = node                               #This node becomes the new parent for this neighbor 
    processed.append(node)                                  #Mark the node as processed
    node = find_lowest_weight_node(weights)                 #Find the next node to process, and loop

print(parents)
