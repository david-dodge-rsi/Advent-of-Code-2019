def convertToIntArray(inputString):
    return [int(i) for i in inputString.split(",")]

programInput = open("input2.txt")
program = convertToIntArray(programInput.read())
program[1] = 12
program[2] = 2

for instruction in range(0, len(program)-1, 4):
    instructionSet = program[instruction : instruction + 4]
    operand = instructionSet[0]
    leftValue = program[instructionSet[1]]
    rightValue = program[instructionSet[2]]
    if operand == 1:
        program[instructionSet[3]] = leftValue + rightValue
    elif operand == 2:
        program[instructionSet[3]] = leftValue * rightValue
    elif operand == 99:
        break

print(program[0])