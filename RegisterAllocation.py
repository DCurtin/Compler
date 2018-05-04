import SelectInstructions
import Parser

def registerAllocation(line, registers):
    program = SelectInstructions.selectInstructions(line)
    #program = line
    #print(program)
    programInstructions = Parser.resolveLayer(program[0])
    if programInstructions[0].lower() != "program":
        print("Incorrect program structure")
        return None
    instructions = programInstructions[1:]
    
    
    live = liveness(instructions)
    interference = interference_graph(instructions, live)
    colors = color_assign(interference)
    program_registers_allocated = assignment(registers, colors, program[0])
    
    return [live, interference, colors, program_registers_allocated]
    
def liveness(instructions):
    live = []
    # print(instructions)
    instructions.reverse()
    for instruct in instructions: #reverse list
        instructParsed = Parser.resolveLayer(instruct)
        #print(instructParsed)
        lastEntrySet = set()
        #lastEntrySet.add() #add empty
        #print("intrstruction: " + str(instructParsed))
        if len(live) > 0:
                lastEntrySet = live[-1].copy()#get after set of the previous position
        if instructParsed[0] == "movq":
            #get last entry from liveness list
            #union read with last set - current write
            #print("instruct: " + instructParsed[2])
            #print("set: " + str(lastEntrySet))
            lastEntrySet.discard(instructParsed[2])
            #print("dif: " + str(lastEntrySet))
            # lastEntrySet = lastEntrySet.difference(instructParsed[2])
            if Parser.resolveLayer(instructParsed[1])[0] == "var": 
                lastEntrySet.add(instructParsed[1])
        if instructParsed[0] == "addq" or instructParsed[0] == "subq":
            if Parser.resolveLayer(instructParsed[1])[0] == "var": 
                lastEntrySet.add(instructParsed[1])
            if Parser.resolveLayer(instructParsed[2])[0] == "var": 
                lastEntrySet.add(instructParsed[2])
                
        if instructParsed[0] == "negq" or instructParsed[0] == "subq":
            if Parser.resolveLayer(instructParsed[1])[0] == "var": 
                lastEntrySet.add(instructParsed[1])
        #print(lastEntrySet)
        live.append(lastEntrySet)
     #print(liveness.reverse())
    live.pop()#remove first entry, treat set as after(i)
    live.reverse()
    live.append(set())
    instructions.reverse()
    
    print("Liveness debug \n")
    for line in live:
        print(line)
    
    return live

def interference_graph(instructions, liveness):
    interference = dict()
    for i in range(len(instructions)):
        instructParsed = Parser.resolveLayer(instructions[i])
        if instructParsed[0] == "movq":
            #print(instructParsed)
            dest = instructParsed[2]
            src = instructParsed[1]
            if Parser.resolveLayer(dest)[0] == "var":
                if dest not in interference:
                    interference[dest] = set()
                for val in liveness[i]:
                    if val != dest and val != src:
                        interference[dest].add(val)
                #interference[dest] = 

        if instructParsed[0] == "addq" or instructParsed[0] == "subq":
            dest = instructParsed[2]
            src = instructParsed[1]
            if Parser.resolveLayer(dest)[0] == "var":
                if dest not in interference:
                    interference[dest] = set()
                for val in liveness[i]:
                    if val != dest:
                        if dest not in interference:
                            interference[dest] = set()
                        interference[dest].add(val)
                        
        if instructParsed[0] == "negq":
            dest = instructParsed[1]
            if Parser.resolveLayer(dest)[0] == "var":
                if dest not in interference:
                    interference[dest] = set()
                for val in liveness[i]:
                    if val != dest:
                        if dest not in interference:
                            interference[dest] = set()
                        interference[dest].add(val)
    print("\ninterference debug: \n")
    for key in interference:
        print(key + " : " + str(interference[key]))
    return interference
    
def color_assign(interference):
    nodes = list(interference.keys())
    colors = [set()]
    while len(nodes) > 0:
        max_node = nodes[0]
        for node in nodes: #find max saturation
            if len(interference[node]) > len(interference[max_node]):
                max_node = node

        color_ind_len = []
        for color_ind in range(len(colors)): #generate list colors with non-adjacent nodes
            if not adjacent(max_node, colors[color_ind], interference):
                color_ind_len.append([color_ind, len(colors[color_ind])])
        
        if len(color_ind_len) > 0: 
            min_pair = color_ind_len[0]
            for pair in color_ind_len: #find color with minimum count
                if min_pair[1] > pair[1]:
                    min_pair = pair
            colors[min_pair[0]].add(max_node)
        else: # if a color with non-adjacentcy could not be found
            color_set = set()
            color_set.add(max_node)
            colors.append(color_set)
        nodes.remove(max_node)
        
    for color in colors:
        print("color_debug: " + str(color))
    return colors
    
def assignment(registers, colors, program):
    #registers = ['rbx']
    mem_base = 8
    reg_cnt = len(registers)
    color_cnt = len(colors)
    #print(program)
    if reg_cnt >= color_cnt:
        for indx in range(color_cnt):
            for var in colors[indx]:
                program = program.replace(var, "(reg " + registers[indx] + ")")
    else:
        for indx in range(reg_cnt):
            for var in colors[indx]:
                program = program.replace(var, "(reg " + registers[indx] + ")")
        stack_cnt = color_cnt - reg_cnt
        for indx in range(reg_cnt, color_cnt):
            for var in colors[indx]:
                program = program.replace(var, "(deref rbp -" + str(mem_base*(indx - reg_cnt + 1)) + ")")
        
    
    return program
    

def adjacent(node_A, nodes, graph):
    if node_A not in graph:
        return False
    for node in nodes:
        if node not in graph:
            continue
        if node_A in graph[node] or node in graph[node_A]:
            return True
    
    return False
    
            
