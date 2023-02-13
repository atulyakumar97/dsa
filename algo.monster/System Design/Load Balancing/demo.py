# demo.py
from flask import Flask
import sys

app = Flask('demo')
port = 8000


@app.route('/')
def hello_world():
    return f'Hello, {port}!\n'


if __name__ == '__main__':
    port = sys.argv[1]
    app.run(host='127.0.0.1', port=port)
