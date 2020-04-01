#Turing Machine Simulator

states = []
fStates = []
tapeSymbols = []
transitionTable = []

def readTMFile():
    tmFile = open('tm.txt', 'r') 
    lines = tmFile.readlines() 

    for i in range(len(lines)):
        line = lines[i].strip()
        if i == 0:
            global states
            states = line.split(",")
        if i == 1:
            global fStates
            fStates = line.split(",")
        if i == 2:
            global tapeSymbols
            tapeSymbols = line.split(",")
        if i > 2:
            stateTransitions = line.split(":")

            for i in range(len(stateTransitions)):
                stateTransitions[i] = stateTransitions[i].split(",")
            
            
            transitionTable.append(stateTransitions)

    tmFile.close()




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
    readTMFile()
    inString = takeInputString()
    tape = runTuringMachine(inString)

    print(tape)
    
   

if __name__ == "__main__":
    main()
