from flask import Flask,render_template

app = Flask(__name__)


students_data = {
    "Abdul-Aziz": 77, "Abdullo": 47, "Abubakr": 59,
    "Ahmadjon": 69, "Amir": 44, "Behruz": 69,
    "Habibulloh": 51, "Ilyos": 64, "Maftunbek": 39,
    "Maryam": 28, "Mubarro": 22, "Najmiya": 60,
    "Otabek": 48, "Shahrom": 83, "Habibullo": 63,
    "Rukhshona": 31, "Osiya": 69, "Bakhtiyor": 32,
    "Muhammadjon": 0, "Timur": 89, "Gulsum": 36,
    "Rayhona": 39, "Abduvozit": 12, "Ismoiljon": 0,
    "Nizar": 72,
}


@app.route("/")
def main():
    return render_template("/main_page.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/students")
def student():
    return render_template("/students.html")


@app.route("/grade/<name>/<int:score>")
def grade(name,score):
    if score >= 80:
        result = "Excellent"
    elif score >= 50:
        result = "Good"
    else:
        result = "Needs practice"
    return f"{name}: {score}% - {result}"



if __name__ == "__main__":
    app.run(debug=True)