def convertToIntArray(inputString):
    return [int(i) for i in inputString.split(",")]

programInput = open("input2.txt")
memory = convertToIntArray(programInput.read())

instructionLength = 4

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

print(memory[0])