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
    query = {'query': request.json['query']}
    # data = request.args.get['name']
    # files = main.main(data)
    print(query['query'])
    toJSON = json.dumps(list(query.values()))
    data = json.loads(toJSON)

    result = main(data[0])
    books = list(result.keys())
    print(books)
    return books


if __name__ == "__main__":
    app.run(debug=True)
