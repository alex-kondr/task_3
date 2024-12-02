import random

from flask import Flask, render_template


app = Flask(__name__, template_folder="templates_2", static_folder="static_2")



# @app.route("/")
@app.get("/")
def index():
    data = [random.randint(1, 50) for _ in range(20)]
    return render_template("index.html", data=data)


@app.get("/results/")
def results():
    grades = [
        {"name": "Барабашка", "value": 89},
        {"name": "Анатолій", "value": 95},
        {"name": "Абабагаламага", "value": 50},
        {"name": "Alex", "value": 100}
    ]

    context = {
        "grades": grades,
        "max_score": 100
    }

    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)