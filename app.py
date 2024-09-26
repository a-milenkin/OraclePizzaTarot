from flask import Flask, render_template, request, jsonify, send_from_directory
from tarot_oracle import TarotOracle
import os

app = Flask(__name__)
tarot_oracle = TarotOracle()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    question = request.form.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    cards, prediction = tarot_oracle.generate_prediction(question)
    return jsonify({
        'cards': cards,
        'prediction': prediction
    })

@app.route('/taro_cards_images/<path:filename>')
def serve_tarot_image(filename):
    return send_from_directory('taro_cards_images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
