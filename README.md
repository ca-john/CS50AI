# CS50AI Project 6b - Questions


**Basic python AI to answer questions**

**Requirements: Inside of the questions directory, run:**
    
    pip3 install -r requirements.txt to install this project’s dependency: nltk for natural language processing.


Each .txt document in corpus is a text file containing the contents of a Wikipedia page. Our AI can find sentences from these files that are relevant to a user’s query. 


Main idea:

> We first load the files from the corpus directory into memory (via the load_files function). Each of the files is then tokenized (via tokenize) into a list of words, which then allows us to compute inverse document frequency values for each of the words (via compute_idfs). The user is then prompted to enter a query. The top_files function identifies the files that are the best match for the query. From those files, sentences are extracted, and the top_sentences function identifies the sentences that are the best match for the query.

**Running**

    $ python questions.py corpus
    Query: What are the types of supervised learning?
    Types of supervised learning algorithms include Active learning , classification and regression.

    $ python questions.py corpus
    Query: When was Python 3.0 released?
    Python 3.0 was released on 3 December 2008.

    $ python questions.py corpus
    Query: How do neurons connect in a neural network?
    Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
