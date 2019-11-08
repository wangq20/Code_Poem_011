#baby burrito
import random as r
from time import sleep 
from poemimages import getimages


def printImages(text):
    words = text.split(' ')
    for word in words:
        word = word.strip(".").strip(";")
        if word in images:
            print(images[word])

images = getimages()
sad = "baby burrito is watching us and listening for our response to his sad face."
waiting = "baby burrito is staring and listening with eyes and mouth wide open."
happy = "baby burrito is happy to be hearing our laughter and smiling back at us."
sleepy = "baby burrito is ready to sleep; all we are hearing is his faint breathing through this wide open mouth;"
sleeping = "baby burrito 's Zs is all we are hearing along with the silence."
changing = "B b is now spreading his legs and wiggling his toes."
wrapped = "B b is still wrapped and bundled very tightly."

feelings = [happy, sad, sleepy]
feeling = r.choice(feelings)
printImages(feeling)
printImages(wrapped)


while True:
    if feeling == sleepy:
        break
    action = ''
    while action != 'feed' and action != 'change' and action != 'entertain':
        action = input ("Would you like to feed, change, or entertain Baby Burrito?")
    if action == 'feed' or action == 'entertain' or action == 'change':
        printImages(waiting)
    if action == 'change':
        printImages(changing)
    else: printImages(wrapped)
    
    sleep(r.randint(1,3))

    tired = True if r.random() > .65 else False
    if tired: 
        printImages(sleepy)
        printImages(wrapped)
        feeling = sleepy

bedtime = ''
while bedtime != 'yes':
    bedtime = input("Would you like to rock Baby Burrito to sleep?").strip().lower()
if bedtime == 'yes':
    sleep(r.randint(1,3))
    printImages(sleeping)
    printImages(wrapped)
