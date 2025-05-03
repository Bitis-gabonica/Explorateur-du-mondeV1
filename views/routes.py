from flask import render_template, request, redirect, url_for, session
from models.country import Country
from models.database import db
from views.api_utils import fetch_country_data_by_code
import random


def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/country/<code>")
    def show_country(code):
        data = fetch_country_data_by_code(code)
        if not data:
            return "Erreur lors de la récupération du pays.", 404
        return render_template("country_details.html", country=data)

    @app.route("/add/<code>")
    def add_country(code):
        if Country.query.filter_by(code=code.upper()).first():
            return redirect(url_for("wishlist"))

        data = fetch_country_data_by_code(code)
        if not data:
            return "Impossible d'ajouter le pays.", 400

        new_country = Country(**data)
        db.session.add(new_country)
        db.session.commit()
        return redirect(url_for("wishlist"))

    @app.route("/wishlist")
    def wishlist():
        countries = Country.query.all()
        return render_template("wishlist.html", countries=countries)

    @app.route("/remove/<int:id>")
    def remove_country(id):
        country = Country.query.get_or_404(id)
        db.session.delete(country)
        db.session.commit()
        return redirect(url_for("wishlist"))

    def generate_quiz():
        countries = Country.query.all()
        if len(countries) < 4:
            return None

        correct = random.choice(countries)
        options = [correct.capital]

        while len(options) < 4:
            c = random.choice(countries)
            if c.capital and c.capital not in options:
                options.append(c.capital)

        random.shuffle(options)
        return {
            "question": f"Quelle est la capitale de {correct.name} ?",
            "answer": correct.capital,
            "options": options
        }

    @app.route("/quiz", methods=["GET", "POST"])
    def quiz():
        if request.method == "POST":
            user_answer = request.form.get("answer")
            correct = session.get("correct_answer")
            result = (user_answer == correct)
            return render_template("quiz_result.html", result=result, correct=correct)

        q = generate_quiz()
        if not q:
            return "Ajoute au moins 4 pays pour jouer."
        session["correct_answer"] = q["answer"]
        return render_template("quiz.html", question=q)

    @app.route("/quiz_result")
    def quiz_result():
        return redirect(url_for("quiz"))