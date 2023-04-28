from flask import Flask, request, jsonify
import sys

sys.path.insert('1', '')
app = Flask(__name__)


@app.route('/search/<query>', methods=['POST'])
def query():
    data = request.form['query']
    files = main(data)
    print(files)
    return files


@app.route("/")
def hello():
    return "hello world"
