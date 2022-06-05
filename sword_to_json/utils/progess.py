class Progress(object):

    def __init__(self, size, length=75):
        super().__init__()
        self._size = size
        self._length = length
        self.update(0)

    def update(self, iteration):
        percent = (iteration / float(self._size)) * 100
        filled = int((percent * self._length) / 100)
        bar = ('█' * filled) + ('-' * (self._length - filled))
        print(f"|{bar}| {percent:>3,.0f}% Complete", end='\r')
        if iteration == self._size:
            print()
