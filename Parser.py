'''
    Class for handling parsing
'''

def resolveLayer(line):
    '''
        Is given a line as input and returns a list of
        [0] = val, variable, or operator
        [1] = first_arg
        [2] = second_arg (some operators are unary)
    '''
    line = line.strip()
    bracketStck = []
    linePose = 0
    if line[linePose] == "(": # open bracket found, get operator, primitive, or argument
        lineItems = []
        operand = ""

        while line[linePose] == "(" or line[linePose] == "[":
            bracketStck.append(line[linePose])
            linePose += 1

        # step through line until the end of the operator, primitive, or argument is found
        while line[linePose] != ")" and line[linePose] != "]" and line[linePose] != "(" and line[linePose] != " ":
            operand += line[linePose]
            linePose += 1
        lineItems.append(operand)

        while(not checkEnd(line, linePose, bracketStck)):
            linePose = skipWhiteSpace(line, linePose)
            itemList = parseArg(line, linePose)
            lineItems.append(itemList[0])
            linePose = itemList[1]

        # if linePose < len(line):
        #     print("closed all brackets before line end")


        return lineItems

    return line

def skipWhiteSpace(line, linePose): #returns linePose after white space
    while line[linePose] == " ":
            linePose += 1 # skip white space
    return linePose

def checkEnd(line, linePose, bracketStck):
    # print(bracketStck)
    if linePose >= len(line) and len(bracketStck) != 0:
        print("End of line before closed brackets")
        return True
    # end of line, check for miscount on brackets otherwise lineItem is a primitive or variable
    while line[linePose] == ")" or line[linePose] == "]": 
            bracket = bracketStck.pop()

            if line[linePose] == "]" and bracket == "(":
                print("%s, %s" % (bracket, line[linePose]))
                print("Bracket close mismatch")

            if line[linePose] == ")" and bracket == "[":
                print("%s, %s" % (bracket, line[linePose]))
                print("Bracket close mismatch")

            linePose += 1
            if linePose >= len(line):
                    return True

    else:
        return False

def parseBracketVar(line, linePose): 
    '''
        travels a set of parentheses e.g. ((( something ))) collecting and 
        keeping count of open and closed parentheses returns new linePose 
        and str of parentheses
    '''
    lineItem = line[linePose]
    bracketStck = [lineItem]
    linePose += 1

    '''
        Capture from left most bracket to right most
    '''
    while len(bracketStck) > 0 and linePose < len(line): 

        if line[linePose] == "(":
            bracketStck.append("(")

        if line[linePose] == "[":
            bracketStck.append("[")

        if line[linePose] == ")":
            if bracketStck.pop() != "(":
                print("Closing wrong bracket type")

        if line[linePose] == "]":
            if bracketStck.pop() != "[":
                print("Closing wrong bracket type")

        lineItem += line[linePose]
        linePose += 1

    return lineItem, linePose


def parseArg(line, linePose):
    if line[linePose] == "(": # if mid arg has open braces
        return parseBracketVar(line, linePose)

    else:
        lineItem = ""
        while line[linePose] != "[" and line[linePose] != "]" and line[linePose] != ")" and line[linePose] != "(" and line[linePose] != " ": # step through line until the end of the operator, primitive, or argument is found
            lineItem += line[linePose]
            linePose += 1
        return lineItem, linePose

