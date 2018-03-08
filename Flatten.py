import Uniquify
import Parser

class Flatten(object):

    tempVars = 0
    def flatten(self, program):
        programUnique = Uniquify.uniquify(program)
        # print("uniquified: \n" + programUnique)
        programUniqueLst = Parser.resolveLayer(programUnique[0])
        #programUniqueLst = programUnique[0]
        if programUniqueLst[0].lower() == "program":
            flattened = "(program " + self.flattenHelper(programUniqueLst[1])[1] + ")"
            # print(flattened)
            # self.tempVars -= 1
            for value in range(self.tempVars):
                programUnique[1].add("tmp."+str(value))
            self.tempVars = 0
            return [flattened, programUnique[1]]

    def flattenHelper(self, line):
        lineLst = Parser.resolveLayer(line)
        if lineLst[0] == "let":
            init = Parser.resolveLayer(lineLst[1]) # get init from let
            var = init[0] #pull var from init
            # print("var: " + var)
            valLst = self.flattenHelper(init[1]) #flatten out value of the var
            init_assign = ""
            # print("VAL LST 0: " + str(valLst[0]))
            # print("VAL LST 1: " + str(valLst[1]))
            if "assign" in valLst[1] and "tmp" in valLst[0]:
                init_assign = valLst[1].replace(valLst[0], var)
                self.tempVars -= 1
            else:
                init_assign = valLst[1] + "(assign " + var + " " + valLst[0] + ") "
            
            bodyLst = self.flattenHelper(lineLst[2])
            # print("BDY LST: " + str(bodyLst))
            init_assign += bodyLst[1]

            return [bodyLst[0], init_assign]

        if lineLst[0] == "+" or lineLst[0] == "-":
            return self.flattenBinaryOp(lineLst)


        # print(line)
        return [line,""]

    def flattenBinaryOp(self, lineLst):
        """
            Recursively flatten the first and second arguments (should be able to handle more than one arg
        """
        varsLst = lineLst[1:]
        priorAssign = ""
        assign = lineLst[0].strip() + " "
        for var in varsLst:
            varFlat = self.flattenHelper(var)
            priorAssign += varFlat[1] + " "
            assign += varFlat[0] + " "

        assign = assign.strip()
        priorAssign = priorAssign.strip()
        var = "tmp." + str(self.tempVars)
        assign = priorAssign + " " + "(assign " +  var + " (" + assign + "))"
        self.tempVars += 1

        # var1Lst = self.flattenHelper(lineLst[1])
        # var2Lst = self.flattenHelper(lineLst[2])
        """
            get the temp var for 
        """
        # var = "tmp." + str(self.tempVars)
        # self.tempVars += 1
        # assign = var1Lst[1] + var2Lst[1] + "(assign " + var + " (" + lineLst[0] + " " + var1Lst[0] + " " + var2Lst[0] + "))"

        return [var, assign]
