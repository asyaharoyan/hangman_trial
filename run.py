#import
import random


class Hangman:
   words = [
       "PYTHON", "HANGMAN", "DEVELOPER", "PROGRAMMING", "COMPUTER", "SOFTWARE",
       "CODING", "ALGORITHM", "FUNCTION", "VARIABLE", "DEBUGGING", "SYNTAX",
       "FRAMEWORK", "DATABASE", "KEYBOARD", "ITERATION", "RECURSION",
       "INTERFACE", "CONDITION", "STATEMENT", "LOOP", "CLASS", "OBJECT",
       "METHOD"
   ]

   hangman = [
   """
   ______________
   |_______
   |      |
   |      
   |     
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |      |
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     /|
   |      
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     
   _____________
   """, 
   """
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
      self.restart = None
      self.word = ""
      self.current_guess = ""
      self.used_letters = []

   def validate_name(self):
      while True:
        name = input("Please enter your name: \n")
        if name.isalpha() and len(name) > 1:
            return name
        else:
            print("Please enter a valid name!")

   def finish_game(self):
      """
      Ending the game if the player does not want to play again.
      """
      print("""
      ----------------------------------------------
      **********************************************
      So sad that you have to go, but see you soon!!
      **********************************************
      ----------------------------------------------
      \n
      """)

   def show_instructions(self):
      """
      Shows the instructions of the game and asks if the player wants to play.
      """
      print("""
      The computer is going to choose a random word. 
      You need to guess the letter. 
      You have 6 chances to fail. 
      You can not guess the same letter 2 times. 
      If you do not guess the word, the man will be hanged :(
      --------------------------------------------------------
      """)
      self.start_guess = input("Do you want to start the game? (Y/N)\n").upper()
      self.check_yes_no()
      return self.start_guess

   def random_word(self):
      """
      The function chooses a random word from the list.
      """
      self.word = random.choice(Hangman.words)
      self.current_guess = "_ " * len(self.word)
      return self.current_guess

   def restart_hangman(self):
      """
      The function asks if the player wants to guess another word.
      """
      self.used_letters = []
      self.start_guess = input("Do you want to start again?(Y/N) \n").upper()
      self.check_yes_no()

   def check_guess(self):
      """
      The function checks if the player guessed right and adds the letter in the word. 
      If it is a wrong guess or the player guesses the same letter the function informs the player and gives a chance to guess again.
      """
      self.random_word()
      # variable to keep track on wrong answers
      wrong = 0
      while wrong < len(self.hangman) - 1 and "_" in self.current_guess:
         print(self.hangman[wrong])
         print("You have used the following letters: ", self.used_letters,
               "\n")
         print("The word is ", self.current_guess, "\n")
         guess = input("Please guess a letter:  \n").upper()
         #check if the input is a letter. The line of the code is taken from https://codereview.stackexchange.com/
         if not guess.isalpha():
            print("That is not a letter. Please try again! \n")
            continue
         if guess in self.used_letters:
            print("""
            _______________________________________________________
            You've already guessed that letter. Try a different one.
            -------------------------------------------------------
            """)
            continue

         if guess in self.word:
            #using enumerate method to find the right letter on the right index
            for word_index, guess_word in enumerate(self.word):
               if guess_word == guess:
                  for letter in self.current_guess:
                     self.current_guess = (
                         self.current_guess[:word_index * 2] + guess_word +
                         self.current_guess[word_index * 2 + 1:])

            print("Correct guess! ", self.current_guess, "\n")
            self.used_letters.append(guess)
         else:
            self.used_letters.append(guess)
            wrong += 1
            print(" Unfortunately you guessed wrong. Pick another letter! \n")
            continue
      #checking if there are no _, then the player guessed the word
      if "_" not in self.current_guess:
         print(
             """
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         Congratulations! You guessed the word:
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         """, self.word, "\n")
         self.restart_hangman()
      else:
         print(self.hangman[wrong])
         print("You could not guess the word. The game is over.\n")
         print("The word was ", self.word, "\n")
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
      print("""
      Try to guess the word.
      *********************
      """)
      self.start_game = input("""
      Do you want to read the instuctions or you want to start the game?
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
      Type S to START the game, 
      E to EXIT the game or 
      I to read the INSTRUCTIONS: 
      """).upper()
      self.answer_check()
      return self.start_game

   def answer_check(self):
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
            self.start_game = input("Please enter a valid value: \n").upper()

   def check_yes_no(self):
      while True:
         if self.start_guess == "Y":
            self.check_guess()
            break
         elif self.start_guess == "N":
            self.finish_game()
            break
         else:
            self.start_guess = input("Please enter a valid value: \n").upper()

   def main(self):
        self.validate_name()
        self.welcome()


#run the program
user_1 = Hangman(name = '')
user_1.main()