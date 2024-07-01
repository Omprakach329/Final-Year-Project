from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

def determine_water_quality(do, ph, co, bod, na, tc):
    if ph > 8.5:
        return "Fair"
    elif ph >= 8:
        return "Excellent"
    elif ph >= 7.5:
        return "Excellent"
    elif ph >= 7:
        return "Excellent"
    elif ph >= 6.5:
        return "Good"
    else:
        return "Fair"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            do = float(request.form['do'])
            ph = float(request.form['ph'])
            co = float(request.form['co'])
            bod = float(request.form['bod'])
            na = float(request.form['na'])
            tc = float(request.form['tc'])

            water_quality = determine_water_quality(do, ph, co, bod, na, tc)

            if water_quality == "Excellent":
                safety_message = "water is Drinkable"
            elif water_quality == "Good":
                safety_message = "water is Drinkable"
            else:
                safety_message = "water is Unsafe for Drinking"

            return f"<div style='text-align:center; font-size: 40px; margin-top: 100px; background-image: url(\"/static/om.png\");'><strong>The predicted water quality is {water_quality}</strong><br>{safety_message}</div>"

        except ValueError:
            return "Please enter valid numeric values"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
