from Flatten import Flatten
import Parser

def selectInstructions(line):
    fl = Flatten()
    program = fl.flatten(line)
    # print(program)
    programLst = Parser.resolveLayer(program[0])
    # print(program)
    lineAsm = ""
    last_assign = ""
    #print(programLst)
    for line in programLst:
        # print(line)
        if line == "Program":
            continue
        lineLst = Parser.resolveLayer(line)
        #print(lineLst)
        if lineLst[0] == "assign":
            lineOp = Parser.resolveLayer(lineLst[2])
            
            #print(str(lineLst[1]) + " : " + str(lineOp) + " : " + str(lineOp) + " : "  + str(isinstance(lineOp, list)))
            if not isinstance(lineOp, list): # check if assignment is a list
                #print(lineLst[1]) # if not it should be a str(int) or var, assign directly
                lineAsm += "(movq " + Parser.resolveCon(lineOp, program[1]) + " " + Parser.resolveCon(lineLst[1], program[1]) + ") "
            else:
                if lineOp[0] == "+":
                    lineAsm += "(movq " + Parser.resolveCon(lineOp[1], program[1]) + " " + Parser.resolveCon(lineLst[1], program[1]) + ") "
                    lineAsm += "(addq " + Parser.resolveCon(lineOp[2], program[1]) + " " + Parser.resolveCon(lineLst[1], program[1]) + ")  "
                if lineOp[0] == "-":
                    lineAsm += "(movq (int 0) " + Parser.resolveCon(lineLst[1], program[1]) + ") "
                    lineAsm += "(subq " + Parser.resolveCon(lineOp[1], program[1]) + " " + Parser.resolveCon(lineLst[1], program[1]) + ") "
            last_assign = Parser.resolveCon(lineLst[1], program[1])
    lineAsm += "(movq " + last_assign + " (reg rax)) "
    asmAndVars = ["(program " + lineAsm.strip() + ")", program[1]]
    return asmAndVars



# def resolveInt(input):
#    if isDecimal(input[1]):
#        isDecimal[0]
