from flask import Flask

app: Flask = Flask(__name__)


@app.route('/', methods=['POST'])
def make_short_url():
    pass


@app.route('/<key>', methods=['GET'])
def get_url(key):
    pass


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
