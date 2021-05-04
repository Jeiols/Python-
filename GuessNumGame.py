print("Welcome,you have to guess a number")
print("Total number of guesses are 10")
print("The number to be guessed is in between 15-30")
s = 23
ng = 1 
while(ng<=10):
    m = int(input("Your guess\n"))
    if m>s:
        print("Choose a lesser number.\n")
    elif m<s:
        print("choose a greater number.\n")
    else:
        print("You won")
        print("Number of Guesses you took,",ng)
        break
    print(10-ng,"Guesses left.\n")
    print("Guess again!")
    ng = ng+1
if(ng>10):
    print("You lost dummy")