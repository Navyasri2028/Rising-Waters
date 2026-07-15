from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("floods.save")
scaler = joblib.load("scaler.save")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['Temp']),
        float(request.form['Humidity']),
        float(request.form['CloudCover']),
        float(request.form['Annual']),
        float(request.form['JanFeb']),
        float(request.form['MarMay']),
        float(request.form['JunSep']),
        float(request.form['OctDec']),
        float(request.form['AvgJune']),
        float(request.form['Sub'])
    ]

    data = np.array(features).reshape(1, -1)

    print("Original Features:", features)
    print("Scaled Data:", data)
    print("Prediction:", model.predict(data))
    print("Probability:", model.predict_proba(data))

    # Prediction
    prediction = model.predict(data)[0]

    # Probability
    probabilities = model.predict_proba(data)[0][1]
    print(probabilities)

    flood_probability = probabilities[0][1] * 100
    no_flood_probability = probabilities[0][0] * 100

    if prediction == 1:
        result = "⚠️ High Flood Risk"
    else:
        result = "✅ No Flood Risk"
    
    print("Flood Probability:", flood_probability)
    print("No Flood Probability:", no_flood_probability)

    return render_template(
        "result.html",
        prediction=result,
        flood_probability=round(flood_probability, 2),
        no_flood_probability=round(no_flood_probability, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)