### Screenshots ###
![](https://github.com/harshdeep-005/Word_Guessing_Puzzle-Python-/blob/main/Screenshot%202025-07-06%20172556.png)
![](https://github.com/harshdeep-005/Word_Guessing_Puzzle-Python-/blob/main/Screenshot%202025-07-06%20172802.png)
![](https://github.com/harshdeep-005/Word_Guessing_Puzzle-Python-/blob/main/Screenshot%202025-07-06%20172827.png)


Hangman Game

This is a simple text-based Hangman game implemented in Python. The game allows players to guess letters to uncover a hidden word within a limited number of attempts.


Installation:
1.Ensure you have Python 3 installed on your computer.

2.Clone this repository to your local machine:
  git clone https://github.com/harshdeep-005/Word_Guessing_Puzzle-Python-

3.Navigate to the project directory:
  cd hangman-game

4.Firstly, put the path of word library file in 89th line of code.

5.Run the game:
  python main_code.py

  
Code Explanation:
1.load_word_library(filename):

>This function reads a text file containing word and hint pairs, separated by commas.
>It strips and cleans each line, ignoring empty lines.
>Each valid line is split into a word (converted to lowercase) and a hint.
>The function returns a list of tuples containing these word and hint pairs.

2.choose_word(word_hint_pairs):

>This function randomly selects a word and hint pair from the provided list of tuples.
>It uses the random.choice() function to make the selection.
>Returns the chosen word and hint as a tuple.

3.display_word(word, guessed_letters):

>This function creates a display string for the word, revealing guessed letters.
>It uses a comprehension to iterate over each letter of the word:
>If the letter has been guessed (found in guessed_letters set), it's displayed.
>Otherwise, an underscore (_) is displayed for unguessed letters.
>The function returns the formatted display string.

4.draw_hangman_part(part_index, max_attempts, num_attempts):

>This helper function retrieves a specific part of the hangman figure based on the number of incorrect attempts.
>It uses predefined strings (hangman_parts) representing different parts of the hangman figure.
>The function returns the specific part string based on the current game state.

5.draw_hangman(num_attempts, max_attempts):

>This function draws the hangman figure based on the number of incorrect attempts.
>It iterates through hangman_parts and prints the corresponding parts if the attempt count is reached.
>The function is called during the game to display the hangman figure.

6.get_user_guess(message="Enter a letter: "):

>This function prompts the user to enter a single alphabetic letter.
>It continues prompting until a valid input (a single letter) is provided.
>The function returns the lowercase valid guess.

7.play_game(word_library_path):

>This function is likely the main game loop where the Hangman game logic is implemented.
>It loads the word library from the specified file path.
>It chooses a random word and hint pair.
>It initializes variables for tracking game state (e.g., max_attempts, guessed_letters).
>It prompts the user to guess letters and manages game progress (e.g., updating display, checking win/lose conditions).
>The game loop continues until the player wins or loses.

To complete and execute the Hangman game, you'll need to implement or call the play_game(word_library_path) function, passing the path to your word library file. Ensure you have a properly formatted word library file with word and hint pairs to use with the game
  
  
How to Play:
1.Launch the game by running main_code.py in the terminal.
2.You will be provided with a hint for the hidden word.
3.Guess letters by entering them one at a time.
4.For each correct guess, the corresponding letters will be revealed in the hidden word.
5.For each incorrect guess, part of the hangman figure will be drawn.
6.Continue guessing until you uncover the entire word or run out of attempts.


Files and Structure:
1.main_code.py: Main Python script containing the Hangman game logic.
2.word_library.txt: Example word library file containing words and hints.
3.README.md: Documentation and instructions for the Hangman game.
