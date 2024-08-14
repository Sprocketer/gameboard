from numpy.typing import NDArray
from typing import Any

class grid():
    """# Grid object class.
    
    `grid_size: int`
        The size of the grid, must be an integer.
    
    `fill: bool`
        If True, the grid will be filled with numbers from 1 to grid_size^2, horizontally from left to right, top to bottom."""
    
    def __init__(self, grid_size: int, fill: bool = False):
        
        if not isinstance(grid_size, int):
            raise ValueError("grid_size must be an integer")
        if not isinstance(fill, bool):
            raise ValueError("fill must be a boolean")

        self.grid_size = grid_size
        self.edge_index = grid_size - 1
        
        self._data = array()
        if fill == True:
            count = 0
            for _ in range(self.grid_size): # for each row
                row = array()
                for _ in range(self.grid_size): # for each item
                    count += 1
                    row.append([count])
                self._data.append(row)
        else:
            for _ in range(self.grid_size): # for each row
                row = array()
                for _ in range(self.grid_size): # for each item
                    row.append([])
                self._data.append(row)
    
    def __repr__(self):
        grid_str = ""
        for row in self._data:
            grid_str += str(row) + "," + "\n"*2
        grid_str = "[" + grid_str[:-3] + "]"
        return grid_str

    def __getitem__(self, pos: tuple[int, int] | NDArray):
        y = self.edge_index - pos[1]
        x = pos[0]
        return self._data[y][x]

    def __iter__(self):
        for elem in self._data:
            yield elem
    
    def __setitem__(self, pos: tuple[int, int] | NDArray, value: Any):
        y = self.edge_index - pos[1]
        x = pos[0]
        self._data[y][x] = value

class array():
    """For internal use, not intended to be accessed externally."""
    
    def __init__(self):
        self._data: list[Any] = []

    def __iter__(self):
        for elem in self._data:
            yield elem
    
    def __str__(self):
        return str(self._data)

    def append(self, item: Any):
        self._data.append(item)
    
    def __getitem__(self, key: int):
        return self._data[key]

    def __setitem__(self, key: int, value: Any):
        self._data[key] = value