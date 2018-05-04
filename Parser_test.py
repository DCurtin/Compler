import Parser
import Uniquify
from Flatten import Flatten
import SelectInstructions
import RegisterAllocation
import TypeCheck

program_file = open("programs.txt", "r")
flatten = Flatten()

for program in program_file:
    print("*** Test string: " + program.strip() + "\n")
    test_lst = Parser.resolveLayer(program)
    print("Test string parsed: " + str(test_lst) + "\n")
    
    test_program_lst = Parser.resolveLayer(test_lst[1])
    print("Test string program parsed: " + str(test_program_lst) + "\n")
    
    print("Uniquified program: " + str(Uniquify.uniquify(program)) + "\n")

    flattened = flatten.flatten(program)
    print("Flattened program: " + str(flattened) + "\n")
    TypeCheck.typeCheck(flattened[0], flattened[1])
    
    print("Select Instructions: " + str(SelectInstructions.selectInstructions(program)) + "\n")
    
    print("RegisterAllocation: " + str(RegisterAllocation.registerAllocation(program, ["rbx"])[3]) + "\n")
    
    print("Type Check Errors: " + str(TypeCheck.typeCheck(flattened[0], flattened[1])) + "\n***\n\n")
    
    
    
    
    
    
    
    



#test2_str = "(program (+ (let ([x 3]) (+ x 5))  8))"
#print("Test string: " + test2_str)

#test2_lst = Parser.resolveLayer(test2_str)
#print("Test string parsed: " + str(test2_lst))

#test2_program_lst = Parser.resolveLayer(test2_lst[1])
#print("Test string program parsed: " + str(test2_program_lst))

'''Liveness: [
[{'(var w.0)'}, 
{'(var w.0)', '(var v.0)'}, 
{'(var w.0)', '(var x.0)'}, 
{'(var x.0)', '(var w.0)'}, 
{'(var y.0)', '(var x.0)', '(var w.0)'}, 
{'(var y.0)', '(var x.0)', '(var w.0)'}, 
{'(var y.0)', '(var z.0)', '(var w.0)'}, 
{'(var z.0)', '(var y.0)'}, 
{'(var tmp.0)', '(var z.0)', '(var y.0)'}, 
{'(var tmp.0)', '(var z.0)'}, 
{'(var tmp.0)'}], 

{'tmp.0', 'tmp.1', 'x.0', 'y.0', 'v.0', 'w.0', 'z.0'}]'''

#rows = 1539;
#samples1 = 1032;
#samples2 = 507;
#rndIDX = randperm(rows);
#traX = X(rndIDX(1:samples1), :);