# Solving River-Crossing puzzles

River- crossing problem is a really interesting puzzle most of us would have encountered as kids. Although, there are many variations of this problem, the basic objective is to carry items from one river bank to another, usually in the fewest trips. The difficulty of the puzzle may arise from restrictions on which or how many items can be transported at the same time, or which or how many items may be safely left together. 

The first problem I came across, is the famous **Wolf, goat and cabbage problem** . After learning that this puzzle that troubled me as a kid could be solved using **graph theory**, it made me rethink my approach on solving all the river-crossing problems I've ever come across. 

 Looking at the problems we can formulate that each valid move ( sending boat from riverbank A to riverbank B with one or more objects ) is resulting in a new state and we can reach the goal state by solving a search problem. When we bring the graph perspective to the problem each state becomes a node and state change becomes an edge. So the problem can be solved by expanding nodes with valid moves until we reach the goal node.

## Implementation

  I started by solving the most popular version of river-crossing problem. Farmer, Wolf, Goat and Cabbage.

***Problem 1***

> *Once upon a time a farmer went to a market and purchased a wolf, a goat, and a cabbage. On his way home, the farmer came to the bank of a river and rented a boat. But crossing the river by boat, the farmer could carry only himself and a single one of his purchases: the wolf, the goat, or the cabbage.*
>
> *If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.*
>
> *The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact. How did he do it?*

![](https://upload.wikimedia.org/wikipedia/commons/2/28/Animasi_untuk_musang%2C_angsa_dan_kekacang_teka_teki.png)

Lets imagine him being on the the bank with the wolf, goat and cabbage as the initial state. From this state he can transitions to many different states, i.e. he could take the wolf with him to the other side, or the goat or the cabbage or he could go alone, but the only sensible choice he could make is to take the goat with him, as all the other choices leads to someone being eaten. Then the same process(BFS) is repeated on all the valid states that we could have gone to, until we reach the goal state i.e. all the items have reached the other side safely. It is possible that be end up going back to a state that we have already visited, to avoid this we have to keep track of whether a state is visited or not.

So to implement this we need a function that generates all the possible states that we can go to from a given state, then we need to validate the states that were generated. While doing this it is possible that we end up going back to a state that we have already visited, to avoid this we have to keep track of whether a state is visited or not and we also need to store how many moves did it take to reach the state, but to do this we need to distinguish one state from another, give it a unique key. To generate the key we associate each item to a score , to avoid collisions let the difference between the scores be large. By creating a dictionary we can map each map each state to a number (the number of  steps taken to reach that state), if a state is not mapped to a  number, then it is not visited.

To transition between states, we need to know the position of the boat, as there is only one driver(the farmer), his position can tell us the position of the boat.

To see a detailed explanation of this problem [refer](Lecture2.md) 

To see my implementation click [here](code/farmer_problem.ipynb)

***Problem 2***

> *Four soldiers need to cross a river. One is arrogant (wearing red plume), one is lazy (black plume), and two are brave (blue plumes).*
>
> *Rules :*
>
> - *Raft can hold maximum of 2 soldiers*
> - *lazy soldier refused to be alone in either side of the river*
> - *The arrogant one refuses to be accompanied on the raft*
>
> *How can they all get to other side?*
>

I tried to solve this problem using the same approach, but couldn't. Even though this problem seems similar to the previous one there are a few key differences:

* the driver is not fixed so we can't determine the position of the boat like we did in the previous case.
* the restriction is not only to who can be at the banks but also to who and how many can be on the boat.

taking these into consideration, I tried to make a generic approach to solve most of the river crossing problems. By just giving the restricted boat, bank states, drivers, boat capacity and the initial state we can get the least number of steps required to cross the river.

To see the implementation click [here](code/River_problem.ipynb)

