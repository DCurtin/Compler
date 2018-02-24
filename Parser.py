'''
    Class for handling parsing
'''

class Parser:
    def resolveLayer(line):
        '''
            Is given a line as input and returns a list of
            [0] = val, variable, or operator
            [1] = first_arg
            [2] = second_arg (some operators are unary)
        '''
        bracketCnt = 0
        linePose = 0
        if line[linePose] == "(": # open bracket found, get operator, primitive, or argument
            lineItems = []
            bracketCnt += 1
            linePose += 1
            operand = ""
            while line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
                operand += line[linePose]
                linePose += 1
            lineItems.append(operand)
    
            while(not Parser.checkEnd(line, linePose, bracketCnt)):
                linePose = Parser.skipWhiteSpace(line, linePose)
                itemList = Parser.parseArg(line, linePose)
                lineItems.append(itemList[0])
                linePose = itemList[1]
                
            
            return lineItems
    
    def skipWhiteSpace(line, linePose): #returns linePose after white space
        while line[linePose] == " ":
                linePose += 1 # skip white space
        return linePose
        
    def checkEnd(line, linePose, bracketCnt):
        if line[linePose] == ")": # end of line, check for miscount on brackets otherwise lineItem is a primitive or variable
                bracketCnt -= 1
                if bracketCnt is not 0:
                    #bracket miscount throw exception
                    print("bracket miscount exception")
                else:
                    return True
        else:
            return False
    
    def parseBracketVar(line, linePose): 
        '''
            travels a set of parentheses e.g. ((( something ))) collecting and 
            keeping count of open and closed parentheses returns new linePose 
            and str of parentheses
        '''
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
    
    
    def parseArg(line, linePose):
        if line[linePose] == "(": # if mid arg has open braces
            return Parser.parseBracketVar(line, linePose)
    
        else:
            lineItem = ""
            while line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
                lineItem += line[linePose]
                linePose += 1
            return lineItem, linePose
        