from random import choice

def get_random_word():
    words_list = ["banana","coffee","summer","winter","family",
                  "yello","school", "guitar","garden","doctor","computer",
                  "football","mountain","internet","elephant","notebook",
                  "birtday","beautiful","breakfast","chocolate" ]
    secret_word = choice(words_list)
    return secret_word

def user_guess():
    abc_lettrs = [chr(i) for i in range(97,123)]
    running = True
    while running:
        user_letter = input("Enter your guess (one Englisg letter)\n").lower()
        if not user_letter in abc_lettrs:
            print("One English letter only!") 
        else:
            running = False
    return user_letter
    

