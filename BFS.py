import timeit

adjacent = []
visited = []
path = []

def create(n):
    global adjacent
    adjacent = [[0]*n for _ in range(n)]
    global visited
    visited = [False]*n

def fill():
    global adjacent, n
    for i in range(n):
        for j in range(n):
            if i != j and adjacent[i][j] != 1:
                while True:
                    try:
                        temp = int(input("Are nodes {} and {} connected? (Enter 0 for No, 1 for Yes): ".format(i, j)))
                        if temp == 0 or temp == 1:
                            adjacent[i][j] = temp
                            adjacent[j][i] = temp
                            break
                        else:
                            print("Invalid input. Please enter 0 or 1.")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

def bfs(start, end):
    global path
    queue = [start]
    visited[start] = True
    while queue:
        current = queue.pop(0)
        path.append(current)
        if current == end:
            print("Path exists from {} to {}".format(start, end))
            print(path)
            return
        for i in range(n):
            if adjacent[current][i] == 1 and not visited[i]:
              queue.append(i)
              visited[i] = True
              if i==end:
                path.append(i)
                print(path)
                return
    print("Path does not exist from {} to {}".format(start, end))


while True:
    try:
        n = int(input("Enter the number of nodes: "))
        if n <= 0:
            print("Number of nodes must be greater than 0. Please enter a valid number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

create(n)

while True:
    try:
        fill()
        break
    except KeyboardInterrupt:
        # Allow the user to interrupt the filling process
        print("Filling interrupted. Please restart the filling process.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

print(adjacent)

while True:
    try:
        start_node = int(input("Enter the start node: "))
        if 0 <= start_node < n:
            break
        else:
            print("Invalid node. Please enter a valid node index.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        end_node = int(input("Enter the end node: "))
        if 0 <= end_node < n:
            break
        else:
            print("Invalid node. Please enter a valid node index.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Measure time taken to perform BFS
bfs_time = timeit.timeit(stmt=lambda: bfs(start_node, end_node), number=1)
print(f"Time taken for BFS: {bfs_time:.6f} seconds")
