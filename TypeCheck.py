import Parser

def typeCheck(flattened_program, var_lst):
    program = Parser.resolveLayer(flattened_program)
    error = None
    if program[0].lower() != "program":
        print("Incorrect program structure")
        return None
    instructions = program[1:]
    #print(var_lst)
    types = dict()
    for instruction in instructions: #first pass 
        line = Parser.resolveLayer(instruction)
        var1 = line[1]
        var2 = Parser.resolveLayer(line[2])

        if(Parser.resolveInt(var2)):
            types[var1] = "Int"
        if(Parser.resolveBool(var2)):
            types[var1] = "Bool"
            
    for instruction in instructions: #second pass 
        line = Parser.resolveLayer(instruction)
        var1 = line[1]
        var2 = Parser.resolveLayer(line[2])

        if(not Parser.resolvePrim(var2)):
            #print(var2)
            op_type = resolveType_h(var1, types)
            if var2[0] == "+":
                var2_1_type = resolveType(var2[1], types, "+")
                var2_2_type = resolveType(var2[2], types, "+")
                op_type = compType(op_type, compType(var2_1_type, var2_2_type))
                if op_type != None and op_type != "Int":
                    return (" Type Error " + str(var2))
                types[var1] = op_type


            if var2[0] == "-":
                var2_1_type = resolveType(var2[1], types, "-")
                op_type = compType(op_type, var2_1_type)
                if op_type != None and op_type != "Int":
                    return (" Type Error: " + str(var1))
                types[var1] = op_type

    return error
    #for type in types:
    #    print(type + " : " + types[type])
    #else:
        #if(var2[0] == "-"
        #if(var2[0] == "+"
        #if(Parser.resolveInt(var2[2])
        #print(Parser.resolveInt(var2))
        
def compType(var1, var2):
    if var1 == None:
        return var2

    if var2 == None:
        return var1

    if var1 == var2:
        return var1
    else:
        return "e"

def resolveType_h(var, types):    
    if var in types:
        type = types[var]
    else:
        type = None
        
    if Parser.resolveInt(var):
        type = "Int"
    
    if Parser.resolveBool(var):
        type = "Bool"
    
    return type

def resolveType(var, types, op):
    type = resolveType_h(var, types)

    if op == "+" or op == "-":
        if type == "Int" or type == None:
            return "Int"
        else:
            return "e"

    if op == "==" or op == ">=" or op == "<=" or op == ">" or op == "<":
        if type == "Bool" or type == None:
            return "Bool"
        else:
            return "e"