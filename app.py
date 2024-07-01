from flask import Flask, render_template, request
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import csv

app = Flask(__name__)

def predict_water_quality(do, ph, co, bod, na, tc):
    X_train = [
        [5.8, 7.2, 8.5, 4.1, 15.0, 80.0],
        [6.5, 7.0, 9.0, 3.8, 18.0, 70.0],
        [7.2, 6.8, 8.2, 4.5, 12.0, 90.0]
    ]
    Y_train = ['Good', 'Excellent', 'Fair']
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    svm_classifier = SVC(kernel='rbf', random_state=42) 
    svm_classifier.fit(X_train_scaled, Y_train)
    
    X_test = [[do, ph, co, bod, na, tc]] 
    X_test_scaled = scaler.transform(X_test)
    y_pred = svm_classifier.predict(X_test_scaled)

    return y_pred[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        do = float(request.form['do'])
        ph = float(request.form['ph'])
        co = float(request.form['co'])
        bod = float(request.form['bod'])
        na = float(request.form['na'])
        tc = float(request.form['tc'])
        
        water_quality = predict_water_quality(do, ph, co, bod, na, tc)
        
        if water_quality == "Excellent":
            safety_message = "water is Drinkable"
        elif water_quality == "Good":
            safety_message = "water is Drinkable"
        else:
            safety_message = "water is Unsafe for Drinking"
        
        return f"The predicted water quality is {water_quality}. {safety_message}"
    except Exception as e:
        print("Error occurred:", e)
        return "An error occurred while processing the request."

if __name__ == '__main__':
    app.run(debug=True)
