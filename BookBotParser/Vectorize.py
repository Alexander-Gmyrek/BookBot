from transformers import BertTokenizer, BertModel
import Sentence
class Vectorize:
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    def __init__(self):
        pass

    def vectorize(self, sentences):
        for sentence in sentences:
            # Tokenize a sentence
            inputs = self.tokenizer(sentence.getString(), return_tensors="pt")

            # Get the output from BERT
            outputs = self.model(**inputs)

            # Sentence vector (pooled output)
            sentence_vector = outputs['pooler_output']
            print(sentence_vector)
            sentence.setVector(sentence_vector)
        return sentences
        