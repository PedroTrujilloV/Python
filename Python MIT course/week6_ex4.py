def genPrimes():
    num  = 2
    while True:
        n = 2              
        while n <= num:
            if num%n == 0:
                break
            n+=1
        if n == num:
            yield num  
            #print num
        num += 1
        

 
#genPrimes()      
            