# q1-4
import copy
from collections import deque

visited = []
stack = []
q=deque()


def dfs(s, g):
    stack.append(s)
    while True:
        curr = stack.pop()
        visited.append(curr)
        print("Steps are: ")
        print(curr)
        if curr in g:
            # print()
           
            print("found")
            print(curr)
            return

        curr1 = copy.deepcopy(curr)
        curr2 = copy.deepcopy(curr)
        curr3 = copy.deepcopy(curr)
        curr4 = copy.deepcopy(curr)
        curr5 = copy.deepcopy(curr)
        curr6 = copy.deepcopy(curr)

        if curr1[0]:
            curr1[1].append(curr1[0].pop())
            if curr1 not in visited:
                stack.append(curr1)

        if curr2[0]:
            curr2[2].append(curr2[0].pop())
            if curr2 not in visited:
                stack.append(curr2)

        if curr3[1]:
            curr3[2].append(curr3[1].pop())
            if curr3 not in visited:
                stack.append(curr3)

        if curr4[1]:
            curr4[0].append(curr4[1].pop())
            if curr4 not in visited:
                stack.append(curr4)

        if curr5[2]:
            curr5[0].append(curr5[2].pop())
            if curr5 not in visited:
                stack.append(curr5)

        if curr6[2]:
            curr6[1].append(curr6[2].pop())
            if curr6 not in visited:
                stack.append(curr6)

        if not stack:
            print("State can't be achieved")
            return


def bfs(s, g):
    q.append(s)
    while True:
        curr = q.popleft()
        visited.append(curr)
        print("Steps are: ")
        print(curr)
        if curr in g:
            print()
            print(curr)
            print("found")
            return

        curr1 = copy.deepcopy(curr)
        curr2 = copy.deepcopy(curr)
        curr3 = copy.deepcopy(curr)
        curr4 = copy.deepcopy(curr)
        curr5 = copy.deepcopy(curr)
        curr6 = copy.deepcopy(curr)

        if curr1[0]:
            curr1[1].append(curr1[0].pop())
            if curr1 not in visited:
                q.append(curr1)

        if curr2[0]:
            curr2[2].append(curr2[0].pop())
            if curr2 not in visited:
                q.append(curr2)

        if curr3[1]:
            curr3[2].append(curr3[1].pop())
            if curr3 not in visited:
                q.append(curr3)

        if curr4[1]:
            curr4[0].append(curr4[1].pop())
            if curr4 not in visited:
                q.append(curr4)

        if curr5[2]:
            curr5[0].append(curr5[2].pop())
            if curr5 not in visited:
                q.append(curr5)

        if curr6[2]:
            curr6[1].append(curr6[2].pop())
            if curr6 not in visited:
                q.append(curr6)

        if not q:
            print("State can't be achieved")
            return


def dis(s, g, depth_limit):
    stack = [(s, 0)]  # Tuple of (node, depth)
    visited = []

    while stack:
        curr, depth = stack.pop()
        visited.append(curr)

        if depth > depth_limit:
            continue

        print("Steps are: ")
        print(curr)

        if curr in g:
            print()
            print(curr)
            print("found")
            return True

        curr1 = copy.deepcopy(curr)
        curr2 = copy.deepcopy(curr)
        curr3 = copy.deepcopy(curr)
        curr4 = copy.deepcopy(curr)
        curr5 = copy.deepcopy(curr)
        curr6 = copy.deepcopy(curr)

        if curr1[0]:
            curr1[1].append(curr1[0].pop())
            if curr1 not in visited:
                stack.append((curr1, depth + 1))

        if curr2[0]:
            curr2[2].append(curr2[0].pop())
            if curr2 not in visited:
                stack.append((curr2, depth + 1))

        if curr3[1]:
            curr3[2].append(curr3[1].pop())
            if curr3 not in visited:
                stack.append((curr3, depth + 1))

        if curr4[1]:
            curr4[0].append(curr4[1].pop())
            if curr4 not in visited:
                stack.append((curr4, depth + 1))

        if curr5[2]:
            curr5[0].append(curr5[2].pop())
            if curr5 not in visited:
                stack.append((curr5, depth + 1))

        if curr6[2]:
            curr6[1].append(curr6[2].pop())
            if curr6 not in visited:
                stack.append((curr6, depth + 1))

    return False

def iterative_deepening_dfs(s, g):
    depth_limit = 0
    while True:
        print("Depth Limit:", depth_limit)
        found = dis(s, g, depth_limit)
        if found:
            break
        else:
            depth_limit += 1

def main():
    s = [['a'], ['b', 'c'], []]
    g = [[['a', 'b', 'c'], [], []], [[], ['a', 'b', 'c'], []], [[], [], ['a', 'b', 'c']]]
    # dfs(s, g)
    bfs(s, g)
    # dls(s,g,4)
    # iterative_deepening_dfs(s,g)

if __name__ == "__main__":
    main()




# q5
import heapq

def addedge(vertices, start, end, cost):
    if start not in vertices:
        vertices[start] = []
    vertices[start].append((end, cost))

def ucs(vertices, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path + [node]
 
        if node not in visited:
            visited.add(node)
            if node in vertices:
                for neighbor, edge_cost in vertices[node]:
                    if neighbor not in visited:
                        heapq.heappush(pq, (cost + edge_cost, neighbor, path + [node]))

    return -1, []

vertices = {}
addedge(vertices, 'S', 'A', 1)
addedge(vertices, 'S', 'C', 15)
addedge(vertices, 'S', 'B', 5)
addedge(vertices, 'A', 'G', 10)
addedge(vertices, 'B', 't', 5)
addedge(vertices, 'C', 'G', 5)

start_node = 'S'
goal_node = 'G'

cost, path = ucs(vertices, start_node, goal_node)
if cost != -1:
    print(f"Minimum Cost from {start_node} to {goal_node}: {cost}")
    print("Path:", ' -> '.join(path))
else:
    print("Goal is not reachable")
