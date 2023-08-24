from transformers import BertTokenizer, BertModel
class Vectorize:
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    # Tokenize a sentence
    inputs = tokenizer("This is a sample sentence.", return_tensors="pt")

    # Get the output from BERT
    outputs = model(**inputs)

    # Sentence vector (pooled output)
    sentence_vector = outputs['pooler_output']