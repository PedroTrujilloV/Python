balance = 5000 #balance
monthlyPaymentRate = 0.02 #monthly payment rate
annualInterestRate =0.18 #annual interes rate
    
def getMIR(rate):
    return rate/12
    
def getMMP(mpr, bn_1):
    return mpr*bn_1
    
def getMUB(bn_1, mmp):
    return bn_1 - mmp
    
def getUBEM(mub,mir):
    return mub+(mir*mub)
    
def creditBalance(b, mmpr, months, r):
    bn=b
    mir = getMIR(r)
    tp = 0
    for m in range(months):
        mmp= getMMP(mmpr,bn)
        mub= getMUB(bn,mmp)
        ubem = getUBEM(mub,mir)
        bn= ubem
        tp = tp + mmp
        print 'Month: '+str(m+1)
        print 'Minimum monthly payment: '+str(round(mmp,2))
        print 'Remaining balance: '+str(round(ubem,2))
    
    print 'Total paid: '+str(round(tp,2))
    print 'Remaining balance: '+str(round(ubem,2))


months = 12
creditBalance(balance, monthlyPaymentRate , months, annualInterestRate)


