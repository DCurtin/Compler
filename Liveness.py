import SelectInstructions
import Parser

def liveness(line):
    program = SelectInstructions.selectInstructions(line)
    programInstructions = Parser.resolveLayer(program[0])
    if programInstructions[0].lower() != "program":
        print("Incorrect program structure")
        return None
    liveness = []
    instructions = programInstructions[1:]
    print(instructions)
    instructions.reverse()
    for instruct in instructions: #reverse list
        instructParsed = Parser.resolveLayer(instruct)
        #print(instructParsed)
        lastEntrySet = set()
        if len(liveness) > 0:
                lastEntrySet = liveness[-1].copy()
        if instructParsed[0] == "movq":
            #get last entry from liveness list
            #union read with last set - current write
            # print("instruct: " + instructParsed[2])
            # print("set: " + str(lastEntrySet))
            lastEntrySet.discard(instructParsed[2])
            # print("dif: " + str(lastEntrySet))
            # lastEntrySet = lastEntrySet.difference(instructParsed[2])
            if Parser.resolveLayer(instructParsed[1])[0] == "var": 
                lastEntrySet.add(instructParsed[1])
        if instructParsed[0] == "addq" or instructParsed[0] == "subq":
            if Parser.resolveLayer(instructParsed[1])[0] == "var": 
                lastEntrySet.add(instructParsed[1])
        #print(lastEntrySet)
        liveness.append(lastEntrySet)
    print(liveness.reverse())
    return [liveness, program[1]]
            
