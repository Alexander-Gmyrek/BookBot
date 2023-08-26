import Parser
import Sentence
import Vectorize

def testParser():
    parser = Parser.Parser()
    sentences = parser.parse("C:\\Users\\agdab\\Desktop\\Projects\\BookBot\\BookBotParser\\sample.pdf")
    for sentence in sentences:
        print(sentence.__str__() + "\n")

def testVectorize():
    vectorizer = Vectorize.Vectorize()
    sentences = [Sentence.Sentence("This is a test sentence.", [1, 1, 1]), Sentence.Sentence("This is another test sentence.", [1, 1, 2])]
    sentences = vectorizer.vectorize(sentences)
    for sentence in sentences:
        print(sentence.__str__() + "\n")

def testFindAnswers():
    #To-do Write test
    pass

def testAiResponse():
    #To-do Write test
    pass

def testBookStorageIn():
    #To-do Write test
    pass

def testBookStorageOut():
    #To-do Write test
    pass

def testmain():
    #To-do Write test
    pass

testVectorize()