# Server For the Application

from flask import Flask
from flask import render_template, request, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/instructions")
def instructions():
    return render_template("instruction.html")


@app.route("/exam")
def exam():
    return render_template("exam.html", question_bank=question_bank)


question_bank = [
    {
        "question": "How many time zones are there in Russia?",
        "options": [
            10,
            11,
            12,
            15
        ],
        "answer": 11

    },
    {
        "question": "What’s the national flower of Japan?",
        "options": [
            "Sun Flower",
            "Daisy",
            "Rose",
            "Cherry blossom"
        ],
        "answer": "Cherry blossom"
    },
    {
        "question": "How many stripes are there on the US flag?",
        "options": [
            10,
            11,
            12,
            13
        ],
        "answer": 13
    },
    {
        "question": "What’s the national animal of Australia?",
        "options": [
            "Elephant",
            "Tiger",
            "Black Mamba",
            "Red Kangaroo"
        ],
        "answer": "Red Kangaroo"
    },
    {
        "question": "How many days does it take for the Earth to orbit the Sun?",
        "options": [
            121,
            365,
            364,
            360
        ],
        "answer": 365
    },
    {
        "question": "Which of the following empires had no written language?",
        "options": [
            "Incan",
            "Roman",
            "Egyptian",
            "Aztec"
        ],
        "answer":"Incan"
    },
    {
        "question": "Until 1923, what was the Turkish city of Istanbul called?",
        "options": [
            "Isanbul",
            "India",
            "Constantinople",
            "Bangladesh"
        ],
        "answer": "Constantinople"
    },
    {
        "question": "What country has the most islands in the world?",
        "options": [
            "Sweden",
            "Norway",
            "Japan",
            "Korea"
        ],
        "answer": "Sweden"
    },
    {
        "question": "What’s the smallest country in the world?",
        "options": [
            "Mexico",
            "India",
            "Pakistan",
            "The Vatican"
        ],
        "answer": "The Vatican"
    },
    {
        "question": "Name the longest river in the world?",
        "options": [
            "The Ganga",
            "The Brahmaputa",
            "The Nile",
            "The Yamuna"
        ],
        "answer": "The Nile"
    }

]


@app.route("/check",  methods=['GET', 'POST'])
def calculateResult():
    if request.method == "GET":
        return render_template("results.html")
    if request.method == "POST":
        content = request.data
        content = content.decode('utf8').replace("'", '"')
        content = json.loads(content)
        count = 0

        for i in range(len(question_bank)):
            if content["results"][i] >= 0:
                if content["results"][i] == question_bank[i]["options"].index(question_bank[i]["answer"]):
                    count += 1
        print(count)
        return jsonify(
            count=count
        )


if __name__ == "__main__":
    app.run(debug=True)
