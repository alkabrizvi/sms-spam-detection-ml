import string
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class TextPreprocessor(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        cleaned_messages = []

        for message in X:
            message = str(message).lower()

            message = message.translate(
                str.maketrans('', '', string.punctuation)
            )

            words = message.split()
            words = [word for word in words if word not in self.stop_words]

            stemmed_words = []

            for word in words:
                stemmed_words.append(self.ps.stem(word))

            final_message = ' '.join(stemmed_words)
            cleaned_messages.append(final_message)

        return cleaned_messages