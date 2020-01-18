import random
import time

# Game Title :  The Slumber of the Doom King

# function that provides input from player 

def input_direction():
    direction1 = input("Which direction do you want to go? ")
    direction=direction1.lower()
    while direction not in ["north", "south", "east", "west", "exit"]:
        direction1 = input("Invalid answer,which direction do you want to go? ")
        direction=direction1.lower()

    return direction

# Stats 

health=100
gold=0
alive=True

# Introduction 


print ("                      The Slumber of the Doom King  ")
print("                                                                                   ")
print("Goal: Steal as much gold as possible and escape the castle of the Doom King before he consume your soul !!")
print("Direction: North/East/South/West/Quit")

time.sleep(1.5)

# Set up the Locations


compass = dict({ "north" : {1:-1,2:-1,3:-1,4:-1,5:1,6:2,7:3,8:4,9:5,10:6,11:7},
                 "east":  {1:2,2:3,3:4,4:-1,5:6,6:7,7:8,8:-1,9:10,10:11,11:12},
                 "south": {1:5,2:6,3:7,4:8,5:9,6:10,7:11,8:12,9:-1,10:-1,11:-1},
                 "west": {1:-1,2:1,3:2,4:3,5:-1,6:5,7:6,8:7,9:-1,10:9,11:10}
                })

descr = dict({
              1: "Location: Master bedroom. You feel something is watching you",
              2: "Location: Nursery. There is a sense of forelorn here",
              3: "Location: Treasury. It has been ransacked a long time ago",
              4: "Location: Library. It is filled with books of black magic   ",
              5: "Location: Dining room. Someone has been here recently",
              6: "Location: Torture chamber. You feel sick with dread...",
              7: "Location: Garden. All flowers has withered and died ",
              8: "Location: Burial Chamber. Something should be forgotten",
              9: "Location: Armoury. Filled with a assortment of demonic weapons",
             10: "Location: Kitchen. Old pots and pans clutters the room ",
             11: "Location: Servant Quarter. A skeleton lies on the floor, a sad sight",
             12: ""})




currentRoom = 1

# Game loop
while alive==True:

    # Describe the current room
    print (descr[currentRoom])

    loot=random.randrange(1,20)
    loot1=str(loot)
    print ("you find",loot1,"gold")
    gold+=loot
    print ("Total gold:",gold)
    print("Life:",health)


    # See if you awake the Doom King or not 
    sleep=random.randint(1,9)

    if sleep ==5 and currentRoom !=12:
        damage=random.randrange(30,60)
        health-=damage        
        print("The Doom King is awake, he attacks you !!")
        print("Life:", health)
        if health <=0:
            print("The Doom King consume your soul and break your body.( THE END )")
            input("Press enter to escape")
            break
        else:
            print("Thankfully you escape and the King falls back into slumber")
            
            

    elif sleep==1 or sleep==2:
        print("You hear the Doom King groan but then silence")

    elif sleep==3 or sleep==4:
        print("The Doom King is left undisturbed")

    elif sleep==6 or sleep==7:
        print("The Doom King remains asleep")

    else:
        print( "The Doom King slumber..") 



    # calling the function of user input 
    newDir = input_direction()
    
     

    # If you wish to exit
    if newDir == "quit":
        print ("Good bye")
        break
    else:

        # Otherwise look up whether there is a path that way
        if compass[newDir][currentRoom] != -1:
            currentRoom = compass[newDir][currentRoom]
        else:
            print ("There is no path in that direction")
        # If you find the exit 
        if  currentRoom ==12:
            print("Location: Exit Gate. You have found the exit, well done !!")
            print("Total gold:",gold," can you do better next time?")
            input("Press enter to escape")
            break






        
        

