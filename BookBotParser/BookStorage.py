import json
import Sentence
import numpy 
from json import JSONEncoder

class BookStorage:
    def __init__(self):
        pass

    def storeBook(self, book, filename):
        # Store book in storage
        i = 0
        storage={}
        for sentence in book:
            vector_data = {1:sentence.getVector()}
            encoded_vector = json.dumps(vector_data , cls=NumpyArrayEncoder)
            storage[i]={"sentence":sentence.getSentence(), "vector":encoded_vector[1], "location":sentence.getLocation() }
            i += 1
        with open(filename, "w") as outfile:
            json.dump(storage, outfile)
        pass

    def getBook(self, filename):
        bookInfo = []
        #open json file
        f=open(filename)
        storage=json.load(f)

        #Creating Sentence
        #sentence = Sentence.Sentence(sentence, location, vector)

        for i in storage:
            NumpyVectorArray = numpy.asarray(storage[i]["vector"])
            bookInfo.append(Sentence.Sentence(storage[i]["sentence"],storage[i]["location"],NumpyVectorArray))
        
        #when finished close file
        f.close()

        # Get book from storage
        return bookInfo


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)