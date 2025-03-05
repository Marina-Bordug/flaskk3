from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
def index(title):
    return render_template('base.html', title=title)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)
