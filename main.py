from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
def index(title):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def train(prof):
    return render_template('prof2.html', prof=prof)


@app.route("/list_prof/<typ>")
def profs(typ):
    professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог",
                   "врач", "инженер по терраформированию", "климатолог",
                   "специалист по радиационноц защите", "астроеголог", "гляциолог",
                   "инженер жизнеобеспечения", "метеоролог", "оператор марсохода",
                   "штурман", "пилот дронов"]
    return render_template("profs.html", professions=professions, typ=typ)


@app.route("/answer")
@app.route("/auto_answer")
def ans():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True"
    }
    return render_template("auto_answer.html", **params )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)
