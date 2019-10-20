from typing import List, Tuple

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
            # getting the states after moving the farmer and the thing to the 
            # other side
            for state in State.__moveFarmerAndThing(self, thing):  
                # if state is a valid state and it is not visited,
                # append it and mark as visited  
                if state.isValid() and int(state) not in visited:
                    states.append(state)
                    visited.append(int(state))

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
    def __moveFarmerAndThing(state, thing) -> List['State']:
        """
        Moves farmer and a thing from one side to another.
        
        Returns:
            List['State']: A list containing the possible states that result in 
            such movement.
        """

        # if the farmer is on the left side, run if body
        if 'f' in state.leftSide:
            # generate a list containing all things except the farmer and `thing` for 
            # the left side
            leftSide = [i for i in state.leftSide if i != 'f' and i != thing]
            # make a list containing the right side things, the farmer and `thing`
            rightSide = state.rightSide + ['f', thing]
            # create a state object and return it
            return [State(left=leftSide, right=rightSide)]

        # this code runs when the farmer is on the right side. When the farmer
        # is on the right side, he can either come back with a thing or come back
        # alone. Hence there are two possible states.

        # variable that stores the possible states
        states = []
        
        # when the farmer comes back with a thing:

        # generate list containing all things except the farmer and `thing` for the
        # right side
        rightSide = [i for i in state.rightSide if i != 'f' and i != thing]

        # create a state with the generated list for the right side, and left side
        # things + farmer and `thing` for the left side
        states.append(State(left=state.leftSide + ['f', thing], right=rightSide))

        # when farmer comes back alone:

        # generate a list containing all things except farmer for the right side
        rightSide = [i for i in state.rightSide if i != 'f']

        # create a state with the generated list for the right side and left side
        # things + farmer for the left side
        states.append(State(left=state.leftSide + ['f'], right=rightSide))

        # return the states
        return states
    
        

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
    visited = [int(initialState)]

    # applying bfs:
    while(len(q) != 0):
        state = q.pop(0)
        
        print(state)

        nextStates = state.next()
        if nextStates is not None:
            q.extend(nextStates)

