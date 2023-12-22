import heapq

# Size of the puzzle board
N = 3

# Node class represents a state in the search space
class Node:
  def __init__(self, m, x, y, newX, newY, level, parent):
    self.parent = parent
    self.m = [row[:] for row in m]
    self.m[x][y], self.m[newX][newY] = self.m[newX][newY], self.m[x][y]
    self.x, self.y = newX, newY
    self.cost = float('inf')
    self.level = level

  def __lt__(self, other):
    return (self.cost + self.level)<(other.cost + 
 other.level)


# Method for printing N x N matrix
def printMatrix(m):
    for row in m:
        print(" ".join(map(str, row)))
    print("")

# Method for allocating a new node
def newNode(m, x, y, newX, newY, level, parent):
    return Node(m, x, y, newX, newY, level, parent)

# Directions for moving tiles (bottom, left, top, right)
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

# Method for calculating the number of misplaced tiles
def calculateCost(initialM, finalM):
    count = 0
    for i in range(N):
        for j in range(N):
            if initialM[i][j] != 0 and initialM[i][j] != finalM[i][j]:
                count += 1
    return count

# Method for checking if (x, y) is a valid matrix coordinate
def isSafe(x, y):
    return 1 if 0 <= x < N and 0 <= y < N else 0

# Printing path from a root node to the destination node
def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.m)

# Method for solving N*N - 1 puzzle algorithm using Branch and Bound method
def solve(initialM, x, y, finalM):
    # Creating a priority queue for storing the live nodes of the search tree
    pq = []

    # Creating a root node and calculating its cost
    root = newNode(initialM, x, y, x, y, 0, None)
    root.cost = calculateCost(initialM, finalM)

    # Adding root to the list of the live nodes
    heapq.heappush(pq, (root.cost + root.level, root))

    # Finding a live node with the least cost, adding its children to the list of live nodes,
    # and finally deleting it from the list
    while pq:
        minNode = heapq.heappop(pq)[1]

        if minNode.cost == 0:
            # If minimum is an answer node, print the path from the root to the destination
            printPath(minNode)
            return

        # Generating children for the current node and adding them to the list of live nodes
        for i in range(4):
            newX, newY = minNode.x + row[i], minNode.y + col[i]
            if isSafe(newX, newY):
                child = newNode(minNode.m, minNode.x, minNode.y, newX, newY, minNode.level + 1, minNode)
                child.cost = calculateCost(child.m, finalM)
                heapq.heappush(pq, (child.cost + child.level, child))

# Main code
if __name__ == "__main__":
    # First configuration (Value 0 is used for the null space)
    initialM = [
        [3, 8, 2],
        [4, 6, 1],
        [5, 7, 0]
    ]

    # Solvable last configuration (Value 0 is used for the null space)
    finalM = [
        [3, 2, 1],
        [4, 0, 8],
        [5, 6, 7]
    ]

    # Blank tile coordinates in the first configuration
    x, y = 2, 2

    # Solve the puzzle problem
    solve(initialM, x, y, finalM)
