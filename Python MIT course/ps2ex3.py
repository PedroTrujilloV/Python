balance = 349182#Lowest Payment: 32093.1
annualInterestRate =0.22 #annual interes rate
#balance = 326887#Lowest Payment: 29784.6
#annualInterestRate =0.2 #annual interes rate


def getMIR(rate):
    return rate/12.0

def getMPLB(bn):#Monthly payment lower bound 
    return bn/12
    
def getMPUB(bn,mir):#Monthly payment upper bound 
    return (bn*((1+mir)**12))/12.0
                                    
def getMUB(bn_1, mmp):
    return bn_1 - mmp
    
def getUBEM(mub,mir):
    return mub+(mir*mub)
    
def Getbalance(mmp,bn,mir):
     
            mub= getMUB(bn,mmp)
            ubem = getUBEM(mub,mir)
            #print 'Minimum monthly payment: '+str(round(mmp,2))
            #print 'Remaining balance: '+str(round(ubem,2))
            
            return ubem
    
def creditBalance(b, months, r):
    bn=b
    mir = getMIR(r)
    mpub=getMPUB(b,mir)
    mplb=getMPLB(b)
    found = False
    tolerance =0.001
    itera =0   
    while not found :
        itera+=1        
        bn=b
        mmp = (mpub+mplb)/2
        
        for m in range(months):
            #print 'Month: '+str(m+1)
            bn = Getbalance(mmp,bn,mir)
        #print str((mpub-mplb)/2)+'< Tolerance:'+str(tolerance)+' itera:'+str(itera)
       
        if bn ==0 or (mpub-mplb)/2<tolerance:
            found = True
            break
            
        if bn<0:
            mpub=mmp
            #mplb=mmp#1
        else:
            mplb=mmp
            #mpub=mmp#1
          
        
    print 'Lowest Payment: '+str(round(mmp,2))

months = 12
creditBalance(balance, months, annualInterestRate)