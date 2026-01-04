import pickle
import re
import string
import nltk
import os
from flask import Flask, render_template, request
nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

MODEL_PATH = os.getenv('MODEL_PATH', 'nlp_model.pkl')
TRANSFORM_PATH = os.getenv('TRANSFORM_PATH', 'transform.pkl')
ensemble = pickle.load(open(MODEL_PATH, 'rb'))
vectorization = pickle.load(open(TRANSFORM_PATH, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news = request.form['news']
        news = news.lower()
        news = re.sub('\[.*?\]', '', news)
        news = re.sub("\\W", " ", news)
        news = re.sub('https?://\S+|www\.\S+', '', news)
        news = re.sub('<.*?>+', '', news)
        news = re.sub('[%s]' % re.escape(string.punctuation), '', news)
        news = re.sub('\n', '', news)
        news = re.sub('\w*\d\w*', '', news)
        news = word_tokenize(news)
        lmtzr = WordNetLemmatizer()
        news = ' '.join([lmtzr.lemmatize(w, wn.NOUN) for w in news])
        data = [news]
        vect = vectorization.transform(data).toarray()
        my_prediction = ensemble.predict(vect)
    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
