from Uniquify import Uniquify
from Parser import Parser

class Flatten(object):

    tempVars = 0
    def flatten(self, program):
        programUnique = Uniquify.uniquify(program)
        print("uniquified: \n" + programUnique)
        programUniqueLst = Parser.resolveLayer(programUnique)
        if programUniqueLst[0].lower() == "program":
            print(self.flattenHelper(programUniqueLst[1])[1])
            self.tempVars = 0
            
    def flattenHelper(self, line):
        lineLst = Parser.resolveLayer(line)
        if lineLst[0] == "let":
            init = Parser.resolveLayer(lineLst[1]) # get init from let
            var = init[0] #pull var from init
            print("var: " + var)
            valLst = self.flattenHelper(init[1]) #flatten out value of the var
            init_assign = ""
            if "assign" in valLst[1]:
                init_assign = valLst[1].replace(valLst[0], var)
                self.tempVars -= 1
            else:
                init_assign = "(assign " + var + " " + valLst[0] + ")\n"
            
            bodyLst = self.flattenHelper(lineLst[2])
            init_assign += bodyLst[1]
            
            return [var, init_assign]
        
        if lineLst[0] == "+":
            """
                Recursively flatten the first and second arguments (should be able to handle more than one arg
            """
            var1Lst = self.flattenHelper(lineLst[1])
            var2Lst = self.flattenHelper(lineLst[2])
            """
                get the temp var for 
            """
            var = "tmp." + str(self.tempVars)
            self.tempVars += 1
            assign = (var1Lst[1] + var2Lst[1] + "(assign " + var + " (+ " + var1Lst[0] + " " + var2Lst[0] + "))\n")
            return [var, assign]
        # print(line)
        return [line,""]
        