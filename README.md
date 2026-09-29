# Tic Tac Toe (Python)

A simple two-player Tic Tac Toe game that runs in the terminal. Built to understand basic game logic: input, turns, move checking, and finding the winner.

## Features

- 3x3 board with positions numbered 1 to 9
- Two players take turns as X and O
- Rejects moves on taken positions
- Rejects moves played out of turn
- Handles wrong input (like letters instead of numbers)
- Checks all rows, columns and diagonals for a win
- Declares a tie when the board is full

## Requirements

- Python 3

## How to Play

1. The board positions are shown at the start:

```
  1  |  2  |  3
-----+-----+-----
  4  |  5  |  6
-----+-----+-----
  7  |  8  |  9
```

2. Type `x` or `o` (X goes first).
3. Type a position number from 1 to 9.
4. Take turns until someone gets three in a row, or the board is full.

## Sample Output

```
X or O: x
Choose a Position number: 1
  X  |     |
-----+-----+-----
     |     |
-----+-----+-----
     |     |

X or O: o
Choose a Position number: 1
That position is already taken
```

## How It Works

- The board is a Python list of 9 items.
- A `turn` variable tracks whose turn it is.
- The `result()` function prints the board.
- A `while` loop runs the game until there is a win or a tie.
