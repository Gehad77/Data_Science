from random import randint

class Game:
    def __init__(self):
        print('''Welcome In Full Game ...... ^_^
            
                Choose Your Game From Our Collection
                Press[1]: Play Car Game
                Press[2]: Play ROCK PAPER SCISSORS
                Press[3]: Play Math Games
                
                ''')
   
        
        self.Choices()

    def Choices(self):
        while True:
            user_choice = input('Enter Your Choice ===> : ')
            try:    
                if user_choice == '1':
                    self.Car()
                elif user_choice == '2':
                    self.Rock_Paper_Scissors()
                elif user_choice == '3':
                    Math()
                elif user_choice == 'quit':
                    break
                    
                else:
                    print('Please Choose Between 1,2 or 3 Or Quit')
                    
            except ValueError:
                print('Please Enter A Valid Choice')
                
    def Car(self):
        print('Welcome Car Game ^_^')
        print('Type Help To Know How To Start')
        command=""
        started = False
        while command != "quit":
            command = input("> Please Type The Order So I Can Go ===>  ").lower()
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
                print ("""
                       
                    I Don`t Understand the Orders Are :
                    
                    start => to start the car 
                    stop => to stop the car 
                    quit => to close the program and stop the car
                    
                    """)   
        
        
    
    def Rock_Paper_Scissors(self):
        print('Welcome To Rock Paper Scissors Game')
        t = ["Rock", "Paper", "Scissors"]
        computer = t[randint(0,2)]
        player = False
        while player == False:
       
            player = input("Rock, Paper, Scissors? ==> ")
            if player == computer:
                print("Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            elif player=="quit":
                break
            else:
                print("That's not a valid play. Check your spelling!")
          
            player = False
            computer = t[randint(0,2)]
            
class Math:
    def __init__(self):
        print('''
                 Welcome In Math Game ...... ^_^
                  Choose Your Game From Our Collection
                  Press[1]: Play Even-Odd Game
                  Press[2]: Play Sum Average Game
                  Press[3]: Play Multiplication Table Game
                  
              ''')
        
        
        self.Choices()

    def Choices(self):
        while True:
            user_choice = input('Enter Your Choice : ')
            try:
                if user_choice == '1':
                    self.Even_Odd_Game()
                elif user_choice == '2':
                    self.Sum_Average_Game()
                elif user_choice == '3':
                    self.Multiplication_Game()
                elif user_choice == 'quit':
                    Game()
                else:
                    print('Please Choose Between 1,2 or 3')
                    
            except :
                print('Please Enter A Valid Number')
                
    def Even_Odd_Game(self):        
        print('Welcome In The Even-Odd Game')
        print('Please Enter A Number ... And I Will Tell You It`s Even Or Odd')
        print('If You Want To Close The Game Enter X')
        while True:
            number=input('Enter A Number : ')
            if number == 'quit':   
                print('closing the program')
                print('Thanks ...')
                break
        
            try:   
                number =int(number)
                if number % 2 == 0:
                    print('it`s a even number')
                else:
                    print('it`s a odd number')
            except:
                print('please Enter A Valid Number')
            
            print('-----------------------')
    
    
    def Sum_Average_Game(self):
        print('Tis Game Will Take Several Numbers And Print The Average of Them')
        try:
            count=int(input('How Maby Numbers Would you Like To Sum : '))
            current_count=0
            sum=0
            while current_count <count:
                number=float(input('Enter The Number : '))
                sum += number
                current_count +=1
            
            print('Sum Of All Numbers = ', sum)
            print('Average Of All Numbers ' , sum/count)
        except :
            print('please Enter A Number')
    
    def Multiplication_Game(self):
        try:
            print('Welcome In Multiplication App ')
            print('Please Enter The Frist Number And Last Number of Multiplication Table : ')
            
            start=int(input('Enter the Frist Number Of The Table : '))
            end=int(input('Enter the Last Number Of The Table : '))
            for x in range(start,end+1):
                for y in range(1,13):
                    print (x,'X' , y , '=' , x*y)
                print('--------------------------------------')
        except :
            print('Please Try Again With A valid INT')
            print('---------------------------------')
            self.Multiplication_Game()
            
            
            
            
            
            
            
            
            
            
            
s1=Game()



