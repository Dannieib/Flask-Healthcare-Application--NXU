from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/") #Incase you intend to run it locally, Please, specify your own mongodb port
db = client["survey_db"]
collection = db["user_data"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "total_income": float(request.form["total_income"]),
            "expenses": {
                "utilities": float(request.form["utilities"]) if request.form.get("utilities") else 0,
                "entertainment": float(request.form["entertainment"]) if request.form.get("entertainment") else 0,
                "school_fees": float(request.form["school_fees"]) if request.form.get("school_fees") else 0,
                "shopping": float(request.form["shopping"]) if request.form.get("shopping") else 0,
                "healthcare": float(request.form["healthcare"]) if request.form.get("healthcare") else 0
            }
        }
        collection.insert_one(data)
        return redirect(url_for("index"))
    return render_template("index.html")


@app.route("/export")
def export_csv():
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)
    df.to_csv("survey_data.csv", index=False)
    return "CSV Exported Successfully"


@app.route("/visualize")
def visualize():
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)
    if df.empty:
        return "No data available for visualization"

    plt.figure(figsize=(8, 5))
    sns.barplot(x=df["age"], y=df["total_income"], palette="viridis")
    plt.xlabel("Age")
    plt.ylabel("Total Income")
    plt.title("Income Distribution by Age")
    plt.savefig("static/income_by_age.png")

    return "Visualization created successfully. Check static folder."


if __name__ == "__main__":
    app.run(debug=True)
