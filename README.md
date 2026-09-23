# TicTacToe (Console)

A two-player Tic Tac Toe game that runs in the terminal.

## How to play

1. The board positions (1-9) are shown at the start of the game.
2. On each turn, enter `x` or `o` for the mark, then enter a position number (1-9) to place it.
3. The board prints after every move.
4. The game ends when three matching marks line up (row, column, or diagonal), or when the board fills up with no winner (tie).

## Known limitations

- Turn order is not enforced; `x` or `o` can be entered on any turn.
- A position can be overwritten even if it is already filled.
- Non-numeric input for the position will crash the program.
