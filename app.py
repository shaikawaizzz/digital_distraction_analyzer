print("flask app is running")
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    study_hours = float(request.form['study_hours'])
    social_media_hours = float(request.form['social_media_hours'])
    youtube_hours = float(request.form['youtube_hours'])
    gaming_hours = float(request.form['gaming_hours'])
    sleep_hours = float(request.form['sleep_hours'])
    phone_unlocks = int(request.form['phone_unlocks'])
    assignments_completed = int(request.form['assignments_completed'])

    # same logic used in synthetic data
    distraction_score = (
        social_media_hours * 2 +
        gaming_hours * 2 +
        phone_unlocks * 0.05 -
        study_hours * 1.5
    )

    return render_template(
        "index.html",
        prediction_text=f"Predicted Distraction Score: {round(distraction_score,2)}"
    )


if __name__ == "__main__":
    app.run(debug=True)
