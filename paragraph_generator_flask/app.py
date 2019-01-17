
from flask import Flask

app = Flask(__name__)


@app.route('/_get_table')
def add_numbers():
    pass


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run()
