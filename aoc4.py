def convertToIntArray(inputString):
    return [int(i) for i in inputString.split(",")]

def initializeMemory():
    programInput = open("input2.txt")
    return convertToIntArray(programInput.read())

def compute(memory, instuctionLength):
    for instructionPointer in range(0, len(memory)-1, instructionLength):
        instruction = memory[instructionPointer : instructionPointer + instructionLength]
        
        opcode = instruction[0]
        parameter1 = instruction[1]
        parameter2 = instruction[2]
        parameter3 = instruction[3]

        value1 = memory[parameter1]
        value2 = memory[parameter2]

        if opcode == 1:
            result = value1 + value2
            memory[parameter3] = result
        elif opcode == 2:
            result = value1 * value2
            memory[parameter3] = result
        elif opcode == 99:
            break
    return memory[0]

instructionLength = 4

for noun in range(0, 100):
    for verb in range(0, 100):
        memory = initializeMemory()
        memory[1] = noun
        memory[2] = verb
        result = compute(memory, instructionLength)
        if result == 19690720:
            print("noun: " + str(noun))
            print("verb: " + str(verb))
            print("solution:" + str((100 * noun) + verb))
            break