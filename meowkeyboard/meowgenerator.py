import keyboard
import random

key2Listen4 = 'page down'
meows = ['mraaowwww', 'mraaowww', 'meeowwww', 'mraaowww', 'meeeowwww', 'mrrrrpp', 'mmreaaaaaooowww', 'mreeaoooww', 'mrrrp', 'mrrrrr', 'mrrrrrppp', 'meeeaaaowww', 'mraaoowww', 'mraooowwww', 'mrrrpp', 'mrrrp', 'miau', 'mmeeoow']
meowAccents = ['~','!','...',' ^^',' :3']


def genRandMeow():
    randomMeow = ''

    for i in range(random.randint(1,3)):
        randomMeow += 'm'
    
    for i in range(random.randint(0,3)):
        randomMeow += 'r'
    
    for i in range(random.randint(1,5)):
        randomMeow += 'e'
    
    for i in range(random.randint(1,5)):
        randomMeow += 'o'
    
    for i in range(random.randint(1,4)):
        randomMeow += 'w'
    
    for i in range(random.randint(0,2)):
        randomMeow += random.choice(meowAccents)
    
    return randomMeow

def genRandMrp():
    randomMrp = ''

    for i in range(random.randint(1,4)):
        randomMrp += 'm'
    
    for i in range(random.randint(1,4)):
        randomMrp += 'r'
    
    for i in range(random.randint(1,4)):
        randomMrp += 'p'
    
    for i in range(random.randint(0,2)):
        randomMrp += random.choice(meowAccents)
    
    return randomMrp

def genRandNya():
    randomNya = ''

    for i in range(random.randint(1,3)):
        randomNya += 'n'
    
    for i in range(random.randint(1,3)):
        randomNya += 'y'

    for i in range(random.randint(1,3)):
        randomNya += 'a'
    
    for i in range(random.randint(0,2)):
        randomNya += random.choice(meowAccents)
    
    return randomNya

for i in range(30): meows.append(genRandMeow())

for i in range(10): meows.append(genRandMrp())

for i in range(10): meows.append(genRandNya())

def accessRandMeow():
    return random.choice(meows)

# def onKeyPress(event):
#     if event.name == key2Listen4:
#         keyboard.write(random.choice(meows)+' ')

# keyboard.on_press(onKeyPress)

# keyboard.wait('esc')