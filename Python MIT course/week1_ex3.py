#lec 2.6 slide4

x=6

if x%2 == 0:
    if x%3 ==0:
        print('Divivsibleby 2')
    else:
        print('Divisible by 2 and not 3')
elif x%3 == 0:
    print('Divisible by 3 but not by 2')
else:
    print('Not divisible by 3 or 2')


happy = int(3)
y = str('hello world')

if happy > 2:
    print(y)
 
 
varA = 1
print(type(varA))