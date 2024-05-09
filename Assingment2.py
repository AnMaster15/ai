# # q1
# import copy
# # global
# q=[]
# visited=[]

# def find_pos(s):
#     for i in range(len(s)):
#         for j in range(len(s[0])):
#             if s[i][j] ==0 :
#                 return [i,j]


# def up(s):
#     pos = find_pos(s)
#     # print (pos)

#     row = pos[0]
#     col = pos[1]
    
#     # new_state = s

#     new_state = [[0,0,0],[0,0,0],[0,0,0]]

#     new_state = copy.deepcopy(s)

#     # for i in range(len(s)):
#     #     for j in range(len(s[0])):
#     #         new_state=s[i][j]


#     if row > 0:
#         new_state[row][col] = new_state[row-1][col]
#         new_state[row-1][col] = 0
    
#     return new_state

# def down(s):
#     pos = find_pos(s)
#     # print (pos)

#     row = pos[0]
#     col = pos[1]

#     new_state = [[0,0,0],[0,0,0],[0,0,0]]

#     new_state = copy.deepcopy(s)

    
#     if row < 2:
#         new_state[row][col] = new_state[row+1][col]
#         new_state[row+1][col] = 0
    
#     return new_state

# def right(s):
#     pos = find_pos(s)

#     row = pos[0]
#     col = pos[1]

#     new_state = [[0,0,0],[0,0,0],[0,0,0]]

#     new_state = copy.deepcopy(s)

#     if col < 2:
#         new_state[row][col] = new_state[row][col+1]
#         new_state[row][col+1] = 0
#         # s[row][col] = s[row][col+1]
#         # s[row][col+1] = 0
#     return new_state

# def left(s):
#     pos = find_pos(s)

#     row = pos[0]
#     col = pos[1]

#     new_state = [[0,0,0],[0,0,0],[0,0,0]]

#     new_state = copy.deepcopy(s)

#     if col > 0:
#         new_state[row][col] = new_state[row][col-1]
#         new_state[row][col-1] = 0
#         # s[row][col] = s[row][col-1]
#         # s[row][col-1] = 0
#     return new_state


# def compare(s,g):
#     if s==g:
#         return 1
#     else:
#         return 0
        
        
#     # for i in range(len(s)):
#     #     for j in range(len(s[0])):
#     #         if s[i][j] != g[i][j]:
#     #             return 0;
    
#     # return 1;

# def search(g):
#     global visited
#     global q
#     # print(q)
#     count=0
#     print(q)
#     print("\n")
#     while(1):
#     # while(count<=4):
#         s=q[0]
#         del q[0]
#         if count <= 4:

#             if compare (s,g) == 1:
#                 print ("found")
#                 exit()
#             else:
#                 generate_children(s)
#                 visited.append(s)
#         # count+=1
#         print("----------------")
#         print(q)
    


# def generate_children (s):
#     global q
#     global visited

#     new_state = up(s)
#     if new_state not in q and new_state not in visited:
#         q.append(new_state)
    
#     new_state = down(s)
#     if new_state not in q and new_state not in visited:
#         q.append(new_state)
    
#     new_state = left(s)
#     if new_state not in q and new_state not in visited:
#         q.append(new_state)
    
#     new_state = right(s)
#     if new_state not in q and new_state not in visited:
#         q.append(new_state)



# def main() :
#     global q
#     s=[[1,2,3],
#     [8,0,4],
#     [7,6,5]]
    
#     g=[[2,8,1],
#     [0,4,3],
#     [7,6,5]]

#     q.append(s) 

#     search (g)

    
#     # ans = compare(s,g)
#     # print(ans)
#     print (s)
#     print("after up newsstae \n")
    
#     new_state = up(s)
#     print (new_state)

#     print(s)
#     # print("after\n")
#     new_state = down(new_state)
#     print("after new down\n")
#     print(new_state)
#     print("print ori \n")
#     print(s)

    
# main()

# # q2
# from collections import deque

# j1 = int(input("Enter the capacity of j1: "))
# j2 = int(input("Enter the capacity of j2: "))
# t = int(input("Enter the target: "))

# visited = set()

# def waterjug(amt1, amt2):
#     queue = deque([(0, 0)])

#     while queue:
#         current_state = queue.popleft()
#         amt1, amt2 = current_state

#         if (amt1 == t and amt2 == 0):
#             print(current_state)
#             return True

#         if current_state not in visited:
#             visited.add(current_state)

#             print(current_state)

#             next_states = [
#                 (0, amt2),              
#                 (amt1, 0),             
#                 (j1, amt2),             
#                 (amt1, j2),            
#                 (amt1 + min(amt2, j1 - amt1), amt2 - min(amt2, j1 - amt1)),  
#                 (amt1 - min(amt1, (j2 - amt2)), amt2 + min(amt1, (j2 - amt2)))
#             ]

#             for state in next_states:
#                 if state not in visited:
#                     queue.append(state)

#     return False

# print("Steps:")
# waterjug(0, 0)

# q3
from sys import maxsize 
from itertools import permutations
V = 4

def travelling_salesman_problem(graph, start): 
    vertices = [] 
    for i in range(V): 
        if i != start: 
            vertices.append(i) 

    min_path = maxsize 
    next = permutations(vertices)
    for perm in next:
        current_path_weight = 0
        current_vertex = start
        for next_vertex in perm: 
            current_path_weight += graph[current_vertex][next_vertex] 
            current_vertex = next_vertex 
        current_path_weight += graph[current_vertex][start] 

        min_path = min(min_path, current_path_weight)       
    return min_path 

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]] 
start = 0
print(travelling_salesman_problem(graph, start))
