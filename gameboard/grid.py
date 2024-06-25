class grid():
    
    def __init__(self, grid_size: int, fill: bool = False):

        self.grid_size = grid_size
        self.edge_index = grid_size - 1
        
        self._data = array()
        if fill:
            count = 0
        for _ in range(self.grid_size): # for each row
            row = array()
            for _ in range(self.grid_size): # for each item
                if fill:
                    count += 1
                    row.append([count])
                else:
                    row.append([])
            self._data.append(row)
    
    def __repr__(self): # print() calls this method
        grid_str = ""
        for row in self._data:
            grid_str += str(row) + "," + "\n"*2
        grid_str = "[" + grid_str[:-3] + "]"
        return grid_str

    def __getitem__(self, key):
        return self._data[self.edge_index - key]

    def __getitem__(self, pos: list[int, int]):
        y = self.edge_index - pos[1]
        x = pos[0]
        return self._data[y][x]

    def __iter__(self):
        for elem in self._data:
            yield elem

class array():
    
    def __init__(self):
        self._data = []

    def __iter__(self):
        for elem in self._data:
            yield elem
    
    def __str__(self):
        return str(self._data)

    def append(self, item):
        self._data.append(item)
    
    def __getitem__(self, key):
        return self._data[key]