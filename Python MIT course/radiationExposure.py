



def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    global b
    b=step
    
    def getBList(start, stop, step):
        if type(step)== int:
            return range(start,stop, step)
        else:
            B=[]
            r = start
            while r < stop:
                B.append(r)
                r += step
            return B
            
            
    def getArea(F):
        return b*F
    
    Bt = getBList(start, stop, step)
    #print Bt
    Ft = map(f,Bt)
    #print '_______________________'
    #print Ft
    At = map(getArea,Ft)
    #print '_______________________'
    #print At
    #print 'result:'
    return sum(At)


print 'result:'
'''Test case 1:
>>> '''
print radiationExposure(0, 5, 1)
#39.10318784326239
'''Test case 2:
>>> '''
#radiationExposure(5, 11, 1)
#22.94241041057671
'''Test case 3:
>>> '''
#print radiationExposure(0, 11, 1)
#62.0455982538
'''Test case 4:
>>> '''
print radiationExposure(40, 100, 1.5)
#0.434612356115