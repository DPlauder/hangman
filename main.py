from random import randint

def choose_word():
  list = []
  datei = open('hangman_woerter.txt', 'r')
  for word in datei.readlines():
    list.append(word.upper())        
  num = randint(0, len(list)-1)
  word = list[num]
  word = [*word]
  word.pop()
  return word

def create_board(word):
    board = []
    for x in word:
      board.append("_")
    return board

def inputs(letters):
  letter = ""
  check = True
  while check == True:
    letter = input('Buchstabe eingeben: ')
    letter = letter.upper()
    check = check_double_letters(letter, letters)
  return letter
 
def check_double_letters(letter, letters):
  double = False
  for x in letters:
    if x == letter:
      print('Buchstabe schon ausgewählt')
      double = True
      break
    else:
      double = False     
  return double
 
def check_letter(word, board, letter):
  hit = False
  for x in range(len(word)):
    if word[x] == letter:
      board[x] = letter
      hit = True
  return hit

def check_win(word, board):
  word = ' '.join(word)
  board = ' '.join(board)
  if word == board:
    return True
  
def init():
  word = choose_word()
  board = create_board(word)
  win = False
  letters = []
  missed = 0
  versuche = 0
  while missed < 10:
    print(board)
    letter = inputs(letters)   
    letterHit = check_letter(word, board, letter)
    letters.append(letter)
    letters.sort() 
    if letterHit == False:
      missed += 1
      print('Fehlversuche', missed)     
    win = check_win(word, board)
    versuche += 1
    if win == True:
      print(letters)
      print('Gewonnen!\n' 'Versuche: ', versuche )
      break
    print('Eingaben: ', letters)
    if missed == 10:
      print('Verloren!\n' 'Versuche: ', versuche)

init()
