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
        self.combinations = {
            ('Шут', 'Маг'): "Начало нового творческого пути с большим потенциалом в кулинарии.",
            ('Императрица', 'Император'): "Баланс между созиданием и структурой в вашей кухне.",
            ('Луна', 'Солнце'): "Переход от неуверенности к ясности и успеху в приготовлении пиццы.",
            ('Смерть', 'Звезда'): "Глубокая трансформация и новые возможности в вашем кулинарном искусстве.",
            ('Отшельник', 'Мир'): "Путь от самопознания к мастерству в приготовлении пиццы.",
            ('Башня', 'Умеренность'): "После неожиданных изменений найдете баланс в кулинарных экспериментах.",
            ('Влюбленные', 'Дьявол'): "Страсть к пицце может привести к искушениям, но это путь к совершенству.",
            ('Колесница', 'Сила'): "Движение вперед с уверенностью в своих кулинарных способностях.",
            ('Справедливость', 'Суд'): "Время оценить свои кулинарные навыки и принять важное решение.",
            ('Иерофант', 'Верховная Жрица'): "Сочетание традиций и интуиции в приготовлении пиццы."
        }

    def draw_cards(self, num_cards=3):
        card_images = os.listdir('taro_cards_images')
        if not card_images:
            return random.sample(self.tarot_cards, min(num_cards, len(self.tarot_cards)))
        return random.sample(card_images, min(num_cards, len(card_images)))

    def interpret_combination(self, cards):
        card_names = [card.split('.')[0].replace('_', ' ') for card in cards]
        for combo, interpretation in self.combinations.items():
            if all(card in card_names for card in combo):
                return interpretation

        # If no specific combination is found, generate a general interpretation
        themes = {
            'Шут': 'новые начинания', 'Маг': 'мастерство', 'Верховная Жрица': 'интуиция',
            'Императрица': 'изобилие', 'Император': 'структура', 'Иерофант': 'традиции',
            'Влюбленные': 'выбор', 'Колесница': 'движение', 'Сила': 'внутренняя сила',
            'Отшельник': 'самопознание', 'Колесо Фортуны': 'перемены', 'Справедливость': 'баланс',
            'Повешенный': 'новый взгляд', 'Смерть': 'трансформация', 'Умеренность': 'гармония',
            'Дьявол': 'искушение', 'Башня': 'внезапные изменения', 'Звезда': 'надежда',
            'Луна': 'интуиция', 'Солнце': 'успех', 'Суд': 'возрождение', 'Мир': 'завершение'
        }

        interpretation = "Ваше кулинарное путешествие включает в себя "
        for card in card_names:
            if card in themes:
                interpretation += f"{themes[card]}, "
        
        interpretation = interpretation.rstrip(', ') + "."
        return interpretation

    def generate_prediction(self, question):
        cards = self.draw_cards()
        zodiac = random.choice(self.zodiac_signs)
        interpretation = self.interpret_combination(cards)
        
        card_names = [f'"{card.split(".")[0].replace("_", " ")}"' for card in cards]
        prediction = f'На ваш вопрос "{question}" выпали карты: {", ".join(card_names)}. {interpretation} {zodiac} будет вашим путеводителем в этом гастрономическом приключении!'
        
        return cards, prediction
