import random
import os

class TarotOracle:
    def __init__(self):
        self.tarot_cards = [
            'Шут', 'Маг', 'Верховная Жрица', 'Императрица', 'Император',
            'Иерофант', 'Влюбленные', 'Колесница', 'Сила', 'Отшельник',
            'Колесо Фортуны', 'Справедливость', 'Повешенный', 'Смерть',
            'Умеренность', 'Дьявол', 'Башня', 'Звезда', 'Луна', 'Солнце',
            'Суд', 'Мир'
        ]
        self.zodiac_signs = [
            'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева',
            'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'
        ]

    def draw_cards(self, num_cards=3):
        card_images = os.listdir('taro_cards_images')
        if not card_images:
            return random.sample(self.tarot_cards, min(num_cards, len(self.tarot_cards)))
        return random.sample(card_images, min(num_cards, len(card_images)))

    def interpret_combination(self, cards):
        combinations = {
            ('Шут', 'Маг'): "Начало нового творческого пути с большим потенциалом.",
            ('Императрица', 'Император'): "Баланс между созиданием и структурой в вашей жизни.",
            ('Луна', 'Солнце'): "Переход от неуверенности к ясности и успеху.",
            ('Смерть', 'Возрождение'): "Глубокая трансформация и новые возможности.",
        }

        for combo, interpretation in combinations.items():
            if all(card.split('.')[0] in cards for card in combo):
                return interpretation

        return "Уникальная комбинация карт предвещает интересные повороты судьбы."

    def generate_prediction(self, question):
        cards = self.draw_cards()
        zodiac = random.choice(self.zodiac_signs)
        interpretation = self.interpret_combination(cards)
        
        card_names = [card.split('.')[0] for card in cards]
        prediction = f"На ваш вопрос '{question}' выпали карты: {', '.join(card_names)}. {interpretation} {zodiac} будет вашим путеводителем в этом гастрономическом приключении!"
        
        return cards, prediction
