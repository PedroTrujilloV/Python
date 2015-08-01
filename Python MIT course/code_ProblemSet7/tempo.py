import string


koala     =  'Koala bears are soft and cuddly'
pillow    =  'I prefer pillows that are soft.'
soda      =  'Soft drinks are great'
pink      =  "Soft's the new pink!"
football  =  '"Soft!" he exclaimed as he threw the football'
microsoft =  'Microsoft announced today that pillows are bad'
nothing   =  'Reuters reports something really boring'
caps      =  'soft things are soft'

text = "asdad asdd'd kl, sadasd. asd" 
print text
punct = string.punctuation

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

def isWordIn(wList, phraseL):
        print phraseL
        if len(phraseL)<=1:
            return True
        elif phraseL[0] not in wList:
            return False
        else:
            return True and isWordIn(wList, phraseL[1:]) 
        
strT = 'asfdNew York Cityasfdasdfasdf'
nyc = 'New York City'
wList = ['asfdNew', 'York', 'Cityasfdasdfasdf']#, 'New', 'York', 'City']
phraseL = ['New', 'York', 'City']

case = nyc in strT 
#print case
#
#print isWordIn(wList, phraseL) and case
#print
#print "York" in ["york", "NewYork", "York's"] or False
#print True and False
#print False or False or True
print 'asdasd'.capitalize()
        
#wt = TitleTrigger('soft')
#wt2 = TitleTrigger('SOFT')
#print wt.isWordIn(football)
#print wt2.isWordIn(football)
#print type(wt) 
#Nt = NotTrigger(wt)

#print Nt.evaluate()
#print type(Nt.trigger)