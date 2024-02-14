from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_pr.html', list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')