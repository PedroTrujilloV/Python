s = 'azcIbobuobegRghaOklA'
vowals ='aeiouAEIOU'
numVow = 0
for letter in s:
    if letter in vowals:
        numVow +=1

print 'Number of vowels: '+str(numVow)


s = 'azcbobobegghaklbobobobobobo'
stringtofind ='bob'
s = 'rbobobloboboqbobfv'
s = 'bobbnbobnbobbebobbobbhboeobobbbobbbobobob'

def getNumtimStr (s,f):
    x=0
    lens=len(s)
    num = 0
    indx=0
    while x<lens+1:
        indx = s.find(f,x,lens)
        if indx>=0:
            num +=1
            x = indx+2
        else:
            x+=1          
    return 'Number of times bob occurs is: '+str(num)
stringtofind ='bob'    
print getNumtimStr(s,stringtofind)

s = 'azcbobobegghakl'
f='abcdefghijklmnopqrstuwxyz'

print 'intersection'+str(set(s).intersection(f))