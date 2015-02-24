import random
import math
import god


charaterArray = ['santiago','maria','susan', 'tommy','shuan']
charaterDead = []

def whoWin(name):
    print 'finally the game has end',name, 'has win!!!'


def police(name):
    suspects = raw_input("who don't you trust")
    if suspects == killer:
        game = False 
        whoWin(police)

def violation (name):
    print name,'was ripped'

def kill(number):
    victim = charaterArray.pop(int(number))
    charaterDead.append(victim)

def createGod():
    theGod =random.randint(0, len(charaterArray))
    theGod = god.character(charaterArray[theGod])
    print theGod
    


print 'insert all the names you want and then type "finish"'
typing = True
while typing :

    character = raw_input('name de character ')
    if character =="finish":
        typing = False
    else:    
        charaterArray.append(character)




global game
game = True
global game1
game1 = True

print charaterArray
while game==True:
    print charaterArray
    print 'in the house there are',(len(charaterArray)), 'but a murderer is between them '
    character = raw_input('which character are you willing to be ? ')

    if character =='end':
        game = False
        game1 = False

       
    if character == 'god':
        print 'as you are the god, you should save one of your beloved creations by giving them protection from the dark powers'
        print ' and when the lights go off........'
        selectSomeone =raw_input('select someone to give immiunity: ')
        if selectSomeone == 'end':
            game1 = False
        else:
            try:
                selection = charaterArray.index(selectSomeone)
                subject = random.randint(0,(len(charaterArray)-2))
                if selection == subject:
                    print 'you were right!!! it was going to be a desaster , thanks for saving him!! \n'
                else:    
                    Kkill(subject)
                    print '\nthere is one less of them\n'
                    print  charaterDead[-1],'is now dead\n'
            except Exception, e:
                print e
                


            
   

       


