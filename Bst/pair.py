class Pair:
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
        
    def __eq__(self, other):
        return self.letter == other.letter
        
    def __hash__(self):
        return hash(self.letter)
        
    def __ne__(self, other):
        return self.letter != other.letter
        
    def __lt__(self, other):
        return self.letter < other.letter
        
    def __le__(self, other):
        return self.letter <= other.letter
        
    def __gt__(self, other):
        return self.letter > other.letter
        
    def __ge__(self, other):
        return self.letter >= other.letter
        
    def __repr__(self):
        return f'({self.letter}, {self.count})'
        
    def __str__(self):
        return f'({self.letter}, {self.count})'
        
