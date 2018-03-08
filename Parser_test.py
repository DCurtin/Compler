import Parser
import Uniquify
from Flatten import Flatten
import SelectInstructions
import Liveness

program_file = open("programs.txt", "r")
flatten = Flatten()

for program in program_file:
    print("*** Test string: " + program.strip() + "\n")
    test_lst = Parser.resolveLayer(program)
    print("Test string parsed: " + str(test_lst) + "\n")
    
    test_program_lst = Parser.resolveLayer(test_lst[1])
    print("Test string program parsed: " + str(test_program_lst) + "\n")
    
    print("Uniquified program: " + str(Uniquify.uniquify(program)) + "\n")
    
    print("Flattened program: " + str(flatten.flatten(program)) + "\n")
    
    print("Select Instructions: " + str(SelectInstructions.selectInstructions(program)) + "\n")
    
    print("Liveness: " + str(Liveness.liveness(program)) + "\n***\n\n")
    
    
    
    
    
    
    
    



#test2_str = "(program (+ (let ([x 3]) (+ x 5))  8))"
#print("Test string: " + test2_str)

#test2_lst = Parser.resolveLayer(test2_str)
#print("Test string parsed: " + str(test2_lst))

#test2_program_lst = Parser.resolveLayer(test2_lst[1])
#print("Test string program parsed: " + str(test2_program_lst))