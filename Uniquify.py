import Parser


def uniquify(line):
    program = Parser.resolveLayer(line)
    if program[0].lower() == 'program':
        uniquieProg = uniquifyHelper(program[1], dict())
        return ["(program " + uniquieProg[0] + ")", uniquieProg[1]]
    else:
        print("Exception")


def uniquifyHelper(line, argList):
    argLabel = set()
    line = Parser.resolveLayer(line)

    if line[0].lower() == "let": # operand
        init = Parser.resolveLayer(line[1]) # parse init
        var = init[0] # store init variable
        valUniq = uniquifyHelper(init[1], argList) # store and parse var value
        val = valUniq[0]
        argLabel.update(valUniq[1])

        '''
           update arglist
        '''
        if var not in argList:
            argList[var] = var + ".0"
        else:
            argList[var] = incrementVar(argList[var])
        argLabel.add(argList[var])
            #increment count
        var = argList[var]
        bodyUniq = uniquifyHelper(line[2], argList) #
        body = bodyUniq[0]
        argLabel.update(bodyUniq[1])

        #build string
        return ["(let" + " ([" + var + " " + val + "]) " + body + ")", argLabel]

    if line[0].lower() == "+":
        uniqVar1 = uniquifyHelper(line[1], argList.copy())
        var1 = uniqVar1[0]
        argLabel.update(uniqVar1[1])

        uniqVar2 = uniquifyHelper(line[2], argList.copy())
        var2 = uniqVar2[0]
        argLabel.update(uniqVar2[1])

        return ["(+ " + var1 + " " + var2+ ")", argLabel]

    if line[0].lower() == "-":
        uniqVar1 = uniquifyHelper(line[1], argList.copy())
        var1 = uniqVar1[0]
        argLabel.update(uniqVar1[1])

        return ["(- " + var1 + ")", argLabel]
    if line[0] in argList.keys():
        return [argList[line[0]], argLabel]
    return [line, argLabel]


def incrementVar(arg):
    argParts = arg.split(".")
    argParts[1] = str(int(argParts[1]) + 1)
    return ".".join(argParts)
