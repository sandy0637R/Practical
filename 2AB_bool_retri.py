# AIM: RETRIEVAL MODEL
documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}

def build_index(docs):
    index = {}
    
    for doc_id, text in docs.items():
        terms = set(text.split())
        
        for term in terms:
            if term not in index:
                index[term] = {doc_id}
            else:
                index[term].add(doc_id)
    
    return index

inverted_index = build_index(documents)

def boolean_and(operands, index):
    if not operands:
        return []

    result = index.get(operands[0], set())

    for term in operands[1:]:
        result = result.intersection(index.get(term, set()))

    return sorted(list(result))

def boolean_or(operands, index):
    result = set()
    
    for term in operands:
        result = result.union(index.get(term, set()))
    
    return sorted(list(result))

def boolean_not(operand, index, total_docs):
    operand_set = set(index.get(operand, set()))
    all_docs_set = set(range(1, total_docs + 1))
    return sorted(list(all_docs_set.difference(operand_set)))

query1 = ["apple", "banana"]
query2 = ["apple", "orange"]

result1 = boolean_and(query1, inverted_index)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not("orange", inverted_index, len(documents))

print("\nDocuments containing 'apple' and 'banana':", result1)
print("\nDocuments containing 'apple' or 'orange':", result2)
print("\nDocuments not containing 'orange':", result3)

# B) For vectorizer


import nltk
import numpy as np
from numpy.linalg import norm
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

nltk.download('stopwords')

train_set = ["The sky is blue.", "The sun is bright."]
test_set = ["The sun in the sky is bright."]

stop_words = stopwords.words('english')

vectorizer = CountVectorizer(stop_words=stop_words)
transformer = TfidfTransformer()

train_vectorized = vectorizer.fit_transform(train_set)
train_tfidf = transformer.fit_transform(train_vectorized).toarray()

test_vectorized = vectorizer.transform(test_set)
test_tfidf = transformer.transform(test_vectorized).toarray()

print("TF-IDF for training set:")
print(train_tfidf)

print("\nTF-IDF for test set:")
print(test_tfidf)

cosine_similarity = lambda a, b: round(np.inner(a, b) / (norm(a) * norm(b)), 3) if norm(a) * norm(b) != 0 else 0

for train_vector in train_tfidf:
    for test_vector in test_tfidf:
        similarity = cosine_similarity(train_vector, test_vector)
        print("Cosine Similarity:", similarity)

