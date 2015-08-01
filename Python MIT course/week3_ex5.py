# -*- coding: utf-8 -*-
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#print len(animals.values())


def howMany(aDict):
    collect=0
    for e in aDict:
        collect+=len(aDict[e])
        print e
        print collect
    print 'result'
    return collect


#print howMany({'a': [12, 8], 'D': [5], 'F': [5, 4, 9, 17], 'O': [12], 'p': [18, 0, 9, 2], 'V': [5, 19]})
# result 14
#print howMany({'e': [], 'w': [17], 'f': [8, 8], 'H': [15, 5, 18, 18], 'J': [15, 19], 'R': [13, 16, 12, 1], 'W': [3, 9], 'Y': [], 'z': [16, 20]})
# result 17
#print howMany(animals['d'])


def biggest(aDict):
    Maxlen=0
    collect = None   
    for e in aDict:
       if Maxlen<=len(aDict[e]):
           Maxlen = len(aDict[e])
           collect=str(e)
    return collect


print biggest({'a': [12, 8], 'D': [5], 'F': [5, 4, 9, 17], 'O': [12], 'p': [18, 0, 9, 2], 'V': [5, 19]})
# result 14
print biggest({})
print biggest({'g': []})
#print biggest({'e': [], 'w': [17], 'f': [8, 8], 'H': [15, 5, 18, 18], 'J': [15, 19], 'R': [13, 16, 12, 1], 'W': [3, 9], 'Y': [], 'z': [16, 20]})
# result 17
#print biggest(animals['d'])
