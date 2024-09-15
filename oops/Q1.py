class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # iterator function.
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(30, 15)

if __name__ == "__main__":

    for attr in rect:
        print(attr)