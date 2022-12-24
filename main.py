import random
import time

def read_words_into_dictionary(three_letter_words, five_letter_words):
    with open("wordlewords.txt", "r") as in_file:
        for word in in_file:
            word = word.strip()
            if len(word) == 3:
                three_letter_words.append(word)
            elif len(word) == 5:
                five_letter_words.append(word)

def display_message():
    print("Program 3: Wordle Reload")
    print("CS 141, Spring 2022, UIC")
    print("The objective of this game is to guess the randomly selected")
    print("word within a given number of attempts. You can select either")
    print("a three or five word board.")
    print("At the conlusion of the game, stats will be displayed.")
    print("Indicators will be given if characters of the user entered")
    print("word are reflected in the guessed word.")
    print("   - If the character is in the correct position, the character "
          "will display as an uppercase value.")
    print("   - If the character is within the random word, the character "
          "will display as a lowercase value.")
    print("  - If you enter a character that is not in the word, an asterisk "
          "'*' will display.")
    print("\n")


def random_word(dictionary):
    max = len(dictionary)
    random_number = random.randint(0, max-1)
    ran_word = dictionary[random_number]
    return ran_word

def binary_search(search_word, dictionary):
    low = 0
    high = len(dictionary) - 1
    while low <= high:
        mid = (low + high) // 2
        if search_word == dictionary[mid]:
          return mid
        elif search_word < dictionary[mid]:
          high = mid - 1
        elif search_word > dictionary[mid]:
          low = mid + 1
    return -1


def validate_guess(guess, menu_option):
    if menu_option == 1:
        if len(guess) != 3:
            print("Invalid word entry - please enter a word that is 3 characters long. ")
            return False
    if menu_option == 2:
        if len(guess) != 5:
            print("Invalid word entry - please enter a word that is 5 characters long. ")
            return False
    return True


# def add_brackets(result, letter):
#     result += "[{}]".format(letter)

def add_brackets(result, letter):
    result.append('[')
    result.append(letter)
    result.append(']')

def comparing_letters(original_word, user_guess):
    result = ""
    for i in range(len(original_word)):
        matched = False
        for j in range(len(user_guess)):
            if original_word[i] == user_guess[j]:
                matched = True
                if i == j:
                    result += "[" + original_word[i].upper() + "]"
                else:
                    result += "[" + original_word[i] + "]"
                break
        if not matched:
            result += "*"
    return result


def board_display(records):
    for item in records:
        print(item)

def display_menu():
    while True:
        print("1. To play Wordle Reload 3 letter play")
        print("2. To play Wordle Reload 5 letter play")
        print("3. Exit the program")
        print("Enter your choice --> ") 
        menu_option = int(input())

        if menu_option == 1:
            return 1
        elif menu_option == 2:
            return 2
        elif menu_option == 3:
            return 3
        else:
            print("Invalid menu option.")
          
def main():
    three_letter_words = []
    five_letter_words = []
    read_words_into_dictionary(three_letter_words, five_letter_words)
    display_message()

    num_attempts = 0
    max_trials = 0
    num_of_guesses = 0
    num_of_streak = 0
    total_success_time = 0
    numberof_games = 0
    max_streaks = 0
    current_streak = 0
  
    while True:
        # menu_option = int(input("Select a menu option: \n1. To play Wordle Reload 3 letter play \n2. To play Wordle Reload 5 letter play \n3. Exit the program \nYour choice --> "))
        menu_option = display_menu()
        if menu_option == 1:
            max_trials = 4
        elif menu_option == 2:
            max_trials = 6
                
        if menu_option == 1:
            print("To get started, enter your first 3 letter word. ")
            print("You have 4 attempts to guess the random word. ")
            print("The timer will start after your first word entry. ")
            print("Try to guess the word within 20 seconds. ")

            rnd_word = random_word(three_letter_words)
            numberof_games += 1
            all_results = []
            elapsed_seconds = 0
            start_time = time.time()
            print(rnd_word)
            while num_attempts < max_trials:
                guess = input("Please enter word --> ")
                guess = guess.lower()
                if validate_guess(guess, menu_option):
                    result = binary_search(guess, three_letter_words)
                    if result == -1:
                        print("Not a playable word, please select another word. ")
                        continue
                    else:
                        result = comparing_letters(rnd_word, guess)
                        if '*' not in result and rnd_word == guess:
                            all_results.append(result)
                            board_display(all_results)
                            num_attempts += 1
                            current_streak += 1
                            total_success_time = total_success_time + time.time() - start_time
                            print()
                            print("Nice Work!  You guessed the correct word")
                            print(f"  - You completed the board in: {total_success_time} seconds")
                            print(f"  - Number of Guesses: {num_attempts}")
                            print(f"  - Current Streak: {current_streak}")
                            num_attempts = 0
                            if current_streak > max_streaks:
                                max_streaks = current_streak
                            break
                        else:
                            all_results.append(result)
                            board_display(all_results)
                            num_attempts += 1
                            current_streak = 0
            if num_attempts >= 4:
              print(f"Sorry, you have exceeded the maximum number of attempts. The word was {rnd_word}")
              current_streak = 0;
              num_attempts = 0;
              continue;
        if menu_option == 2:
            print("To get started, enter your first 5 letter word. ")
            print("You have 6 attempts to guess the random word. ")
            print("The timer will start after your first word entry. ")
            print("Try to guess the word within 40 seconds. ")

            rnd_word = random_word(five_letter_words)
            numberof_games += 1
            all_results = []
            elapsed_seconds = 0
            start_time = time.time()
            print(rnd_word)
            while num_attempts < max_trials:
                guess = input("Please enter word --> ")
                guess = guess.lower()
                if validate_guess(guess, menu_option):
                    result = binary_search(guess, five_letter_words)
                    if result == -1:
                        print("Not a playable word, please select another word. ")
                        continue
                    else:
                        result = comparing_letters(rnd_word, guess)
                        if '*' not in result and rnd_word == guess:
                            all_results.append(result)
                            board_display(all_results)
                            num_attempts += 1
                            current_streak += 1
                            total_success_time = total_success_time + time.time() - start_time
                            print()
                            print("Nice Work!  You guessed the correct word")
                            print(f"  - You completed the board in: {total_success_time} seconds")
                            print(f"  - Number of Guesses: {num_attempts}")
                            print(f"  - Current Streak: {current_streak}")
                            num_attempts = 0
                            if current_streak > max_streaks:
                                max_streaks = current_streak
                            break
                        else:
                            all_results.append(result)
                            board_display(all_results)
                            num_attempts += 1
                            current_streak = 0
            if num_attempts >= 6:
              print(f"Sorry, you have exceeded the maximum number of attempts. The word was {rnd_word}")
              current_streak = 0;
              num_attempts = 0;
              continue;
        if menu_option == 3:
            print("Overall Stats: ")
            print(f" - Your longest streak is: {max_streaks}")
            if max_streaks > 0:
              avg = total_success_time / numberof_games
              print(f"- Average word completion time: {avg}")
              print(f"Exiting Program")
            break;
          
if __name__ == "__main__":
    main()