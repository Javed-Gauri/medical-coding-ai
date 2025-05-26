from flask import Flask, request
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Replace with your actual model logic
    return {
        "icd10": "J18.9", 
        "cpt": "99213",
        "risk": 0.15
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
