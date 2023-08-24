# Create parser class for bookbot
from PyPDF2 import PdfReader
import Sentence
class Parser:
    def __init__(self):
        self.sentences = []

    def parse(self, text):
        sentences = []
        #turn pdf into text
        reader = PdfReader(text)
        number_of_pages = len(reader.pages)
        for page_num in range(number_of_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            
            #split int paragraphs
            paragraphs = page_text.split("\n")

            #remove empty paragraphs
            for paragraph in paragraphs:
                if paragraph == "":
                    paragraphs.remove(paragraph)
            
            #split into sentences
            for paragraph in paragraphs:
                paragraphNum = paragraphs.index(paragraph)

                print(paragraph + str(paragraphNum) + " \n")

                #split into sentences
                sentencelist = paragraph.split(".")

                #remove empty sentences
                for sentence in sentencelist:
                    if sentence.replace(' ', '') == "":
                        sentencelist.remove(sentence)

                for sentence in sentencelist:
                    location = [page_num + 1, paragraphNum + 1, sentencelist.index(sentence) + 1]
                    sentences.append(Sentence.Sentence(sentence, location))
                    
        #return sentences array
        return sentences