import flask
import pickle
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import sys
from flask import Flask, request, jsonify, render_template

model=pickle.load(open('clf.pickle','rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return flask.render_template("index.html")

@app.route('/clas',methods=['POST'])
def clas():
		text=[x for x in flask.request.form.values()]
		#text="മോശം "
		tok=word_tokenize(text[0])

		result=model.classify(dict([token,True] for token in tok))
		#return redirect('/')
		return render_template('index.html',pred=result)
if __name__ == '__main__':
	app.run(debug=True)
