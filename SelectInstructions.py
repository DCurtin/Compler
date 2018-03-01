from Flatten import Flatten
from Parser import Parser

class  SelectInstructions:

    def selectInstructions(line):
        fl = Flatten()
        program = fl.flatten(line)
        # print(program)
        program = Parser.resolveLayer(program)
        # print(program)
        lineAsm = ""
        for line in program:
            print(line)
            if line == "Program":
                continue
            lineLst = Parser.resolveLayer(line)
            if lineLst[0] == "assign":
                lineOp = Parser.resolveLayer(lineLst[2])
                lineAsm += "(movq " + lineOp[1] + " " + lineLst[1] + ")"
                if lineOp[0] == "+":
                    lineAsm += "(addq " + lineOp[2] + " " + lineLst[1] + ")"
                if lineOp[0] == "-":
                    lineAsm += "(subq " + lineOp[2] + " " + lineLst[1] + ")"
        return lineAsm

    def isDecimal(input):
        try:
            int(input)
            return True
        except error:
            return False
            
    def resolveInt(input):
        if isDecimal(input[1]):
            isDecimal[0

