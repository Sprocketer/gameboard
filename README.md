# Gameboard

This library creates a 3-dimensional grid object with 2 fixed-length dimensions (x, y) and a third unfixed-length dimension (z).

Example use cases include multi-agent simulations where multiple agents can be placed on a 2D grid and be in the same cell, or board games where the board is a 2D grid and pieces can be stacked on top of or adjacent to each other.

The primary purpose of this project is to be able to access coordinates just as on a coordinate plane.

e.g. with the variable `board` of type `grid`, `board[0, 0]` will return the bottom-left corner of the grid.

## Install

Run:

```bash
pip install gameboard
```

## Example Usage

```python
from gameboard import grid

board = grid(grid_size = 3, fill = True)
print(board)

# [[[1], [2], [3]],
#
# [[4], [5], [6]],
#
# [[7], [8], [9]]]

print(board[2, 1])

# [6]

board[2, 1].append('a')
print(board)

# [[[1], [2], [3]],
#
# [[4], [5], [6, 'a']],
#
# [[7], [8], [9]]]
```

## Warning

This project does not currently work with negative indices for the y-coordinate when accessing the grid.

This project is in an early development stage and may not be suitable for all use cases. For ease of use, the `__iter__` dunder method has been implemented for both the y-axis and x-axis arrays, and the `append` method has been implemented for adding elements to the z-dimension arrays.
