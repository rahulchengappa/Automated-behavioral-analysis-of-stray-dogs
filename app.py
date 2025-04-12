from flask import Flask, request, jsonify
from flask_cors import CORS  # Optional if you're using Live Server

app = Flask(__name__)
CORS(app)  # Allow requests from browser

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"message": "No file received", "danger": True}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "Empty file name", "danger": True}), 400

    # Your model prediction logic here
    # For now, return dummy response
    return jsonify({
        "message": "Dog seems calm",
        "danger": False
    })

if __name__ == '__main__':
    app.run(debug=True)

