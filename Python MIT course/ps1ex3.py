
s = 'azcbobobegghakl'

s = 'rysaugealvkw'

a='abcdefghijklmnopqrstuvwxyz'
f='abcdefghijklmnopqrstuvwxyz'
def findLongSubString(s,f):
    init=0
    indx=0
    lsubstr=''
    substr=''
    for letter in s:        
        indx = f.find(letter)
               
        if indx >= init:            
            substr = substr + letter
            if len(lsubstr)<len(substr):
                lsubstr = substr 
        else:
            if len(lsubstr)<len(substr):
                lsubstr = substr             
            substr = letter
        init = indx        
    print 'Longest substring in alphabetical order is: '+lsubstr
     

findLongSubString(s,f)