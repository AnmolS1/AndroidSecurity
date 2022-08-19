class HashTable:
	def __init__(self, size):
		self.size = (size + 9) // 10 * 10
		self.hash_table = self.create_table()
	
	def create_table(self):
		return [[] for _ in range(self.size)]
	
	def set(self, key, val):
		hash_key = hash(key) % self.size
		hash_index = self.hash_table[hash_key]
		
		found = False
		for i, kv in enumerate(hash_index):
			k, v = kv
			
			if k == key:
				found = True
				break
		
		if found:
			hash_index[i] = (key, val)
		else:
			hash_index.append((key, val))
	
	def get(self, key):
		hash_key = hash(key) % self.size
		hash_index = self.hash_table[hash_key]
		
		for i, kv in enumerate(hash_index):
			k, v = kv
			
			if k == key:
				return v
		
		return False