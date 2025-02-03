import random
import os

def load_word_library(filename):
    """
    Load word and hint pairs from a text file.

    Args:
        filename (str): Path to the word library file.

    Returns:
        list: A list of tuples containing word and hint pairs.
    """
    word_hint_pairs = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            # Split each line into word and hint using comma as delimiter
            parts = line.strip().split(',', maxsplit=1)
            if len(parts) != 2:
                # If the line format is incorrect, skip it and print an error message
                print(f"Error: Line {line_number} in the word library file does not have the correct format. Skipping this line.")
                continue
            word, hint = parts
            # Add the word and hint pair to the list after stripping whitespace
            word_hint_pairs.append((word.strip().lower(), hint.strip()))
    return word_hint_pairs

def choose_word(word_hint_pairs):
    """
    Choose a random word and hint pair from the given list.

    Args:
        word_hint_pairs (list): List of tuples containing word and hint pairs.

    Returns:
        tuple: A randomly chosen word and hint pair.
    """
    return random.choice(word_hint_pairs)

def display_word(word, guessed_letters):
    """
    Create a display string for the word with guessed letters revealed.

    Args:
        word (str): The word to be guessed.
        guessed_letters (list): List of letters that have been guessed correctly.

    Returns:
        str: A string representing the current state of the word with guessed letters revealed.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter  # Show the letter if guessed
        else:
            display += "_"  # Show underscore for letters not guessed
    return display

def draw_stickman(num_attempts, total_attempts):
  """
  Draw a stick figure representing hangman based on the fraction of incorrect attempts.

  Args:
      num_attempts (int): Number of incorrect guesses.
      total_attempts (int): Total number of attempts allowed.
  """
  stickman_parts = [
      "  _______",
      " |/      |",
      " |      (o)",
      " |     --|--",
      " |       |",
      " |      / \\",
      " |",
      "_|___"
  ]
  # Calculate the fraction of incorrect attempts
  fraction = num_attempts / total_attempts
  # Calculate the number of stickman parts to display based on the fraction
  parts_to_display = int(fraction * len(stickman_parts))
  # Draw the stickman parts based on the fraction of incorrect attempts
  for i in range(parts_to_display):
      print(stickman_parts[i])
  print("\n")

def main():
    print("Welcome to the Word Guessing Game!")
    # Specify the full path to your word library file
    word_library_path = "/media/harshdeep-singh/Disk/HaRrY/Coding BootCamp/Python Project/Code/word_library.txt"
    # Check if the file exists
    if not os.path.isfile(word_library_path):
        print("Error: Word library file not found.")
        return

    # Load word and hint pairs from the library file
    word_hint_pairs = load_word_library(word_library_path)
    # Choose a random word and hint pair
    word, hint = choose_word(word_hint_pairs)
    z=int((1+len(word))/2)
    max_attempts = z+2
    guessed_letters = []

    print("Hint: {}".format(hint))
    print("The word has {} letters:".format(len(word)))
    print(display_word(word, guessed_letters))

    remaining_attempts = max_attempts
    while remaining_attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word:
                print("Correct guess!")
                guessed_letters.append(guess)
                if set(guessed_letters) >= set(word):  # Check if all letters in word are guessed
                    print("Congratulations! You guessed the word '{}'!".format(word))
                    break
            else:
                print("Incorrect guess!")
                remaining_attempts -= 1
                draw_stickman(max_attempts - remaining_attempts, max_attempts)

        else:
            print("Invalid input! Please enter a single letter.")

        print("Attempts remaining: {}".format(remaining_attempts))
        print(display_word(word, guessed_letters))

    if remaining_attempts == 0:
        print("Sorry, you ran out of attempts. The word was '{}'.".format(word))

if __name__ == "__main__":
    main()
