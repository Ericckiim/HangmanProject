import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD_BANK = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop'
'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language',
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus',
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'wind'
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive',
 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure',
 'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter',
 'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy'
 'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship',
 'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 
 'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment',
 'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion',
 'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation'
 'absence', 'mystery', 'morning', 'device', 'thoughts']


# Function that picks a random word from the word bank and returns the chosen word

def pick_word():
    return random.choice(WORD_BANK)

# Function that checks if inputted charcter belongs in the word, returns true if yes and false if no

def check_character(guess, answer):
    if guess in answer:
        return True
    else:
        return False

# Function that prints the amount of spaces in the answer
def space_printer(answer):
    spaces = ""
    
    for i in range(0,len(answer)):
        spaces += ("_ ")

    return spaces

# Function that goes through the characters of a word and replaces the ones that match
def fill_answer(guess, answer):
    spaces = space_printer(answer)
    spaceslist = []
    for c in spaces:
        spaceslist += "_"

    answerlist = []
    for c in answer:
        answerlist += c

    for i in answerlist:
        if guess == answerlist[i]:
            spaceslist[i] = guess


# Runs the game

def game():
    answer = pick_word()
    numTurns = 6
    picIndex = 0

    print("Welcome to hangman!")
    print(HANGMANPICS[picIndex])
    print(answer)
    print("The answer is: " + space_printer(answer))

    guess = input("Make your first guess: ")

    #if check_character(guess, answer):

if __name__ == "__main__":
    game()