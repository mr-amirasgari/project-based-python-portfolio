import random


def validate_input(guess):
    if not guess.isdigit():
        print("Please enter a valid number.")
        return False
    else:
        guess = int(guess)
        if guess>100 or guess<1:
            print("Please enter a number between 1 and 100.")
            return False
        return True
    

def main():
    rand_num=random.randint(1,100)
    score =100
    while True:
        guess = input("Guess a number between 1 and 100: ")
        
        if guess == 'q':
            print("Thanks for playing!")
            break
        if not validate_input(guess):
            continue
        guess = int(guess)
        if guess == rand_num:
            print(f"Your score is: {score}")
            wanna_play = input("Do you want to play again? (y/n): ")
            if wanna_play == 'y':
                rand_num=random.randint(1,100)
                score = 100
                continue
            else:
                print("Thanks for playing!")
                break
                
            
        elif guess > rand_num:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")
         
        score -= 10
        score = max(score, 0)
            
    
    
if __name__ == "__main__":
    
    main()