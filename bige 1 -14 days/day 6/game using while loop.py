#Start a normal game
#Mentor - Code with Mosh

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already Started!")
        else:
            started = True
            print("Car Started.....")
    elif command == "stop":
        if not started:
            print("Car is already Stopped!")
        else:
            started = False
            print("Car Stopped.")
    elif command == "help":
        print('''
Start - to start the Car
stop - to stop the Car
quite - to quite 
        ''')
    elif command == "quite":
        print('Game exit. Thank you!')
        break
    else:
        print("Sorry! I don't understand what are you talking about ")