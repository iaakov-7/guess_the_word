from random import choice
from time import sleep


WORDS_LIST = ["banana","coffee","summer","winter","family",
                  "yellow","school", "guitar","garden","doctor","computer",
                  "football","mountain","internet","elephant","notebook",
                  "birthday","beautiful","breakfast","chocolate" ]

def get_random_word():
    secret_word = choice(WORDS_LIST)
    return secret_word

def user_guess():
    abc_letters = [chr(i) for i in range(97,123)]
    user_letter = input("Enter your guess (one Englisg letter)\n").lower()
    while not user_letter in abc_letters:
        print("One English letter only!")
        user_letter = input("Enter your guess (one English letter)\n").lower()
    return user_letter

def show_word_status(word_in_lst_version):
    return f"the status of word is: {" ".join(word_in_lst_version)}"

def show_used_letters(used_letters):
    return f"the used wrong words are: {" ,".join(used_letters)}"

def show_how_many_attempts_left(current_attempts):
    return f"you have left {current_attempts} attempts"
     
def show_status_game(masked_word,current_attempts,used_letters):
    return f"""{show_word_status(masked_word)}
    {show_how_many_attempts_left(current_attempts)}
    {show_used_letters(used_letters)}"""

def check_user_guess(user_letter,secret_word):
    return user_letter in secret_word

def update_masked_word(user_letter,masked_word,secret_word):
    for i, letter in enumerate(secret_word):
            if user_letter == letter:
                masked_word[i] = letter 

def check_victory(masked_word):
    return "_" not in masked_word

def check_if_used_letter(user_letter,used_letters,masked_word):
    return user_letter in used_letters or user_letter in masked_word                                          

def game_management():
    attempts = 7
    current_attempts = attempts
    secret_word = get_random_word()     
    masked_word = ["_"] * len(secret_word)
    used_letters = ""
    print(show_word_status(masked_word))
    while current_attempts:
        user_letter = user_guess()
        if check_if_used_letter(user_letter,used_letters,masked_word):
            print(f"""you used this letter
{show_status_game(masked_word,current_attempts,used_letters)}""")
            continue
        if check_user_guess(user_letter,secret_word):
            update_masked_word(user_letter,masked_word,secret_word)
            if check_victory(masked_word):    
                return f"""Congratulations, you guessed the whole word: '[{secret_word}]' 
you used {attempts - current_attempts} from {attempts} attempts"""
            else:
                print(f"""Successful guess 
{show_status_game(masked_word,current_attempts,used_letters)}""")      
        else:     
            current_attempts -= 1
            used_letters += user_letter
            print(f"""boo..., wrong guess! 
{show_status_game(masked_word,current_attempts,used_letters)}""")
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
                    print(game_management())
                    sleep(2)
                case 2:
                    print("bye...")
                    running = False
                case _:
                     print("Enter 1 or 2 only!")   
        except ValueError:
            print("Enter 1 or 2 only!")
            
menu()


