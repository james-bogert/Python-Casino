import random
import time

game_choice = 0
menu_loop = 1       #only values that stay constant outside of the games

money = int(1000)
roulette_roll = 0
roulette_roll2 = 0
roulette_number = 0
roulette_color = 0
roulette_bet = 0
roulette_title = 1
slots_roll = 0
slots_roll2 = 0             #this is where i defined every variable that i use in the entire program
slots_roll3 = 0
slots_bet = 0
slots_loop = 0
slots_list = ["Apple     ", "Star      ", "BAR       ", "Orange    ", "Diamond   ", "WIN       "]
slots_title = 1
blja_user_rand = 0
blja_comp_rand = 0
blja_user_num = 0
blja_comp_num = 0
blja_ace = 0
blja_list = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
blja_user_display = []
blja_menu = True
blja_loop = 0
blja_bet = 0
blja_title = 1

def def_pro (x,y,z):
    def_pro2 = 0
    def_loop = False

    while def_loop != True:
        for a in range(y,(z + 1)):              #this is a function that i can use for defensive programing on any input in the rest of the program.
            if str(x) == str(a):                #You can set the value that is being compared, and the range of values it is being compared against
                def_pro2 += 1                   #a for loop will loop the amount of times the range is set to. if the number of the loop is ever equal to the value
        if def_pro2 != 1:                       #that was set 1 is added to def_pro2. if def_pro2 never equals 1 it means that the value never equaled any numbers
            print("THAT IS AN INVALID INPUT")   #in the range and so is not equal. it will then ask you to reinput the value and will go around until def_pro2 = 1.
            x = input("TRY AGAIN: ")
        elif def_pro2 == 1:
            def_loop = True
    return x

print("\n /$$$$$$$  /$$     /$$ /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$ ")
time.sleep(0.3)
print("| $$__  $$|  $$   /$$/|__  $$__/| $$  | $$ /$$__  $$| $$$ | $$       /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$ /$$__  $$")
time.sleep(0.3)
print("| $$  \ $$ \  $$ /$$/    | $$   | $$  | $$| $$  \ $$| $$$$| $$      | $$  \__/| $$  \ $$| $$  \__/  | $$  | $$$$| $$| $$  \ $$")
time.sleep(0.3)
print("| $$$$$$$/  \  $$$$/     | $$   | $$$$$$$$| $$  | $$| $$ $$ $$      | $$      | $$$$$$$$|  $$$$$$   | $$  | $$ $$ $$| $$  | $$")
time.sleep(0.3)
print("| $$____/    \  $$/      | $$   | $$__  $$| $$  | $$| $$  $$$$      | $$      | $$__  $$ \____  $$  | $$  | $$  $$$$| $$  | $$")    #ascii art for the begining of the program
time.sleep(0.3)
print("| $$          | $$       | $$   | $$  | $$| $$  | $$| $$\  $$$      | $$    $$| $$  | $$ /$$  \ $$  | $$  | $$\  $$$| $$  | $$")
time.sleep(0.3)
print("| $$          | $$       | $$   | $$  | $$|  $$$$$$/| $$ \  $$      |  $$$$$$/| $$  | $$|  $$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/")
time.sleep(0.3)
print("|__/          |__/       |__/   |__/  |__/ \______/ |__/  \__/       \______/ |__/  |__/ \______/ |______/|__/  \__/ \______/ ")
time.sleep(0.3)
print("Welcome to the Python Casino.")
print("Right now there are 3 choices for games: Roulette, Slots, and BlackJack.") #starting text
print("You will start with 1000 chips, Good Luck and Enjoy")

