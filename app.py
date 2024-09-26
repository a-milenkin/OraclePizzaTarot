from flask import Flask, render_template, request, jsonify
from tarot_oracle import TarotOracle

app = Flask(__name__)
tarot_oracle = TarotOracle()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Here you would typically save and process the image
    # For this example, we'll skip image processing and just generate a prediction

    card, prediction = tarot_oracle.generate_prediction()
    return jsonify({
        'card': card,
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
