import random

# word to chiose from the list
word_list = ["generator", "brightless", "containing", "vocabulary", "welcome", "timeline", "selection", "workplace", "language", "important", "computer", "paragraphs", "longest", "expresses", "composed", "government", "synonyms", "enormous", "prognosticator", "messagem"]

# picking random word from the list 
selected_word = random.choice(word_list)

#starting the game
number_of_guesses = 6
guessed_letters = []
print("_________________________")
#loop the until the game won or lose
while number_of_guesses > 0:
    #ask the player for input
    guess = input("gusses your letter?").lower()
    # check the input
    if len(guess) != 1:
        print("please input a single letter")
        continue

    if guess in guessed_letters:
        print("you have already guess that letter")
        continue
    
    #check the guess
    if guess in selected_word:
        print("correct")

        guessed_letters.append(guess)
        word = "".join([x if x in guessed_letters else "_" for x in selected_word])
        print(word)

        if "_" not in word:
            print("you win")
            break
    
    else:
        print("incorrect")
        guessed_letters.append(guess)
        number_of_guesses = number_of_guesses-1
        print(" ".join(["0" if i < number_of_guesses else "|" for i in range(6)]))
        if number_of_guesses == 0:
            print("you lose, the word was " + selected_word)
print("______________________")