while menu_loop == 1:                       #while loop for every piece of code i want to to repeat while the game is running

    print("Your Current Balance is " + str(money))                      #tells player there current ballance
    game_choice = input("Enter 1 for Roulette, Enter 2 For Slots, Enter 3 for BlackJack, Enter 4 to EXIT: ") #input for menu system
    game_choice = int(def_pro(game_choice,1,4)) #example of the defesive programing function in action.

    if int(game_choice) == 1:               #start of the first game(roulette)
        if roulette_title == 1:             #the title if statement exists so that the ascii art will only print once no matter how many times the game is repeated
            print("______ _____ _   _ _      _____ _____ _____ _____ ")
            time.sleep(0.1)
            print("| ___ \  _  | | | | |    |  ___|_   _|_   _|  ___|")
            time.sleep(0.1)
            print("| |_/ / | | | | | | |    | |__   | |   | | | |__  ")     #ascii art for roulette
            time.sleep(0.1)
            print("|    /| | | | | | | |    |  __|  | |   | | |  __| ")
            time.sleep(0.1)
            print("| |\ \\" + "\ \_/ / |_| | |____| |___  | |   | | | |___ ")
            time.sleep(0.1)
            print("\_| \_|\___/ \___/\_____/\____/  \_/   \_/ \____/ ")
            time.sleep(0.1)
            print("")
            roulette_title = 0  #making sure the if statement never repeats

        roulette_roll = 0
        roulette_roll2 = 0
        roulette_number = 0     #redefining all the variables so values dont carry over from previous playthrouhgs of the game
        roulette_color = 0
        roulette_bet = 0

        roulette_number = input("Enter a Number from 1-35, For color choice enter 0: ") #gives 2 option. basicaly 1 is odds 1/35 of winning. 0 is odds of 1/2.
        roulette_number = int(def_pro(roulette_number,0,35))
        if roulette_number == 0:
            roulette_color = input("Enter 1 for Red, Enter 2 For Black: ")  #only runs if user inputs 0, asks them for which color they want
            roulette_color = int(def_pro(roulette_color,1,2))

        roulette_bet = input("Now Place Your Bet: ")            #places the bet
        roulette_bet = int(def_pro(roulette_bet,0,money))

        if roulette_number != 0:
            roulette_roll = random.randint(1,35)            #randomly chooses a value for the user input to be compared against
        elif roulette_number == 0:                          #both are run whether or not the user inputs 0 or 1-35 at the begining
            roulette_roll2 = random.randint(1,2)

        print("Spinning Wheel")
        time.sleep(.500)
        print("Throwing in Ball")   #print text for presentation of the game
        time.sleep(1)
        print("Getting Results")
        time.sleep(1)
        if (roulette_number == roulette_roll) and (roulette_number != 0):   #there is only 2 options if the user puts 1-35.
            money = money + (int(roulette_bet) * 35)
            print("It landed on " + str(roulette_roll) + ". you guessed " + str(roulette_number) + ": YOU WIN!")
        elif roulette_number == 0:
            if roulette_color == roulette_roll2:       #there are more options for color choice because i cant just print the value of
                if roulette_roll2 == 1:                 #roullete_roll2 for the print statement. Basically just for presentation aswell.
                    print("It landed on a Red Number: YOU WIN!")
                    money = money + roulette_bet
                elif roulette_roll2 == 2:
                    print("It landed on a Black Number: YOU WIN!")
                    money = money + roulette_bet                    #money is given back with the odds of losing, so theoretically
            elif roulette_color != roulette_roll2:                  #if enough of the game is played then money should return back
                if roulette_roll2 == 1:                             #to exactly 1000
                    print("It landed on a Red Number: YOU LOSE")    #money is the only value that carries over from game to game
                    money = money - roulette_bet                    #instead of reseting when the game is re-run
                elif roulette_roll2 == 2:
                    print("It landed on a Black Number: YOU LOSE")
                    money = money - roulette_bet
        elif roulette_number != roulette_roll:
            money = money - int(roulette_bet)
            print("Sorry but the number landed on " + str(roulette_roll) + ": YOU LOSE")

    if int(game_choice) == 2:       #start of game 2(slots)
        if slots_title == 1:
            print(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
            time.sleep(0.1)
            print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
            time.sleep(0.1)
            print("| |    _______   | || |   _____      | || |     ____     | || |  _________   | || |    _______   | |")
            time.sleep(0.1)
            print("| |   /  ___  |  | || |  |_   _|     | || |   .'    `.   | || | |  _   _  |  | || |   /  ___  |  | |")
            time.sleep(0.1)
            print("| |  |  (__ \_|  | || |    | |       | || |  /  .--.  \  | || | |_/ | | \_|  | || |  |  (__ \_|  | |")   #ascii art for slots
            time.sleep(0.1)
            print("| |   '.___`-.   | || |    | |   _   | || |  | |    | |  | || |     | |      | || |   '.___`-.   | |")   #never runs again like before
            time.sleep(0.1)
            print("| |  |`\____) |  | || |   _| |__/ |  | || |  \  `--'  /  | || |    _| |_     | || |  |`\____) |  | |")
            time.sleep(0.1)
            print("| |  |_______.'  | || |  |________|  | || |   `.____.'   | || |   |_____|    | || |  |_______.'  | |")
            time.sleep(0.1)
            print("| |              | || |              | || |              | || |              | || |              | |")
            time.sleep(0.1)
            print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
            time.sleep(0.1)
            print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
            time.sleep(0.1)
            print("")
            slots_title = 0

        slots_bet = input("Place Your Bet: ")
        slots_bet = int(def_pro(slots_bet,0,money)) #money is used instead of a set value so that the user can never bet more than they have
        print("Rolling the Slots")
        time.sleep(0.5)
        slots_loop = 0
        for slots_loop in range(0,10):
            slots_roll = random.randint(0,5)        #simulates the rolling of the slots
            slots_roll2 = random.randint(0,5)       #real value isnt decided until the end
            slots_roll3 = random.randint(0,5)       #so this is just more presentation but i think it looks really nice
            print(slots_list[slots_roll] + slots_list[slots_roll2] + slots_list[slots_roll3])
            time.sleep(0.2)
        slots_roll = random.randint(0, 5)       #decides the final value for the slots
        slots_roll2 = random.randint(0, 5)      #i put it below so that i could make the print
        slots_roll3 = random.randint(0, 5)      #of the real values bold and seperate
        print(" ")
        print('\033[1m' + slots_list[slots_roll] + slots_list[slots_roll2] + slots_list[slots_roll3] + '\033[0m') #value for bold
        if (slots_roll == slots_roll2) and (slots_roll2 == slots_roll3):    #there is three options. if none are equal, if two are equal, or if all three are equal
            print("All 3 are the same: YOU WIN!")
            money = money + (slots_bet) * 36
        elif (slots_roll == slots_roll2) or (slots_roll == slots_roll3) or (slots_roll2 == slots_roll3):
            print("Two of them are the same: YOU WIN!")
            money = money + (slots_bet) * 6
        else:                               #sometimes i wont put an else statement when i can because i like the to be specific when
            print("Sorry but they are all different: YOU LOSE") #i make if statements.
            money = money - slots_bet

    if int(game_choice) == 3:   #start of game 3 (blackjack
        if blja_title == 1:
            print("  ____  _               _____ _  __    _         _____ _  __")
            time.sleep(0.1)
            print(" |  _ \| |        /\   / ____| |/ /   | |  /\   / ____| |/ /")
            time.sleep(0.1)
            print(" | |_) | |       /  \ | |    | ' /    | | /  \ | |    | ' / ")   #ascii art for blackjack
            time.sleep(0.1)
            print(" |  _ <| |      / /\ \| |    |  < _   | |/ /\ \| |    |  <  ")
            time.sleep(0.1)
            print(" | |_) | |____ / ____ \ |____| . \ |__| / ____ \ |____| . \ ")
            time.sleep(0.1)
            print(" |____/|______/_/    \_\_____|_|\_\____/_/    \_\_____|_|\_\\")
            time.sleep(0.1)
            print("")
            blja_title = 0

        blja_user_num = 0
        blja_comp_num = 0       #resetting all values like before
        blja_menu = True
        blja_user_display.clear()   #clears the list instead of setting its value

        while blja_menu == True:
            blja_comp_rand = random.randint(1,13)
            if 1 < blja_comp_rand < 10:
                blja_comp_num += blja_comp_rand     #this code plays its own mini game of blackjack before the user does
            elif blja_comp_rand == 1:               #uses some simple logic.
                if blja_comp_num + 11 >= 21:        #if the computer is over 16 it wont run again
                    blja_comp_num += 1              #if an ace is chosen, it go as high as it can aslong as it doesnt lose the game
                elif blja_comp_num + 11 < 21:
                    blja_comp_num += 11
            elif 10 < blja_comp_rand:
                blja_comp_num += 10
            if blja_comp_num > 16:
                blja_menu = False

        blja_bet = input("How Much Would You Like To Bet: ")    #i thought it would be easier to bet once instead of betting
        blja_bet = int(def_pro(blja_bet,0,money))               #every deal like in real blackjack, aslo you cant see your
        blja_menu = True                                        #enemys cards so it is kind of blind gambling.
        while blja_menu == True:
            print("Dealing Cards")
            time.sleep(0.5)
            blja_user_rand = random.randint(1,13)
            if blja_user_rand > 9:
                blja_user_num += 10
            elif blja_user_rand == 1:
                blja_ace = input("You Got Dealt an Ace. Enter 1 for One, enter 2 for Eleven: ")
                blja_ace = int(def_pro(blja_ace,1,2))
                if blja_ace == 1:                       #it has simular logic bet lets the user decide when to stop or when to re-run
                    blja_user_num += 1                  #and how much an ace will equal if they get one.
                elif blja_ace == 2:                     #it automaticaly stops if the value is greater than or equal to 21
                    blja_user_num += 11
            elif 1 < blja_user_rand < 10:
                blja_user_num += blja_user_rand
            blja_user_display.append(blja_list[blja_user_rand-1])
            if blja_user_rand != 1:                                             #prints out the card they got that round
                print("You Got Dealt A " + str(blja_list[blja_user_rand-1]))    #all the cards they have in there hand
            print("Your Current Hand Is:")                                      #and the total value of there cards added
            for a in range(0,len(blja_user_display)):                           #up.
                print(blja_user_display[a])
            print("Your Current Total is " + str(blja_user_num))                #the total hand print works with a four loop
            if blja_user_num >= 21:                                             #that runs as many times as the list is long
                blja_menu = False
            else:
                blja_loop = input("Enter 1 to Deal Again, Enter 2 to Finish: ")
                blja_loop = int(def_pro(blja_loop,1,2))
                if blja_loop == 2:
                    blja_menu = False

        print("Your Final Score Is " + str(blja_user_num))
        print("The Computers Final Score Is " + str(blja_comp_num)) #i wanted to have a seperate print statement if anybody
        if blja_user_num < 22 and blja_comp_num < 22:               #went over 21 because i wanted the user to still
            if blja_user_num == blja_comp_num:                      #lose there money even if the computer goes over to
                print("-ITS A TIE-")                                #also a diferent print statement for presentation
            elif blja_user_num > blja_comp_num:
                money += blja_bet                            #youll find that the actual logic is not that long
                print("YOU WIN!")                            #but the presentaion takes up most of the lines
            elif blja_user_num < blja_comp_num:              #of code in the whole program.
                money -= blja_bet
                print("YOU LOSE!")
        elif blja_user_num > 21 and blja_comp_num < 22:
            money -= blja_bet
            print("You Went Over 21. YOU LOSE!")
        elif blja_user_num < 22 and blja_comp_num > 21:
            money += blja_bet
            print("Computer Went Over 21. YOU WIN!")
        elif blja_user_num > 21 and blja_comp_num > 21:
            money -= blja_bet
            print("Both You and the Computer Went Over 21. YOU LOSE!")

    if money <= 0:
        print("Sorry, but your broke: GAME OVER")   #this runs if your money is ever equal to 0, it just runs the leaving code
        game_choice = 4

    if int(game_choice) == 4:
        time.sleep(0.5)
        exit("Thanks for trying out the PYTHON CASINO.\nCome Back Soon!")   #exits the program so the while loop doesnt re-run
