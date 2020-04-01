#Turing Machine Simulator

tape = []
states = []
fStates = []
tapeSymbols = []
transitionTable = []

def initStates():
    noStates = input("Enter number of states: ")

    for i in range(0, int(noStates)):
        state = input("Enter state: ")
        states.append(state)

def initFStates():
    noStates = input("Enter number of final states: ")

    for i in range(0, int(noStates)):
        state = input("Enter final state: ")
        fStates.append(state)

def initTapeSymbols():
    noSymbols = input("Enter number of symbols: ")

    for i in range(int(noSymbols)):
        symbol = input("Enter symbol: ")
        tapeSymbols.append(symbol)

    tapeSymbols.append("B")

def initTransitionTable():
    print(states)
    print(tapeSymbols)
    for i in range(len(states)):
        stateTransitions = []
        for j in range(len(tapeSymbols)):
            inputS = input("Enter transition for state " + states[i] + " on symbol " + tapeSymbols[j] + ": ")
            stateTransitions.append(inputS.split(","))
        transitionTable.append(stateTransitions)


def takeInputString():
    inputString = input("Enter input string: ")
    return inputString

    
def runTuringMachine(inString):
    tapehead = 0
    currState = states[0]
    tape = list(inString)
    count = 1000

    while count > 0:
        if currState in fStates:
            print("Input Accepted")
            return tape

        i = states.index(currState)
        j = tapeSymbols.index(tape[tapehead])

        transition = transitionTable[i][j]

        if len(transition) == 3:
            currState = transition[0]
            tape[tapehead] = transition[1]

            if transition[2] == "L" and tapehead > 0:
                tapehead = tapehead -1
            elif transition[2] == "R":
                tapehead = tapehead + 1
                if tapehead > len(tape) - 1:
                    tape.append("B")
        elif len(transition) == 1 and transition[0] == "-":
            print("Input Rejected")
            return tape

        printTape = []
        for i in range(len(tape)): 
            if i == tapehead:
                printTape.append(currState)
            
            printTape.append(tape[i])
        print(printTape)
                
        count = count-1


def main():
    initStates()
    initFStates()
    initTapeSymbols()
    initTransitionTable()
    inString = takeInputString()
    tape = runTuringMachine(inString)

    print(tape)
    
   

if __name__ == "__main__":
    main()
