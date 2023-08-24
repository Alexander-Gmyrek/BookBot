import Parser
import Sentence

parser = Parser.Parser()
sentences = parser.parse("C:\\Users\\agdab\\Desktop\\Projects\\BookBot\\BookBotParser\\sample.pdf")
for sentence in sentences:
    print(sentence.__str__() + "\n")