class CodingProblem27:
	def __init__(self,query):
		self.query = query
		self.brackets = {
			"(" : ")",
			"[" : "]",
			"{" : "}",
		}
		self.matchingBraketsPossibleIndexes = range(1,(len(self.query))/2+1)
		self.matchingBraketsPossibleIndexes = [x * 2 - 1 for x in self.matchingBraketsPossibleIndexes]
	def isQueryLengthEven(self):
		if len(self.query) % 2 == 0:
			return True
		else:
			return False
	def findMatchingBracketAtPossibleIndex(self,bracket):
		#print("Bracket passed in find matching bracket -> "+bracket);
		matchingBracket = self.brackets[bracket]
		for run in range(len(self.matchingBraketsPossibleIndexes)):
			if(matchingBracket == self.query[self.matchingBraketsPossibleIndexes[run]]):
				return self.matchingBraketsPossibleIndexes[run]
		return -1
	def checkIfBracketsBalanced(self):
		#print("Query in brackets balance function ->"+self.query)
		# First check if the length of the string is even. If it is odd there is no way the brackets are balanced
		if self.isQueryLengthEven() == 0:
			return False
		index = 0
		query = self.query
		while (len(self.query)) != 0:
			#print("query at START of while -> "+query)
			# Matching bracket has to be at an even-1 index up to the length of the query
			# Take the bracket at first position and make find it's corresponding bracket
			# Take that whole substring minus the above two matching brackets and check the sub brackets recursively
			# Continue with the rest of the string until a false is returned
			index = matchingBracketIndex = self.findMatchingBracketAtPossibleIndex(self.query[0])
			#print("Index for matching bracket -> "+str(index))
			if(index == -1):
				return False
			if(index == 1) and (len(self.query) == 2):
				return True
			if(index == 1):
				self.query = self.query[index+1:]
			else:
				checkForSubBrackets = CodingProblem27(self.query[1:index])
				if checkForSubBrackets.checkIfBracketsBalanced() == 0:
					return False
				self.query = self.query[index+1:]
			#print("query at END of while -> "+self.query)
		return True