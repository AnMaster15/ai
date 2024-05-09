# q1-3

import copy
import heapq

def found_empty(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return i, j
            
def misplaced_tiles(start,goal):
    tile=0
    for i in range(len(start)):
        for j in range(len(start[i])):
            if(start[i][j]!=goal[i][j] and start[i][j]==0):
                tile=+1
    return tile

def up(start):
    new_start=copy.deepcopy(start)
    row,col=found_empty(start)
    if row>0:
        new_start[row][col]=new_start[row-1][col]
        new_start[row-1][col]=0
        return new_start
    else:
        return start
    
def down(start):
    new_start=copy.deepcopy(start)
    row,col=found_empty(start)
    if row<2:
        new_start[row][col]=new_start[row+1][col]
        new_start[row+1][col]=0
        return new_start
    else:
        return start
    
def left(start):
    new_start=copy.deepcopy(start)
    row,col=found_empty(start)
    if col>0:
        new_start[row][col]=new_start[row][col-1]
        new_start[row][col-1]=0
        return new_start
    else:
        return start
    

def right(start):
    new_start=copy.deepcopy(start)
    row,col=found_empty(start)
    if col<2:
        new_start[row][col]=new_start[row][col+1]
        new_start[row][col+1]=0
        return new_start 
    else:
        return start

def best_first_search(start, goal):
    visited = []
    heap = [(misplaced_tiles(start, goal), start, [])]
    heapq.heapify(heap)

    while heap:
        _,state, path = heapq.heappop(heap)
        if state == goal:
            return path + [state]
        visited.append(state)
        for move in [up, down, left, right]:
            new_state = move(state)
            if new_state not in visited:
                heapq.heappush(heap, (misplaced_tiles(new_state, goal), new_state, path + [state]))
    return None
        
def hill_climbing(start, goal):
    visited = []
    current_state = start

    while current_state != goal:
        visited.append(current_state)

        possible_moves = [move(current_state) for move in [up, down, left, right] if move(current_state)]
        
        best_neighbor = min(possible_moves, key=lambda neighbor: misplaced_tiles(neighbor, goal), default=None)
        
        if not best_neighbor or misplaced_tiles(best_neighbor, goal) >= misplaced_tiles(current_state, goal):
            return None
        
        current_state = best_neighbor

    visited.append(current_state) 
    return None

def astar_search(start, goal):
    visited = []
    heap = [(misplaced_tiles(start, goal), 0, start, [])] 
    heapq.heapify(heap)

    while heap:
        _, cost, state, path = heapq.heappop(heap)
        if state == goal:
            return path + [state]

       
        visited.append(state)
        for move_func in [up, down, left, right]:
            new_state = move_func(state)
            if new_state is not None and new_state not in visited:
                new_cost = cost + 1 
                heapq.heappush(heap, (new_cost + misplaced_tiles(new_state, goal), new_cost, new_state, path + [state]))

    return None

def main():
    start=[[2,0,3],[1,8,4],[7,6,5]]
    goal=[[1,2,3],[8,0,4],[7,6,5]]
    print('start')
    print(start)
    print('goal')
    print(goal)
    
    print('Steps to get the answer')
    # result=best_first_search(start, goal)
    result= hill_climbing(start, goal)
    # result=astar_search(start, goal)
    if result:
        print("Result found:")
        for state in result:
            print("Misplaced tiles:", misplaced_tiles(state, goal))
            print(state)
    else:
           print("Solution not found.")
main()

#q4
def calculate_path_cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        and_nodes = condition['AND']
        path_a = sum(H[node] + weight for node in and_nodes)
        cost[' AND '.join(and_nodes)] = path_a
    
    if 'OR' in condition:
        or_nodes = condition['OR']
        path_b = min(H[node] + weight for node in or_nodes)
        cost[' OR '.join(or_nodes)] = path_b
    return cost

def update_cost_and_get_least(conditions, H, weight=1):
    least_cost = {}
    for key in reversed(conditions):
        condition = conditions[key]
        print(f"{key}: {condition} >>> {calculate_path_cost(H, condition, weight)}")
        cost = calculate_path_cost(H, condition, weight)
        H[key] = min(cost.values())
        least_cost[key] = calculate_path_cost(H, condition, weight)
    return least_cost

def get_shortest_path(start, updated_cost, H):
    path = start
    if start in updated_cost:
        min_cost = min(updated_cost[start].values())
        min_key = min(updated_cost[start], key=updated_cost[start].get)
        next_nodes = min_key.split()

        if len(next_nodes) == 1:
            start = next_nodes[0]
            path += '<--' + get_shortest_path(start, updated_cost, H)
        else:
            path += '<--(' + min_key + ') '
            start = next_nodes[0]
            path += '[' + get_shortest_path(start, updated_cost, H) + ' + '
            start = next_nodes[-1]
            path += get_shortest_path(start, updated_cost, H) + ']'
    return path

H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

weight = 1
print('Updated Cost:')
updated_cost = update_cost_and_get_least(conditions, H, weight)
print('*' * 75)
print('Shortest Path:\n', get_shortest_path('A', updated_cost, H))
