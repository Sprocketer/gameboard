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
from gameboard.grid import grid

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

board[2, 2].remove(3)
print(board)

# [[[1], [2], []],
#
# [[4], [5], [6, 'a']],
#
# [[7], [8], [9]]]

print(2 in board[1, 2])

# True

print(2 in board[2, 1])

# False

position = [1, 0]
print(board[position])

# [8]

data = [2, 3, 4]
board[position].append(3)
board[position].append(data)

# [[[1], [2], []],
#
# [[4], [5], [6, 'a']],
#
# [[7], [8, 3, [2, 3, 4]], [9]]]

import numpy as np
pos = np.array([0, 0])
board[pos] = ['0']
print(board)

# [[[1], [2], []],
#
# [[4], [5], [6, 'a']],
#
# [['0'], [8, 3, [2, 3, 4]], [9]]]
```

The `fill` parameter is set to `True` for the example, where all squares are numbered.
If you set the `fill` parameter to `False` ***or*** do not specify (default is `False`), all z-axis arrays will be empty.

## Warning

This project does not currently work with negative indices for the y-coordinate when accessing the grid.

This project is in an early development stage and may not be suitable for all use cases. For ease of use, the `__iter__` dunder method has been implemented for both the y-axis and x-axis arrays, and the `append`/`remove` methods and `__iter__` dunder method work for adding, removing and iterating through elements in the z-dimension arrays as the z-dimension arrays are simply Python lists.
