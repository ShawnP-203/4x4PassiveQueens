# Shawn Plackiyil
# 9-24-2022 (last updated 9-25-2022)
# Passive Queens
# Places 4 chess queens on a board in positions where their attack lines don't overlap
from random import choice
boardNumbers = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15))
boardClockwise = (0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4)
while True:
  queenPossibilities = []
  for row in boardNumbers:
    for square in row:
      if row in boardNumbers[::3] and square not in row[::3] \
      or row not in boardNumbers[::3] and square in row[::3]:
        # Queens cannot be in corners or the four center squares
        queenPossibilities.append(square)
  queenPossibilities = choice(queenPossibilities)
  queens = [queenPossibilities] # Needs to be initialized as a list
  
  while len(queens) < 4:
    for number in boardClockwise:
      if queens[len(queens) - 1] == number:
        if len(queens) == 1: calculationDirection = choice([-3, 3])
        # Chooses the direction when starting the algorithm which travels the board's edges
        boardClockwiseIndex = boardClockwise.index(number) + calculationDirection
        if boardClockwiseIndex > 11: boardClockwiseIndex -= 12
        # Above handler is only necessary for oversized indices because
        # Python already has a feature which counts negative indices from the end of a list
        queenPossibilities = boardClockwise[boardClockwiseIndex]
    queens.append(queenPossibilities)
  
  boardFormat = [""] * 16
  for queenCount, queen in enumerate(queens, start = 1):
    for square, item in enumerate(boardFormat):
      # The only reason item exists is so square gets the iteration number and not a tuple
      if queen == square:
        boardFormat[square] = " ♕ {} ".format(queenCount)
      elif "♕" not in boardFormat[square]: boardFormat[square] = "empty"
      # This conditional ensures that "empty" doesn't overwrite a queen
  board = """
  Placed 4 passive chess queens on a board:
  
   {} | {} | {} | {}
  ------------------------------
   {} | {} | {} | {}
  ------------------------------
   {} | {} | {} | {}
  ------------------------------
   {} | {} | {} | {}
  """.format(*boardFormat) # Unpacks list to the 16 placeholders
  # Output starts here
  print(board)
  retry = "initializer" # retry can get anything as long as it's truthy
  while retry and retry != "R":
    retry = input("Press [ENTER] to exit or [R] to run again. ").upper().strip()
  if not retry: break
