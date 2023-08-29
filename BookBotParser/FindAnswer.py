from sklearn.metrics.pairwise import cosine_similarity
import Sentence
import Vectorize
import numpy as np

class FindAnswer:

    def __init__(self):
        pass

    def findAnswer(self, question, sentences):
        # Vectorize the question
        vectorizer = Vectorize.Vectorize()
        question_vector = vectorizer.vectorize([Sentence.Sentence(question, [0, 0, 0], [])])[0].getVector()

        # Get sentence Vectors
        sentence_vectors = [sentence.getVector() for sentence in sentences]

        # Get similarities and sort them
        similarities = [cosine_similarity([vector], [question_vector]) for vector in sentence_vectors]
        sorted_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)

        print(similarities)


        # Get the top N most relevant sentences
        N = 5
        top_sentences = [sentences[i] for i in sorted_indices[:N]]

        # Get only return sentences that are above a certain similarity threshold
        threshold = 0.3
        top_sentences = [sentence for sentence in top_sentences if similarities[sentences.index(sentence)] > threshold]

        # Return the top sentences
        return top_sentences


    

