from flask import Flask, render_template, request, jsonify, send_from_directory
from tarot_oracle import TarotOracle
import os

app = Flask(__name__)
tarot_oracle = TarotOracle()

@app.route('/')
def index():
    # Печатает 'hello world' в консоль
    print('hello world')
    # Отображает и возвращает шаблон 'index.html'
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Извлекает 'question' из данных формы
    question = request.form.get('question')
    # Проверяет, существует ли 'question'
    if not question:
        # Возвращает сообщение об ошибке в формате JSON, если 'question' не предоставлен
        return jsonify({'error': 'No question provided'}), 400

    # Генерирует предсказание с помощью таро оракула на основе данного вопроса
    cards, prediction = tarot_oracle.generate_prediction(question)
    # Возвращает карты и предсказание в формате JSON
    return jsonify({
        'cards': cards,
        'prediction': prediction
    })

@app.route('/taro_cards_images/<path:filename>')
def serve_tarot_image(filename):
    return send_from_directory('taro_cards_images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
