### 9.1 - 희소 리스트 만들기 (p.456)

# code : 9-11.py
def sparse(ns):
	dic = {}
	index = 0
	for n in ns:
		if n != 0:
			dic[index] = n
		index += 1
	return dic

# # Test code
# print(sparse([]))                        # {}
# print(sparse([0,0,3,0,0,0,0,0,0,7,0,0])) # {2: 3, 9: 7}
# print(sparse([1,0,2,0,0,0,9,0,0]))       # {0: 1, 2: 2, 6: 9}

### 9.2 - 두 희소 리스트 덧셈 (p.457)

# code : 9-12.py
def sparse_add(ms,ns):
	mvalues = ms.values()
	nvalues = ns.values()
	for key in ms:
		value = ns.get(key)
		if value != None:
			ms[key] += value
			del ns[key]
	for key in ns:
		ms[key] = ns[key]
	return ms

# # test code
# print(sparse_add({},{}))                           # {}
# print(sparse_add({2: 3, 9: 7},{}))                 # {2: 3, 9: 7}
# print(sparse_add({},{0: 1, 2: 2, 6: 9}))           # {0: 1, 2: 2, 6: 9}
# print(sparse_add({2: 3, 9: 7},{0: 1, 2: 2, 6: 9})) # {2: 5, 9: 7, 0: 1, 6: 9}