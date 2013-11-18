import sys

class Board(object):
    """docstring for Board"""
    def __init__(self,tiles):
        self.tiles = tiles ## a list of 9 ints
        self.rows = []
        self.cols = []

    def make_rows(self):
        j = 0
        for i in range(3,10,3):
            row = []
            while j < i:
                row.append(self.tiles[j])
                j+=1

            self.rows.append(row)

    def make_cols(self):
        



    def check():
        pass
        ##FIXME





def main():
    stdin = sys.stdin.readline().rstrip()
    input_tiles = [char for char in stdin]
    b = Board(input_tiles)
    b.make_rows()
    print b.rows
if __name__ == '__main__':
    main()