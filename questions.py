import nltk
import sys
import os
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():
    nltk.download('punkt')
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    file_dict = dict()
    files_list = [txt_file for txt_file in os.listdir(directory)
                      if os.path.isfile(os.path.join(directory, txt_file))]
    for txt in files_list:
        with open(os.path.join(directory, txt), encoding='utf-8', mode='r') as file:
            contents = file.read()
        file_dict[txt] = contents
    return file_dict


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    nltk.download("punkt")
    word: str
    word_list = list()
    for word in nltk.word_tokenize(document):
        if any(character.isalpha() for character in word):
            word_list.append(word.lower())
    return word_list


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    total_documents = len(documents)
    idf_dict = dict()
    words = set()
    for val in documents.values():
        words.update(val)
    for word in words:
        num_docs = sum(word in documents[document] for document in documents)
        if num_docs != 0:
            idf_dict[word] = math.log((total_documents/num_docs))
    return idf_dict


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    filename_list = list()
    tf_idf = dict()
    for fl in files:
        tf_idf[fl] = 0
        for word in query:
            t_f = 0
            if word in files[fl]:
                t_f += 1
            if word not in idfs:
                return
            tf_idf[fl] += t_f * idfs[word]
    unsorted = list(tf_idf.values())
    unsorted.sort(reverse=True)
    for i in unsorted:
        for file, val in tf_idf.items():
            if val == i:
                filename_list.append(file)
    return filename_list[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    tf_dict = dict()
    for s in sentences:
        tf_dict[s] = 0
        for w in query:
            if w in sentences[s]:
                tf_dict[s] += idfs[w]
    tf_l = list(tf_dict.items())
    tf_l.sort(key=lambda i: i[1], reverse=True)
    k = [i[0] for i in tf_l]
    ret_list = k[:n]
    return ret_list


if __name__ == "__main__":
    # main()
    files = load_files("corpus")
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)
    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)
    print(filenames)
