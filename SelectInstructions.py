from Flatten import Flatten
import Parser

def selectInstructions(line):
    fl = Flatten()
    program = fl.flatten(line)
    # print(program)
    programLst = Parser.resolveLayer(program[0])
    # print(program)
    lineAsm = ""
    for line in programLst:
        print(line)
        if line == "Program":
            continue
        lineLst = Parser.resolveLayer(line)
        if lineLst[0] == "assign":
            lineOp = Parser.resolveLayer(lineLst[2])

            if len(lineOp) < 2:
                lineAsm += "(movq " + lineOp + " " + lineLst[1] + ") "
            else:
                if lineOp[0] == "+":
                    lineAsm += "(movq " + lineOp[1] + " " + lineLst[1] + ") "
                    lineAsm += "(addq " + lineOp[2] + " " + lineLst[1] + ")  "
                if lineOp[0] == "-":
                    lineAsm += "(movq 0 " + lineLst[1] + ") "
                    lineAsm += "(subq " + lineOp[1] + " " + lineLst[1] + ") "
    asmAndVars = ["(program " + lineAsm.strip() + ")", program[1]]
    return asmAndVars

def isDecimal(input):
    try:
        int(input)
        return True
    except error:
        return False

def resolveInt(input):
    if isDecimal(input[1]):
        isDecimal[0]
