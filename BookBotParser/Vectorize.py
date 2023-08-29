from transformers import BertTokenizer, BertModel
import Sentence
import numpy as np

class Vectorize:
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    def __init__(self):
        pass

    def vectorize(self, sentences):
        for sentence in sentences:
            # Tokenize a sentence
            inputs = self.tokenizer(sentence.getSentence(), return_tensors="pt")

            # Get the output from BERT
            outputs = self.model(**inputs)

            # Sentence vector (pooled output)
            sentence_vector = outputs['pooler_output'].detach().numpy()[0]
            sentence.setVector(sentence_vector)
        return sentences
        