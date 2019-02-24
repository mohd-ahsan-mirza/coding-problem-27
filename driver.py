from module import *

cp = CodingProblem27("([])[]({})")
if(cp.checkIfBracketsBalanced() == 1 ):
    print(cp.getBracketQuery() + " PASSED AS EXPECTED")
else:
    print(cp.getBracketQuery + " SHOUDN'T HAVE FAILED")

cp = CodingProblem27("([)]")
if(cp.checkIfBracketsBalanced() == 0):
    print(cp.getBracketQuery() + " FAILED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE PASSED")

cp = CodingProblem27("((()")
if(cp.checkIfBracketsBalanced() == 0):
    print(cp.getBracketQuery() + " FAILED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE PASSED")

cp = CodingProblem27("{[()]}")
if(cp.checkIfBracketsBalanced() == 1 ):
    print(cp.getBracketQuery() + " PASSED AS EXPECTED")
else:
    print(cp.getBracketQuery + " SHOUDN'T HAVE FAILED")

cp = CodingProblem27("{[(])}")
if(cp.checkIfBracketsBalanced() == 0):
    print(cp.getBracketQuery() + " FAILED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE PASSED")

cp = CodingProblem27("{{[[(())]]}}")
if(cp.checkIfBracketsBalanced() == 1):
    print(cp.getBracketQuery() + " PASSED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE FAILED")

cp = CodingProblem27("][][")
if(cp.checkIfBracketsBalanced() == 0):
    print(cp.getBracketQuery() + " FAILED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE PASSED")

cp = CodingProblem27("[[][]]")
if(cp.checkIfBracketsBalanced() == 1):
    print(cp.getBracketQuery() + " PASSED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE FAILED")

cp = CodingProblem27("[]()()(((([])))")
if(cp.checkIfBracketsBalanced() == 0):
    print(cp.getBracketQuery() + " FAILED AS EXPECTED")
else:
    print(cp.getBracketQuery() + " SHOULDN'T HAVE PASSED")





