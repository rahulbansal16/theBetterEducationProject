from typing import List

class State:
    """
    Represents a state.
    """

    value = {'f': 10000, 'g': 1, 'c': 50, 'w': 100000}

    def __init__(self, left: List[str] = None, right: List[str] = None):
        self.leftSide = left
        self.rightSide = right

    def next(self) -> List['State']:
        """
        Generates a list of next possible states.
        
        Returns:
            List['State']: The list of next possible states.
        """
        states = []

        # getting the side with the farmer
        farmerSide = self.leftSide if 'f' in self.leftSide else self.rightSide

        # looping through every thing in the farmer side except the farmer
        for thing in [i for i in farmerSide if i != 'f']:
            # getting the state after moving the farmer and the thing to the 
            # other side
            nextState = State.__moveFarmerAndThing(self, thing)
            # if state is a valid state and it is not visited,
            # append it. 
            if nextState.isValid():
                states.append(nextState)

        # checking if the farmer was on the right side. If he was on the right side
        # another state is possible. That state is when the farmer comes back alone
        if farmerSide == self.rightSide:
            # making the state
            nextState = State(
                # adding farmer to the left side
                left=self.leftSide + ['f'],
                # removing farmer from right side
                right=[i for i in self.rightSide if i != 'f']
            )
            # appending the state if the state is valid
            if nextState.isValid():
                states.append(nextState)

        return states

    def isValid(self) -> bool:
        """
        checks whether the state is valid or not.
        
        Returns:
            bool: True, if the state is valid, False otherwise.
        """
        # if there is a goat and wolf on the side where the farmer is not there then return false
        if ('w' in self.leftSide and 'g' in self.leftSide and 'f' not in self.leftSide) or \
           ('w' in self.rightSide and 'g' in self.rightSide and 'f' not in self.rightSide):
            return False
        # if there is a cabbage and a goat on the side the farmer is not there then return false
        if ('c' in self.leftSide and 'g' in self.leftSide and 'f' not in self.leftSide) or \
           ('c' in self.rightSide and 'g' in self.rightSide and 'f' not in self.rightSide):
            return False

        # else return true
        return True

    def __int__(self) -> int:
        """
        Maps the state to a unique key based on contents. The things on the left side
        are added to the key, and the things on the right side are subtracted from the
        key.
        
        Returns:
            int: The value of the key
        """
        key = 0
        for thing in self.leftSide:
            key += State.value[thing]
        
        for thing in self.rightSide:
            key -= State.value[thing]
        return key

    def __str__(self) -> str:
        return "State [left side: {}, right side: {}".format(self.leftSide, self.rightSide)

    @staticmethod
    def __moveFarmerAndThing(state, thing) -> 'State':
        """
        Moves farmer and a thing from one side to another.
        
        Returns:
            'State': The state that result in such movement.
        """

        # if the farmer is on the left side, run if body
        if 'f' in state.leftSide:
            return State(
                # removing farmer and `thing` from left side
                left=[i for i in state.leftSide if i != 'f' and i != thing],
                # adding farmer and `thing` to right side
                right=state.rightSide + ['f', thing]
            )

        # this code runs when the farmer is on the right side. 
        return State(
            # adding farmer and `thing` to the left side
            left=state.leftSide + ['f', thing],
            # removing farmer and `thing` from right side
            right=[i for i in state.rightSide if i != 'f' and i != thing]
        )
        

    @staticmethod
    def initial() -> 'State':
        """
        Returns the initial state.
        
        Returns:
            State: The initial state.
        """

        return State(left=['f', 'g', 'c', 'w'], right=[])


if __name__ == "__main__":
    # creating initial state
    initialState = State.initial()

    # initializing queue
    q = [initialState]
    # intializing visited array
    visited = []

    # applying bfs:
    while len(q) != 0:
        # dequeue the queue
        currentState = q.pop(0)

        # if the state has already been visited, run the next iteration
        if int(currentState) in visited:
            continue

        # visit the state    
        print(currentState)
        # add state to visited array
        visited.append(int(currentState))
        # generate the next states
        nextStates = currentState.next()

        # add the next states to the queue if they have not been 
        # visited
        for _state in nextStates:
            if int(_state) not in visited:
                q.append(_state)
        
