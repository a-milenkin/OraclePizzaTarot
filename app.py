from flask import Flask, render_template, request, jsonify
from tarot_oracle import TarotOracle

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
