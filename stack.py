class Stack:
	def __init__(self):
		self.stack = []
	
	def __str__(self):
		return 'S: [' + ','.join([str(element) for element in self.stack]) + ']'
	
	def is_empty(self):
		return len(self.stack) == 0
	
	def push(self, element):
		self.stack.append(element)
		
	def top(self):
		if len(self.stack) == 0:
			raise Exception('Error: stack is empty')
		else:
			return self.stack[-1]
		
	def pop(self):
		if len(self.stack) == 0:
			raise Exception('Error: stack is empty')
		else:
			last_item = self.stack[-1]
			self.stack.pop()
			return last_item


if __name__ == '__main__':
	S = Stack()

	print(S.is_empty())

	S.push(1)
	S.push(2)
	S.push(3)

	print(S)

	print(S.pop())
	print(S.pop())
	print(S.pop())
	print(S.pop()) # Exception: stack is empty