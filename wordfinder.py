"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, file):
        self.file = file

    def random(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        file.close()
        return random.choice(lines).strip('\n')
    
    