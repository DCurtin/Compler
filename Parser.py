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
        bracketCnt = 0
        linePose = 0
        if line[linePose] == "(": # open bracket found, get operator, primitive, or argument
            lineItems = ["","",""]
            bracketCnt += 1
            linePose += 1
            
            while line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
                lineItems[0] += line[linePose]
                linePose += 1
                
            while line[linePose] == " ":
                linePose += 1 # skip white space
                
            if line[linePose] == ")": # end of line, check for miscount on brackets otherwise lineItem is a primitive or variable
                bracketCnt -= 1
                if bracketCnt is not 0:
                    #bracket miscount throw exception
                    print("bracket miscount exception")
                else:
                    return lineItems
            
            if line[linePose] == "(": # if mid arg has open braces
                firstArgLst = self.parseBracketVar(line, linePose)
                lineItems[1] = firstArgLst[0]
                linePose = firstArgLst[1]
                
            if lineItems[1] == "":
                while line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
                lineItems[1] += line[linePose]
                linePose += 1
                
            while line[linePose] == " ":
                linePose += 1 # skip white space
                
                
            if line[linePose] == ")": # end of line, check for miscount on brackets otherwise lineItem is a primitive or variable
            bracketCnt -= 1
            if bracketCnt is not 0:
                #bracket miscount throw exception
                print("bracket miscount exception")
            else:
                return lineItems
        
            ''' 
                if line[linePose] == "(": # start of first argument
                bracketCnt.append(line[linePose])
                while line[linePose] != ")":
            '''
                    
                
    def parseBracketVar(self, line, linePose): #travels a set of parentheses e.g. ((( something ))) collecting and keeping count of open and closed parentheses returns new linePose and str of parentheses
        
                    bracketCnt = 1
                    lineItem = line[linePose]
                    linePose += 1
                    
                    '''
                        Capture from left most bracket to right most
                    '''
                    while bracketCnt > 0 and linePose < len(line): 
                    
                        if line[linePose] == "(":
                            bracketCnt += 1
                            
                        if line[linePose] == ")":
                            bracketCnt -= 1
                            
                        lineItem += line[linePose]
                        linePose += 1
                    
                    return lineItem, linePose
            
        