x = 'pi'
y = 'pie'

x, y = y , x
 

x = 4
def f(x):
    print x
    
    while x>3:
        break
        print 'hi'/x
#f(x)

a1 = {'a'}
a2 = {'b'}

#print a1 == a2


myst = ( { 1: [1,1], 2: [2,2]}, { 'a': ['a',1], 'b': ['b',2] } )

#print type(myst)

kl = [(1,2,3,4)]
#kl[1] = 5


mt = (1,2,3,4)
#mt[1] = 5 

#print kl
#print mt
strg = "sd"
'''
for th in strg:
    if th=='sd':
        print 'found'
'''    

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
    
    
#print Square(5)

def Mylog(x,b):
    bn = b
    r=0
    while bn <= x:
        r  += 1
        bn *= b
    
    return r
    

x= 16
b= 2

x = 15
b = 3

x = 0
b = 0
#print Mylog(x,b)
    



def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    aListC = aList[:]
    subList = []
    for substr in aListC:
        if len(substr) < 4:
            subList.append(substr)
    return subList
    
    
aList = ["apple", "cat", "dog", "banana"]
aList = ["", "", "", ""]
aList = ["12345", "sdfg", "", "   "]
aList = ["12345", "sdfg", "'''''", "    "]
aList = []

#print aList
#print lessThan4(aList)
#print aList


def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N <10:
        return N
    else:
        return sumDigits(N/10)+(N%10)
        

print sumDigits(126)
print sumDigits(1520)
print sumDigits(0)
print sumDigits(1)
print sumDigits(99999999999)
print sumDigits(7)

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  
    targetList =[]
    for key in aDict:
        if aDict[key] == target:
            targetList.append(key)
    return targetList


aDict = {10:3, 8:1, 4:2, 2:6, 5:1, 1:5, 3:2, 7:2, 0:2}
aDict = {}
aDict = {3:1}
aDict = {0:1}
target = 1
#print keysWithValue(aDict, target)

def f(s):
    return 'a' in s
    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    Lc = L[:]
    for s in Lc:
        if not f(s):
            L.remove(s) 
            
    return len(L)

#run_satisfiesF(L, satisfiesF)

L = ['a', 'b', 'a']
L = []
L = ['a', 'b']
L = ['a',  'a']
L = ['d', 'c', 'b']
L = ['a', 'b', '']
L = ['', '6', '']
L = ['a', 'b', 'a', 'c']
L = ['a', 'b', 'a', 'c', 'a', 'd', 'e']
L = ['', 'b']
print satisfiesF(L)
print L