varB = 2
varA = 3


if type(varA)== str:
    if type(varB) == str:
        lenA=len(varA)
        lenB=len(varB)
        if lenA == lenB:
            print('equal')
        elif lenA>lenB:
            print('bigger')
        else:
            print('smaller')
    else:
        print('string involved')
elif type(varB) == float or type(varB) == int:
    if varA == varB:
        print('equal')
    elif varA > varB:
        print('bigger')
    else:
        print('smaller')
else:
    print('string involved')
        



#  type(varB)==str :
  #  