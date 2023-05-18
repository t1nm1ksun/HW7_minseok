import numpy as np

def compute_cosine_similarity(DOCS, Query):
    
    dot_product = np.dot(DOCS, Query)

    
    docs_norms = np.linalg.norm(DOCS, axis=1)
    query_norm = np.linalg.norm(Query)

   
    cosine_similarity = dot_product / (docs_norms * query_norm)

    return cosine_similarity

def main():
    DOCS = np.array([[1, 1, 0, 1, 0, 1],
                     [1, 1, 1, 0, 1, 0],
                     [1, 1, 0, 1, 0, 0]])

    Query = np.array([1, 1, 0, 0, 1, 0])

    #
    similarity_scores = compute_cosine_similarity(DOCS, Query)

   
    for i, similarity in enumerate(similarity_scores):
        print(f"doc{i+1} = {similarity:.2f}")

if __name__ == "__main__":
    main()

