from flask import Flask, render_template

app = Flask(__name__)


# Rota principal
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/explorer')
def explorer():
    return render_template('explorer.html')


if __name__ == '__main__':
    app.run(debug=True)
