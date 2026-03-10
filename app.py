from flask import Flask, request, redirect, render_template
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import json

app = Flask(__name__)

# Google API scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Railway variable
credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    credentials_info,
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key("1EPAxJ0XYGn4Mnu2WMTi_0oOPNtBGj-fwwxP4AEw8HF0").sheet1


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lampiran3")
def lampiran3():
    return render_template("lampiran3.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/submit", methods=["POST"])
def submit():

    form = request.form

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [
        timestamp,
        form.get("nama"),
        form.get("jawatan"),
        form.get("mp"),
        form.get("tahun"),
        form.get("1.1"),
        form.get("catatan_1.1"),
        form.get("2.1"),
        form.get("catatan_2.1"),
        form.get("2.2"),
        form.get("catatan_2.2"),
        form.get("3.1"),
        form.get("catatan_3.1"),
        form.get("3.2"),
        form.get("catatan_3.2"),
        form.get("3.3"),
        form.get("catatan_3.3"),
        form.get("3.4"),
        form.get("catatan_3.4"),
        form.get("3.5"),
        form.get("catatan_3.5"),
        form.get("4.1"),
        form.get("catatan_4.1"),
        form.get("4.2"),
        form.get("catatan_4.2"),
        form.get("4.3"),
        form.get("catatan_4.3"),
        form.get("5.1"),
        form.get("catatan_5.1"),
        form.get("5.2"),
        form.get("catatan_5.2"),
        form.get("5.3"),
        form.get("catatan_5.3"),
        form.get("5.4"),
        form.get("catatan_5.4"),
        form.get("5.5"),
        form.get("catatan_5.5"),
        form.get("5.6"),
        form.get("catatan_5.6"),
        form.get("1.1_b"),
        form.get("catatan_1.1_b"),
        form.get("1.2_b"),
        form.get("catatan_1.2_b"),
        form.get("1.3_b"),
        form.get("catatan_1.3_b"),
        form.get("1.4_b"),
        form.get("catatan_1.4_b"),
        form.get("1.5_b"),
        form.get("catatan_1.5_b"),
        form.get("1.6_b"),
        form.get("catatan_1.6_b"),
        form.get("1.7_b"),
        form.get("catatan_1.7_b"),
        form.get("1.8_b"),
        form.get("catatan_1.8_b"),
        form.get("1.9_b"),
        form.get("catatan_1.9_b"),
        form.get("1.10_b"),
        form.get("catatan_1.10_b"),
        form.get("1.11_b"),
        form.get("catatan_1.11_b"),
    ]

    sheet.append_row(row)

    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
