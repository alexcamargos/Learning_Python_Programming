import os

from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect(
        os.environ.get('REDIRECT_TOP', 'https://alexcamargos.github.io'),
        code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
