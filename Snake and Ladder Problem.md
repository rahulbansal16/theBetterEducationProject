# Snake and Ladder Problem 

Problem statement: Given that you have control on the outcome of the dice rolled in a snake and ladder game, find the minimum number of throws required to reach the end of the game. Below is the image of a snake and ladder board on which we have to find the number of throws.

![snakeAndLadderBoard](assets\snakeAndLadderBoard.png)





## How do we proceed further ?

Here are the broad steps that one can keep in mind:

 *  Convert the problem into a graph problem
 *  The idea is to consider the given snake and ladder board as a directed
    graph with number of vertices equal to the number of cells in the board
 *  Since, all the edges are of "equal weight", it can be solved using breadth first search to find the shortest path











# Algorithm Discussion

Following the steps as discussed above, convert the problem into graphs. Each cell on the board will be a node in the graph. The idea is to reach the destination node in the minimum number of steps from the source node. It is nothing but a problem to find the shortest path to reach the destination node. Since, all the edges are of equal weight - we can use `breadth first search` to find the same.

The other data structures that we will require are: A queue, A visited array and a collection/class/structure that will contain two values - Value of the vertex and the number of tries (number of times dice is rolled) to reach the vertex. 

This structure/class/collection will be enqueued. So, let us enqueue the first or the source node in the queue and mark the index in the visited array as 1 (means that node is visited). It is important to note that at any given index, the next move will be `  v+1, v+2, v+3, v+4, v+5 or v+6`, where v is the current index.

Now, we dequeue the head of the queue and enqueue the next six possible nodes. Before enqueuing we have to check if the node is visited or not, if it is visited we need not enqueue (it will already be in the queue) and if it is not visited - we enqueue it and change the value as visited. 

Let us take an example to understand the algorithm:

Suppose the source node is 1, the number of tries taken to reach here is 0. So `{1,0}` is enqueued in the queue. Now, when it is dequeued, the next 6 possible values, i.e, `{2,1},{3,1},{4,1},{5,1},{6,1},{7,1}`, where the first value is the vertex value and the second value is the number of tries taken to reach the vertex, are enqueued in the queue. Now, the head of the node is `{2,1}` is dequeued and the next 6 values needed to be enqueued in the queue. But, the next 5 values are already present in the queue, which is confirmed by the visited array, so only `{8,2}` is the value that is enqueued.

This process has to be repeated till we reach the destination node. Once we reach the destination node, the number of tries needed to reach the vertex will be the required answer. 















# Code 

```python
def getMinDiceThrows(move, N): 
      
    # The graph has N vertices. Mark all 
    # the vertices as not visited 
    visited = [False] * N 
  
    # Create a queue
    queue = [] 
  
    # Mark the node 0 as visited and enqueue it 
    visited[0] = True
    
    # Enqueue 0'th vertex 
    queue.append(QueueEntry(0, 0)) 
  
    # Do a BFS starting from vertex at index 0 
    qe = QueueEntry() # A queue entry (qe) 
    while queue: 
        qe = queue.pop(0) 
        v = qe.v # Vertex no. of queue entry 
  
        # If front vertex is the destination 
        # vertex, we are done 
        if v == N - 1: 
            break
  
        # Otherwise dequeue the front vertex  
        # and enqueue its adjacent vertices  
        # (or cell numbers reachable through 
        # a dice throw) 
        j = v + 1
        while j <= v + 6 and j < N: 
          
            # If this cell is already visited, 
            # then ignore 
            if visited[j] is False: 
                  
                # Otherwise calculate its  
                # distance and mark it  
                # as visited 
                a = QueueEntry() 
                a.dist = qe.dist + 1
                visited[j] = True
  
                # Check if there a snake or ladder 
                # at 'j' then tail of snake or top 
                # of ladder become the adjacent of 'i' 
                a.v = move[j] if move[j] != -1 else j 
  
                queue.append(a) 
  
            j += 1
  
    # We reach here when 'qe' has last vertex 
    # return the distance of vertex in 'qe 
    return qe.dist 
  
```

