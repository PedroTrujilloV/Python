balance = 500000
#monthlyPaymentRate = 0.02 #monthly payment rate
annualInterestRate =0.2 #annual interes rate

balance = 349182#Lowest Payment: 32093.1
annualInterestRate =0.22 #annual interes rate
'''

def getMIR(rate):
    return rate/12
    
def getMMP(r, bn_1):
    return (((bn_1+(bn_1*r))/12.0)-(((bn_1+(bn_1*r))/12.0)%10))-(((bn_1+(bn_1*r))/12.0*0.2)-(((bn_1+(bn_1*r))/12.0*0.2)%10))
        
def getMUB(bn_1, mmp):
    return bn_1 - mmp
    
def getUBEM(mub,mir):
    return mub+(mir*mub)
    
def creditBalance(b, months, r):
    bn=b
    mir = getMIR(r)
    #mmp=0
    mmp = getMMP(r,bn)
    while bn >=0:
        bn=b
        tp = 0  
        mmp+=10      
        for m in range(months):
            mub= getMUB(bn,mmp)
            ubem = getUBEM(mub,mir)
            bn= ubem
            tp = tp + mmp
            print 'Month: '+str(m+1)
            print 'Minimum monthly payment: '+str(round(mmp,2))
            print 'Remaining balance: '+str(round(ubem,2))
        
        print 'Total paid: '+str(round(tp,2))
        print 'Remaining balance: '+str(round(ubem,2))
        
    print 'Lowest Payment: '+str(round(mmp,2))

months = 12
creditBalance(balance, months, annualInterestRate)

'''

def getMIR(rate):
    return rate/12

def getMMP(r, bn_1):
    return (((bn_1+(bn_1*r))/12.0)-(((bn_1+(bn_1*r))/12.0)%10))-(((bn_1+(bn_1*r))/12.0*0.2)-(((bn_1+(bn_1*r))/12.0*0.2)%10))
         
def getMUB(bn_1, mmp):
    return bn_1 - mmp
    
def getUBEM(mub,mir):
    return mub+(mir*mub)
    
def creditBalance(b, months, r):
    bn=b
    mir = getMIR(r)
    mmp = getMMP(r,bn)
    while bn >=0:
        bn=b
        mmp+=10    
        for m in range(months):
            mub= getMUB(bn,mmp)
            ubem = getUBEM(mub,mir)
            bn= ubem
            print 'Month: '+str(m+1)
            print 'Minimum monthly payment: '+str(round(mmp,2))
            print 'Remaining balance: '+str(round(ubem,2))
        
    print 'Lowest Payment: '+str(round(mmp,2))

months = 12
creditBalance(balance, months, annualInterestRate)

