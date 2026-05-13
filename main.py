from random import choice
from time import sleep


def get_random_word():
    words_list = ["banana","coffee","summer","winter","family",
                  "yello","school", "guitar","garden","doctor","computer",
                  "football","mountain","internet","elephant","notebook",
                  "birtday","beautiful","breakfast","chocolate" ]
    secret_word = choice(words_list)
    return secret_word

def user_guess():
    abc_letters = [chr(i) for i in range(97,123)]
    running = True
    while running:
        user_letter = input("Enter your guess (one Englisg letter)\n").lower()
        if not user_letter in abc_letters:
            print("One English letter only!") 
        else:
            running = False
    return user_letter

def show_word_status(word_in_lst_version):
    return " ".join(word_in_lst_version)

def game():
    attempts = 7
    current_attempts = attempts
    secret_word = get_random_word()     
    word_with_lines = ["_"] * len(secret_word)
    used_letters = ""
    print(show_word_status(word_with_lines))
    while current_attempts:
        user_letter = user_guess()
        if user_letter in used_letters:
            print(f"""you used this letter! 
all used letters: {", ".join(used_letters)}""")
            continue
        used_letters += user_letter
        flag = False
        for i, letter in enumerate(secret_word):
            if user_letter == letter:
                flag = True
                word_with_lines[i] = letter
                
                if "_" not in word_with_lines:
                    return f"""Congratulations, you guessed the whole word: '[{secret_word}]' 
you used {attempts - current_attempts} from {attempts} attempts"""  
        if flag == True:    
            print(f"""Successful guess 
the word now is: {show_word_status(word_with_lines)}""") 
    
        else:
            current_attempts -= 1
            print(f"""booz, wrong guess! 
You have {current_attempts} attempts left
Status of word is {show_word_status(word_with_lines)}""")
    return f"You failed, The game is over because you used all attempts the word was: '[{secret_word}]'"    

def menu():
    running = True
    while running:
        try:
            action = int(input("""--------------------------------
Welcome to 'guess the word' game
--------------------------------
   press 1 to start the game 
   press 2 to exit 
        : """))

            match action:
                case 1:
                    print(game())
                    sleep(3)
                case 2:
                    print("bye...")
                    running = False
                case _:
                     print("Enter 1 or 2 only!")   
            
        except ValueError:
            print("Enter 1 or 2 only!")
            
menu()


