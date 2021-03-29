import random

def print2DArray(arr):
  for x in arr:
    for y in x:
      print(str(y), end = " ")
    print()

def findSum(arr):
  sum = 0

  for x in arr:
    for y in x:
      sum += y

  return sum

# initialize board
board = [0] * 10

for x in range(10):
  board[x] = [0] * 10

#fill board w random values
for x in range(10):
  for y in range(10):
    board[x][y] = random.randrange(0, 10, 1)

print2DArray(board)
print(findSum(board))