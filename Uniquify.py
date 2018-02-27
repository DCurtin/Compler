from Parser import Parser


class Uniquify:


    def uniquify(line):
        program = Parser.resolveLayer(line)
        if program[0].lower() == 'program':
            return "(program " + Uniquify.uniquifyHelper(program[1], dict()) + ")"
        else:
            print("Exception")
            
    def uniquifyHelper(line, argList):
        line = Parser.resolveLayer(line)

        if line[0].lower() == "let": # operand
            init  = Parser.resolveLayer(line[1]) # parse init
            var = init[0] # store init variable
            val = Uniquify.uniquifyHelper(init[1], argList) # store and parse var value

            '''
               update arglist
            '''
            if var not in argList:
                argList[var] = var + ".0"
            else:
                argList[var] = Uniquify.incrementVar(argList[var])
                #increment count
            var = argList[var]
            body = Uniquify.uniquifyHelper(line[2], argList) #

            #build string
            return "(let" + " ([" + var + " " + val + "]) " + body + ")"

        if line[0].lower() == "+":
            return "(+ " + Uniquify.uniquifyHelper(line[1], argList.copy()) + " " + Uniquify.uniquifyHelper(line[2], argList.copy()) + ")"
        
        if line[0].lower() == "-":
            return "(- " + Uniquify.uniquifyHelper(line[1], argList.copy()) + " " + Uniquify.uniquifyHelper(line[2], argList.copy()) + ")"
            
        if line[0] in argList.keys():
            return argList[line[0]]
        
        return line



    def incrementVar(arg):
        argParts = arg.split(".")
        argParts[1] = str(int(argParts[1]) + 1)
        return ".".join(argParts)