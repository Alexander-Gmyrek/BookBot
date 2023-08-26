class Sentence:
    location = []
    sentence = ""
    vector = []
    def __init__(self, sentence, location):
        self.sentence = sentence
        self.location = location
        self.vector = []

    def setVector(self, vector):
        self.vector = vector
    
    def __str__(self):  
        return self.sentence + " " + str(self.location) + " " + str(self.vector)
    
    def getString(self):
        return self.sentence