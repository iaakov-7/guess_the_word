from random import choice

def get_random_word():
    words_list = ["banana","coffee","summer","winter","family",
                  "yello","school", "guitar","garden","doctor","computer",
                  "football","mountain","internet","elephant","notebook",
                  "birtday","beautiful","breakfast","chocolate" ]
    secret_word = choice(words_list)
    return secret_word


