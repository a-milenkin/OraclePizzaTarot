import random
import os
from openai import OpenAI

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
        self.card_meanings = {
            'Шут': 'новые начинания, спонтанность',
            'Маг': 'мастерство, творчество',
            'Верховная Жрица': 'интуиция, тайны',
            'Императрица': 'изобилие, плодородие',
            'Император': 'структура, авторитет',
            'Иерофант': 'традиции, обучение',
            'Влюбленные': 'выбор, гармония',
            'Колесница': 'движение вперед, контроль',
            'Сила': 'внутренняя сила, храбрость',
            'Отшельник': 'самопознание, уединение',
            'Колесо Фортуны': 'перемены, циклы',
            'Справедливость': 'баланс, честность',
            'Повешенный': 'новый взгляд, жертва',
            'Смерть': 'трансформация, обновление',
            'Умеренность': 'гармония, баланс',
            'Дьявол': 'искушение, зависимость',
            'Башня': 'внезапные изменения, разрушение',
            'Звезда': 'надежда, вдохновение',
            'Луна': 'интуиция, иллюзии',
            'Солнце': 'успех, радость',
            'Суд': 'возрождение, пробуждение',
            'Мир': 'завершение, достижение'
        }
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def draw_cards(self, num_cards=3):
        card_images = os.listdir('taro_cards_images')
        if not card_images:
            return random.sample(self.tarot_cards, min(num_cards, len(self.tarot_cards)))
        return random.sample(card_images, min(num_cards, len(card_images)))

    def generate_ai_prediction(self, question, cards):
        card_names = [card.split('.')[0].replace('_', ' ') for card in cards]
        zodiac = random.choice(self.zodiac_signs)
        
        card_descriptions = "\n".join([f"{card}: {self.card_meanings.get(card, 'значение неизвестно')}" for card in card_names])
        
        messages = [
            {"role": "system", "content": "Вы - мистический предсказатель, специализирующийся на гадании на картах Таро с уклоном в кулинарию и приготовление пиццы."},
            {"role": "user", "content": f'''
Создайте уникальное и разнообразное предсказание на основе следующей информации:
Вопрос: "{question}"
Выпавшие карты Таро: {', '.join(card_names)}

Для каждой карты:
{card_descriptions}

Знак зодиака: {zodiac}

Предсказание должно быть тесно связано с названиями и значениями выпавших карт, а также с кулинарией и приготовлением пиццы. 
Используйте творческий подход, юмор и метафоры, связанные с пиццей и ее ингредиентами.
Не используйте шаблонные фразы вроде "Ваше кулинарное путешествие включает в себя".
Ответ должен быть на русском языке и состоять из 4-5 уникальных предложений.
'''}
        ]

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=200,
                n=1,
                temperature=0.9,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating AI prediction: {e}")
            return None

    def generate_prediction(self, question):
        cards = self.draw_cards()
        for _ in range(3):  # Try up to 3 times
            prediction = self.generate_ai_prediction(question, cards)
            if prediction and "Ваше кулинарное путешествие включает в себя" not in prediction:
                return cards, prediction
        
        # If we still don't have a good prediction, generate a more randomized one
        zodiac = random.choice(self.zodiac_signs)
        card_names = [f'"{card.split(".")[0].replace("_", " ")}"' for card in cards]
        pizza_elements = ['соус', 'сыр', 'тесто', 'начинка', 'духовка', 'нарезка', 'подача']
        random_elements = random.sample(pizza_elements, 3)
        prediction = f'Карты {", ".join(card_names)} предвещают неожиданный поворот в вашем кулинарном приключении! {random_elements[0].capitalize()} станет вашим вдохновением, {random_elements[1]} преподнесет сюрприз, а {random_elements[2]} раскроет ваш потенциал. {zodiac} подскажет, когда пицца будет идеальной!'
        
        return cards, prediction
