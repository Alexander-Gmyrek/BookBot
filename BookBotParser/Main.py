import Parser
import Sentence
import Vectorize
import BookStorage
import FindAnswer
import os

def testParser():
    parser = Parser.Parser()
    sentences = parser.parse("C:\\Users\\agdab\\Desktop\\Projects\\BookBot\\BookBotParser\\sample.pdf")
    for sentence in sentences:
        print(sentence.__str__() + "\n")

def testVectorize():
    vectorizer = Vectorize.Vectorize()
    sentences = [Sentence.Sentence("This is a test sentence.", [1, 1, 1], []), Sentence.Sentence("This is another test sentence.", [1, 1, 2], [])]
    sentences = vectorizer.vectorize(sentences)
    for sentence in sentences:
        print(sentence.__str__() + "\n")

def testFindAnswers():
    # Test data
    filename = "SampleSentences.json"
    question = "What is the capital of France?"

    #if the file does not exist, create it
    if not os.path.exists(filename):
        sentences = [
            Sentence.Sentence("Paris is the capital of France.", [1, 0, 0], []),
            Sentence.Sentence("Berlin is the capital of Germany.", [0, 1, 0], []),
            Sentence.Sentence("George Bush did 9/11", [1, 1, 1], []),
            Sentence.Sentence("I sprained my ankle", [1, 1, 2], []),

            Sentence.Sentence("Tokyo is the capital of Japan.", [1, 0, 0], []),
            Sentence.Sentence("Canberra is the capital of Australia.", [0, 1, 0], []),
            Sentence.Sentence("Neil Armstrong walked on the moon.", [1, 1, 1], []),
            Sentence.Sentence("I forgot my umbrella at home.", [1, 1, 2], []),

            Sentence.Sentence("Rome is the capital of Italy.", [1, 0, 1], []),
            Sentence.Sentence("Ottawa is the capital of Canada.", [0, 1, 1], []),
            Sentence.Sentence("Albert Einstein developed the theory of relativity.", [1, 1, 0], []),
            Sentence.Sentence("My cat knocked over the vase.", [1, 1, 2], []),

            Sentence.Sentence("Madrid is the capital of Spain.", [1, 0, 0], []),
            Sentence.Sentence("Beijing is the capital of China.", [0, 1, 0], []),
            Sentence.Sentence("The Titanic sank in 1912.", [1, 1, 1], []),
            Sentence.Sentence("I lost my keys in the park.", [1, 1, 2], []),

            Sentence.Sentence("Cairo is the capital of Egypt.", [1, 0, 1], []),
            Sentence.Sentence("Brasília is the capital of Brazil.", [0, 1, 1], []),
            Sentence.Sentence("Shakespeare wrote Romeo and Juliet.", [1, 1, 0], []),
            Sentence.Sentence("I baked cookies for the party.", [1, 1, 2], []),

            Sentence.Sentence("Athens is the capital of Greece.", [1, 0, 0], []),
            Sentence.Sentence("New Delhi is the capital of India.", [0, 1, 0], []),
            Sentence.Sentence("The pyramids are located in Giza.", [1, 1, 1], []),
            Sentence.Sentence("I missed the morning train.", [1, 1, 2], []),

            Sentence.Sentence("Oslo is the capital of Norway.", [1, 0, 1], []),
            Sentence.Sentence("Nairobi is the capital of Kenya.", [0, 1, 1], []),
            Sentence.Sentence("Mona Lisa was painted by Leonardo da Vinci.", [1, 1, 0], []),
            Sentence.Sentence("I spilled coffee on my shirt.", [1, 1, 2], []),

            Sentence.Sentence("Lisbon is the capital of Portugal.", [1, 0, 0], []),
            Sentence.Sentence("Buenos Aires is the capital of Argentina.", [0, 1, 0], []),
            Sentence.Sentence("Mount Everest is the highest mountain in the world.", [1, 1, 1], []),
            Sentence.Sentence("I watched the sunset from the beach.", [1, 1, 2], []),
            Sentence.Sentence("asafdfagfhtehbf.", [1, 1, 2], []),
        ]

        sentences = Vectorize.Vectorize().vectorize(sentences)

        # Store the book
        BookStorage.BookStorage().storeBook(sentences, filename)
    else:
        sentences = BookStorage.BookStorage().getBook(filename)

    finder = FindAnswer.FindAnswer()
    result = finder.findAnswer(question, sentences)

    for sentence in result:
        print(sentence.getSentence())

    if (len(result) == 1):
        print("Test 1 passed")
    if (result[0].getSentence() == "Paris is the capital of France."):
        print("Test 2 passed")

    pass

def testAiResponse():
    #To-do Write test
    pass

def testBookStorageIn():
    #To-do Write test
    # Create some example data
    sentence_data = [
        Sentence.Sentence("Hello world!", [0,0,1], [0.1, 0.2, 0.3]),
        Sentence.Sentence("Testing is important.", [0,0,2], [0.4, 0.5, 0.6]),
    ]
    # Create a BookStorage instance
    book_storage = BookStorage.BookStorage()
    
    # Store the book
    book_storage.storeBook(sentence_data)
    
    # Get the stored book
    retrieved_book = book_storage.getBook("sample.json")
    print(retrieved_book)
    pass

def testBookStorageOut():
    #To-do Write test
    pass

def testmain():
    #To-do Write test
    pass

testFindAnswers()