from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    with open('index.html', 'r') as file:
        html_content = file.read()
    return html_content 


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
