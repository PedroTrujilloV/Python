base =  -3
exp =  0
#base=-6.25 #1.0000
#exp=0
res = 0 
#base=-1.39 #-1.3900
#exp=1
base = 8.24 # 175123692.2889
exp=9
#base=-6.73
#exp= 0

def iterPower(base, exp):
    bas = base
    exp = abs(exp)
    if exp==0:
        return base/abs(base)
    else:
        while exp > 1:
            base *= bas
            exp-=1
 #           print 'res= '+str(base)+' base= '+str(bas)+' exp= '+str(exp)
        return base
    

#print iterPower(base, exp) 



def recurPower(base, exp):
    if exp ==0:
        return base/base
    elif exp == 1:
        return base
    else:
        return base*recurPower(base,exp-1)
        
    
#print recurPower(base, exp)     


def recurPowerNew(base, exp):
    if exp ==0:
        return 1
    elif exp >0:        
        if exp%2==0:
            #print 'even'
            return recurPowerNew(base*base,exp/2)
        else:
            #print 'odd'
            return base*recurPowerNew(base,exp-1)
    else:
        return base
        

#print recurPowerNew(base, exp)   
def gcdIter(a,b):
    c=a
    if a>=b: 
        c=b
    while c>1:
        #print 'itera'+str(c)
        if a%c==0 and b%c==0:
            #print '%= '+str(c)
            return c            
        c-=1
    return 1

     
#print gcdIter(a,b)


def gcdRecur(a,b):
    print 'itera  a='+str(a)+' b= '+str(b)
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)
a=17
b=12        
#b=9
#a=12
#a=154
#b=44
#a=32 # 4
#b=20
a=60 # 15
b=165


#print gcdRecur(a,b)


def lenIter(aStr):
    
    numC=0 
    for c in aStr:
            numC +=1
      
    return numC


s='hello world!'
#print len(s)
#print 'Number of characters= '+str(lenIter(s))


def lenRecur(aStr):
    print aStr
    if aStr=='':
        return 0
    else:
        return 1+lenRecur(aStr[:-1])
    

#print lenRecur(s)


s='spd e2ratc1vmlqzib!'
#print s[6:]
#s='edacb'
def isIn(char,aStr):
    
    def isChar(char, aStr):
        #print aStr##..........................
        midp=len(aStr)/2
        midle= aStr[midp]
        #print ' '*midp+'|'#+'='+str(midp)+' midle='+midle##.....................
        if char==midle:
            return True
        else:
            if len(aStr)<=1 :
                return False
            elif char>midle:
                return True and isIn(char, aStr[midp:])
            else:
                return True and isIn(char, aStr[:midp])

    def orgAlphStr(aStr,c):
        if c<0:
            return aStr
        else:
            return orgAlphStr(compareLetters(aStr),c-1)
        
    def compareLetters(aStr):
        if len(aStr)<=1:
            return aStr
        elif aStr[0]>=aStr[1]:
            return aStr[1]+compareLetters(aStr[0]+aStr[2:])
        else:
            return aStr[0]+compareLetters(aStr[1:])
    
    if char=='' or aStr=='':
        return False
    else:
        return isChar(char, orgAlphStr(aStr,len(aStr)) )
    
print isIn('a','')




#def semordnilap(str1, str2):
    
def semordnilapWrapper2(str1, str2):
    
    lenstr1 = len(str1)
    lenstr2 = len(str2)
    #if is empty or Equal strings cannot be semordnilap
    if str1 == '' or str2 == '' or str1 == str2:
        return False
        
    # A single-length string cannot be semordnilap
    if lenstr1 == 1 or lenstr2 == 1or lenstr2!=lenstr1:
        return False
    
    #if there is any space in the word 
    if ' ' in str1 or ' ' in str2:
        return False
    
    return semordnilap(str1, str2)
    
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    if str1 == '' or str2 == '' or len(str1)!=len(str2):#no for wrapper2
        return False        
    elif len(str1) <= 1:
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:],str2[:-1])
            

str1='tact'
str2='cat'
'''
print 'case 1: '+str(semordnilapWrapper(str1, str2))

str1='desserts'
str2='stressed'


print 'case 2: '+str(semordnilapWrapper(str1, str2))

str1='desserts'
str2=''


print 'case 3: '+str(semordnilapWrapper(str1, str2))

str1='dessrtse'
str2='stressed'


print 'case 4: '+str(semordnilapWrapper(str1, str2))

str1='desse rt'
str2='stressed'

print 'case 5: '+str(semordnilapWrapper(str1, str2))
#print semordnilap(str1, str2)

'''










































































