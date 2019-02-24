from module import *

cp1 = CodingProblem27("([])[]({})")
if(cp1.checkIfBracketsBalanced() == 1 ):
    print("CP1 SHOULD Pass")
else:
    print("ERROR: CP1 SHOUDN'T HAVE Failed")

cp2 = CodingProblem27("([)]")
if(cp2.checkIfBracketsBalanced() == 0):
    print("CP2 SHOULD FAIL")
else:
    print("CP2 SHOULDN'T HAVE PASSED")

cp3 = CodingProblem27("((()")
if(cp3.checkIfBracketsBalanced() == 0):
    print("CP3 SHOULD FAIL")
else:
    print("CP3 SHOULDN'T HAVE PASSED")



