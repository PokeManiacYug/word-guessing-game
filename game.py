from word_finder import word_finder_func
import os, signal, time


def user_inp_comms():
    keepTaking = True
    while keepTaking:
        len_of_word = int(input('\nWhat should be the length of the word?\n'))
        if len_of_word > 32:
            print("\nI don't really know a word that big. If you do know one, then..... well, good for you, I guess...\n")
            continue
        no_of_guesses = int(input('\nHow many guesses do you want?\n'))
        if no_of_guesses < len_of_word:
            print("\nHmmm... You need more guesses than the length of the chosen word. Trust me on that.\n")
            continue
        elif no_of_guesses == len_of_word:
            print("o_O Daring today, aren't we? You'll need more guesses, but you do you...\n")
            keepTaking = False
        else:
            keepTaking = False
    return len_of_word, no_of_guesses


def take_user_input():
    
    len_of_word, no_of_guesses = user_inp_comms()
    word_for_game = word_finder_func(len_of_word)
    losing_screen_word = word_for_game
    the_guesses = []
    correct_guess_count = 0
    star_array = []

    for i in range(len_of_word):
        star_array.append('*')
   
    while no_of_guesses > 0:
        guess = input('\nEnter your guess\n').strip()
        if len(guess) > 1:
            print("\nYou can't guess multiple letters at once. Please only guess one letter.\n")
            continue
        the_guesses.append(guess)

        if guess in word_for_game:
            correct_guess_count += 1
            print(f'\nCorrect guess\n')
            posi = word_for_game.rindex(guess)+1
            no_of_guesses -= 1
            correct(word_for_game,guess,posi,star_array)
            if correct_guess_count == len_of_word:
                victory_screen()
                break
            word_for_game = word_for_game.replace(guess, '*')
            print(f'\n{no_of_guesses} guesses remain\n')

        else:
            print('\nIncorrect guess\n')
            no_of_guesses -= 1
            incorrect(star_array)
            print(f'\n{no_of_guesses} guesses remain\n')
            if no_of_guesses == 0:
                losing_screen(losing_screen_word)

def correct(word_for_game,guess,posi,star_array):
    if guess in word_for_game:
        star_array.pop(posi-1)
        star_array.insert(posi-1, guess)
    print(*star_array)

def incorrect(star_array):
    print(*star_array)

def victory_screen():
    print('\n\n\n\nC O N G R A T U L A T I O N S \n\n Y O U\tW I N\n')
    print('\nThanks for playing the word guessing game....')
    play_again()

def losing_screen(losing_screen_word):
    print('\nSorry! YOU LOSE!')
    print(f'\n\nThe word was "{losing_screen_word}"')
    play_again()


def play_again():
    keepAsking = True
    while keepAsking:
        print('\n\nDo you want to play again... (Y/N)\n')
        choice = input("Pressing 'Y' will start a new game. Pressing 'N' will quit the terminal window\n").lower()
        if choice == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            keepAsking = False
            take_user_input()
        elif choice == 'n':
            keepAsking = False
            print('\nThanks again for playing the word guessing game!!!')
            time.sleep(2)
            print('\nClosing the terminal in 5 seconds...')
            time.sleep(5)
            os.kill(os.getppid(), signal.SIGHUP)
        else:
            print("\nThat was neither a Yes, nor a No... But I'll give you the benefit of the doubt and ask again...")
            continue



if __name__ == "__main__":
    take_user_input()
