# import random to shuffle the words,  colorama for colors
import random
import os
# import colorama
# from colorama import Fore, Back, Style
# how to use the library is taken from https://www.youtube.com/watch?v=u51Zjlnui4Y
# colorama.init(autoreset = True) # to reset the colort after each line


class Hangman:
   words = {
       "PYTHON":
       "A powerful programming language",
       "HANGMAN":
       "A classic word-guessing game",
       "DEVELOPER":
       "Someone who writes code",
       "PROGRAMMING":
       "The process of writing computer programs",
       "COMPUTER":
       "An electronic device for processing data",
       "SOFTWARE":
       "Programs and data that run on a computer",
       "CODING":
       "The act of writing code or programming",
       "ALGORITHM":
       "A step-by-step procedure for solving a problem",
       "FUNCTION":
       "A reusable block of code that performs a specific task",
       "VARIABLE":
       "A storage location identified by a memory address and a symbolic name",
       "DEBUGGING":
       "The process of finding and fixing errors in code",
       "SYNTAX":
       "The set of rules that dictate the combinations of symbols that are considered to be correctly structured programs",
       "FRAMEWORK":
       "A pre-built structure that developers can use to build software applications",
       "DATABASE":
       "A structured collection of data",
       "KEYBOARD":
       "An input device that uses a set of keys or buttons to send data to a computer",
       "ITERATION":
       "The repetition of a process in order to generate a sequence of outcomes",
       "RECURSION":
       "A programming concept where a function calls itself directly or indirectly",
       "INTERFACE":
       "A point where two systems meet and interact",
       "CONDITION":
       "A statement that controls the flow of execution in a program",
       "STATEMENT":
       "An instruction that performs an action in a program",
       "LOOP":
       "A programming construct that repeats a group of statements",
       "CLASS":
       "A blueprint for creating objects",
       "OBJECT":
       "An instance of a class in object-oriented programming",
       "METHOD":
       "A function associated with an object in object-oriented programming"
   }

   # the hangman picture
   hangman = [
       """
   ______________
   |_______
   |      |
   |      
   |     
   |     
   _____________
    """, """
   ______________
   |_______
   |      |
   |      O
   |     
   |     
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |      |
   |     
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |     /|
   |      
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     / 
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     / \\
   _____________
   """
   ]

   def __init__(self, name):
      self.name = name
      self.start_game = None
      self.start_guess = None
      self.word = ""
      self.current_guess = ""
      self.description = ""
      self.used_letters = []

   def clear(self):
      os.system('cls' if os.name == 'nt' else 'clear')

   def validate_name(self):
      """
        The function validates the name input to make sure that it is at least 2 letters.
        """
      while True:
         name = input("Please enter your name: \n")
         if name.isalpha() and (len(name) > 1 and len(name) < 15):
            self.name = name.upper()
            break
         else:
            print(Fore.RED + "Please enter a valid name!")
            continue

   def show_instructions(self):
      """
        Shows the instructions of the game and asks if the player wants to play.
        """
      print(Fore.GREEN + """
        The computer is going to choose a random word. 
        You need to guess the letter. 
        You have 6 chances to fail. 
        You can not guess the same letter 2 times. 
        If you do not guess the word, the man will be hanged :(
        --------------------------------------------------------
        """)
      self.start_guess = input(
          Fore.YELLOW + "Do you want to start the game? (Y/N)\n").upper()
      self.check_yes_no()
      return self.start_guess

   def random_word(self):
      """
        The function generates a random word from the list and its description.
        """
      self.word = random.choice(list(Hangman.words.keys()))
      # Show dashes instead of the word.
      self.current_guess = "_ " * len(self.word)
      self.description = Hangman.words[self.word]
      return self.current_guess, self.description

   def restart_hangman(self):
      """
        The function asks if the player wants to guess another word.
        """
      self.used_letters = []
      self.start_guess = input(Fore.YELLOW +
                               "Do you want to start again?(Y/N) \n").upper()
      self.check_yes_no()

   def check_guess(self):
      """
        The function checks if the player guessed right and adds the letter in the word. 
        If it is a wrong guess or the player guesses the same letter the function informs the player 
        and gives a chance to guess again.
        """
      self.random_word()
      print(Fore.CYAN + self.description)
      # local variable to keep track on wrong answers
      wrong = 0
      # Loop the function untill the game is over.
      while wrong < len(self.hangman) - 1 and "_" in self.current_guess:
         print(self.hangman[wrong])
         print("You have used the following letters: ", self.used_letters,
               "\n")
         print("The word is ", self.current_guess, "\n")
         guess = input(Fore.BLUE + "Please guess a letter:  ").upper()
         self.clear()
         # check if the input is a letter.
         # The line of the code is taken from https://codereview.stackexchange.com/
         if not guess.isalpha():
            print(Fore.RED + "That is not a letter. Please try again! \n")
            continue
         elif len(guess) > 1:
            print(Fore.RED + "Please pick one letter!")
            continue

         # check if the user has already guessed the letter
         if guess in self.used_letters:
            print(Fore.RED + """
            _______________________________________________________
            You've already guessed that letter. Try a different one.
            -------------------------------------------------------
            """)
            continue

         if guess in self.word:
            # using enumerate method to find the right letter on the right index
            for word_index, guess_word in enumerate(self.word):
               if guess_word == guess:
                  for letter in self.current_guess:
                     self.current_guess = (
                         self.current_guess[:word_index * 2] + guess_word +
                         self.current_guess[word_index * 2 + 1:])

            #Congradulate the player and continue the game
            print(Fore.GREEN + "Correct guess! ", self.current_guess, "\n")
            self.used_letters.append(guess)
         else:
            self.used_letters.append(guess)
            wrong += 1
            print(Fore.RED +
                  "Unfortunately you guessed wrong. Pick another letter! \n")
            continue

      #checking if there are no _, then the player guessed the word
      if "_" not in self.current_guess:
         print(
             Fore.GREEN + """
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             Congratulations! You guessed the word:
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             """, self.word, "\n")
         self.restart_hangman()
      else:
         print(self.hangman[wrong])
         print(Fore.RED + "You could not guess the word. The game is over.\n")
         print(Back.CYAN + "The word was ", self.word, "\n")
         self.restart_hangman()

   def welcome(self):
      """
        The start of the game. Welcomes the player and asks if they want to read instryctions.
        """
      print(f"""
        ******************************
        Welcome to HANGMAN {self.name}.
        ******************************
        ------------------------------
        """)
      self.start_game = input("""
        ///////////////////////////////////////////////////////////////////
        Do you want to read the instuctions or you want to start the game?
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        -------------------------------------------------------------------\n
        Tye:
        S to START the game,
        E to EXIT the game,
        I to read the INSTRUCTIONS: \n
        """).upper()
      self.check_welcome_input()
      return self.start_game

   def finish_game(self):
      """
        Ending the game if the player does not want to play again.
        """
      print(Fore.CYAN + """
        ----------------------------------------------
        **********************************************
        So sad that you have to go, but see you soon!!
        **********************************************
        ----------------------------------------------
        \n
        """)

   def check_welcome_input(self):
      """
        The function checks and validates the user input to call functions accordingly.
        """
      while True:
         if self.start_game == "S":
            self.check_guess()
            break
         elif self.start_game == "I":
            self.show_instructions()
            break
         elif self.start_game == "E":
            self.finish_game()
            break
         else:
            self.start_game = input(Fore.RED +
                                    "Please enter a valid value: \n").upper()
            continue

   def check_yes_no(self):
      while True:
         if self.start_guess == "Y":
            self.check_guess()
            break
         elif self.start_guess == "N":
            self.finish_game()
            break
         else:
            self.start_guess = input(Fore.RED +
                                     "Please enter a valid value: \n").upper()
            continue

   def main(self):
      """
        Add the functions in one with the right order
        """
      self.validate_name()
      self.welcome()


user1 = Hangman(name="")
user1.main()
