from flask import Flask, render_template, request, redirect, url_for
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
import string
ps = PorterStemmer()
tfidf = pickle.load(open('tfidf_vec.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

try:
    nltk.download("punkt")
    nltk.download("stopwords")
except:
    pass

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer", methods = ["GET","POST"])
def answer():


    if request.method == "POST":
        sentence = request.form.get("sentence")

        def transform_text(sentence):
            sentence = sentence.lower()
            sentence = nltk.word_tokenize(sentence)

            y = []
            for i in sentence:
                if i.isalnum():
                    y.append(i)

            sentence = y[:]

            y.clear()

            for i in sentence:
                if i not in stopwords.words("english") and i not in string.punctuation:
                    y.append(i)

            sentence = y[:]
            y.clear()

            for i in sentence:
                y.append(ps.stem(i))

            return " ".join(y)

        sms = transform_text(sentence)
        # vectorize
        vector = tfidf.transform([sms])
        # predict
        prediction = model.predict(vector)[0]
        # display

        return render_template("answer.html", prediction = prediction)

    else:
        return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug = True)