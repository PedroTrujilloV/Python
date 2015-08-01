end = True
while end == True:
    c = True
    low = 0
    high = 100
    chose = str (raw_input('Please think of a integer number between 0 and 100!  press enter'))
    while c == True:
        ans = (high + low)/2
        print ' '
        print 'Is your secret number '+str(ans)+'?'
        chose = str (raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.: '))
        #if chose!='h' or chose!='c' or chose!='l':
           # print 'Sorry, I did not understand your input.'
        if chose == 'c':
            print 'Game over. Your secret number was:'+str(ans)+' !!!'
            chose = str (raw_input('Play again? yes(y)/exit(anything)'))
            if chose != 'y':
                end = False
                break
            else:
                c=False             
        elif chose == 'h':
            high=ans
        elif chose == 'l':
            low=ans
        else:
            print 'Sorry, I did not understand your input.'
                
                
                
                
                
                
    