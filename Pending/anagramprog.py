# Easy way

def anagramMappings(A, B):
	result = [0]*len(A)
	for j in range(len(A)):
		for i in range(len(B)):
			if B[i] == A[j]
				result[j] = i
	return result

# the above should run in O(MN) time.

# better solution

def anagramMappings(A,B):
	seen = {}
	Seen2 = {B[i]: i for i in range(len(B))}
	for i in range(len(B)):
		seen[B[i]] = i
	result = [0]*len(A)
	Res2 = [seen[A[i]] for i in range(len(A)]
	for i in range(len(A)):
		result[i] = seen[A[i]]
	return result

def anagramMappings(A,B):
	seen = {B[i]: i for i in range(len(B))}
	result= [seen[A[i]] for i in range(len(A)]
	return result
