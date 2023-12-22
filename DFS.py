import timeit

adjacent = []
visited =[]
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
      if i!=j and adjacent[i][j]!=1:
        temp = int(input("Are nodes {} and {} connected? ".format(i, j)))
        if temp == 1:
          adjacent[i][j] = 1
          adjacent[j][i] = 1

def dfs(start, end):
  global path
  queue = [start]
  visited[start] = True
  while queue:
    print(queue)
    current = queue.pop()
    path.append(current)
    if current == end:
      print("Path exists from {} to {}".format(start, end))
      print(path)
      return
    for i in range(n):
      if adjacent[current][i] == 1 and not visited[i]:
        print(queue,i)
        queue.append(i)
        visited[i] = True
  print("Path does not exist from {} to {}".format(start, end))

n = int(input("Enter the number of nodes: "))
create(n)
fill()
print(adjacent)
start_node = int(input("Enter the start node: "))
end_node = int(input("Enter the end node: "))

# Measure time taken to perform DFS
dfs_time = timeit.timeit(stmt=lambda: dfs(start_node, end_node), number=1)
print(f"Time taken for DFS: {dfs_time:.6f} seconds")
