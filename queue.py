class Queue:
	def __init__(self):
		self.queue = []
	
	def __str__(self):
		return 'Q: [' + ','.join([str(element) for element in self.queue]) + ']'
	
	def is_empty(self):
		return len(self.queue) == 0
	
	def enqueue(self, element):
		self.queue.append(element)
		
	def dequeue(self):
		if len(self.queue) == 0:
			raise Exception('Error: queue is empty')
		else:
			first_item = self.queue[0]
			self.queue.pop(0)
			return first_item


if __name__ == '__main__':
	print('a')
	Q = Queue()

	print(Q.is_empty())

	Q.enqueue(1)
	Q.enqueue(2)
	Q.enqueue(3)

	print(Q)

	print(Q.dequeue())
	print(Q.dequeue())
	print(Q.dequeue())
	print(Q.dequeue()) # Exception: queue is empty
