import pandas as pd
import sys
import re


#run below if you dont have the csv
# df = pd.read_csv("data.csv")

# print(df.head)

# tweet_and_labels = df.filter(['tweet'], axis = 1)
# print(tweet_and_labels.head)

# tweet_vector = tweet_and_labels.to_csv("tweets.csv", index= True)
def cleanDocs(documents):
    documents_clean = []
    for d in documents:
        # Remove Unicode
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        document_test = re.sub(r'@\w+', '', document_test)
        # Lowercase the document
        document_test = document_test.lower()
        # Remove punctuations
        document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
        # Lowercase the numbers
        document_test = re.sub(r'[0-9]', '', document_test)
        # Remove the doubled space
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(document_test)
    return documents_clean