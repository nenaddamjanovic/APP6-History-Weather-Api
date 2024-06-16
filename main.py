from flask import Flask, render_template
import pandas as pd
# Flask: A lightweight web framework in Python for building web applications.
# render_template: A function from Flask used to render HTML templates.
# pandas (pd): A powerful data manipulation and analysis library in Python.

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Combines the base path "data_small/TG_STAID" with the station number,
    # ensuring it is zero-padded to six digits using .zfill(6), and appends
    # ".txt" to form the filename.
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    #  Reading the CSV file:
    df = pd.read_csv(filename,
                     skiprows=20,
                     parse_dates=["    DATE"])  # Parses the column named " DATE" as dates.
    # Extracting the temperature:
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Summary:
# Home Route (/): Renders an HTML template (home.html). API Route (
# /api/v1/<station>/<date>): Reads a temperature data file based on the
# station and date provided, processes the data, and returns it as JSON.
