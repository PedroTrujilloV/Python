testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
''' >>> print testList
  [1, 4, 8, 9]'''
print applyToEach(testList, abs)
print testList

testList = [1, -4, 8, -9]
  
  
def Nplus1(n):
    return n+1

''' >>> print testList
  [2, -3, 9, -8]'''  
print applyToEach(testList, Nplus1)
print testList

testList = [1, -4, 8, -9]

def Pow2(n):
    return n**2

''' >>> print testList
  [1, 16, 64, 81]''' 
print applyToEach(testList, Pow2)
print testList