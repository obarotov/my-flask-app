from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head><title>My App</title></head>
    <body>
    <h1>Welcome to Flask</h1>
    <p>This is HTML returned from Python</p>
    <a href="/about">Go to about</a>
    </body>
    </html>
    """


@app.route("/about")
def about():
    return "This is the about page"

@app.route("/student/<name>")
def student(name):
    return f"Hello {name}"


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