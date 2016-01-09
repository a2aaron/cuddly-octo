TAPE_LENGTH = 50
ZERO_POINT = floor(tapeLength/2) #assumes that this point is zero on our tape

tape = []
currPosition = ZERO_POINT
currState = None
stateTableTuple = [(),(),(),(),()] #array of 5-tuples of (currState, scannedSymbol, printSymbol, moveTape, newState)

def moveHead(direction): #take "Left", "L" or "Right", "R"
    if direction == "L" or direction == "Left":
        currPosition = currPosition - 1
    elif direction == "R" or direction == "Right":
        currPosition = currPosition - 1

def scanSymbol():
    return tape[currPosition]

def newState(newState):
    currState = newState

def nextState(currState, scannedSymbol):
    for i in stateTableTuple:
        if currState == stateTableTuple[i][0] and stateTableTuple[i][1]:

