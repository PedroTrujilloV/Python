x=9
ans= 0
itersLeft = x
print(' x | ans | itersLeft')
while(itersLeft != 0 ):
    ans = ans + x
    itersLeft = itersLeft -1
    messaje = ' '+str(x)+' |  '+str(ans)+'  | '+str(itersLeft)
    print(len(messaje)*'_.')
    print(messaje)

print(len(messaje)*'_.') 
print(str(x)+'*'+str(x)+'='+str(ans))


num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop' 