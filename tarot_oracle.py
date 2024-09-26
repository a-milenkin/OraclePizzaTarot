import random

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
        return random.sample(self.tarot_cards, num_cards)

    def interpret_combination(self, cards):
        combinations = {
            ('Шут', 'Маг'): "Начало нового творческого пути с большим потенциалом.",
            ('Императрица', 'Император'): "Баланс между созиданием и структурой в вашей жизни.",
            ('Луна', 'Солнце'): "Переход от неуверенности к ясности и успеху.",
            ('Смерть', 'Возрождение'): "Глубокая трансформация и новые возможности.",
        }

        for combo, interpretation in combinations.items():
            if all(card in cards for card in combo):
                return interpretation

        return "Уникальная комбинация карт предвещает интересные повороты судьбы."

    def generate_prediction(self, question):
        cards = self.draw_cards()
        zodiac = random.choice(self.zodiac_signs)
        interpretation = self.interpret_combination(cards)
        
        prediction = f"На ваш вопрос '{question}' выпали карты: {', '.join(cards)}. {interpretation} {zodiac} будет вашим путеводителем в этом гастрономическом приключении!"
        
        return cards, prediction

