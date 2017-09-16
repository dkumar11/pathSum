import unittest
class TestSumPath(unittest.TestCase):
	def testSanity(self):
		# Corner case 1: if a node is a leafNode
		n1 = Node(value = 1)

		#Case 2: a regular tree where height of the tree is 2
		n2 = Node(5,Node(3,2,4),Node(7,6,8))

		# Corner case 3: if the tree is null, should return -1
		n3 = Node()

		n4_left = Node(6, 2, 0)
		n7_left = Node(9,2, 5)
		n7_right = Node(1,4,5)
		n1_left = Node(4, n4_left, 9)
		n1_right = Node(7, n7_left, n7_right)
		n4 = Node(1, n1_left, n1_right)

		self.assertEqual(n1.sumPaths(),1)

		self.assertEqual(n2.sumPaths(), 2220)

		self.assertEqual(n3.sumPaths(), -1)

		self.assertEqual(n4.sumPaths(), 10087)



class Node:
	def __init__(self, value = None, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value


	def sumPaths(self):

		# if the input node is null
		if self.value == None:
			return -1

		# if the input node has no left and right branch, but still contains a value
		if self.left == None  and self.right == None:
			return self.value

		# obtaining the list of all possible paths in the tree
		lstOfPaths = Node.allPaths(self)
		result = 0

	""" 
	Iterating through each path, which is a list that contains that concatinated 
		values of the path as a string, and converting it to an integer so that it can 
		be added to result.
		NOTE: Another approach would be to just use integers and keep multiplying with 
		10 time some factor to build up the number, though that would not work if the
		numbers were larger than 9. This string approach works for  all possible
		integer values
	"""
		for path in lstOfPaths:
			pathNum = Node.convertToInteger(path)
			result += pathNum
		return result

	"""
	Helper menthod that returns a list of paths form root to leaf in a concatinated 
	string format
	"""
	@staticmethod
	def allPaths(currNode):
		if currNode == None:
			return []
		if Node.isLeaf(currNode):
			return [str(currNode)]
		left = Node.allPaths(currNode.left)
		right = Node.allPaths(currNode.right)
		leftPlusRight = left + right;
		result = []
		for path in leftPlusRight:
			result.append(str(currNode.value) + path)
		return result

	
	@staticmethod
	def isLeaf(node):
		return isinstance(node, int)
	
	@staticmethod
	def convertToInteger(lst):
		if isinstance(lst, str):
			return int(lst)
		if isinstance(lst, list):
			return int(lst[0])


if __name__ == "__main__":
	unittest.main()