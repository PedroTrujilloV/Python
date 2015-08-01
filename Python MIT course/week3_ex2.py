t1=(1,('a',2,4),'two', 3,'four',5,6)

#t1=(0,0)
#t1=(0,0,0, 0,0,0,0)
#t1=(0)
#print t1
aTup=t1
print t1[0]



def oddTuples(aTup):
    if aTup==(0):
        return (0)
    elif len(aTup)<=1: 
        return aTup
    else:
        return aTup[::2]
        
#print aTup
#print oddTuples(aTup)


x = [1, 2, [3, 'John', 4], 'Hi'] 

print x

print range(3, 10)

print range(3, 10.5, 0.5)