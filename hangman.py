import random

def hangman():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    while tries > 0:
        word_guessed = ""
        for letter in word:
            if letter in guessed_letters:
                word_guessed += letter
            else:
                word_guessed += "_"

        if word_guessed == word:
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break

        print(f"Word: {word_guessed}")
        print(f"Tries left: {tries}")

        guess = input("Enter a letter or the full word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You have already guessed that letter. Try again.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct!")
            else:
                tries -= 1
                print("Incorrect guess. Try again.")
        elif len(guess) == len(word) and guess == word:
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break
        else:
            tries -= 1
            print("Incorrect guess. Try again.")

    if tries == 0:
        print(f"Out of tries! The word was '{word}'.")

hangman()
