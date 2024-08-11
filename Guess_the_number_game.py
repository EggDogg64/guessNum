import random

def main():

    print("What's up,bro?! Hey,Let's start playing Russian Roulette!\n")
    print("Are you ready to die? LOL!\n Answer Yes or No. You can still turn back now. LOL!")

    ans = input("Press Yes or No\n")

    if ans != "Yes":
        return 
    elif ans == "Yes":
        return gameStart()

def gameStart():
    minNum = int(input("Enter the minimum value here --->"))
    maxNum = int(input("Enter the maximum value here --->"))
    count = int(input("How many times do you wanna challenge? Enter Num here-->"))

    if(minNum < maxNum):
        deathBullet = makeDeathBullet(minNum,maxNum)
    else:
        print("Enter collect Number")
        gameStart()
    
    pullTrigger(minNum,maxNum,deathBullet,count)

def pullTrigger(min,max,death,count):

    print(f"you have {count} times Okey?")

    while count != 0:
        ans = int(input("Enter the Number you think is a number that isn't a death bullet."))

        if(ans == death):
            print("..........You are dead......")
            return
        
        else:
            count=count-1
            if count == 0:
                break
            print("You are lucky man...")
            print(f"But you {count} more left...")
    
    print("Congratulations lucky dude. You made it back alive!")

    return 
        




def makeDeathBullet(min,max):
    randomNum = random.randint(min, max)

    return randomNum



main()
