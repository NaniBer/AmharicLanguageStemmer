import json
import package.stemmer.main
from flask import Flask, request, jsonify

from package.stemmer.main import main

app = Flask(__name__)


@app.route("/members")
def members():
    return {"members": [1, 2, 3]}


@app.route('/search', methods=['POST'])
def query():
    books = []
    query = request.json['query']
    print(query)

    result = main(query)
    books = list(result.keys())
    print(books)
    return jsonify(books)


@app.route('/read',  methods=['POST'])
def read():
    file = request.json['file_name']
    content = ''
    path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/{file}.txt"

    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, encoding='utf-16') as f:
            content = f.read()

    print(content)
    return jsonify(content)


if __name__ == "__main__":
    app.run(debug=True)
