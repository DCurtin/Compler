'''
    Class for handling parsing
'''
class Parser(object):
    # FRONT_BRACKETS = ["[","("]
    # END_BRACKETS = ["]",")"]
    
    def resolveLayer(self, line):
        '''
            Is given a line as input and returns a list of
            [0] = val, variable, or operator
            [1] = first_arg
            [2] = second_arg (some operators are unary)
        '''
        bracketStack = []
        linePose = 0
        if line[linePose] == "(": # open bracket found, get operator, primitive, or argument
            lineItems = ["","",""]
            bracketStack.append(line[linePose])
            linePose += 1
            
            while line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
                lineItems[0] += line[linePose]
                linePose += 1
                
            if line[linePose] == ")": # end of line, check for miscount on brackets otherwise lineItem is a primitive or variable
                bracketStack.pop()
                if len(bracketStack) > 0:
                    #bracket miscount throw exception
                    print("bracket miscount exception")
                else:
                    return lineItems
            
            while line[linePose] == " ":
                linePose += 1 # skip white space
            
            if line[linePose] == "(": # if mid arg has open braces
            
            ''' 
                if line[linePose] == "(": # start of first argument
                bracketStack.append(line[linePose])
                while line[linePose] != ")":
            '''
                    
                
    def parseBracketVar(self, line, linePose): #travels a set of parentheses e.g. ((( something ))) collecting and keeping count of open and closed parentheses returns new linePose and str of parentheses
        
                    bracketStack.push(line[linePose])
                    lineItems[1] += line[linePose]
                    linePose += 1
                    
                    while len(bracketStack) > 0 and linePose < len(line): # run through middle arg up to the last closing bracket
                    
                        if line[linePose] == "(":
                            bracketStack.push("(")
                            
                        if line[linePose] == ")":
                            bracketStack.pop()
                            
                        lineItems[1] += line[linePose]
                        linePose += 1
                    # traversed entire argument
            
        