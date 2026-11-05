import random
Words = ["PYTHON","COMPUTER","PROGRAM","HANGMAN","KEYBOARD"]
word = random.choice(Words)
guessed = set()
attempts = 6
print("Welcome to Hangman Game!")
while attempts > 0:
    display=" "
    for letter in Words:
        if letter in guessed:
            display += letter + " "
        else:
            display + "_________"
    print("\nWord :",display)
    print("Attempt left:",attempts)


    if all(letter in guessed for letter in word):
        print("You win!")

        break

    guess = input("Guess a letter:").upper()
    if len(guess) != 1 or not guess.isalpha():
        print("Enter one alphabet only!")

        continue

    if guess in guessed:
        
        print("Already guessed!")

        continue
    guessed.add(guess)
    if guess in word:
        print("correct!")
    else:
        attempts -=1
        print("Wrong guess!")

if attempts == 0:
    print("Game over!")
    print("Word was:",word)
