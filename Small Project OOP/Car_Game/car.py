# a car game
command=""
started = False
while command != "quit":
    command = input("> ").lower()
    if command=="start":
        if started:
            print("Car already started")
        else:
            started=True
            print('i`m ready to go')
    elif command=="stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print('car stopped')
    elif command=="help":
        print ("""
               start => to start the car 
               stop => to stop the car 
               quit => to close the program and stop the car
               """)
    elif command =="quit":
        print('car stopped')
        break
    else:
        print ("i don`t understand that")    




